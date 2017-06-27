'''Interface to FoW tank team authoritative fact database.

TODO: extend this out beyond just tank teams.
'''
import logging
import sqlite3
from sqlite3 import Error

logger = logging.getLogger(__name__)


def row2dict(cursor, row):
    '''Utility function for sqlite3 row factory to use to convert retrieved row data to dict.

    Args:
        cursor (<sqlite3.Cursor>): cursor object retrieved from database connection.
        row (tuple): database row data.
    Returns:
        dict: retrived row data with database column labels for keys.
    '''
    rowdict = {}
    for idx, col in enumerate(cursor.description):
        rowdict[col[0]] = row[idx]
    return rowdict


class Database(object):
    '''Interface to sqlite FoW database.

    Instantiation opens the names database, it must be closed manually when it's time to disconnect.

    TODO: make a base class and subclass it for different database interfaces.

    Args:
        db_name (str): the full name (including path) of the FoW database to use.
    '''

    @property
    def conn(self):
        '''<sqlite3.Connection>: connection object to FoW database.'''
        return self._conn

    def select_tank(self, tank_name):
        '''Select the (assumed) unique data for the named tank team.

        Args:
            tank_name (str): request characteristics from the database for this specific tank team name.
        Returns:
            dict: the tank_name characteristics or None.
        '''
        row = None
        try:
            self.conn.row_factory = row2dict
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM tank_teams WHERE Name=?", (tank_name,))
            row = cur.fetchone()
        except Error as exc:
            logging.error('query failed for tank team name {}, {}'.format(tank_name, exc))
        else:
            if row is None:
                logging.error('query failed, tank team name {} not found'.format(tank_name))
        return row

    def disconnect(self):
        '''Close the database connection.
        '''
        self.conn.close()

    def __init__(self, db_name):
        self._conn = sqlite3.connect(db_name)
