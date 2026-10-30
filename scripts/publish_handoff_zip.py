#!/usr/bin/env python3
"""Publish exact high-fidelity handoff assets into the connected Git clone.

Usage:
  python scripts/publish_handoff_zip.py /path/to/TEKY_ROVER_GITHUB_COMPLETE_ASSETS_AND_SOURCE.zip --push
  python scripts/publish_handoff_zip.py /path/to/TEKY_ROVER_GITHUB_COMPLETE_ASSETS_AND_SOURCE.zip --dry-run

Run from the local clone of quanpl86/TEKY-ROBOT-MODEL, authenticated with GitHub.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import subprocess
import sys
from zipfile import ZipFile

PREFIX = "TEKY_ROVER_GITHUB_HANDOFF/"
FOLDERS = {"assets", "manifests", "qa", "scripts", "inputs"}
EXPECTED_REPOSITORY = "quanpl86/TEKY-ROBOT-MODEL"


def run(*args: str) -> None:
    subprocess.run(args, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path)
    parser.add_argument("--push", action="store_true", help="Push committed assets to origin/main")
    parser.add_argument("--dry-run", action="store_true", help="Verify archive without modifying files")
    parser.add_argument("--no-inputs", action="store_true", help="Omit 25 historical source GLBs in inputs/")
    args = parser.parse_args()

    cwd = Path.cwd()
    if not (cwd / ".git").exists():
        raise SystemExit("Run from the TEKY-ROBOT-MODEL Git clone root.")
    if not args.archive.is_file():
        raise SystemExit(f"Cannot locate ZIP file: {args.archive}")
    remote = subprocess.check_output(["git", "remote", "get-url", "origin"], text=True).strip()
    if EXPECTED_REPOSITORY.lower() not in remote.lower():
        raise SystemExit(f"Unexpected Git remote: {remote}; expected {EXPECTED_REPOSITORY}")
    if subprocess.check_output(["git", "branch", "--show-current"], text=True).strip() != "main":
        raise SystemExit("Checkout main before publishing.")

    with ZipFile(args.archive) as z:
        if z.testzip() is not None:
            raise SystemExit("ZIP CRC failed.")
        index = json.loads(z.read(PREFIX + "manifests/file_index.json"))
        records = index["files"]
        failures = []
        for rec in records:
            rel = rec["path"]
            member = PREFIX + rel
            try:
                data = z.read(member)
            except KeyError:
                failures.append(f"MISSING: {rel}")
                continue
            if hashlib.sha256(data).hexdigest() != rec["sha256"]:
                failures.append(f"SHA256 MISMATCH: {rel}")
            if len(data) != rec["bytes"]:
                failures.append(f"BYTE SIZE MISMATCH: {rel}")
        if failures:
            raise SystemExit("\n".join(failures))

        upload = []
        for info in z.infolist():
            if info.is_dir() or not info.filename.startswith(PREFIX):
                continue
            relative = info.filename[len(PREFIX):]
            parts = PurePosixPath(relative).parts
            if not parts or parts[0] not in FOLDERS:
                continue
            if args.no_inputs and parts[0] == "inputs":
                continue
            if any(p in {"", ".", ".."} for p in parts):
                raise SystemExit(f"Unsafe archive path: {relative}")
            if relative == "scripts/publish_handoff_zip.py":
                continue
            upload.append((info, relative))

        print(f"Validated {len(records)} canonical GLBs, SHA256 and size exact.")
        print(f"Selected {len(upload)} files from source archive; dry-run={args.dry_run}")
        if args.dry_run:
            return 0

        for info, relative in upload:
            dest = (cwd / relative).resolve()
            if not dest.is_relative_to(cwd.resolve()):
                raise SystemExit(f"Unsafe extraction target: {relative}")
            dest.parent.mkdir(parents=True, exist_ok=True)
            with z.open(info) as src, dest.open("wb") as out:
                shutil.copyfileobj(src, out)

    paths = sorted({p.split("/", 1)[0] for _, p in upload})
    run("git", "add", *paths)
    run("git", "diff", "--cached", "--stat")
    staged = subprocess.run(["git", "diff", "--cached", "--quiet"], check=False)
    if staged.returncode == 0:
        print("No pending changes. Assets already match existing commit.")
        return 0
    if staged.returncode != 1:
        raise SystemExit("git diff --cached failed.")

    run("git", "commit", "-m", "assets: publish V3.8.5 high fidelity rover library and 9 modules")
    if args.push:
        run("git", "push", "origin", "main")
        print("PUSH DONE. Verify GitHub assets/ tree and indexed SHA256 before marking complete.")
    else:
        print("COMMIT CREATED locally. Run: git push origin main")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
