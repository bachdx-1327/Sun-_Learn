# RESTfull API: Tìm hiểu về RESTful API

Hãy tưởng tượng bạn đang xây dựng một ngôi nhà thông minh.

- Bạn muốn hệ thống đèn tự động bật khi bạn về nhà.
- Bạn muốn hệ thống điều hòa tự động điều chỉnh nhiệt độ theo thời tiết.
- Bạn muốn hệ thống an ninh thông báo cho bạn khi có người lạ đột nhập.

Để thực hiện những điều này, bạn cần kết nối các thiết bị khác nhau trong nhà với nhau.

API RESTful có thể coi là "cánh cửa" giúp bạn kết nối mọi thứ. API RESTful là một giao diện mà hai hệ thống máy tính sử dụng để trao đổi thông tin một cách an toàn qua internet. Hầu hết các ứng dụng kinh doanh phải giao tiếp với các ứng dụng nội bộ và bên thứ ba khác để thực hiện tác vụ.

## API là gì?

Trước khi đi vào khái niệm về RESTful API, chúng ta sẽ dùng điểm qua một số kiến thức cơ bản về API. API là viết tắt của Application Programming Interface (Giao diện lập trình ứng dụng). Nó là một tập hợp các quy tắc và định nghĩa cho phép các phần mềm giao tiếp với nhau. API hoạt động như một "cánh cửa" giúp các ứng dụng kết nối và trao đổi dữ liệu. Về mặt kết quả thì API có thể trả về dữ liệu mà bạn cần cho ứng dụng của mình ở những kiểu dữ liệu phổ biến như JSON hay XML.

Ví dụ:

- **Bạn sử dụng ứng dụng đặt vé máy bay**: Ứng dụng này sử dụng API để kết nối với hệ thống đặt vé của hãng hàng không, lấy thông tin về các chuyến bay, giá vé và đặt vé cho bạn.
- **Bạn sử dụng mạng xã hội**: Mạng xã hội sử dụng API để kết nối với các ứng dụng khác, ví dụ như ứng dụng nhắn tin, cho phép bạn chia sẻ bài viết hoặc hình ảnh lên các ứng dụng khác.

Có nhiều loại API khác nhau, mỗi loại được sử dụng cho mục đích khác nhau.

Dưới đây là một số ví dụ về các loại API phổ biến:

- **API RESTful**: Loại API phổ biến nhất, được sử dụng để truy cập và thao tác dữ liệu trên web.
- **API GraphQL**: Loại API mới hơn, cho phép bạn truy cập dữ liệu một cách linh hoạt hơn.
- **API SOAP**: Loại API truyền thống hơn, được sử dụng để trao đổi dữ liệu giữa các ứng dụng web.

## RESTful API là gì?

Mình hiểu đơn giản thì RESTful API là một tiêu chuẩn dùng trong việc thiết kế API cho các ứng dụng web (thiết kế services) để tiện cho việc quản lý các resource.

REST (REpresentational StateTransfer) là một dạng chuyển đổi cấu trúc dữ liệu, một kiểu kiến trúc để viết API. Nó sử dụng phương thức HTTP đơn giản để tạo cho giao tiếp giữa các máy. Vì vậy, thay vì sử dụng một URL cho việc xử lý một số thông tin người dùng, REST gửi một yêu cầu HTTP như GET, POST, DELETE, vv đến một URL để xử lý dữ liệu.

Kết hợp nhiều ý lại với nhau thì chúng ta có RESTful API :3. Chức năng quan trọng nhất của REST là quy định cách sử dụng các HTTP method (như GET, POST, PUT, DELETE…) và cách định dạng các URL cho ứng dụng web để quản các resource. RESTful không quy định logic code ứng dụng và không giới hạn bởi ngôn ngữ lập trình ứng dụng, bất kỳ ngôn ngữ hoặc framework nào cũng có thể sử dụng để thiết kế một RESTful API.

## RESTful API hoạt động như thế nào?

### Định dạng cơ bản

Gồm có ba thành phần chính:

- **URL Endpoint**: Là một liên kết URL đại diện cho tài nguyên mà chúng ta muốn truy cập. Tài nguyên có thể là văn bản, hình ảnh, tài liệu hoặc bất kỳ mục dữ liệu nào. Ví dụ: example.com/surveys cho phép chúng ta xem hoặc tạo mẫu khảo sát và example.com/surveys/123/responses cho phép chúng ta thực hiện tương tự đối với tất cả các phản hồi của khảo sát 123.
- **HTTP verb**: Cho biết máy chủ những gì chúng ta muốn thực hiện với tài nguyên điểm cuối URL. Ví dụ, một yêu cầu POST có nghĩa là chúng ta muốn tạo một mẫu khảo sát mới và một yêu cầu GET có nghĩa là chúng ta muốn xem một mẫu khảo sát hiện có.
- **Body message**: Là một tải trọng tùy chỉnh tùy chọn chứa thông báo với các thuộc tính và giá trị mà chúng ta muốn sử dụng để tạo hoặc cập nhật một tài nguyên nhất định. Ví dụ: chúng ta muốn tạo một phản hồi mới cho khảo sát 123 đã thu thập được, bao gồm điểm NPS tích cực là 9, một tin nhắn phản hồi ngắn và ID duy nhất của người phản hồi đã cung cấp phản hồi.

### HTTP verb

Có 5 lệnh động từ cơ bản khi thực hiện yêu cầu HTTP:

- GET: Thực hiện yêu cầu chỉ đọc để xem một hoặc nhiều tài nguyên.
- POST: Tạo một tài nguyên mới dựa trên tải trọng được cung cấp trong thân của yêu cầu.
- DELETE: Hủy tài nguyên được cung cấp dựa trên ID được cung cấp.
- PUT: Cập nhật toàn bộ các trường của tài nguyên dựa trên thân được cung cấp hoặc tạo một tài nguyên mới nếu chưa tồn tại.
- PATCH: Chỉ cập nhật các trường của tài nguyên nếu nó tồn tại.
  Hầu hết các ứng dụng và tài nguyên sẽ hỗ trợ tất cả các lệnh này. Đây thường được gọi là ứng dụng CRUD:

| HTTP Verb | Chức năng   |
| --------- | ----------- |
| CREATE    | POST        |
| READ      | GET         |
| UPDATE    | PUT & PATCH |
| DELETE    | DELETE      |

### URL Endpoint

Điểm cuối URL trong API RESTful đại diện cho bất kỳ đối tượng, dữ liệu hoặc dịch vụ nào được API có thể truy cập. Ví dụ: example.com/surveys đại diện cho dữ liệu của tất cả các mẫu khảo sát và example.com/surveys/123/responses đại diện cho dữ liệu của tất cả các phản hồi cho một khảo sát nhất định.

## Kết luận

RESTful API là một phong cách kiến trúc phần mềm linh hoạt và hiệu quả để thiết kế các API web. RESTful API cung cấp nhiều lợi ích, bao gồm khả năng linh hoạt, khả năng mở rộng, dễ sử dụng và bảo mật. Khi thiết kế RESTful API, cần lưu ý một số yếu tố quan trọng, chẳng hạn như xác định các tài nguyên, thiết kế URI, sử dụng các phương thức HTTP chính xác, trả về mã trạng thái HTTP chính xác và tài liệu API.

## Reference

- https://viblo.asia/p/restful-api-la-gi-1Je5EDJ4lnL
- https://aws.amazon.com/vi/what-is/restful-api/
- https://mannhowie.com/rest-api
