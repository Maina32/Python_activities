#Program for volume of a cylinder
import math

def cylinder_volume(radius, height):
   
    return math.pi * (radius ** 2) * height


r = 4
h = 20
print(f"The volume of the cylinder is: {cylinder_volume(r, h):.2f}")

