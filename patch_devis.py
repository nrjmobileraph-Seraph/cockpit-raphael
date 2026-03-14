import sqlite3
db = sqlite3.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
c = db.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS devis_artisans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    corps_metier TEXT,
    artisan TEXT DEFAULT '',
    devis_montant REAL DEFAULT 0,
    paye_montant REAL DEFAULT 0,
    statut TEXT DEFAULT 'a_faire',
    date_devis TEXT DEFAULT '',
    date_paiement TEXT DEFAULT '',
    note TEXT DEFAULT ''
)""")

# Pre-remplir les corps de metier typiques renovation T3
corps = [
    ('Electricite', '', 0, 'a_faire', 'Mise aux normes tableau + prises + luminaires'),
    ('Plomberie', '', 0, 'a_faire', 'Salle de bain + cuisine + WC'),
    ('Peinture', '', 0, 'a_faire', 'Murs + plafonds toutes pieces'),
    ('Sols', '', 0, 'a_faire', 'Parquet ou carrelage selon pieces'),
    ('Cuisine', '', 0, 'a_faire', 'Meubles + plan de travail + electromenager'),
    ('Salle de bain', '', 0, 'a_faire', 'Douche + meuble vasque + WC si separe'),
    ('Menuiserie', '', 0, 'a_faire', 'Portes interieures + placards'),
    ('Divers', '', 0, 'a_faire', 'Imprevus chantier (~10%)'),
]

for corps_m, artisan, montant, statut, note in corps:
    c.execute("INSERT INTO devis_artisans (corps_metier, artisan, devis_montant, statut, note) VALUES (?,?,?,?,?)",
              (corps_m, artisan, montant, statut, note))

db.commit()
db.close()
print('Table devis_artisans creee avec 8 corps de metier')
