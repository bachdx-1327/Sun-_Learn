# Docstring and Typehint

Docstring là chuỗi văn bản được sử dụng để mô tả chức năng, lớp hoặc module trong Python. Docstring được viết bằng ngôn ngữ tự nhiên, dễ hiểu, giúp người đọc hiểu được mục đích, cách sử dụng và các thành phần của code.

Example:

```
def greet(name):
  """
  This function greets the person by name.

  Args:
      name: The name of the person to greet. (str)

  Returns:
      A greeting message. (str)
  """
  return f"Hello, {name}!"

message = greet("Bard")
print(message)
```

Typehint là cách để khai báo kiểu dữ liệu cho biến, tham số và giá trị trả về của hàm trong Python. Typehint giúp tăng khả năng đọc hiểu code, phát hiện lỗi sớm và cải thiện hiệu suất code

```
def greet(name: str) -> str:
  """Greets the person by name."""
  return f"Hello, {name}!"

message = greet("Bard")  # Type checking can happen here with static type checkers
print(message)
```

Lợi ích khi sử dụng Docstring và Typehint:

- Tăng khả năng đọc hiểu code: Docstring và Typehint giúp code dễ hiểu hơn cho cả người viết và người đọc.
- Phát hiện lỗi sớm: Typehint giúp phát hiện lỗi sai kiểu dữ liệu ngay trong quá trình viết code.
- Cải thiện hiệu suất code: Typehint giúp trình thông dịch Python tối ưu hóa code hiệu quả hơn.
