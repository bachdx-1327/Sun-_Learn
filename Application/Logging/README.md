# Log cho Python, sử dụng sao cho đúng và dễ nhận biết?

## Tại sao chúng ta lại cần sử dụng log trong python

Mục tiêu tối thượng của nó có lẽ đó là nhận biết các lỗi dễ dàng và thuận tiện hơn so với việc chúng ta print kết quả của nó ra liên tục.

Đây là module tiêu chuẩn (được pack kèm bộ cài mặc định) do cộng đồng Python phát triển, dễ dàng sử dụng và cực kỳ linh hoạt. Logging cung cấp cho lập trình viên những tiện ích như:

- Phân chia level cho các thông báo lỗi, cho phép tuỳ chọn mức độ nghiêm trọng của các thông báo, cho phép hoặc không cho phép hiển thị một thông báo đã được phân loại. Cho phép cấu hình output của thông báo lỗi là trên console hoặc file hoặc nguồn khác Lập trình viên có thể chọn các mức sau khi viết nội dung log, các mức được liệt kê có độ nghiêm trọng lớn dần.

Mức Nội dung

- DEBUG Thông tin chi tiết, thường là thông tin để tìm lỗi
- INFO Thông báo thông thường, các thông tin in ra khi chương trình chạy theo đúng kịch bản
- WARNING Thông báo khi nghi vấn bất thường hoặc lỗi có thể xảy ra, tuy nhiên chương trình vẫn có thể hoạt động
- ERROR Lỗi, chương trình có thể không hoạt động được một số chức năng hoặc nhiệm vụ nào đó, thường thì nên dùng ghi bắt được Exception
- CRITICAL Lỗi, chương trình gặp lỗi nghiêm trọng không thể giải quyết được và bắt buộc phải dừng lại

## Sử dụng module logging cơ bản
