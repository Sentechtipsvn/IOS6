# Quy ước phạm vi dự án — iOS 6 Huyền Thoại

Ngày chốt: 19/11/2026 · Chủ dự án: © Sentechtipsvn

## Kết quả thử nghiệm hiện có

- Thiết bị thực tế: **iPhone 7 Plus — iOS 15.8.8 — Dopamine rootless**.
- Theme thử nghiệm **iOS 6 Reference (Local)** đã được chủ dự án cài, SnowBoard nhận và bật thành công.
- Hình ảnh chủ dự án gửi cho thấy icon ứng dụng hệ thống và màn hình chính mang phong cách iOS 6 rõ rệt.
- SnowBoard báo **38 icons, 0 extensions**. Con số này là thống kê theme, **không xác nhận đủ 38 ứng dụng đã được đổi icon**.
- Giai đoạn hiện tại: **kiểm thử nội bộ cá nhân**; chưa phát hành bản Stable.

## Quyết định sản phẩm bắt buộc

### 1) Theme iOS 6 — miễn phí hoàn toàn
- **Miễn phí vĩnh viễn**; không có Pro, paywall hoặc cơ chế license thương mại.
- Chỉ tập trung vào **Home Screen**, **app icons**, **Dock/biểu tượng thư mục**, hình nền/giao diện trang chủ khi có phương án an toàn; bổ sung icon xuất hiện **bên trong ứng dụng Cài đặt** nếu cơ chế theme/extension tương thích cho phép.
- Không chứa code hook SpringBoard cho khóa máy/status bar/audio. Các chức năng phụ phải riêng biệt, không được khiến gói icon phụ thuộc vào tweak hệ thống.
- Có thể mở rộng bộ icon ứng dụng bên thứ ba; phải kiểm tra từng Bundle ID thực tế.
- Đóng gói icon rootless để bật/tắt và gỡ sạch từ SnowBoard/Sileo; giữ nguyên cấu hình và dữ liệu người dùng.
- Chỉ công bố là tương thích những phiên bản iOS/thiết bị đã được kiểm thử thật.

### 2) System tweak — dự án/module độc lập
- Nghiên cứu riêng **Lock Screen**, cử chỉ mở/khóa máy, âm thanh khóa/mở khóa, âm thanh sạc, **status bar** và các hiệu ứng UI.
- Gói, mã định danh, lịch phát hành, cài đặt, xử lý lỗi và cơ chế gỡ bỏ **tách khỏi theme icon**.
- Không chỉnh trực tiếp phân vùng hệ thống hay MobileGestalt; thử module riêng để tránh Safe Mode.
- Không được tự động cài hoặc bắt buộc phải có tweak hệ thống khi cài theme.
- Tweak riêng **chưa được xác nhận khả thi** cho iOS 15.8.8; cần nghiên cứu/kiểm thử từng chức năng.

## Quy định phát hành và quyền sử dụng

- **Bản hiện tại** dùng icon tham chiếu lịch sử từ fork `Sentechtipsvn/iOS-6-Icons` để **Sếp thử nội bộ**.
- Miễn phí **không đồng nghĩa có quyền tái phân phối**. Icon Apple hoặc của bên thứ ba có quyền sở hữu riêng; kho fork công khai không tự động trao giấy phép.
- **Không phát hành public gói icon nguyên bản đã trích xuất** trước khi có quyền phù hợp hoặc thay bằng bản thiết kế độc lập/được cấp phép. Cần ghi rõ attribution và điều kiện license nơi áp dụng.
- Bản theme công cộng sau này **Free 100%** và tuân thủ quyền tác giả, nhãn hiệu.
- Không nhầm artifact test ngắn hạn với bản Stable/Release chính thức.

## Thứ tự phát triển
1. 0.2 — Chốt chất lượng icon, hoàn chỉnh danh mục/Bundle ID, kiểm thử độ ổn định và thao tác bật/tắt theme.
2. 0.3 — Kiểm tra icon trong Settings, bổ sung Home Screen/Folder/Dock theo cấu hình SnowBoard an toàn, không hook hệ thống.
3. Theme Free — Chuẩn hóa artwork được phép chia sẻ, tài liệu Việt/Anh, khả năng gỡ sạch; công khai chỉ khi đủ điều kiện.
4. System Tweak — Mở dự án riêng và nghiên cứu độc lập Lock Screen, âm thanh, status bar.

**Nguyên tắc không thay đổi:** THEME chỉ làm đẹp giao diện chính và biểu tượng; TWEAK hệ thống là sản phẩm riêng, không gộp.
