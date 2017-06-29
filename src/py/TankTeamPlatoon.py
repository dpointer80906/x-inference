'''

'''
import TankTeamFacts
import TankTeamState

VALID_SKILL = ['conscript', 'trained', 'veteran']
VALID_MOTIVATION = ['reluctant', 'confident', 'fearless']


class TankTeamPlatoon(object):
    '''

    Args:
        tank_name (str): name of the unique tank type name in this platoon.
        cpn (tuple) company number, platoon number, tank number count.
        skill (str): platoon skill
        motivation (str): platoon motivation
    '''

    @property
    def state(self):
        '''dict <TankTeamState>: collection of tank team states for all tanks in this platoon.'''
        return self._state

    @property
    def facts(self):
        '''<TankTeamFacts>: database facts about tank_name.'''
        return self._facts

    @property
    def skill(self):
        '''str: platoon skill.'''
        return self._skill

    def motivation(self):
        '''str: platoon motivation.'''
        return self._motivation

    def _init_state(self, cpn, force):
        '''Create the states for each member of this tank_team.

        Args:
            cpn (tuple) company number, platoon number, tank number count.
            force (str): 'friendly' or 'enemy'
        Returns:

        '''
        state = {}
        dim_front = self.facts.get_fact('dim_front')
        dim_side = self.facts.get_fact('dim_side')
        if force == 'friendly':
            initial_x = 2.0 * dim_front
            initial_y = 2.0 + dim_side
            initial_angle = 0.0
        else:
            initial_x = 2.0 * dim_front
            initial_y = 5.0 + dim_side
            initial_angle = 180.0
        cp = cpn[0] * 100 + cpn[1] * 10
        for tank_number in range(1, cpn[2]+1):
            cpn = cp + tank_number
            state[cpn] = TankTeamState.TankTeamState(initial_x, initial_y, initial_angle, dim_front, dim_side)
        return state

    def __init__(self, tank_name, cpn, skill, motivation, force):
        self._tank_name = tank_name
        self._skill = skill
        self._motivation = motivation
        self._facts = TankTeamFacts.TankTeamFacts(tank_name)
        self._state = self._init_state(cpn, force)
