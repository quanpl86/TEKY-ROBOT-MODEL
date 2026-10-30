# Release Status / Upload Evidence

| Item | Status as of 2026-10-30 | Location |
|---|---|---|
| Agent instructions | UPLOADED | `AGENTS.md`, `.github/copilot-instructions.md` |
| Project architecture and long-term roadmap | UPLOADED | `docs/` |
| Family config / sensor catalog / 9 attachment catalog | UPLOADED | `configs/` |
| Four **schematic** GLBs | UPLOADED, DRAFT | `assets/prototypes/v4_procedural_studies/*.glb` |
| Four V3.8.5-derived high-fidelity canonical variants | EXPORTED LOCALLY; GITHUB UPLOAD PENDING | Hand-off ZIP, `assets/base/` |
| 9 standalone V3.7-derived attachments | EXPORTED LOCALLY; GITHUB UPLOAD PENDING | Hand-off ZIP, `assets/attachments/` |
| Guard, drivetrain parts, optional sensors | EXPORTED LOCALLY; GITHUB UPLOAD PENDING | Hand-off ZIP, `assets/protection`, `assets/drivetrains`, `assets/sensors` |
| Native GEARS/TEKY physics acceptance | NOT TESTED | Pending TEKY runtime team |

**Do not confuse the uploaded DRAFT GLBs with approved full production GLBs.** High fidelity assets stay in the attached archive until a binary-preserving Git upload is done and verified on GitHub. Never describe 9 attachment binary assets as present in GitHub until visible as files on main.

The geometry QA validates import/export and initial positions. Dynamic collision, camera FOV, 20mm line following, transmission torque and 2-block high-lift remain runtime checks.
