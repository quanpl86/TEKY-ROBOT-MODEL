# Project Brief — TEKY Modular Competition Rover

## North Star
An expandable educational competition-grade rover family: robust, compact, visually premium, physically credible and easy to assemble with different wheels, transmissions, sensors and mission attachments for TEKY ROBOT and future Godot/Three.js engines.

## Fixed baseline
Chassis: dark graphite + yellow + cyan industrial style; four ordinary rubber wheels, 2 rear motorized and 2 front passive on axles. Protection frame independent; default no task attachment, no LiDAR, no laser, no transmission chain. The central elevated camera is an independently removable sensor pack; user history currently prefers it installed but it must not become structural to the chassis.

## Options
- 2WD rubber/rubber: default.
- 2WD rear rubber + passive front Omni.
- Two motor, rear rubber to front Omni via side chain transmission.
- Two motor, rear rubber to front rubber via side chain transmission.
- New drive types need their own collider, wheel dynamics and tested turning behavior.

## Attachments
1. Push and collect frame; 2. Rotating sweeper; 3. Single pivot lift; 4. Linear forklift; 5. Ball launcher; 6. Multi-joint arm; 7. Magnetic slider; 8. Tilting bucket; 9. Two-stage linear lift and dual-block floor-pickup gripper.
Long-term: stacker, conveyors, 2x2 or 4x1 block movers, adaptive gripper, lift forks, telescopic booms, turntables, new launchers, racks and sensor bars.

## Sensor ecosystem
3 bottom ColorSensors aligned for 20mm line, front color reader with optical aperture, ultrasonic front/rear where fitted, optional single central elevated camera, LiDAR 360°, Laser range sensors, Gyro, GPS, touch end-stops. Visual sensor shells must mount firmly, and functional GEARS cores should be hidden only visually. A line-of-sight test must use optical origin and cone, not the entire sensor's bounding box.

## Technical priorities
P0: real collision-free modular base, mount integrity, chain path, accurate wheel pivots, baseline schema; P1: runtime physics, attachment dock interface, sensor vis/physics separation; P2: dynamic mission demos, stability/torque, camera segmentation; P3: optimized PBR presentation, automated CI QA and educational task configurations.

## Prior work
The validated appearance source is V3.8.5, built upon V3.8.3 geometry cleanups, V3.8.2 chain fix, 9 V3.7 attachments, V3.6.1 direct floor pickup and V3.4.x elevator work. Historical success is **visual/offline**, not a verified GEARS runtime endorsement.
