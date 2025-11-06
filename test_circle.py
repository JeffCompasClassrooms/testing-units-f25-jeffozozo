import unittest
import math
from circle import Circle

class TestCircle(unittest.TestCase):

    def test_circle_initializer_returns_instance(self):
        circle = Circle(5)
        self.assertIsInstance(circle, Circle)

    def test_circle_initializer_with_valid_radius(self):
        circle = Circle(5)
        self.assertEqual(circle.mRadius, 5)
        circle = Circle(5.5)
        self.assertEqual(circle.mRadius, 5.5)

    def test_get_radius_returns_correct_radius(self):
        circle = Circle(5)
        radius = circle.getRadius()
        self.assertEqual(radius, 5)
    
    def test_set_radius_succeeds_given_positive_value(self):
        circle = Circle(5)
        result = circle.setRadius(10)
        self.assertTrue(result)

    def test_set_radius_succeeds_given_zero_value(self):
        circle = Circle(5)
        result = circle.setRadius(0)
        self.assertTrue(result)

    def test_set_radius_fails_given_negative_value(self):
        circle = Circle(5)
        result = circle.setRadius(-10)
        self.assertFalse(result)

    def test_get_area_returns_correct_area_with_valid_radius(self):
        circle = Circle(5)
        area = circle.getArea()
        self.assertEqual(area, 5 * 5 * math.pi)
        self.assertEqual(round(area, 2), 78.54)
        circle = Circle(2)
        area = circle.getArea()
        self.assertEqual(area,2 * 2 * math.pi)

if __name__ == '__main__':
    unittest.main()
