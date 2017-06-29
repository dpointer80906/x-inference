'''Manage the position state of one tank team.
'''
import math
import Coord


class Position(object):
    '''Provide position services for a single tank.

    Args:
        center (<Coord>): initial x,y coordinates of center of tank (inches)
        angle (float): initial orientation of tank front (degrees)
        dim_front (float): length of tank front & rear (inches)
        dim_side (float): length of tank sides (inches)
    '''

    @property
    def center(self):
        '''<Coord>: x,y coordinates of center of tank (inches).'''
        return self._center

    @property
    def angle(self):
        '''float: orientation of line normal to tank front relative to origin of playing field (degrees)'''
        return self._angle

    @property
    def cos_angle(self):
        '''float: convenience function providing cosine of current angle.'''
        return math.cos(self.angle * 0.01745329252)

    @property
    def sin_angle(self):
        '''float: convenience function providing sine of current angle.'''
        return math.sin(self.angle * 0.01745329252)

    @property
    def half_front(self):
        '''float: halved length of tank front or rear (inches).'''
        return self._half_front

    @property
    def half_side(self):
        '''float: halved length of tank sides (inches).'''
        return self._half_side

    @property
    def rect_coords(self):
        '''dict: current x,y positions of the four tank bounding rectangle vertices.'''
        return self._rect_coords

    def _rotate(self, unrot_point):
        '''Rotate a given x,y point by current angle.

        Args:
            unrot_point (<Coord>): unrotated point to rotate by angle.
        Returns:
            <Coord>: unrot_point rotated by angle.
        '''
        normalized = Coord.Coord(unrot_point.x - self.center.x, unrot_point.y - self.center.y)
        xp = (normalized.x * self.cos_angle - normalized.y * self.sin_angle) + self.center.x
        yp = (normalized.y * self.cos_angle + normalized.x * self.sin_angle) + self.center.y
        return Coord.Coord(xp, yp)

    def update(self, new_center, new_angle):
        '''Update the center, angle and rectangle vertex positions of this tank.

        Args:
            new_center (<Coord>): the new center coordinates for this tank.
            new_angle (float): the new front armor angle for this tank, in degrees.
        '''
        self._center = self.center.set_xy(new_center.x, new_center.y)
        self._angle = new_angle
        unrot_front_left = Coord.Coord(self.center.x - self.half_front, self.center.y + self.half_side)
        unrot_front_right = Coord.Coord(self.center.x + self.half_front, self.center.y + self.half_side)
        unrot_rear_right = Coord.Coord(self.center.x + self.half_front, self.center.y - self.half_side)
        unrot_rear_left = Coord.Coord(self.center.x - self.half_front, self.center.y - self.half_side)
        self._rect_coords['front_left'] = self._rotate(unrot_front_left)
        self._rect_coords['front_right'] = self._rotate(unrot_front_right)
        self._rect_coords['rear_right'] = self._rotate(unrot_rear_right)
        self._rect_coords['rear_left'] = self._rotate(unrot_rear_left)

    def __init__(self, center, angle, dim_front, dim_side):
        self._center = center
        self._angle = angle
        self._half_front = dim_front/2.0
        self._half_side = dim_side/2.0
        self._rect_coords = {'front_left': Coord.Coord(0.0, 0.0),
                             'front_right': Coord.Coord(0.0, 0.0),
                             'rear_right': Coord.Coord(0.0, 0.0),
                             'rear_left': Coord.Coord(0.0, 0.0)}