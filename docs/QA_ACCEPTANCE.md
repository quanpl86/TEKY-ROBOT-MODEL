# QA Acceptance / Release Gates

## Geometry (offline)
- Reimport every GLB, check number of meshes, triangle count, bounds and byte count; all m → mm conversions correct.
- Mechanical dimensions: wheel diameter and centers, guard mounting, axle/pivot, sensor housing/mount, no floating bolts/panels, closed cap on roofs/covers, no overlaps in moving pair except intended mating surfaces.
- Normal face orientation, metallic/roughness PBR, consistent color palette.
- For each of four drivetrains: proper wheel type, front wheel passive/coupled as described, no extra motor; chain straight segments tangent to sprocket pitch circles and no chain through hub.
- For each attachment: dynamic sweep (hinge, slide, spin, fully extended max) plus static startup.
- Optical cones: camera near/far floor, medium signs, colored 40mm cubes, ultrasonic 2-way, color sensor three positions, 360° LiDAR including camera pole obstruction if installed.
- No duplicate visual from full previews plus part assemblies.

## Runtime tests (GEARS/Ammo/BabylonJS)
- Two driven motors independent left/right, forward and turn signs, 4 wheels contact ground, no guard collision with tires, terrain/curb, wall reverse-align collision, chain physical torque only if coupled.
- 20mm line follow using center or left+right; readings correct independent of arm position.
- Camera target lines, signs and block color under 9 attachment rest poses; test head occlusion when arm lifts; LiDAR 360 sweep when installed.
- Pickup cube 40mm directly from floor, close grip, lift 1–2 blocks, carry, turn, brake, reach and place on 200mm platform, release; no dropping/tilt and certified torque/friction limits.
- Verify center of gravity under maximum lift and braking; use hardware or simulation mass values, do not invent a safe payload.
- Render performance for multiple robots, export and import in the current TEKY build.

## Status
Record JSON fields `geometry_validated`, `runtime_tested`, `runtime_passes`, `known_issues`, `baseline_variant`, `asset_manifest_version`. Never use `RUNTIME_ACCEPTED` without actual GEARS simulation logs/videos/assertions.
