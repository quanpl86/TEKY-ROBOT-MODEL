# Low-poly procedural GLB draft — NOT the V3.8.5 production model

These four `*_DRAFT.glb` files have been directly uploaded as **actual binary GLB** to GitHub through the Git blob interface. They are preliminary lightweight geometry proving that all four drivetrain combinations can be represented as separate assets.

They are deliberately **not** equivalent to the high-detail V3.8.5 robot and should **not** be used as a production design, source for wheel colliders, or replacement for the reviewed full asset family.

- No LiDAR, laser, attachments or chain in the default draft.
- Rear motors visually represented, front wheels passive in default model.
- Chain variants have separate left/right sprocket chains. **Visual motion only; no real physics coupling certified**.
- 3 bottom line sensor housings, front ultrasonic and removable central camera represented schematically.
- Guard is excluded from production Base by architecture; any visual frame in these draft proof-of-pipeline files is only a schematic placeholder and must not create an extra physical collider if a dedicated Guard GLB is attached.

**Authoritative high-fidelity 32-GLB release** is delivered separately as `TEKY_ROVER_GITHUB_COMPLETE_ASSETS_AND_SOURCE.zip`, with exact V3.8.5-derived material and 9 historical attachments. These binaries have **not yet been pushed to repository main**. Run `scripts/publish_assets.sh` from that extracted package against a local clone to upload the exact binaries.
