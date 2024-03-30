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