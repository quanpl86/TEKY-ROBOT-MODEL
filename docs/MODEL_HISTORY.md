# Development History / Design Decisions
- V1–V2: four-wheel modular platform, sensors, bumper/guard, initial motors and mission blocks 40x40x40mm.
- V2.9: screw orientation, sensor mounts and floating geometry cleanups.
- V3.1: front wheels changed to Omni option to reduce lateral scrub when turning.
- V3.2–V3.3: nine mission attachments; gearbox, launcher, sweeper, bucket, forklift, arm, magnetic slide, grippers.
- V3.4: two-stage elevator + parallel gripper, endstop graphics and height target 20–22cm.
- V3.5–V3.6: heavy lift concepts, center of mass, rail/carriage fixes, load 2x2 box support; concept stability calculations **not runtime**.
- V3.6.1: direct-floor compact gripper for up to two 40mm cubes, scoop/tray removed.
- V3.6.2–V3.7: Omni front clearance fixes; modular guard and common docking; nine attachments updated.
- V3.8: twin left/right chain sprockets, motorized rear rubber drive to front wheel, ratio 1:1. Separate guard frame.
- V3.8.2: chain tangency correction, premium independent guard.
- V3.8.3: guard–chassis mounts and camera/laser bracket fixes.
- V3.8.4: central elevated single camera moved back to clear front attachment docks; camera scan is obstructed at near field in some attachment poses.
- V3.8.5: camera +15mm and LiDAR +25mm towards front; 9 historical attachments; visual mount correction. **Legacy optional-sensor full variant only.**
- 2026-10-30 **canonical reset**: default base is 4 rubber tires, rear motorized, front passive, no chain/attachment/LiDAR/laser. Keep old designs as selectable packages, NOT default.

No prior visual-only GLB is evidence of load-bearing performance, pass-through motor, accurate color/vision classification or collision-free sweep without test.
