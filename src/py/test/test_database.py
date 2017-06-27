from unittest import TestCase
from Database import Database
import sqlite3

VALID_DB_NAME = '/Applications/PyCharm.app/Contents/bin/fow.sqlite'
INVALID_DB_NAME = '/Applications/PyCharm.app/Contents/bin/fow.sqlit'


class TestDatabase(TestCase):

    def setUp(self):
        print('\n***** executing {}'.format(self._testMethodName))

    def test_conn(self):
        '''Apparently connecting to a database can not fail. sqlite3 creates whatever if it does not exist.
        '''
        database = Database(VALID_DB_NAME)
        self.assertTrue(database.conn is not None)
        database.disconnect()
        database = Database(INVALID_DB_NAME)
        self.assertTrue(database.conn is not None)
        database.disconnect()

    def test_select_tank_valid_db_invalid_name(self):
        '''Should not find invalid tank name.
        '''
        database = Database(VALID_DB_NAME)
        tank = database.select_tank('Pz')
        self.assertTrue(tank is None)
        self.assertRaises(sqlite3.Error)
        database.disconnect()

    def test_select_tank_invalid_db_valid_name(self):
        '''Should not find the tank_teams table since db is invalid.
        '''
        database = Database(INVALID_DB_NAME)
        tank = database.select_tank('Panzer IV H')
        self.assertTrue(tank is None)
        self.assertRaises(sqlite3.Error)
        database.disconnect()

    def test_select_tank_valid_db_valid_name(self):
        '''All is well.
        '''
        database = Database(VALID_DB_NAME)
        tank = database.select_tank('Panzer IV H')
        self.assertTrue(tank is not None)
        database.disconnect()

    def test_disconnect(self):
        '''Apparently this can't fail, either. sqlite3 will open up -something- first, which may then be closed.
        '''
        database = Database(VALID_DB_NAME)
        database.disconnect()

    def test_disconnect_closed(self):
        '''Can't operate on a closed database.
        '''
        database = Database(VALID_DB_NAME)
        database.disconnect()
        _ = database.select_tank('Panzer IV H')
        self.assertRaises(sqlite3.Error)
