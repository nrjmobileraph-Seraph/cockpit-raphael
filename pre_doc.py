import os
app_path = 'C:/Users/BoulePiou/cockpit-raphael/app.py'
db_path = 'C:/Users/BoulePiou/cockpit-raphael/cockpit.db'
f = open(app_path, 'r', encoding='utf-8')
t = f.read()
f.close()
nb_lignes = t.count(chr(10))
nb_fonctions = t.count('def ')
taille = os.path.getsize(app_path)
taille_db = os.path.getsize(db_path)
print(f'app.py : {nb_lignes} lignes, {nb_fonctions} fonctions, {taille//1024} Ko')
print(f'cockpit.db : {taille_db//1024} Ko')
