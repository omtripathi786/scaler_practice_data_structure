import copy

from magic_method import Point


class Rectangle:
    def __init__(self, *args):
        """
        Initialize a Rectangle object.

        Args:
            *args: Variable number of arguments. The constructor can be called in three ways:
                - With two Point objects representing the top-left and bottom-right corners.
                - With four integers representing the x and y coordinates of the top-left and bottom-right corners.
                - With a single Rectangle object for copying.

        Raises:
            ValueError: If invalid arguments are provided.
        """
        if len(args) == 2 and isinstance(args[0], Point) and isinstance(args[1], Point):
            self.topLeft = copy.deepcopy(args[0])  # Use deepcopy here
            self.bottomRight = copy.deepcopy(args[1])  # Use deepcopy here
        elif len(args) == 4 and all(isinstance(arg, (int, float)) for arg in args):
            self.topLeft = Point(args[0], args[1])
            self.bottomRight = Point(args[2], args[3])
        elif len(args) == 1 and isinstance(args[0], Rectangle):
            self.topLeft = copy.deepcopy(args[0].topLeft)
            self.bottomRight = copy.deepcopy(args[0].bottomRight)
        else:
            raise ValueError("Invalid arguments for Rectangle initialization.")
