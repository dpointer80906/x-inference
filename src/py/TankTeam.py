'''FoW Tank Team Characteristics

'''
import Database


class TankTeam(object):
    '''

    '''

    @property
    def name(self):
        '''str: '''
        return self._characteristics['Name']

    @property
    def weapon(self):
        '''str: '''
        return self._characteristics['Weapon']

    @property
    def mobility(self):
        '''str: '''
        return self._characteristics['Mobility']

    @property
    def front(self):
        '''int: front armor value'''
        return self._characteristics['Front']

    @property
    def side(self):
        '''int: side armor value'''
        return self._characteristics['Side']

    @property
    def top(self):
        '''int: side armor value'''
        return self._characteristics['Top']

    @property
    def wrange(self):
        '''int: main weapon range, in inches'''
        return self._characteristics['Range']

    @property
    def rof(self):
        '''int: main gun rate of fire'''
        return self._characteristics['ROF']

    @property
    def at(self):
        '''int: anti-tank'''
        return self._characteristics['AT']

    @property
    def firepower(self):
        '''int: firepower baseline, ex. 3 means 3+'''
        return self._characteristics['Firepower']

    def __init__(self, characteristics):
        self._characteristics = characteristics
