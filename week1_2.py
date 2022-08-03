import math

class Formula:
    def perimeter(self):
        pass
    def area(self):
        pass

class Rectangle(Formula):
    def perimeter(self, l, b):
        return 2 * (l + b)
    def area(self, l, b):
        return l * b

class Circle(Formula):
    def perimeter(self, r):
        return 2 * 3.14 * r
    def area(self, r):
        return 3.14 * r * r

class Triangle(Formula):
    def perimeter(self, a, b, c):
        return a + b + c
    def area(self, a, b, c):
        s = int((a + b + c)/2)
        a=(s*(s-a)*(s-b)*(s-c))**0.5
        return a

x = Rectangle()
y = Circle()
z = Triangle()
print("Perimeter of Rectangle:", x.perimeter(10, 20))
print("Area of Rectangle:", x.area(10, 30))
print("Perimeter of Circle:", y.perimeter(5))
print("Area of Circle:", y.area(5))
print("Perimeter of Triangle:", z.perimeter(5, 6, 7))
print("Area of triangle:", z.area(5, 6, 7))