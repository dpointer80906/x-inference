from unittest import TestCase
from Coord import Coord


class TestCoord(TestCase):

    def setUp(self):
        print('\n***** executing {}'.format(self._testMethodName))

    def test_set_x(self):
        x = 3.2
        y = 6.4
        point = Coord(x, y)
        self.assertEqual(point.x, x)
        self.assertEqual(point.y, y)
        x = 1.0
        point.set_x(x)
        self.assertEqual(point.x, x)
        self.assertEqual(point.y, y)

    def test_set_y(self):
        x = 3.2
        y = 6.4
        point = Coord(x, y)
        self.assertEqual(point.x, x)
        self.assertEqual(point.y, y)
        y = 1.0
        point.set_y(y)
        self.assertEqual(point.x, x)
        self.assertEqual(point.y, y)

    def test_set_xy(self):
        x = 3.2
        y = 6.4
        point = Coord(x, y)
        self.assertEqual(point.x, x)
        self.assertEqual(point.y, y)
        x = 0.0
        y = 1.0
        point.set_xy(x, y)
        self.assertEqual(point.x, x)
        self.assertEqual(point.y, y)
