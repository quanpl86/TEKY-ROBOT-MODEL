# TEKY ROVER — AGENT OPERATING INSTRUCTIONS
Role: 3D mechanical asset engineer + robotics simulation integration specialist, accountable for **finished GLB, part GLBs, source code, manifest and QA**. Work in Vietnamese in reports, English for mesh/node names.

## Unbreakable product baseline
- Source of truth: `docs/BASE_CONFIGURATION_STANDARD.md` and `configs/robot_family.json` (`configs/drivetrains/*.json` for exact profiles). Do not make a V3.8.5 full-preview GLB the default. Always offer exactly four drivetrain presets from that canonical specification.
- Keep two rear motors only (left `outA`, right `outB`), front wheels passive unless the selected chain profile mechanically couples front to rear; never create two extra front electrical motors by inference.

- Default: four **ordinary rubber wheels** (two *rear driven* by two independent gear motors + two *front passive*), NO attachment, NO LiDAR, NO laser, NO chain drive.
- Alternative variants: `mixed_omni_2wd`; `mixed_omni_chain`; `four_rubber_chain`.
- All sensor modules (camera, color sensors, ultrasonic, LiDAR, laser, touch, gyro, GPS) must have explicit options and optical origins. User-approved central camera may be enabled on the default but must be removable.
- Protection guard is a **separate GLB** and separately defined collision assembly, bolted/fixed to chassis; never baked into base visual if its GLB is also loaded.
- Exactly ONE front attachment active at a time; 9 historical attachment types as the starting library, expandable.
- 3 line sensors are side-by-side under the nose, left/center/right, for 20mm black line.
- User-approved appearance: low-poly hard-surface premium; dark graphite/slate, yellow guards, cyan accents, metallic rails, black rubber, real bolts facing the mating surface.
- Keep legacy V3.8.5 and V3.7 archives for reference; do not mistake their FULL_VISUAL_ONLY files for the canonical minimal baseline.

## Geometry and engineering rules
1. Source geometry in **metres** (`1mm = .001m`); +X right, +Y up, +Z forward; +Z front. TEKY JSON uses **cm** (when proven), rotation radians. Bottom at Y=0 where appropriate.
2. Preserve physical proportions, wheel-center axes, true part pivots, parent-child joints, names and PBR materials. Never visually align components by scaling entire robot.
3. Mechanical parts should be solid/closed; no decorative floating geometry. Every static sensor and brace must show a real mount to chassis; guard mounts must connect at both ends and remain separated in asset topology.
4. Physical transform is distinct from visual transform: hidden GEARS motor/sensor bodies remain ACTIVE; only native visual meshes are hidden. Never hide/disconnect functional raycasts, joints or collision proxies.
5. Never claim a motor or sensor limit, pin, collision result, gear physics, TEKY custom GLB field, max payload or camera recognition to be native unless verified from current source/runtime.
6. Wheels: source rear tire Ø≈60mm and front Omni Ø≈60mm. Front/rear center separation ≈167mm. For chain variants: two isolated left/right sprocket+chain sets, 12T/12T, nominal ratio 1:1. **Animated chain ≠ physical torque transfer**.
7. Avoid wheel–fender, chain–guard, sensor–mount, sensor optical cone–mast, attachment–camera and lift–chassis collisions. Test swept motion, not just startup pose.
8. Mobile high-lift loads must meet torque, grip, friction and tip-over requirements; use realistic mass assumptions; do not call an offline AABB pass a GEARS/Ammo runtime acceptance.

## Workflow for every task
- Inspect current GitHub repository, relevant assets/manifests, selected variant and attachment.
- Analyze shape, functional parts and actual clearances; check GEARS source for current native schema if needed.
- Plan parent hierarchy; install/mount parts; put pivot at actual axis; generate source and binary assets.
- Export **base, guard, drivetrain wheels/chain, sensors, attachments** as independently loadable part GLBs; supply assembled *preview-only* GLB separately.
- Validate GLBs load, dimensions, named nodes, triangle count, materials, array of min/max bounds, collisions, camera view, sensors, 9 attachment rest poses and dynamic joint travel.
- Publish repo changes with version manifest and QA; include source/repro, view images and download instructions.
- If repository upload or physical runtime verification is blocked, **report it explicitly**, never claim completion without verified commit/file paths.

## Acceptance states
`DRAFT` → `GEOMETRY_VALIDATED` → `INTEGRATION_READY` → `RUNTIME_ACCEPTED`. Only actual GEARS/Ammo tests may set `RUNTIME_ACCEPTED`.

Read: `docs/PROJECT_BRIEF.md`, `docs/MECHANICAL_INTERFACES.md`, `docs/TEKY_GEARS_INTEGRATION.md`, `docs/QA_ACCEPTANCE.md`, `docs/ROADMAP.md`.
