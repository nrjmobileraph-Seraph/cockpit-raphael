import sqlite3, json
db = sqlite3.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
c = db.cursor()

# Mise a jour profil
c.execute("""UPDATE profil SET
    capital_initial = 461000,
    rail_mensuel = 2760,
    aah_mensuel = 1033,
    loyer_net = 320,
    taux_mdph = 75,
    age_fin_aah = 64,
    rendement_av = 0.035,
    cible_c92 = 50000
    WHERE id = 1""")

# Mise a jour capital
c.execute("""INSERT INTO capital
    (date, cc, livret_a, ldds, lep, av1, av2, av3,
     av1_rendement, av2_rendement, av3_rendement,
     note)
    VALUES ('2026-03-12',
     500, 22950, 12000, 10000,
     130000, 130000, 155550,
     0.035, 0.035, 0.035,
     'v4.3 - Capital 461 000 EUR - SCI 296100 + Succession 217400 - travaux 33000 - donation 3349 - mobilier 15000 - charges 1075')""")

# Planning chronologique dans jalons
c.execute("DELETE FROM chronologie WHERE 1=1")

jalons = [
    ('2026-03-12', 'Confirmer abattement handicap Anne-Lyse - notaire', 'rouge', 0),
    ('2026-03-12', 'Demander dates baux appart + garage aux parents', 'rouge', 0),
    ('2026-04-01', 'Appel notaire - RDV donation usufruit MEYLAN', 'rouge', 0),
    ('2026-04-15', 'Reception AV Jean-Luc (+34 500 EUR)', 'vert', 34500),
    ('2026-04-25', 'Signature donation usufruit MEYLAN (-3 349 EUR)', 'rouge', -3349),
    ('2026-04-26', 'Envoi conge LRAR locataire appart (3 mois)', 'orange', 0),
    ('2026-04-26', 'Envoi conge garage (courtoisie)', 'orange', 0),
    ('2026-05-01', 'Contacter artisans - demande devis renovation', 'orange', 0),
    ('2026-05-01', 'Declaration LMNP P0i + ouverture CFE', 'orange', 0),
    ('2026-05-01', 'Choix comptable LMNP (jedeclaremonmeuble)', 'orange', 0),
    ('2026-05-01', 'Selection agence bail mobilite', 'orange', 0),
    ('2026-06-10', 'Virement net SCI (+296 100 EUR)', 'vert', 296100),
    ('2026-06-30', 'Acompte travaux 30% (-9 900 EUR)', 'orange', -9900),
    ('2026-07-05', 'Virement net succession (+182 900 EUR)', 'vert', 182900),
    ('2026-07-27', 'Deadline droits succession (deduits par notaire)', 'rouge', 0),
    ('2026-08-01', 'Recuperation appart + garage MEYLAN', 'vert', 0),
    ('2026-08-01', 'Versement parents demarre (325 EUR/mois)', 'orange', -325),
    ('2026-09-01', 'Debut chantier renovation MEYLAN', 'orange', 0),
    ('2026-11-15', 'Fin chantier - Solde artisans 70% (-23 100 EUR)', 'orange', -23100),
    ('2026-12-01', 'Achat mobilier LMNP (-15 000 EUR)', 'orange', -15000),
    ('2026-12-31', 'CFE + comptable + charges courantes (-1 075 EUR)', 'jaune', -1075),
    ('2027-01-15', 'Signature premier bail mobilite', 'vert', 0),
    ('2027-01-15', 'Premieres recettes locatives (+320 EUR/mois)', 'vert', 320),
]

for date, action, niveau, flux in jalons:
    c.execute("INSERT INTO chronologie (date, action, niveau, flux) VALUES (?,?,?,?)",
              (date, action, niveau, flux))

db.commit()
db.close()

# Verification
db2 = sqlite3.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
c2 = db2.cursor()
c2.execute("SELECT COUNT(*) FROM chronologie")
nb = c2.fetchone()[0]
c2.execute("SELECT capital_initial, rail_mensuel, loyer_net FROM profil WHERE id=1")
row = c2.fetchone()
db2.close()

print(f'Jalons inseres: {nb}')
print(f'Profil: capital={row[0]}, rail={row[1]}, loyer_net={row[2]}')
print('Base de donnees v4.3 OK')
