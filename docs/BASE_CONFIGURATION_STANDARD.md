# Chuẩn cấu hình Base Robot & hệ truyền động (đã chốt)

**Tài liệu nguồn chuẩn cho mọi AI Agent, thiết kế GLB, manifest và cấu hình TEKY Rover.**

## 1. Base mặc định
- Chassis và khung bảo vệ: **hai asset độc lập**, ghép cơ khí bằng gá cố định. Không dùng combined GLB như cấu hình vật lý runtime.
- **4 bánh cao su thường**, không dùng bánh Omni.
- Hai bánh **sau** chủ động, mỗi bánh gắn một motor riêng: trái `outA`, phải `outB` (mapping dự kiến, cần đối chiếu cấu hình port runtime).
- Hai bánh **trước** bị động, chỉ có trục, ổ quay, không nhận truyền động và không có cổng motor.
- **Không attachment** ở `Attachment_Dock_Front`, **không LiDAR**, **không laser**, **không xích** ở cấu hình mặc định.
- Các cảm biến line, ultrasonic, camera trung tâm (nếu được chọn) thuộc **Sensor Pack**, không phải hình học không thể tháo khỏi chassis. Không mặc nhiên xóa camera hay cảm biến dò line đã chốt ở các phiên bản trước.

## 2. Bốn cấu hình chọn trong Robot Selector

| ID | Bánh sau | Bánh trước | Lực quay bánh trước | Motor |
|---|---|---|---|---|
| `default_4rubber_2wd` | 2 bánh cao su chủ động | 2 bánh cao su bị động | Quay tự do | 2 |
| `mixed_omni_2wd` | 2 bánh cao su chủ động | 2 bánh Omni bị động | Quay tự do, con lăn giảm ma sát ngang | 2 |
| `mixed_omni_chain` | 2 bánh cao su chủ động | 2 bánh Omni | Xích truyền mô-men riêng trái/phải từ bánh sau | 2 |
| `four_rubber_chain` | 2 bánh cao su chủ động | 2 bánh cao su | Xích truyền mô-men riêng trái/phải từ bánh sau | 2 |

**Lưu ý quan trọng:** Hai mẫu có xích là dẫn động cả hai trục từ **hai motor**; bánh trước không có motor điện riêng. Nếu dùng cách gọi 4WD, cần phân biệt cơ khí có bốn bánh nhận mô-men với native `WheelActuator` bốn động cơ (không phải cấu hình này).

## 3. Cơ khí chung
- Bốn cấu hình dùng **cùng chuẩn dock attachment, cùng khung chassis**, chỉ thay wheel kit + transmission kit tương ứng.
- Bánh sau giữ nguyên kiểu cao su bám đường. Bánh trước thay giữa **cao su bị động** và **Omni bị động/được kéo qua xích**.
- Hai bộ nhông–xích khi có: một bên trái, một bên phải; nhông 12T/12T, tỉ số danh định 1:1; khoảng cách trục nguồn V3.8.x khoảng 167 mm; chuyển động nhánh thẳng tiếp tuyến với vòng chia, không đi xuyên tâm nhông.
- Khung bảo vệ bánh và xích phải là asset riêng (`Protection_Frame_Root`) có collider độc lập về mặt authoring, fixed với chassis lúc mô phỏng.
- Đừng nhân đôi rigid body/mesh khi đã load GLB preview lắp tổng thể.
- Kích thước GLB tính bằng mét, TEKY cấu hình tọa độ cm khi đã xác nhận schema; +X phải, +Y lên, +Z trước.

## 4. Ranh giới kỹ thuật và trạng thái
- Tệp `configs/drivetrains/*.json` là **cấu hình dự án tham chiếu**, không phải JSON native TEKY import được ngay.
- Hệ xích có **animation khác với mô phỏng truyền lực**; TEKY phải triển khai/kiểm chứng khớp/coupling vật lý.
- Bản `assets/prototypes/v4_procedural_studies/*_DRAFT.glb` dùng xác minh pipeline, chưa thay model V3.8.5. Các GLB high-fidelity và 9 attachment còn có bước publish riêng theo `docs/RELEASE_STATUS.md`.
- Kiểm tra bánh thường trước: chiều rộng, trục gắn, khe hở guard và collision; bánh cao su trước hiện là thiết kế cần QA bổ sung.

## 5. Hợp đồng phân lớp
```text
Robot_Root
├── Chassis_Root                      # thân robot và hai motor sau
├── Protection_Frame_Root             # tách asset/collider; fixed-to-chassis
├── Drive_System
│   ├── Wheel_Rear_Left               # driven outA
│   ├── Wheel_Rear_Right              # driven outB
│   ├── Wheel_Front_Left              # passive OR chain-coupled
│   ├── Wheel_Front_Right             # passive OR chain-coupled
│   ├── Chain_Drive_Left [optional]
│   └── Chain_Drive_Right [optional]
├── Sensor_Packs                       # line/ultrasonic/camera as configured
└── Attachment_Dock_Front
    └── Attachment_Root [none by default, one when selected]
```

**Tiêu chí chấp nhận cấu hình mặc định:** 4 bánh cao su, 2 motor sau độc lập, 2 bánh trước quay tự do, không xích, không attachment, không LiDAR/laser, guard riêng có gá, trục bánh/pivot chính xác. Mọi cấu hình phải vượt QA hình học và GEARS runtime trước khi gắn nhãn `RUNTIME_ACCEPTED`.
