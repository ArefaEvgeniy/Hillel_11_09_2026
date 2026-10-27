from file_02 import Point


class Circle(Point):

    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def __str__(self):
        return f"Circle(x:{self.x}, y:{self.y}, radius:{self.radius})"


circle_1 = Circle(2, 10, 5)
print(circle_1)
print(circle_1.distance_from_origin())
