import sqlite3
db = sqlite3.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
c = db.cursor()

# Ajouter colonne scenario MDPH dans profil
try:
    c.execute("ALTER TABLE profil ADD COLUMN mdph_80plus INTEGER DEFAULT 0")
    print('Colonne mdph_80plus ajoutee')
except:
    print('Colonne mdph_80plus existe deja')

# Ajouter un jalon pour la reponse MDPH
c.execute("""INSERT INTO chronologie 
    (date_cible, age_cible, action, montant, sens, categorie, auto, fait, note)
    VALUES ('2026-06-01', 50.8, 'Reponse MDPH - taux 80% ou plus ?', 0, 'info', 'action', 0, 0, 
    'Si OUI: AAH a vie, plan ameliore. Si NON: AAH stop 64 ans, bascule ASPA.')""")
print('Jalon MDPH ajoute')

db.commit()
db.close()
print('OK')
