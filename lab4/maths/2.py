def calculate_area_trapezoid(height, base1, base2):
    area = (base1 + base2) / 2 * height
    return area

# Get input values
height = float(input("Height: "))
base1 = float(input("First base value: "))
base2 = float(input("Second base value: "))

# Calculate and print the area
area = calculate_area_trapezoid(height, base1, base2)
print("The area of the trapezoid is:", area)
