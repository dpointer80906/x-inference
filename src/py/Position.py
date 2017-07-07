'''Manage the position state of one tank team.
'''
from Coord import Coord


class Position(object):
    '''Provide position services for a single tank.

    Args:
        vector (<Coord.PolarCoord>): initial x,y,angle coordinates from center of tank (inches, degrees).
        front (float): length of tank front & rear (inches)
        side (float): length of tank sides (inches)
    '''

    @property
    def vector(self):
        '''<Coord.PolarCoord>: x,y,angle coordinates from center of tank (inches).'''
        return self._vector

    @property
    def dim(self):
        '''dict: front and side dimensions of tank (inches). keys: [front, side].'''
        return self._dim

    @property
    def vertices(self):
        '''dict: x,y of the four tank vertices. keys:[front_left, front_right, rear_right, rear_left].'''
        return self._vertices

    def _set_vertices(self):
        '''Calculate the tank bounding rectangle vertex points given current class properties.
        '''
        def rotate(unrot_point):
            '''Rotate a given x,y point by current angle property.

            Args:
                unrot_point (<Coord>): unrotated point to rotate by angle.
            Returns:
                <Coord>: unrot_point rotated by angle.
            '''
            normalized = Coord(unrot_point.x - self.vector.x, unrot_point.y - self.vector.y)
            xp = (normalized.x * self.vector.cos_angle - normalized.y * self.vector.sin_angle) + self.vector.x
            yp = (normalized.y * self.vector.cos_angle + normalized.x * self.vector.sin_angle) + self.vector.y
            return Coord(xp, yp)

        half_front = self.dim['front']/2.0
        half_side = self.dim['side']/2.0
        unrot_front_left = Coord(self.vector.x - half_front, self.vector.y + half_side)
        unrot_front_right = Coord(self.vector.x + half_front, self.vector.y + half_side)
        unrot_rear_right = Coord(self.vector.x + half_front, self.vector.y - half_side)
        unrot_rear_left = Coord(self.vector.x - half_front, self.vector.y - half_side)
        self._vertices['front_left'] = rotate(unrot_front_left)
        self._vertices['front_right'] = rotate(unrot_front_right)
        self._vertices['rear_right'] = rotate(unrot_rear_right)
        self._vertices['rear_left'] = rotate(unrot_rear_left)

    def update(self, new_vector):
        '''Update the vector property of this tank, then update the vertices property.

        Args:
            new_vector (<Coord.PolarCoord>): new x,y coordinates of vector of tank (inches).
        '''
        self._vector.set_vector(new_vector)
        self._set_vertices()

    def __init__(self, vector, front, side):
        self._vector = vector
        self._dim = {'front': front, 'side': side}
        self._vertices = {}
        self._set_vertices()
