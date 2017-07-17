from unittest import TestCase
from Position import Position
from Coord import Coord
from Coord import PolarCoord
import math

INITIAL_X = 3.0
INITIAL_Y = 3.0
INITIAL_ANGLE = 270.0
INITIAL_FRONT = 1.2
INITIAL_SIDE = 2.5
INITIAL_RECT_COORDS = [Coord(4.25, 3.6), Coord(4.25, 2.4), Coord(1.75, 2.4), Coord(1.75, 3.6)]

UNROT_POS_1 = [Coord(2.4, 4.25), Coord(3.6, 4.25), Coord(3.6, 1.75), Coord(2.4, 1.75)]
ROT_POS_1 = [Coord(4.25, 3.6), Coord(4.25, 2.4), Coord(1.75, 2.4), Coord(1.75, 3.6)]
UNROT_POS_2 = [Coord(2.4, 4.25), Coord(3.6, 4.25), Coord(3.6, 1.75), Coord(2.4, 1.75)]
ROT_POS_2 = [Coord(2.079, 4.036), Coord(3.232, 4.367), Coord(3.921, 1.964), Coord(2.768, 1.633)]
ROTATE_2 = 16.0
UPDATE_1 = [Coord(4.104, 4.201), Coord(5.098, 4.872), Coord(6.496, 2.799), Coord(5.502, 2.128)]
RECT_COORDS_1 = [Coord(2.209, 4.005), Coord(3.086, 4.823), Coord(4.791, 2.995), Coord(3.914, 2.177)]


class TestPosition(TestCase):

    def setUp(self):
        '''Announce each test & set default values for Position class.'''
        print('\n***** executing {}'.format(self._testMethodName))
        self.position = Position(PolarCoord(INITIAL_X, INITIAL_Y, INITIAL_ANGLE), INITIAL_FRONT, INITIAL_SIDE)

    def test_class_properties(self):
        '''Check the initialized class properties.'''
        self.assertEqual(self.position.vector.x, INITIAL_X)
        self.assertEqual(self.position.vector.y, INITIAL_Y)
        self.check_angle(INITIAL_ANGLE)
        self.assertEqual(self.position.dim['front'], INITIAL_FRONT)
        self.assertEqual(self.position.dim['side'], INITIAL_SIDE)
        self.check_rect_coords(INITIAL_RECT_COORDS)

    def test__set_center_and_angle(self):
        '''Change the center coords and check it got changed properly.'''
        x = 3.5
        y = 7.2
        angle = 43.0
        self.position.update(PolarCoord(x, y, angle))
        self.assertEqual(self.position.vector.x, x)
        self.assertEqual(self.position.vector.y, y)
        self.check_angle(angle)

    def test__set_rect_coords(self):
        '''Set a new center & angle, then see if set_rect_coords generates the proper answer.'''
        x = 3.5
        y = 3.5
        angle = 43.0
        self.position.update(PolarCoord(x, y, angle))
        expected = RECT_COORDS_1
        self.check_rect_coords(expected)

    def test_update(self):
        ''''''
        x = 5.3
        y = 3.5
        angle = 34.0
        self.position.update(PolarCoord(x, y, angle))
        self.check_rect_coords(UPDATE_1)

    def check_rect_coords(self, expected):
        '''Utility to check actual against expected rectangle coordinates.

        Args:
            expected (list): the four expected corner coordinates to compare against actual.
        '''
        actual = []
        for vertex in ['front_left', 'front_right', 'rear_right', 'rear_left']:
            actual.append(Coord(self.position.vertices[vertex].x, self.position.vertices[vertex].y))
        for idx in range(0, len(expected)):
            self.assertAlmostEqual(actual[idx].x, expected[idx].x, places=3)
            self.assertAlmostEqual(actual[idx].y, expected[idx].y, places=3)

    def check_angle(self, expected):
        '''Utility to check if the new angle is set properly & check its sin/cos.

        Args:
            expected (float):
        '''

        rad_angle = math.radians(expected)
        self.assertEqual(self.position.vector.angle, expected)
        self.assertAlmostEqual(self.position.vector.cos_angle, math.cos(rad_angle), places=5)
        self.assertAlmostEqual(self.position.vector.sin_angle, math.sin(rad_angle), places=5)
