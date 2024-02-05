import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, x_change, y_change):
        self.x += x_change
        self.y += y_change

    def dist(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

point1 = Point(3, 4)
point2 = Point(1, 1)

point1.show()

point1.move(1, 1)
point1.show()

print("Distance:", point1.dist(point2))
