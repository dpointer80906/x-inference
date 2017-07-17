'''

'''
import TankTeamPlatoon
import pprint


def main():
    '''

    Returns:

    '''
    name = 'Panzer IV H'
    friendly_platoon = TankTeamPlatoon.TankTeamPlatoon(name, (1, 1, 1), 'confident', 'veteran', 'friendly')
    enemy_platoon = TankTeamPlatoon.TankTeamPlatoon(name, (3, 1, 1), 'confident', 'veteran', 'enemy')
    pprint.pprint(friendly_platoon.state[111].position.current())
    pprint.pprint(enemy_platoon.state[311].position.current())


if __name__ == "__main__":
    main()
