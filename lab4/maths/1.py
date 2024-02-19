import math

def deg_to_rad(degrees):
    return degrees * math.pi / 180

degree = 15
radian = deg_to_rad(degree)
print(f"Output radian: {radian:.6}")
