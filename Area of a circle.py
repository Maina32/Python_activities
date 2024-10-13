#Program for area of a circle
def area_of_circle():
    radius = float(input("Enter the radius: "))
    area = 3.1434567 * (radius ** 2)
    print(f"The area of the circle is: {area: .2f}")
    
area_of_circle()