class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        pass
        return f"Point(x:{self.x}, y:{self.y})"

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


if __name__ == "__main__":
    point_1 = Point(3, 4)
    point_2 = Point(6)
    point_3 = Point(y=4, x=3)

    print(f"x: {point_3.x}, y: {point_3.y}")
    print(point_3)
    print(point_2)

    print(point_1.distance_from_origin())

    print(point_1 == 34)
    print(point_1 == point_3)

    point_4 = point_1 + point_2
    print(point_4)
    print(point_1)

    # PyGame
