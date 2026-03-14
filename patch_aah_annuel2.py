import sqlite3
db = sqlite3.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
c = db.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS aah_suivi (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mois TEXT UNIQUE,
    montant_prevu REAL DEFAULT 0,
    montant_reel REAL DEFAULT 0,
    date_saisie TEXT DEFAULT CURRENT_DATE,
    note TEXT DEFAULT ''
)""")

previsions = [
    ('2026', 625, 0, 'Base revenus 2024 - SCI active'),
    ('2027', 625, 0, 'Estimation prudente - revenus 2025 SCI'),
    ('2028', 900, 0, 'AAH remonte - revenus 2026 partiels SCI'),
    ('2029', 1033, 0, 'AAH pleine - revenus 2027 = 0 SCI + LMNP 0'),
    ('2030', 1033, 0, 'AAH pleine'),
    ('2031', 1033, 0, 'AAH pleine'),
    ('2032', 1033, 0, 'AAH pleine'),
    ('2033', 1033, 0, 'AAH pleine'),
    ('2034', 1033, 0, 'AAH pleine'),
    ('2035', 1033, 0, 'AAH pleine'),
    ('2036', 1033, 0, 'AAH pleine'),
    ('2037', 1033, 0, 'AAH pleine'),
    ('2038', 1033, 0, 'AAH pleine'),
    ('2039', 0, 0, 'AAH stop 64 ans (si MDPH < 80%) ou 1033 (si >= 80%)'),
]

for annee, prevu, reel, note in previsions:
    c.execute("INSERT OR IGNORE INTO aah_suivi (mois, montant_prevu, montant_reel, note) VALUES (?,?,?,?)",
              (annee, prevu, reel, note))

db.commit()
db.close()
print('Table aah_suivi creee')
print('14 entrees de 2026 a 2039')
