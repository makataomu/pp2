import math

def calculate_area_regular_polygon(num_sides, side_length):
    apothem = side_length / (2 * math.tan(math.pi / num_sides))
    area = 0.5 * num_sides * apothem * side_length

    return area

# Get input from the user
num_sides = int(input("Input number of sides: "))
side_length = float(input("Input the length of a side: "))

# Calculate and print the area
area = calculate_area_regular_polygon(num_sides, side_length)
print("The area of the polygon is:", round(area, ndigits=5))
