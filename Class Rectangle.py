import math
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width 
        
    def perimeter(self):
        return 2 * (self.length + self.width)
length  = int (input("Enter length:"))
width  = int (input("Enter width:"))
rect = Rectangle (length,width)
print(f"The area is{rect.area()}")
print(f"The perimeter is{rect.perimeter()}")
print(f"Length: {rect.length}")
print(f"Width: {rect.width}")
rect.area()
rect.perimeter()
rect.length
rect.width


