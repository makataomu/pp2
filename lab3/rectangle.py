from shape import Shape

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
        self.compute_area()

    def compute_area(self):
        self.object_area = self.length * self.width

    def area(self):
        super().area(area=self.object_area)


rec = Rectangle(2,4)
rec.area()