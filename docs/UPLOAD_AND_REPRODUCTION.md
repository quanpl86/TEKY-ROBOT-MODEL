# Binary asset publishing / reproducibility

Canonical assets are generated from historical high-fidelity V3.8.5 and V3.7 sources; binary GLBs are **not** text JSON. A project bundle includes `assets/base/*.glb` (four variants), `assets/protection/*.glb`, `assets/drivetrains/*.glb`, `assets/sensors/*.glb`, `assets/attachments/*/*.glb`, `manifests/*`, `qa/*`.

## Source inputs
Store source GLBs locally under `inputs/v385/` and V3.7 module GLBs under `inputs/v37/modules/`. The Python build script relies on source scene node names recorded in the legacy GLBs. When using a new source, audit the node grouping and regenerate QA instead of silently substituting.

## Publish
1. Check `manifests/file_index.json` and SHA256 for all outputs.
2. Use native Git or GitHub UI to upload actual `.glb` bytes; do **not** paste base64 text into files with `.glb` extension.
3. Version with a release tag; include one `*_VISUAL_ONLY.glb` for viewing, never a default runtime duplicate.
4. Keep `main` canonical and mark geometry vs physics acceptance separately.

## Status of initial handoff
Repository instructions and configs are tracked here. Latest real high-fidelity source **V3.8.5** exists in the conversation export; direct GitHub binary upload via connector may require a separate transport step, and files are not considered uploaded until visible in GitHub's `assets/` tree. Never report an asset as hosted here without checking a returned GitHub file URL.
