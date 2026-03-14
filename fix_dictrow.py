p='C:/Users/BoulePiou/cockpit-raphael/db_wrapper.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Remplacer DictRow pour que iter() renvoie les valeurs pas les cles
old = '''class DictRow(dict):
    def __getitem__(self, key):
        if isinstance(key, int):
            return list(self.values())[key]
        return super().__getitem__(key)'''

new = '''class DictRow(dict):
    def __getitem__(self, key):
        if isinstance(key, int):
            return list(self.values())[key]
        return super().__getitem__(key)

    def __iter__(self):
        return iter(self.values())

    def __len__(self):
        return super().__len__()

    def keys(self):
        return super().keys()'''

t = t.replace(old, new)

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print('DictRow corrige - iter() renvoie les valeurs')

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
