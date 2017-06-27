'''FoW Tank Team Characteristics

Module to return characteristic data on a specific tank team. The authoritative source of characteristic
names (keys) and data is the Database class. Characteristics do not change unless the fundamental data in the
FoW mission briefing for a tank team unit changes.
'''
import logging
import Database

DB_NAME = '/Applications/PyCharm.app/Contents/bin/fow.sqlite'

logger = logging.getLogger(__name__)


class TankTeamFacts(object):
    '''Tank Team facts

    Args:
        tank_name(str): request characteristics from the database for this specific tank team name.
    '''

    @property
    def characteristics(self):
        '''dict: tank team characteristic name to value mappings.'''
        return self._characteristics

    def get_fact(self, key):
        '''Request a tank team fact value.

        If it exists, returns the requested value from the local read-only copy of the database record
        for the named tank, else return None and a log error message.

        Args:
            key (str): the key of the requested tank team characteristic.
        Returns:
            int or str value of specified key; or None if key not in characteristics.
        '''
        if self.characteristics is not None:
            if key in self.characteristics.keys():
                return self.characteristics[key]
            else:
                msg = 'Tank Team characteristic \"{}\" not found.'.format(key)
                msg += '\nValid Tank Team characteristic names are {}'.format(list(self.characteristics.keys()))
                logger.error(msg)
        return None

    def __init__(self, tank_name):
        database = Database.Database(DB_NAME)
        self._characteristics = database.select_tank(tank_name)
        database.disconnect()
