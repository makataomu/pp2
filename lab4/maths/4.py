def calculate_parallelogram_area(base, height):
    area = base * height
    return area

# Get input from the user
base = float(input("Enter the length of base: "))
height = float(input("Enter the height of parallelogram: "))

# Calculate and print the area
area = calculate_parallelogram_area(base, height)
print("The area of the parallelogram is:", round(area, ndigits=4))
