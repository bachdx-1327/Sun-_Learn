# SOLID Design Principles với Python

Lập trình hướng đối tượng (OOP) là một phương pháp lập trình phổ biến giúp tổ chức mã thành các lớp và đối tượng. Tuy nhiên về việc thiết kế các lớp và đối tượng hiệu quả không phải là việc dễ dạng. Và có một quy chuẩn được giới thiệu trong [Design Principles and Design Patterns] của Robert C.Martin.

SOLID là từ viết tắt của 5 nguyên tắc quan trọng khi làm việc với lập trình hướng đối tượng:

- S - Single Responsibility Principle
- O - Open/Closed Principle
- L - Liskov Substitution Principle
- I - Interface Segregation Principle
- D - Dependency Inversion Principle

## Single Responsibility Principle (SRP)

**Giải thích**

Quy tắc SRP (Single Responsibility Principle) là là một trong những nguyên tắc thiết kế quan trọng nhất trong lập trình hướng đối tượng (OOP). Quy tắc này nêu rằng:

**Mỗi lớp chỉ nên có một trách nhiệm duy nhất.**

Điều này có nghĩa là mỗi lớp chỉ nên tập trung vào một chức năng cụ thể và không nên thực hiện các công việc không liên quan.

Vậy tại sao chúng ta lại phải đơn nhiệm?

Lý do chính cho việc áp dụng quy tắc đơn nhiệm là để giúp cho mã dễ hiểu dễ bảo trì và dễ mở rộng hơn.
Hãy tưởng tượng có bạn có một chiếc máy có thể làm tất cả mọi thứ: vừa có thể nướng bánh, vừa có thể giặt quần áo, rửa bát đĩa, ... Nghe có vẻ thật là tiện lợi nhưng cũng có thể đem đến một cố vấn đề không hề nhỏ: Ví dụ như chỉ cần dùng một chức năng nhỏ thôi nhưng vẫn phải khởi động toàn bộ lên, hoặc là khởi động sẽ rất cầu kì, muốn phát triển một tính năng thì cũng khá là khó khăn, ... Vì thế chúng ta nên để nó tách ra theo từng chức năng cụ thể của vật dụng đó.

Ví dụ cho một đoạn code vi phạm SRP:

```
class Employee:
  def __init__(self, name, salary, vacation_days):
    self.name = name
    self.salary = salary
    self.vacation_days = vacation_days

  def calculate_paycheck(self):
    return self.salary / 2

  def request_vacation(self, days):
    if self.vacation_days >= days:
      self.vacation_days -= days
      return True
    else:
      return False

  def send_email(self, email_address, message):
    # Gửi email
    pass
```

Và tuân theo SRP

```
class EmployeeInfo:
  def __init__(self, name, salary, vacation_days):
    self.name = name
    self.salary = salary
    self.vacation_days = vacation_days

class Payroll:
  def __init__(self, employee_info):
    self.employee_info = employee_info

  def calculate_paycheck(self):
    return self.employee_info.salary / 2

class VacationTracker:
  def __init__(self, employee_info):
    self.employee_info = employee_info

  def request_vacation(self, days):
    if self.employee_info.vacation_days >= days:
      self.employee_info.vacation_days -= days
      return True
    else:
      return False

class Email:
  def __init__(self):
    pass

  def send_email(self, email_address, message):
    # Gửi email
    pass

class Employee:
  def __init__(self, name, salary, vacation_days):
    self.name = name
    self.salary = salary
    self.vacation_days = vacation_days
    self.payroll = Payroll(self)
    self.vacation_tracker = VacationTracker(self)
    self.email = Email()

  def calculate_paycheck(self):
    return self.payroll.calculate_paycheck()

  def request_vacation(self, days):
    return self.vacation_tracker.request_vacation(days)

  def send_email(self, email_address, message):
    self.email.send_email(email_address, message)
```

## Open Close Principle (OCP)

**Lớp (class) nên mở rộng cho hành vi mới, nhưng đóng đối với sửa đổi.**

Điều này có nghĩa là:

- **Mở rộng**: Bạn có thể thêm chức năng mới vào lớp mà không cần sửa đổi mã hiện có của lớp.
- **Đóng**: Bạn không được sửa đổi mã hiện có của lớp để thêm chức năng mới.

**Phương án:**

- Mỗi khi muốn thêm chức năng mới cho chương trình ta nên viết class mới mở rộng class cũ
- Thực

**Lợi ích:**

Việc áp dụng OCP mang lại nhiều lợi ích, bao gồm:

- **Dễ bảo trì**: Việc sửa đổi mã hiện có có thể dẫn đến lỗi. OCP giúp bạn tránh sửa đổi mã hiện có, do đó giảm nguy cơ lỗi.
- **Dễ mở rộng**: OCP giúp bạn dễ dàng thêm chức năng mới vào lớp mà không cần sửa đổi mã hiện có.
- **Tái sử dụng**: OCP giúp bạn dễ dàng tái sử dụng mã vì bạn có thể mở rộng lớp hiện có thay vì tạo ra một lớp mới.

Ví dụ:

```
class Car:
  def __init__(self, speed):
    self.speed = speed

  def move(self):
    print(f"Car is moving at {self.speed} km/h")
```

Nếu bạn muốn thêm chức năng mới thì bạn cần tạo một class mới và kế thừa lại từ lớp cũ và viết thêm code đằng sau:

```
class Car:
  def __init__(self, speed):
    self.speed = speed

  def move(self):
    print(f"Car is moving at {self.speed} km/h")

class SelfDrivingCar(Car):
  def __init__(self, speed):
    super().__init__(speed)

  def move(self):
    if self.is_self_driving:
      print("Car is driving itself")
    else:
      super().move()

  def enable_self_driving(self):
    self.is_self_driving = True

  def disable_self_driving(self):
    self.is_self_driving = False
```

## Liskov substitution principle (LSP)

**Trong một chương trình, các object của class con có thể thay thế class cha mà không làm thay đổi tính đúng đắn của chương trình.**

Có thể nói rõ hơn là nếu một chương trình sử dụng một đối tượng của lớp cha thì chương trình đó cũng có thể sử dụng một đối tượng của lớp con thay thế mà không cần sửa đổi mã.

Thật sự là vẫn chưa rõ ràng lắm nhỉ, xem thử một ví dụ về lỗi này.

```
class Shape:
  def area(self):
    raise NotImplementedError

class Rectangle(Shape):
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def area(self):
    return self.width * self.height

class Square(Shape):
  def __init__(self, side_length):
    self.side_length = side_length

  def area(self):
    return self.side_length ** 2

def print_area(shape):
  print(f"The area of the shape is {shape.area()}")

# Tạo một hình chữ nhật
rectangle = Rectangle(5, 10)

# In diện tích hình chữ nhật
print_area(rectangle)

# Tạo một hình vuông
square = Square(5)

# In diện tích hình vuông
print_area(square)
```

Output sẽ là

```
The area of the shape is 50
The area of the shape is 25
```

Tuy nhiên, nếu bạn thay thế rectangle bằng square trong hàm print_area(), mã sẽ in ra:

```
The area of the shape is 25
```

Giải quyết:

Đưa thêm thuộc tính vào class con.

```
class Shape:
  def area(self):
    raise NotImplementedError

class Rectangle(Shape):
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def area(self):
    return self.width * self.height

class Square(Rectangle):
  def __init__(self, side_length):
    super().__init__(side_length, side_length)

def print_area(shape):
  print(f"The area of the shape is {shape.area()}")
```

## Interface segregation principle (ISP)

**Thay vì dùng 1 interface lớn, ta nên tách thành nhiều interface nhỏ, với nhiều mục đích cụ thể**

Đoạn này sẽ dễ hiểu hơn một chút, chúng ta nên tấch interface ra thành nhiều interface nhỏ, gồm các method liên quan đến nhau để thuận tiện cho vuệc implement và quản lý.

```
class Animal:
  def eat(self):
    raise NotImplementedError

  def sleep(self):
    raise NotImplementedError

  def move(self):
    raise NotImplementedError

class Dog(Animal):
  def eat(self):
    print("Dog is eating")

  def sleep(self):
    print("Dog is sleeping")

  def move(self):
    print("Dog is moving")

class Cat(Animal):
  def eat(self):
    print("Cat is eating")

  def sleep(self):
    print("Cat is sleeping")

  def move(self):
    print("Cat is moving")
```

Chuyển sang theo quy tắc ISP thành:

```
class Eater:
  def eat(self):
    raise NotImplementedError

class Sleeper:
  def sleep(self):
    raise NotImplementedError

class Mover:
  def move(self):
    raise NotImplementedError

class Dog(Eater, Sleeper, Mover):
  def eat(self):
    print("Dog is eating")

  def sleep(self):
    print("Dog is sleeping")

  def move(self):
    print("Dog is moving")

class Cat(Eater, Sleeper, Mover):
  def eat(self):
    print("Cat is eating")

  def sleep(self):
    print("Cat is sleeping")

  def move(self):
    print("Cat is moving")
```

## Dependency inversion principle (DIP)

    Các module cấp cao không nên phụ thuộc vào các modules cấp thấp. Cả 2 nên phụ thuộc vào abstraction.
    Interface (abstraction) không nên phụ thuộc vào chi tiết, mà ngược lại. ( Các class giao tiếp với nhau thông qua interface, không phải thông qua implementation.)

Ví dụ:

```
class Car:
  def __init__(self):
    self.engine = Engine()

  def start_engine(self):
    self.engine.start()

class Engine:
  def start(self):
    print("Engine is starting")
```

Lớp Car phụ thuộc trực tiếp vào lớp Engine. Việc thay đổi lớp Engine sẽ ảnh hưởng đến lớp Car.

Chỉnh lại theo DIP:

```
class Engine:
  def start(self):
    raise NotImplementedError

class Car:
  def __init__(self, engine: Engine):
    self.engine = engine

  def start_engine(self):
    self.engine.start()

class ElectricEngine(Engine):
  def start(self):
    print("Electric engine is starting")

class GasolineEngine(Engine):
  def start(self):
    print("Gasoline engine is starting")
```

Sử dụng kế thừa và tính trừu tượng để giúp cho lớp Cả không trực tiếp phụ thuộc vào lớp Engine.

## Kết luận

SOLID Design Principles là tập hợp các nguyên tắc thiết kế quan trọng giúp bạn tạo ra mã OOP chất lượng cao. Bài viết này đã giới thiệu 5 nguyên tắc SOLID và cách áp dụng chúng trong Python. Việc áp dụng SOLID Design Principles sẽ giúp bạn viết mã dễ đọc, dễ hiểu, dễ bảo trì và có thể mở rộng.
