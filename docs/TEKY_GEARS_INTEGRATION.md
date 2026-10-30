# TEKY ROBOT / GEARS native integration notes

Upstream basis: https://github.com/QuirkyCort/gears (not automatically identical to TEKY fork). Verified `Robot.js` logic creates native wheels via `outA` / `outB` when `options.wheels`; component ordering assigns additional `outC` etc and sensor `in1...` sequentially. Do not blindly assume native max number of motors/sensors or port IDs in the TEKY fork.

## Two-layer architecture
- **Visual layer**: custom GLB meshes for chassis, guard, motors, wheels, sensors and attachment; selectable visibility, no duplicate geometry.
- **Functional layer**: GEARS native motors/actuators, joints, sensor raycasters/readPixels, collision proxies, physics body and constraints. Native meshes can be visually hidden, **not disabled** (do not blindly call setEnabled(false) on native sensor object).

## Defaults
Two rear drive motors (outA and outB); two front passive wheels. No LiDAR/Laser, no chains or attachments by default. Add selected modules using typed factory and dedicated current-port registry. Avoid double-adding auto-generated wheels AND wheel components.

## Sensor binding
- One optional central elevated CameraSensor; forward +Z lens, relative pitch down. Upstream `CameraSensor` uses a FreeCamera RTT; default 100x100 pixels and sensorFov 1.3 radians, source-specific. Read visual optical origin, then map native camera origin to same position in cm.
- 3 bottom ColorSensor cores (left/center/right), down towards Y-, mapped to line 20mm.
- Ultrasonic at true front/back housing orientation if selected.
- LiDAR/Ray + LaserRangeSensor optional, and should not be created on base default. For LiDAR scan subtract all occluding beams in all 360 directions, do not assume unobstructed.

## Transmission variants
Default: front WheelPassive or equivalent native passive-collision wheels, no motor/coupling.
Mixed Omni 2WD: passive Omni rollers; ensure lateral traction properties and rotation signs.
Chain variants: two independent rear-to-front constraints with 1:1 angular rate; **physical torque transfer and simulation must be implemented/verified**, not inferred from glTF animation. Avoid extra assigned motor ports unless explicit design.
Guard collider is independent authoring asset but fixed to chassis at runtime; collide with wall/blocks, not internal chain or tires; count fixed mass once.

## Import checklist
Resolve custom-GLB binding schema from TEKY source **before** creating `teky_robot.json`. Unknown custom fields must be documented as adapters, not represented as recognized GEARS JSON. Test both axes and rotations and use real sensor signal checks. Use `docs/QA_ACCEPTANCE.md` for acceptance.
