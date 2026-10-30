# TEKY ROBOT MODEL — Modular Rover

Kho asset 3D, cấu hình cơ khí và tài liệu R&D cho **TEKY Modular Rover** dùng trong TEKY ROBOT / GEARS, BabylonJS, Godot và chương trình Robotics/STEM.

> **Quy tắc chuẩn (2026-10-30):** Base chuẩn **4 bánh cao su thường** gồm **2 bánh sau chủ động + 2 bánh trước bị động**, **không attachment, không LiDAR, không laser**. Camera trung tâm, ba cảm biến dò line và ultrasonic là module được quản lý riêng; một cấu hình có thể chọn chúng theo manifest.

## Cấu hình truyền động
| ID | Bánh sau | Bánh trước | Truyền từ sau sang trước | Trạng thái |
|---|---|---|---|---|
| `default_4rubber_2wd` | 2 bánh cao su, motor độc lập | 2 bánh cao su bị động | Không | Base mặc định |
| `mixed_omni_2wd` | 2 bánh cao su chủ động | 2 bánh Omni bị động | Không | Tùy chọn |
| `mixed_omni_chain` | 2 bánh cao su chủ động | 2 bánh Omni nhận truyền động | 2 xích riêng, 1:1 | Tùy chọn kỹ thuật |
| `four_rubber_chain` | 2 bánh cao su chủ động | 2 bánh cao su nhận truyền động | 2 xích riêng, 1:1 | Tùy chọn kỹ thuật |

Giữ riêng `Chassis`, `Protection_Frame`, `Wheels/Drive`, `Sensors` và `Attachments`. Không được dùng file `*_VISUAL_ONLY.glb` làm nguồn vật lý kết hợp với các part riêng để tránh trùng collider/mesh.

## Lưu ý nghiệm thu
Asset hình học khác với cấu hình chạy thật. Native GEARS joints, sensors, motors, mass, friction và va chạm phải được kiểm chứng riêng. Các phiên bản V3.8.x gốc là tài liệu di sản và nguồn kiểm tra, **không mặc định là cấu hình tối thiểu**.

Xem `AGENTS.md`, `docs/`, `configs/`, `assets/`, `qa/` và `scripts/` để phát triển.

## Cấu hình Base chuẩn đã chốt
Đọc **[Base Configuration Standard](docs/BASE_CONFIGURATION_STANDARD.md)** và file nguồn [robot_family.json](configs/robot_family.json) trước khi dựng hoặc sửa model. Có bốn profile riêng trong [configs/drivetrains/](configs/drivetrains/). Default là **4 bánh cao su, 2 bánh sau chủ động, 2 bánh trước bị động**, **không attachment/LiDAR/laser/xích**.
