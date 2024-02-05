from shape import Shape

class Square(Shape):
    def __init__(self, length):
        super().__init__()  
        self.length = length

    def area(self):
        self.object_area = self.length * self.length  
        super().area(area=self.object_area)


square = Square(3)
square.area()  

shape = Shape() 
shape.area()  
