import unittest

from magic_method import Point
from rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_constructor_with_coordinates(self):
        rectangle = Rectangle(1, 2, 3, 4)
        self.assertEqual(rectangle.topLeft.x, 1)
        self.assertEqual(rectangle.topLeft.y, 2)
        self.assertEqual(rectangle.bottomRight.x, 3)
        self.assertEqual(rectangle.bottomRight.y, 4)

    def test_constructor_with_points(self):
        topLeft = Point(1, 2)
        bottomRight = Point(3, 4)
        rectangle = Rectangle(topLeft, bottomRight)
        self.assertEqual(rectangle.topLeft, topLeft)
        self.assertEqual(rectangle.bottomRight, bottomRight)
        self.assertIsNot(rectangle.topLeft, topLeft)
        self.assertIsNot(rectangle.bottomRight, bottomRight)

    def test_constructor_with_rectangle(self):
        originalRectangle = Rectangle(1, 2, 3, 4)
        copiedRectangle = Rectangle(originalRectangle)
        self.assertEqual(originalRectangle.topLeft, copiedRectangle.topLeft)
        self.assertEqual(originalRectangle.bottomRight, copiedRectangle.bottomRight)
        self.assertIsNot(originalRectangle.topLeft, copiedRectangle.topLeft)
        self.assertIsNot(originalRectangle.bottomRight, copiedRectangle.bottomRight)

    def test_constructor_with_invalid_arguments(self):
        # Test constructor with invalid number of arguments
        with self.assertRaises(ValueError):
            rectangle = Rectangle()

        with self.assertRaises(ValueError):
            rectangle = Rectangle(1, 2, 3)

        with self.assertRaises(ValueError):
            rectangle = Rectangle(Point(1, 2), Point(3, 4), Point(5, 6))


if __name__ == "__main__":
    unittest.main()
    rect1 = Rectangle(1, 2, 3, 4)
    rect2 = Rectangle(Point(1, 2), Point(3, 4))
    rect3 = Rectangle(rect1)
