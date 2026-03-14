import sqlite3
db = sqlite3.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
c = db.cursor()

# 1. Mise a jour profil (colonnes correctes)
c.execute("""UPDATE profil SET
    loyer_net = 320,
    aah_mensuel = 1033,
    rail_mensuel = 2760,
    taux_mdph = 75,
    capital_cible = 50000,
    rendement_annuel = 0.035
    WHERE id = 1""")
print('Profil mis a jour')

# 2. Mise a jour capital (total = 461 000)
c.execute("""INSERT INTO capital
    (date, cc, livret_a, ldds, lep, av1, av2, av3,
     av1_date_ouverture, av2_date_ouverture, av3_date_ouverture,
     av1_versements, av2_versements, av3_versements,
     av1_rendement, av2_rendement, av3_rendement, note)
    VALUES ('2026-03-12',
     500, 22950, 12000, 10000,
     130000, 130000, 155550,
     '2016-01-01','2026-01-01','2010-01-01',
     95000, 500, 110000,
     0.035, 0.035, 0.035,
     'v4.3 - Capital 461000 - SCI 296100 + Succession 217400 - travaux 33000 - donation 3349 - mobilier 15000 - charges 1075')""")
total = 500+22950+12000+10000+130000+130000+155550
print(f'Capital insere: {total} EUR')

# 3. Chronologie - supprimer anciens jalons
c.execute("DELETE FROM chronologie")
print('Anciens jalons supprimes')

# 4. Inserer planning complet
jalons = [
    ('2026-03-12', 50.5, 'Confirmer abattement handicap Anne-Lyse - notaire', 0, 'info', 'action', 0, 0, 'URGENT - droits passent de 43564 a 131193 sans abattement'),
    ('2026-03-12', 50.5, 'Demander dates baux appart + garage aux parents', 0, 'info', 'action', 0, 0, 'Pour planifier conges locataires'),
    ('2026-04-01', 50.6, 'Appel notaire - RDV donation usufruit MEYLAN', 0, 'info', 'action', 0, 0, 'Apres 28/04 mere 81 ans = usufruit 20%'),
    ('2026-04-15', 50.6, 'Reception AV Jean-Luc', 34500, 'entree', 'succession', 0, 0, 'Virement direct assureur - 0 EUR impot art 990 I'),
    ('2026-04-25', 50.7, 'Signature donation usufruit MEYLAN', 3349, 'sortie', 'meylan', 0, 0, 'Notaire TTC + TPF + CSI + debours'),
    ('2026-04-26', 50.7, 'Envoi conge LRAR locataire appart (3 mois)', 0, 'info', 'action', 0, 0, 'Bail meuble echeance aout 2026'),
    ('2026-04-26', 50.7, 'Envoi conge garage (courtoisie)', 0, 'info', 'action', 0, 0, 'Pas de bail - recuperation courtoisie'),
    ('2026-05-01', 50.7, 'Contacter artisans - demande devis renovation', 0, 'info', 'action', 0, 0, 'Renovation complete T3'),
    ('2026-05-01', 50.7, 'Declaration LMNP P0i + ouverture CFE', 0, 'info', 'action', 0, 0, 'Obligatoire avant location'),
    ('2026-05-01', 50.7, 'Choix comptable LMNP', 0, 'info', 'action', 0, 0, 'jedeclaremonmeuble.com ou equivalent'),
    ('2026-05-01', 50.7, 'Selection agence bail mobilite', 0, 'info', 'action', 0, 0, 'Gestion 9% negocie mandat 3 ans'),
    ('2026-06-10', 50.8, 'Virement net SCI (+296 100 EUR)', 296100, 'entree', 'sci', 0, 0, 'Net de tout - notaire vire en 1 fois'),
    ('2026-06-30', 50.8, 'Acompte travaux 30%', 9900, 'sortie', 'meylan', 0, 0, 'Travaux totaux 33 000 EUR'),
    ('2026-07-05', 50.9, 'Virement net succession (+182 900 EUR)', 182900, 'entree', 'succession', 0, 0, 'Droits + frais deduits par notaire'),
    ('2026-07-27', 50.9, 'Deadline droits succession', 0, 'info', 'jalon', 0, 0, 'Deja deduits dans le virement notaire'),
    ('2026-08-01', 51.0, 'Recuperation appart + garage MEYLAN', 0, 'info', 'jalon', 0, 0, 'Bail meuble echeance aout + garage courtoisie'),
    ('2026-08-01', 51.0, 'Versement parents demarre (325 EUR/mois)', 325, 'sortie', 'recurrent', 0, 0, 'Contribution foyer - nourriture electricite eau TEOM'),
    ('2026-09-01', 51.0, 'Debut chantier renovation MEYLAN', 0, 'info', 'jalon', 0, 0, '6-10 semaines apres signature devis'),
    ('2026-11-15', 51.2, 'Fin chantier - Solde artisans 70%', 23100, 'sortie', 'meylan', 0, 0, '70% de 33 000 EUR'),
    ('2026-12-01', 51.3, 'Achat mobilier LMNP', 15000, 'sortie', 'meylan', 0, 0, 'Ameublement complet T3'),
    ('2026-12-31', 51.3, 'CFE + comptable + charges courantes', 1075, 'sortie', 'meylan', 0, 0, 'Copro 140 + PNO 115 + elec 120 + CFE 300 + comptable 400'),
    ('2027-01-15', 51.4, 'Signature premier bail mobilite', 0, 'info', 'jalon', 0, 0, 'Appart + garage meme bail meme locataire'),
    ('2027-01-15', 51.4, 'Premieres recettes locatives (+320 EUR/mois)', 320, 'entree', 'recurrent', 0, 0, 'LMNP reel - base imposable 0 EUR - AAH protegee'),
]

for j in jalons:
    c.execute("""INSERT INTO chronologie
        (date_cible, age_cible, action, montant, sens, categorie, auto, fait, note)
        VALUES (?,?,?,?,?,?,?,?,?)""", j)

db.commit()
db.close()

# Verification
db2 = sqlite3.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
c2 = db2.cursor()
c2.execute("SELECT COUNT(*) FROM chronologie")
nb = c2.fetchone()[0]
c2.execute("SELECT loyer_net, rail_mensuel, aah_mensuel FROM profil WHERE id=1")
row = c2.fetchone()
c2.execute("SELECT cc+livret_a+ldds+lep+av1+av2+av3 FROM capital ORDER BY date DESC LIMIT 1")
cap = c2.fetchone()[0]
db2.close()

print(f'Jalons inseres: {nb}')
print(f'Profil: loyer_net={row[0]}, rail={row[1]}, aah={row[2]}')
print(f'Capital total: {cap}')
print('Base de donnees v4.3 OK')
