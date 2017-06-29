'''

'''
import Position


class TankTeamState(object):
    '''

    '''

    @property
    def position(self):
        '''<Position>: Current state position of tank team.'''
        return self._position

    def __init__(self, initial_x, initial_y, initial_angle, dim_front, dim_side):
        self._position = Position.Position(initial_x, initial_y, initial_angle, dim_front, dim_side)
