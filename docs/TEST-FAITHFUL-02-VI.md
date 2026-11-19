# Đường dẫn thử nghiệm iOS6 Faithful 0.2 (iPhone 7 Plus)

Bản này dùng icon từ repo Sếp đã fork làm **mẫu tham chiếu cá nhân**, không phải bộ icon Sentech đã được cấp quyền phát hành thương mại. Không đưa gói này lên kho Sileo công khai.

## Tải trên iPhone (không cần máy tính)
1. Mở trang [GitHub Actions của nhánh thử nghiệm](https://github.com/Sentechtipsvn/IOS6/actions/workflows/faithful-personal-test.yml).
2. Mở workflow chạy thành công gần nhất (**biểu tượng xanh**).
3. Trong mục **Artifacts**, chọn `iOS6-Faithful-0.2-PERSONAL-TEST-ONLY` để tải ZIP (GitHub có thể yêu cầu đăng nhập).
4. Giải nén ZIP bằng ứng dụng Tệp/Filza. Bên trong có tệp `.deb`.
5. Mở `.deb` bằng Filza/Sileo, cài đặt.
6. Vào Cài đặt → SnowBoard → Themes, chọn **iOS 6 Reference (Local)**, rồi áp dụng nếu SnowBoard yêu cầu.

**Đây là package riêng** `com.sentechtipsvn.retro6.reference-local`, không ghi đè package `com.sentechtipsvn.retro6.icons`. Chọn lại Retro 6 nếu muốn so sánh. Bản này thay icon, không thay giao diện khóa, âm báo hay hoạt ảnh.

**Lưu ý:** Bundle ID các ứng dụng bên thứ ba có thể không trùng với app trên máy. Nếu không thấy icon đổi, ghi lại tên app để chỉnh sau. Test icon Phone/Safari/Camera/Settings trước; kiểm tra respring, Safe Mode và khả năng trở về giao diện gốc.

**Tình trạng pháp lý:** Repo ảnh tham chiếu công khai không có giấy phép rõ ràng; phần lớn icon Apple là tài nguyên của Apple. Workflow không commit ảnh đó vào git và không tạo GitHub Release, nhưng artifact trong repo công khai không phải kênh phân phối riêng tư tuyệt đối. Chỉ dùng gói làm bản thử nghiệm; không chuyển tiếp, quảng bá tải xuống hoặc bán khi chưa có quyền cần thiết.

**Khôi phục:** tắt `iOS 6 Reference (Local)` trong SnowBoard và xóa `com.sentechtipsvn.retro6.reference-local` trong Sileo.
