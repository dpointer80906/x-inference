'''Two-dimensional x,y coordinate services.
'''
import math


class Coord(object):
    '''Provides getters and setters to class vars x and y and both.

    Args:
        x (float): initial x value
        y (float): initial y value
    '''

    @property
    def xy(self):
        '''tuple(float, float): x and y coordinates, authoritative source.'''
        return self._xy

    @property
    def x(self):
        '''float: get x coordinate from authoritative source.'''
        return self.xy[0]

    @property
    def y(self):
        '''float: get y coordinate from authoritative source.'''
        return self.xy[1]

    def set_x(self, x):
        '''Set a new x value in authoritative source, leave y unchanged.

        Args:
            x (float): new x value for authoritative source.
        '''
        y = self.y
        self._xy = (x, y)

    def set_y(self, y):
        '''Set a new y value in authoritative source, leave x unchanged.

        Args:
            y (float): new y value for authoritative source.
        '''
        x = self.x
        self._xy = (x, y)

    def set_xy(self, x, y):
        '''Set new x and y values in authoritative source.'''
        self._xy = (x, y)

    def __init__(self, x, y):
        self._xy = (x, y)


class PolarCoord(Coord):
    '''Adds angle services to x,y coordinate class.

    '''
    @property
    def vector(self):
        '''tuple(float, float, float): '''
        return (self.x, self.y, self.angle)

    @property
    def angle(self):
        '''float: orientation of line normal to tank front relative to origin of playing field (degrees)'''
        return self._angle

    @property
    def cos_angle(self):
        '''float: convenience function providing cosine of current angle.'''
        return math.cos(math.radians(self.angle))

    @property
    def sin_angle(self):
        '''float: convenience function providing sine of current angle.'''
        return math.sin(math.radians(self.angle))

    def set_vector(self, new_vector):
        '''

        Args:
            vector <PolarCoord>:
        '''
        self.set_xy(new_vector.x, new_vector.y)
        self._angle = new_vector.angle

    def __init__(self, x, y, angle):
        super().__init__(x, y)
        self._angle = angle


    def _set_vector(self, new_vector):
        '''Change the value of the vector property to new_vector.
        Args:
            new_vector <Coord.PolarCoord>: x,y,angle coordinates from center of tank (inches, degrees).
        '''
        self.vector.set_vector(new_vector)