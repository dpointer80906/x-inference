'''Two-dimensional x,y coordinate services.
'''


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
