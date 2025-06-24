# create a base class shape with a method area().implement sub

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


r = Rectangle(5,3)

print("Area of Rectangle:", r.area())
