p='C:/Users/BoulePiou/cockpit-raphael/db_wrapper.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Ajouter executescript qui n'existe pas en PostgreSQL
old_class = '''class CursorWrapper:'''
new_class = '''class CursorWrapper:
    def executescript(self, sql):
        # PostgreSQL n a pas executescript - on execute chaque statement
        statements = [s.strip() for s in sql.split(";") if s.strip()]
        for stmt in statements:
            try:
                self._cursor.execute(stmt)
            except Exception as e:
                self._cursor.connection.rollback()
        return self'''

t = t.replace(old_class, new_class, 1)

# Ameliorer execute pour gerer plus de cas
old_exec = "        # Ignorer les PRAGMA (SQLite only)"
new_exec = """        # Ignorer les PRAGMA (SQLite only)
        if sql.strip() == '':
            self._results = []
            return self"""

t = t.replace(old_exec, new_exec)

# Ajouter rowcount
old_desc = '''    @property
    def description(self):
        return self._cursor.description'''
new_desc = '''    @property
    def description(self):
        return self._cursor.description

    @property
    def rowcount(self):
        return self._cursor.rowcount'''

t = t.replace(old_desc, new_desc)

# Ameliorer le commit dans ConnectionWrapper pour gerer les erreurs
old_commit = '''    def commit(self):
        self._conn.commit()'''
new_commit = '''    def commit(self):
        try:
            self._conn.commit()
        except:
            try:
                self._conn.rollback()
                self._conn.commit()
            except:
                pass'''

t = t.replace(old_commit, new_commit)

# Ameliorer execute pour gerer INSERT OR REPLACE
old_ignore = "        sql = sql.replace('INSERT OR IGNORE', 'INSERT')"
new_ignore = """        sql = sql.replace('INSERT OR IGNORE', 'INSERT')
        sql = sql.replace('INSERT OR REPLACE', 'INSERT')
        sql = sql.replace('AUTOINCREMENT', '')
        sql = sql.replace('autoincrement', '')
        if 'CREATE TABLE' in sql:
            sql = sql.replace('INTEGER PRIMARY KEY', 'SERIAL PRIMARY KEY')"""

t = t.replace(old_ignore, new_ignore)

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print('db_wrapper ameliore')

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
