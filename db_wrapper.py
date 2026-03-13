# db_wrapper.py - Traducteur SQLite -> PostgreSQL
# Ce fichier fait croire a app.py qu'il parle a SQLite
# alors qu'en realite il parle a Supabase

import psycopg2
import psycopg2.extras
import re

import os
DB_CONFIG = {
    'host': os.environ.get('DB_HOST', 'aws-1-eu-west-1.pooler.supabase.com'),
    'port': int(os.environ.get('DB_PORT', 6543)),
    'dbname': os.environ.get('DB_NAME', 'postgres'),
    'user': os.environ.get('DB_USER', 'postgres.zyizvlrwsatxqehhqiwh'),
    'password': os.environ.get('DB_PASS', 'Seraphetraph/62//26**')
}

class DictRow(dict):
    def __getitem__(self, key):
        if isinstance(key, int):
            return list(self.values())[key]
        return super().__getitem__(key)

    def __iter__(self):
        return iter(self.values())

    def __len__(self):
        return super().__len__()

    def keys(self):
        return super().keys()

class CursorWrapper:
    def __init__(self, cursor):
        self._cursor = cursor

    @property
    def description(self):
        return self._cursor.description

    @property
    def lastrowid(self):
        try:
            self._cursor.execute("SELECT lastval()")
            return self._cursor.fetchone()['lastval']
        except:
            return 0

    @property
    def description(self):
        return self._cursor.description

    @property
    def lastrowid(self):
        try:
            self._cursor.execute("SELECT lastval()")
            return self._cursor.fetchone()['lastval']
        except:
            return 0

    def execute(self, sql, params=None):
        # Ignorer les PRAGMA (SQLite only)
        if 'PRAGMA' in sql:
            self._results = []
            return self
        # Remplacer ? par %s
        sql = sql.replace('?', '%s')
        # Remplacer INSERT OR IGNORE
        sql = sql.replace('INSERT OR IGNORE', 'INSERT')
        # Remplacer CURRENT_DATE (compatible)
        # Remplacer INTEGER PRIMARY KEY AUTOINCREMENT
        sql = sql.replace('AUTOINCREMENT', '')
        sql = sql.replace('autoincrement', '')
        try:
            if params:
                self._cursor.execute(sql, params)
            else:
                self._cursor.execute(sql)
        except Exception as e:
            # Si erreur unique constraint, ignorer
            if 'duplicate key' in str(e).lower() or 'unique' in str(e).lower():
                self._cursor.connection.rollback()
            else:
                self._cursor.connection.rollback()
                print(f'DB Error: {e}')
        return self

    def fetchone(self):
        try:
            row = self._cursor.fetchone()
            if row is None:
                return None
            return DictRow(row)
        except:
            return None

    def fetchall(self):
        try:
            rows = self._cursor.fetchall()
            return [DictRow(r) for r in rows]
        except:
            return []

class ConnectionWrapper:
    def __init__(self):
        self._conn = psycopg2.connect(**DB_CONFIG, cursor_factory=psycopg2.extras.RealDictCursor)
        self._conn.autocommit = False
        self.row_factory = None

    def cursor(self):
        return CursorWrapper(self._conn.cursor())

    def execute(self, sql, params=None):
        c = self.cursor()
        c.execute(sql, params)
        return c

    def commit(self):
        self._conn.commit()

    def rollback(self):
        self._conn.rollback()

    def close(self):
        try:
            self._conn.commit()
            self._conn.close()
        except:
            pass

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

def connect(path=None):
    return ConnectionWrapper()

# Pour compatibilite avec sqlite3.Row
Row = dict
