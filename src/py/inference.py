'''

'''
import Database
import TankTeam


def main():
    '''

    Returns:

    '''
    database = Database.Database('/Applications/PyCharm.app/Contents/bin/fow.sqlite')
    tank_teams = {}
    tank_teams['Panzer IV H'] = TankTeam.TankTeam(database.select_tank('Panzer IV H'))
    print(tank_teams['Panzer IV H'].name )


if __name__ == "__main__":
    main()
