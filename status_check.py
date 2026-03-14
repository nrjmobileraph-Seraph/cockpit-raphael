import sqlite3
db = sqlite3.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
c = db.cursor()

# Ajouter jalons prix plancher
jalons = [
    ('2026-07-01', 50.9, 'PLANCHER MAISON La Ravoire : ne pas vendre en dessous de 207 000 EUR', 0, 'info', 'action', 0, 0, 'Valeur succession 200k + 7k frais caches = 207k minimum. Au-dessus de 207k = marge nette.'),
    ('2026-07-01', 50.9, 'PLANCHER APPART Bassens : ne pas vendre en dessous de 290 000 EUR', 0, 'info', 'action', 0, 0, 'Appartement neuf VEFA - marge du neuf couvre les frais caches.'),
]

for j in jalons:
    c.execute("""INSERT INTO chronologie
        (date_cible, age_cible, action, montant, sens, categorie, auto, fait, note)
        VALUES (?,?,?,?,?,?,?,?,?)""", j)

db.commit()

# Verification complete
c.execute("SELECT COUNT(*) FROM chronologie")
nb_jalons = c.fetchone()[0]
c.execute("SELECT COUNT(*) FROM chronologie WHERE fait=1")
nb_faits = c.fetchone()[0]
c.execute("SELECT COUNT(*) FROM aah_suivi")
nb_aah = c.fetchone()[0]
c.execute("SELECT loyer_net, rail_mensuel, aah_mensuel, taux_mdph FROM profil WHERE id=1")
profil = c.fetchone()
c.execute("SELECT cc+livret_a+ldds+lep+av1+av2+av3 FROM capital ORDER BY date DESC LIMIT 1")
cap = c.fetchone()[0]

db.close()

print('=== ETAT COCKPIT v4.3 ===')
print(f'Capital en base: {cap:,.0f} EUR')
print(f'Profil: loyer={profil[0]}, rail={profil[1]}, aah={profil[2]}, mdph={profil[3]}%')
print(f'Jalons: {nb_jalons} (dont {nb_faits} faits)')
print(f'AAH suivi: {nb_aah} annees')
print()
print('=== CE QUI MARCHE ===')
print('Dashboard Phase 0 avec barre progression capital')
print('Page Jalons interactive (saisie, ecart, confirmation 1M/6M)')
print('Page AAH/CAF/PCH avec saisie annuelle')
print('Badge MDPH dynamique (AAH STOP 64 / AAH A VIE)')
print('Badge Plan Operationnel garanti 92 ans')
print('Prix planchers vente ajoutes')
print('Table AAH 2026-2039')
print()
print('=== RESTE A FAIRE ===')
print('1. Mettre a jour page Annexe avec chiffres v3')
print('2. Tester un flux complet')
print('Prix planchers ajoutes OK')
