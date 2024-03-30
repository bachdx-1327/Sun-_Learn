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
