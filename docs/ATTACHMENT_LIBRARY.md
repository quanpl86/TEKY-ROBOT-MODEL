# Nine detachable attachments
Only one attached to `Attachment_Dock_Front` at a time. Native hardware must be hidden visually but **still active**. Mount stays on Chassis; attachment kinematic descendants follow their respective joint.

| ID | Name | Mechanism | QA hotspots |
|---|---|---|---|
| 01 | push_capture | Fixed bumper / optional widening linear guides | 40mm mission block centering, camera and color reader |
| 02 | rotating_sweeper | Revolute sweeper | Sweep arc vs front bumper and 3 line sensors |
| 03 | single_pivot_lift | Revolute hinge | Angle sign, safe lifted range and load moment |
| 04 | linear_forklift | Prismatic vertical lift | Legs and rail vs bumper; vertical minimum clearance |
| 05 | ball_launcher | Rotating wheels / launcher | Ball feeder, alignment, runtime physics, shield |
| 06 | articulated_arm | Linked revolute joints | Parent-child axes, collisions and center of gravity |
| 07 | magnetic_slider | Prismatic carriage + magnetic effector | Force behavior, sensor compatibility |
| 08 | tilt_bucket | Revolute bucket | High-angle bucket can block ultrasonic; must resolve |
| 09 | two_stage_direct_gripper | Dual prismatic lift + parallel gripper | Floor pick of 1–2 40mm cubes; lift 220mm target; end stops; retract only above safe height |

The historical GLBs were authored for V3.7/V3.8.x. They are geometry reference, **not yet certified** across all new wheel configurations; validate dock and dynamic clearances before release. For all new modules publish: `module_assembled.glb`, each movable part GLB, `manifest.json`, motor/port and sensor mapping, range/limits, collision proxy and five-pose visual QA.
