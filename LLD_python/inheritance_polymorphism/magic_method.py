import copy


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __copy__(self):
        return Point(self.x, self.y)

    def __deepcopy__(self, memo):
        if memo is None:
            memo = {}
        return Point(self.x, self.y)


