import math
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius **2
        
    def perimeter(self):
        return 2 * math.pi * self.radius
radius  = int (input("Enter radius:"))
circ = Circle (radius)
print(f"The area is{circ.area()}")
print(f"The perimeter is{circ.perimeter()}")
print(f"Radius: {circ.radius}")
circ.area()
circ.perimeter()
circ.radius


