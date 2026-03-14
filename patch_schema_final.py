import sqlite3
db = sqlite3.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
c = db.cursor()

colonnes = [
    ('montant_reel', 'REAL', '0'),
    ('date_reelle', 'TEXT', "''"),
    ('confirme_1mois', 'INTEGER', '0'),
    ('date_confirme_1mois', 'TEXT', "''"),
    ('confirme_6mois', 'INTEGER', '0'),
    ('date_confirme_6mois', 'TEXT', "''"),
]

for nom, typ, defaut in colonnes:
    try:
        c.execute(f"ALTER TABLE chronologie ADD COLUMN {nom} {typ} DEFAULT {defaut}")
        print(f'Colonne {nom} ajoutee')
    except:
        print(f'Colonne {nom} existe deja')

# Verifier que toutes les entrees avec flux ont bien les colonnes
c.execute("SELECT id, action, montant, sens FROM chronologie WHERE montant > 0")
rows = c.fetchall()
print(f'Flux a suivre: {len(rows)}')
for r in rows:
    print(f'  [{r[3]}] {r[1]} : {r[2]:,.0f} EUR')

db.commit()
db.close()
print('Schema OK')
