#Program to find surface area of a cylinder
import math
def surface_area_of_cylinder(radius, height):
    # Surface Area formula: SA = 2πr² + 2πrh
    surface_area = 2 * math.pi * radius **2  + 2 * math.pi * radius * height
    return surface_area
radius = float(input("Enter the radius of the cylinder:"))
height = float(input("Enter the height of the cylinder:"))
surface_area = surface_area_of_cylinder(radius, height)
print("surface area:",surface_area)
   