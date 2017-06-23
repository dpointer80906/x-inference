'''

'''
import sqlite3
from sqlite3 import Error


class Database(object):
    '''

    '''

    @property
    def conn(self):
        ''''''
        return self._conn

    def select_tank(self, name):
        '''

        Args:
            name:

        Returns:
            dict:
        '''
        def row2dict(cursor, row):
            d = {}
            for idx, col in enumerate(cursor.description):
                d[col[0]] = row[idx]
            return d

        try:
            self.conn.row_factory = row2dict
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM tank_teams WHERE Name=?", (name,))
            return cur.fetchone()
        except Error as exc:
            print(exc)
        return None

    def _create_connection(self, db_file):
        '''create a database connection to the SQLite database specified by the db_file

        Args:
            db_file: database file name

        Returns:
            Connection object or None
        '''
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as exc:
            print(exc)
        return None

    def __init__(self, db_file):
        self._conn = self._create_connection(db_file)
        if self.conn is None:
            print('connection not established')
