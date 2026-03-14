import sqlite3

db = sqlite3.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
c = db.cursor()

# Table chronologie
c.execute("""CREATE TABLE IF NOT EXISTS chronologie (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date_cible TEXT,
    age_cible REAL,
    action TEXT,
    montant REAL DEFAULT 0,
    sens TEXT DEFAULT 'info',
    categorie TEXT DEFAULT 'jalon',
    auto INTEGER DEFAULT 0,
    fait INTEGER DEFAULT 0,
    note TEXT DEFAULT ''
)""")

# Vider et remplir
c.execute("DELETE FROM chronologie")

actions = [
    # MAINTENANT
    ('2026-03-15', 50.5, 'Ouvrir AV2 Linxea Spirit 2', 500, 'sortie', 'av', 0, 0, 'Horloge 8 ans demarre'),
    ('2026-03-20', 50.5, 'RDV medecin - dossier MDPH >=80%', 0, 'info', 'mdph', 0, 0, 'Levier +282 000 EUR'),
    ('2026-04-01', 50.6, 'Deposer dossier MDPH complet', 0, 'info', 'mdph', 0, 0, 'Avant 60 ans imperatif'),
    ('2026-04-15', 50.6, 'Notaire: testament + mandat + donation NP', 1300, 'sortie', 'juridique', 0, 0, '3 actes en 1 RDV'),
    ('2026-06-01', 50.8, 'Cloturer AV Carrefour Horizons', 0, 'entree', 'av', 0, 0, 'Reinjecter en AV2'),
    ('2026-06-15', 50.8, 'Reduire buffer livrets a 16 560 EUR', 18390, 'transfert', 'epargne', 0, 0, 'Surplus -> AV1'),
    ('2026-07-01', 50.9, 'Lancer travaux parents', 75000, 'sortie', 'travaux', 0, 0, 'MaPrimeRenov ~11 400 EUR'),
    ('2026-09-01', 51.0, 'Demande MaPrimeRenov ANAH', 11400, 'entree', 'travaux', 0, 0, 'Aides panneaux + isolation'),

    # CHAQUE ANNEE (modele 2027)
    ('2027-01-01', 51.4, 'Recalcul ARVA annuel', 0, 'info', 'arva', 1, 0, 'Pioche optimale recalculee'),
    ('2027-01-01', 51.4, 'Tax-Gain Harvesting AV1', 4600, 'info', 'fiscal', 1, 0, 'Cristalliser 4600 EUR PV a 0% IR'),
    ('2027-01-01', 51.4, 'Revalorisation loyer IRL', 0, 'info', 'lmnp', 1, 0, 'Verifier indice INSEE'),

    # CHAQUE MOIS (automatique)
    ('2026-04-01', 50.6, 'Pioche mensuelle Livret A -> CC', 1279, 'transfert', 'mensuel', 1, 0, 'AAH 1033 + Loyer 448 + Pioche 1279 = 2760'),

    # JALONS FUTURS
    ('2030-08-26', 55.0, 'Bilan mi-parcours Phase 1', 0, 'info', 'jalon', 0, 0, 'Verifier trajectoire vs theorique'),
    ('2033-08-26', 58.0, 'Abattement AV2 disponible', 0, 'info', 'fiscal', 0, 0, '2x4600 = 9200 EUR/an PV exonerees'),
    ('2035-08-26', 60.0, 'DEADLINE MDPH - CRITIQUE', 0, 'info', 'mdph', 0, 0, 'Si rate = irreversible'),
    ('2037-08-26', 62.0, 'Estimation T3 Meylan (3 agences)', 0, 'info', 'immo', 0, 0, 'Preparer vente a 64 ans'),
    ('2039-08-26', 64.0, 'AAH sarrete', -1033, 'perte', 'revenus', 1, 0, 'Phase 2 demarre'),
    ('2039-08-26', 64.0, 'Vente T3 Meylan + garage', 252510, 'entree', 'immo', 0, 0, 'Reinjecter en AV'),
    ('2039-08-26', 64.0, 'Loyer LMNP sarrete', -448, 'perte', 'revenus', 1, 0, 'Plus de locataire'),
    ('2039-09-01', 64.0, 'Reinjecter 252 510 EUR en AV3', 252510, 'transfert', 'av', 0, 0, 'Capital rebondit a ~613 000 EUR'),
    ('2048-08-26', 73.0, 'Dernier moment souscrire RVD', 50000, 'sortie', 'rvd', 0, 0, '2 ans avant activation'),
    ('2050-08-26', 75.0, 'Activation RVD +450 EUR/mois', 450, 'entree', 'rvd', 1, 0, 'Phase 3 demarre - pioche reduite'),
    ('2055-08-26', 80.0, 'Bilan dependance GIR', 0, 'info', 'sante', 0, 0, 'Evaluer EHPAD / aide domicile'),
    ('2060-08-26', 85.0, 'Bilan succession Anne-Lyse', 0, 'info', 'succession', 0, 0, 'AV beneficiaires verifies'),
    ('2067-08-26', 92.0, 'Cible atteinte - 50 000 EUR', 50000, 'info', 'fin', 0, 0, 'Mission accomplie'),
]

for a in actions:
    c.execute("INSERT INTO chronologie (date_cible,age_cible,action,montant,sens,categorie,auto,fait,note) VALUES (?,?,?,?,?,?,?,?,?)", a)

db.commit()
db.close()
print(f'{len(actions)} actions inserees')
print('Chronologie OK')
