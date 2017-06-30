from unittest import TestCase
from Position import Position
from Coord import Coord
import math


class TestPosition(TestCase):

    def setUp(self):
        print('\n***** executing {}'.format(self._testMethodName))
        self.x = 3.0
        self.y = 3.0
        self.coord = Coord(self.x, self.y)
        self.angle = 270.0
        self.front = 1.2
        self.side = 2.5
        self.position = Position(self.coord, self.angle, self.front, self.side)

    def test_center(self):
        self.assertEqual(self.position.center.x, self.x)
        self.assertEqual(self.position.center.y, self.y)

    def test_angle(self):
        self.assertEqual(self.position.angle, self.angle)

    def test_cos_angle(self):
        rad_angle = math.radians(self.position.angle)
        self.assertAlmostEqual(self.position.cos_angle, math.cos(rad_angle), places=5)

    def test_sin_angle(self):
        rad_angle = math.radians(self.position.angle)
        self.assertAlmostEqual(self.position.sin_angle, math.sin(rad_angle), places=5)

    def test_half_front(self):
        self.assertEqual(self.position.half_front, self.front/2.0)

    def test_half_side(self):
        self.assertEqual(self.position.half_side, self.side/2.0)

    def test_rect_coords(self):
        init = Coord(0.0, 0.0)
        self.assertEqual(self.position.rect_coords['front_left'].x, init.x)
        self.assertEqual(self.position.rect_coords['front_left'].y, init.y)
        self.assertEqual(self.position.rect_coords['front_right'].x, init.x)
        self.assertEqual(self.position.rect_coords['front_right'].y, init.y)
        self.assertEqual(self.position.rect_coords['rear_right'].x, init.x)
        self.assertEqual(self.position.rect_coords['rear_right'].y, init.y)
        self.assertEqual(self.position.rect_coords['rear_left'].x, init.x)
        self.assertEqual(self.position.rect_coords['rear_left'].y, init.y)

    def test__rotate(self):
        position = Position(self.coord, self.angle, self.front, self.side)
        unrot_position = [Coord(2.4, 4.25), Coord(3.6, 4.25), Coord(3.6, 1.75), Coord(2.4, 1.75)]
        expected_position = [Coord(4.25, 3.6), Coord(4.25, 2.4), Coord(1.75, 2.4), Coord(1.75, 3.6)]
        for idx in range(0, len(unrot_position)):
            expected = expected_position[idx]
            actual = position._rotate(unrot_position[idx])
            self.assertAlmostEqual(expected.x, actual.x, places=3)
            self.assertAlmostEqual(expected.y, actual.y, places=3)
        position = Position(self.coord, 16.0, self.front, self.side)
        unrot_position = [Coord(2.4, 4.25), Coord(3.6, 4.25), Coord(3.6, 1.75), Coord(2.4, 1.75)]
        expected_position = [Coord(2.079, 4.036), Coord(3.232, 4.367), Coord(3.921, 1.964), Coord(2.768, 1.633)]
        for idx in range(0, len(unrot_position)):
            expected = expected_position[idx]
            actual = position._rotate(unrot_position[idx])
            self.assertAlmostEqual(expected.x, actual.x, places=3)
            self.assertAlmostEqual(expected.y, actual.y, places=3)

    def test_update(self):
        position = Position(self.coord, self.angle, self.front, self.side)
