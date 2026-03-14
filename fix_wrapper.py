p='C:/Users/BoulePiou/cockpit-raphael/db_wrapper.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Ajouter la propriete description au CursorWrapper
old = '''    def execute(self, sql, params=None):'''
new = '''    @property
    def description(self):
        return self._cursor.description

    @property
    def lastrowid(self):
        try:
            self._cursor.execute("SELECT lastval()")
            return self._cursor.fetchone()['lastval']
        except:
            return 0

    def execute(self, sql, params=None):'''

t = t.replace(old, new, 1)

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print('description + lastrowid ajoutes')

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
