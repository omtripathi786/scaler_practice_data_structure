import copy
import unittest

from magic_method import Point


class TestPoint(unittest.TestCase):
    def test_constructor(self):
        point = Point(3, 4)
        self.assertEqual(point.x, 3)
        self.assertEqual(point.y, 4)

    def test_constructor_neg(self):
        # Test constructor with negative coordinates
        point = Point(-3, -4)
        self.assertEqual(point.x, -3)
        self.assertEqual(point.y, -4)

    def test_eq(self):
        # Test equality between two different points
        point1 = Point(3, 4)
        point2 = Point(3, 4)
        self.assertEqual(point1, point2)

        # Test equality between two points with different coordinates
        point3 = Point(5, 6)
        self.assertNotEqual(point1, point3)

    def test_str(self):
        # Test string representation of a point
        point = Point(3, 4)
        self.assertEqual(str(point), "(3, 4)")

    def test_copy(self):
        # Test shallow copy
        point = Point(3, 4)
        point_copy = copy.copy(point)
        self.assertEqual(point, point_copy)
        self.assertIsNot(point, point_copy)

        # Test modifying the shallow copy doesn't affect the original point
        point_copy.x = 5
        self.assertNotEqual(point.x, point_copy.x)

    def test_deepcopy(self):
        # Test deep copy
        point = Point(3, 4)
        point_deepcopy = copy.deepcopy(point)
        self.assertEqual(point, point_deepcopy)
        self.assertIsNot(point, point_deepcopy)

        # Test modifying the deep copy doesn't affect the original point
        point_deepcopy.x = 5
        self.assertNotEqual(point.x, point_deepcopy.x)


if __name__ == "__main__":
    unittest.main()
