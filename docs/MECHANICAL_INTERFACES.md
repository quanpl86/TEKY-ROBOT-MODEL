# Mechanical Interfaces (reference; metres in GLB)

## Global axes
+X right, +Y up, +Z forward. Positions here in mm unless stated. Typical wheel diameter 60mm, wheel center Y=30mm. Tire geometry must have bottom≈0mm; any negative ground penetration is a QA issue.

## Drivetrain (source V3.8.x reference)
| Part | Center X,Y,Z mm | Motion | Control |
|---|---|---|---|
| Rear drive left | -95,30,-71 | continuous about X | outA (verify sign) |
| Rear drive right | 95,30,-71 | continuous about X | outB (verify sign) |
| Front left | -107,30,96 | passive or chain-coupled | no extra motor unless redesigned |
| Front right | 107,30,96 | passive or chain-coupled | no extra motor unless redesigned |

X centers of rear wheels describe the **rear rubber visual reference**. If GEARS uses its built-in Wheel placement differently, transform/offset must be reconciled. Center-to-center axle distance along Z: 167mm. Original front Omni width about 20mm; rear rubber width about 48mm. A rubber front replacement must fit the guard and maintain lateral clearance; any scaled-derived draft geometry must be marked provisional.

## Chain
2 separate open chains left/right; 12T rear and 12T front; ratio 1:1; pitch radius around 14.07mm, center distance 167mm. Straight chain sections tangent to equal sprocket pitch circles. Never place one straight run through the wheel axle. The chain animation comes from driven wheel rotation; a real power transfer requires runtime physics linkage or explicit constraint and preserves Omni free lateral roller properties where applicable.

## Guard
`Protection_Frame_Root` contains front/side/rear bumpers, side windows, side chain shields, corners and fixed bolt plates. Separate GLB + collider proxies. Fixed to Chassis with distributed mating mounts, NOT a free body. Collision with wall/blocks enabled; collision with internal wheels/chain disabled by filters if appropriate; count its mass only once.

## Sensor mounting
- Camera legacy V3.8.5 optical/body reference: center [0,330,-100], tilt ~27° down. Camera mast must be separate/detachable and its foot anchored to chassis; guard optional brace allowed only with no double-mass.
- LiDAR legacy OPTIONAL: scan reference [0,143,-59]; camera pole occludes rear LiDAR region in V3.8.5; never call 360° unobstructed until ray test passes.
- Rear/side/front laser: OPTIONAL; default no laser.
- 3 line color readers: left/center/right next to each other under front of chassis, facing down; check 20mm line width and calibration.

## Attachment dock
`Attachment_Dock_Front` is a stable mounting interface; maintain 3D datum, centerline, mounting screw pattern and references. **Hole pitch is not certified by current public GEARS source**; measure from canonical GLB, store transform/mount manifest and do not fake mm values. Moving guard/camera must not occupy dock or dynamic joint envelope. Test full joint sweep and sensor occlusion with each module.

## Pivot conventions
Wheel center at axle, sprocket center at shaft, arm joint at hinge, linear slider origin at start of stroke, end effector at attachment face, sensor origin at optical center. Export part GLB pivot-local and an assembled-view preview separately.
