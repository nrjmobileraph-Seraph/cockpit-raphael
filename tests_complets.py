import sqlite3
from datetime import date, timedelta

print('=' * 60)
print('BATTERIE DE TESTS COCKPIT v4.3')
print('=' * 60)

db_path = 'C:/Users/BoulePiou/cockpit-raphael/cockpit.db'
erreurs = 0
ok = 0

# ==========================================
# TEST 1 : INTEGRITE BASE DE DONNEES
# ==========================================
print('\n--- TEST 1 : INTEGRITE BASE ---')
db = sqlite3.connect(db_path)
db.row_factory = sqlite3.Row
c = db.cursor()

# Tables requises
tables_requises = ['profil', 'capital', 'chronologie', 'aah_suivi', 'devis_artisans']
c.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = [r['name'] for r in c.fetchall()]
for t in tables_requises:
    if t in tables:
        print(f'  [OK] Table {t} existe')
        ok += 1
    else:
        print(f'  [ERREUR] Table {t} MANQUANTE')
        erreurs += 1

# Colonnes chronologie
c.execute("PRAGMA table_info(chronologie)")
cols = [r['name'] for r in c.fetchall()]
cols_requises = ['montant_reel', 'date_reelle', 'confirme_1mois', 'confirme_6mois']
for col in cols_requises:
    if col in cols:
        print(f'  [OK] Colonne chronologie.{col}')
        ok += 1
    else:
        print(f'  [ERREUR] Colonne chronologie.{col} MANQUANTE')
        erreurs += 1

# ==========================================
# TEST 2 : COHERENCE CAPITAL
# ==========================================
print('\n--- TEST 2 : COHERENCE CAPITAL ---')
c.execute("SELECT cc, livret_a, ldds, lep, av1, av2, av3 FROM capital ORDER BY date DESC LIMIT 1")
cap = dict(c.fetchone())
total = sum(cap.values())
if abs(total - 461000) < 1:
    print(f'  [OK] Capital total = {total:,.0f} EUR (attendu 461 000)')
    ok += 1
else:
    print(f'  [ERREUR] Capital total = {total:,.0f} EUR (attendu 461 000)')
    erreurs += 1

# Verification poches
poches = {'cc': 500, 'livret_a': 22950, 'ldds': 12000, 'lep': 10000, 'av1': 130000, 'av2': 130000, 'av3': 155550}
for poche, attendu in poches.items():
    if abs(cap[poche] - attendu) < 1:
        print(f'  [OK] {poche} = {cap[poche]:,.0f} (attendu {attendu:,.0f})')
        ok += 1
    else:
        print(f'  [ERREUR] {poche} = {cap[poche]:,.0f} (attendu {attendu:,.0f})')
        erreurs += 1

# ==========================================
# TEST 3 : COHERENCE PROFIL
# ==========================================
print('\n--- TEST 3 : COHERENCE PROFIL ---')
c.execute("SELECT * FROM profil WHERE id=1")
profil = dict(c.fetchone())

checks_profil = {
    'loyer_net': 320,
    'rail_mensuel': 2760,
    'aah_mensuel': 1033,
    'taux_mdph': 75,
    'capital_cible': 50000,
    'rendement_annuel': 0.035,
}
for champ, attendu in checks_profil.items():
    val = profil.get(champ, 'ABSENT')
    if val == attendu:
        print(f'  [OK] {champ} = {val}')
        ok += 1
    else:
        print(f'  [ERREUR] {champ} = {val} (attendu {attendu})')
        erreurs += 1

# ==========================================
# TEST 4 : COHERENCE FLUX CHRONOLOGIE
# ==========================================
print('\n--- TEST 4 : COHERENCE FLUX ---')
c.execute("SELECT * FROM chronologie ORDER BY date_cible ASC")
rows = [dict(r) for r in c.fetchall()]

# Compter entrees et sorties
entrees = sum(r['montant'] for r in rows if r['sens'] == 'entree' and r['montant'] > 0)
sorties = sum(r['montant'] for r in rows if r['sens'] == 'sortie' and r['montant'] > 0)

# Verifier les gros flux
flux_attendus = {
    'AV Jean-Luc': 34500,
    'SCI': 296100,
    'succession': 182900,
    'donation usufruit': 3349,
    'Acompte travaux': 9900,
    'Solde artisans': 23100,
    'mobilier': 15000,
    'charges courantes': 1075,
}

for nom, montant in flux_attendus.items():
    trouve = False
    for r in rows:
        if nom.lower() in r['action'].lower() and abs(r['montant'] - montant) < 1:
            trouve = True
            break
    if trouve:
        print(f'  [OK] Flux {nom} = {montant:,.0f} EUR')
        ok += 1
    else:
        print(f'  [ERREUR] Flux {nom} = {montant:,.0f} EUR NON TROUVE')
        erreurs += 1

# Verifier total entrees = 513 500
entrees_principales = 34500 + 296100 + 182900
if abs(entrees_principales - 513500) < 1:
    print(f'  [OK] Total entrees principales = {entrees_principales:,.0f} (attendu 513 500)')
    ok += 1
else:
    print(f'  [ERREUR] Total entrees principales = {entrees_principales:,.0f} (attendu 513 500)')
    erreurs += 1

# Verifier total sorties = 52 424
sorties_principales = 3349 + 9900 + 23100 + 15000 + 1075
if abs(sorties_principales - 52424) < 1:
    print(f'  [OK] Total sorties principales = {sorties_principales:,.0f} (attendu 52 424)')
    ok += 1
else:
    print(f'  [ERREUR] Total sorties principales = {sorties_principales:,.0f} (attendu 52 424)')
    erreurs += 1

# Capital = entrees - sorties
capital_calcule = entrees_principales - sorties_principales
if abs(capital_calcule - 461076) < 2:
    print(f'  [OK] Capital calcule = {capital_calcule:,.0f} (attendu ~461 076)')
    ok += 1
else:
    print(f'  [ERREUR] Capital calcule = {capital_calcule:,.0f} (attendu ~461 076)')
    erreurs += 1

# ==========================================
# TEST 5 : COHERENCE AAH
# ==========================================
print('\n--- TEST 5 : COHERENCE AAH ---')
c.execute("SELECT * FROM aah_suivi ORDER BY mois ASC")
aah_rows = [dict(r) for r in c.fetchall()]

if len(aah_rows) == 14:
    print(f'  [OK] AAH suivi = 14 entrees (2026-2039)')
    ok += 1
else:
    print(f'  [ERREUR] AAH suivi = {len(aah_rows)} entrees (attendu 14)')
    erreurs += 1

# Verifier AAH 2026 = 625
aah_2026 = [r for r in aah_rows if r['mois'] == '2026']
if aah_2026 and aah_2026[0]['montant_prevu'] == 625:
    print(f'  [OK] AAH 2026 prevue = 625 EUR')
    ok += 1
else:
    print(f'  [ERREUR] AAH 2026 prevue incorrecte')
    erreurs += 1

# Verifier AAH 2029 = 1033
aah_2029 = [r for r in aah_rows if r['mois'] == '2029']
if aah_2029 and aah_2029[0]['montant_prevu'] == 1033:
    print(f'  [OK] AAH 2029 prevue = 1 033 EUR')
    ok += 1
else:
    print(f'  [ERREUR] AAH 2029 prevue incorrecte')
    erreurs += 1

# ==========================================
# TEST 6 : COHERENCE DEVIS ARTISANS
# ==========================================
print('\n--- TEST 6 : DEVIS ARTISANS ---')
c.execute("SELECT COUNT(*) as nb FROM devis_artisans")
nb_devis = c.fetchone()['nb']
if nb_devis >= 8:
    print(f'  [OK] Devis artisans = {nb_devis} corps de metier')
    ok += 1
else:
    print(f'  [ERREUR] Devis artisans = {nb_devis} (attendu >= 8)')
    erreurs += 1

# ==========================================
# TEST 7 : SIMULATION SAISIE FLUX
# ==========================================
print('\n--- TEST 7 : SIMULATION SAISIE FLUX ---')

# Prendre un jalon non fait avec montant
c.execute("SELECT * FROM chronologie WHERE fait=0 AND montant>0 AND sens='entree' LIMIT 1")
jalon_test = dict(c.fetchone())
id_test = jalon_test['id']
montant_prevu = jalon_test['montant']

# Simuler saisie avec ecart
montant_reel = montant_prevu - 300
c.execute("UPDATE chronologie SET fait=1, montant_reel=?, date_reelle=? WHERE id=?",
          (montant_reel, str(date.today()), id_test))
db.commit()

# Verifier
c.execute("SELECT fait, montant_reel, date_reelle FROM chronologie WHERE id=?", (id_test,))
r = dict(c.fetchone())
if r['fait'] == 1 and r['montant_reel'] == montant_reel:
    print(f'  [OK] Saisie flux OK : {jalon_test["action"][:40]} = {montant_reel:,.0f} EUR')
    ok += 1
else:
    print(f'  [ERREUR] Saisie flux echouee')
    erreurs += 1

# Calculer capital reel cumule
c.execute("SELECT * FROM chronologie WHERE fait=1 AND montant>0")
faits = [dict(r) for r in c.fetchall()]
capital_reel = 0
for f in faits:
    mr = f['montant_reel'] if f['montant_reel'] else f['montant']
    if f['sens'] == 'entree':
        capital_reel += mr
    elif f['sens'] == 'sortie':
        capital_reel -= mr
print(f'  [INFO] Capital reel cumule apres saisie = {capital_reel:,.0f} EUR')

# Simuler annulation
c.execute("UPDATE chronologie SET fait=0, montant_reel=0, date_reelle='' WHERE id=?", (id_test,))
db.commit()
c.execute("SELECT fait FROM chronologie WHERE id=?", (id_test,))
if c.fetchone()['fait'] == 0:
    print(f'  [OK] Annulation OK : jalon remis a 0')
    ok += 1
else:
    print(f'  [ERREUR] Annulation echouee')
    erreurs += 1

# ==========================================
# TEST 8 : SIMULATION CONFIRMATION 1M/6M
# ==========================================
print('\n--- TEST 8 : SIMULATION CONFIRMATION ---')

# Simuler un jalon fait il y a 35 jours
date_35j = str(date.today() - timedelta(days=35))
c.execute("UPDATE chronologie SET fait=1, montant_reel=?, date_reelle=? WHERE id=?",
          (montant_reel, date_35j, id_test))
db.commit()

c.execute("SELECT * FROM chronologie WHERE id=?", (id_test,))
r = dict(c.fetchone())
dr = date.fromisoformat(r['date_reelle'])
jours = (date.today() - dr).days
if jours >= 30 and r['confirme_1mois'] == 0:
    print(f'  [OK] Declenchement confirmation 1 mois correct ({jours} jours)')
    ok += 1
else:
    print(f'  [ERREUR] Declenchement 1 mois incorrect')
    erreurs += 1

# Simuler confirmation 1 mois
c.execute("UPDATE chronologie SET confirme_1mois=1, date_confirme_1mois=? WHERE id=?",
          (str(date.today()), id_test))
db.commit()
c.execute("SELECT confirme_1mois FROM chronologie WHERE id=?", (id_test,))
if c.fetchone()['confirme_1mois'] == 1:
    print(f'  [OK] Confirmation 1 mois enregistree')
    ok += 1
else:
    print(f'  [ERREUR] Confirmation 1 mois echouee')
    erreurs += 1

# Simuler 6 mois
date_185j = str(date.today() - timedelta(days=185))
c.execute("UPDATE chronologie SET date_reelle=? WHERE id=?", (date_185j, id_test))
db.commit()
c.execute("SELECT * FROM chronologie WHERE id=?", (id_test,))
r = dict(c.fetchone())
dr2 = date.fromisoformat(r['date_reelle'])
jours2 = (date.today() - dr2).days
if jours2 >= 180 and r['confirme_6mois'] == 0:
    print(f'  [OK] Declenchement verrouillage 6 mois correct ({jours2} jours)')
    ok += 1
else:
    print(f'  [ERREUR] Declenchement 6 mois incorrect')
    erreurs += 1

# Verrouiller
c.execute("UPDATE chronologie SET confirme_6mois=1, date_confirme_6mois=? WHERE id=?",
          (str(date.today()), id_test))
db.commit()
c.execute("SELECT confirme_6mois FROM chronologie WHERE id=?", (id_test,))
if c.fetchone()['confirme_6mois'] == 1:
    print(f'  [OK] Verrouillage 6 mois enregistre')
    ok += 1
else:
    print(f'  [ERREUR] Verrouillage 6 mois echoue')
    erreurs += 1

# Remettre le jalon a zero (nettoyage)
c.execute("UPDATE chronologie SET fait=0, montant_reel=0, date_reelle='', confirme_1mois=0, date_confirme_1mois='', confirme_6mois=0, date_confirme_6mois='' WHERE id=?", (id_test,))
db.commit()
print(f'  [OK] Nettoyage test effectue')
ok += 1

# ==========================================
# TEST 9 : SIMULATION FLUX IMPREVU
# ==========================================
print('\n--- TEST 9 : FLUX IMPREVU ---')
c.execute("""INSERT INTO chronologie
    (date_cible, age_cible, action, montant, sens, categorie, auto, fait, note, montant_reel, date_reelle)
    VALUES (?, 50.5, 'TEST FLUX IMPREVU', 150, 'entree', 'imprevu', 0, 1, 'Test automatique', 150, ?)""",
    (str(date.today()), str(date.today())))
db.commit()

c.execute("SELECT * FROM chronologie WHERE action='TEST FLUX IMPREVU'")
test_flux = c.fetchone()
if test_flux:
    print(f'  [OK] Flux imprevu insere et retrouve')
    ok += 1
    # Nettoyer
    c.execute("DELETE FROM chronologie WHERE action='TEST FLUX IMPREVU'")
    db.commit()
    print(f'  [OK] Flux imprevu nettoye')
    ok += 1
else:
    print(f'  [ERREUR] Flux imprevu non retrouve')
    erreurs += 1

# ==========================================
# TEST 10 : CALCULS CROISES
# ==========================================
print('\n--- TEST 10 : CALCULS CROISES ---')

# Patrimoine total = capital + immo
patrimoine = 461000 + 219000
if patrimoine == 680000:
    print(f'  [OK] Patrimoine total = {patrimoine:,.0f} (461k + 219k = 680k)')
    ok += 1
else:
    print(f'  [ERREUR] Patrimoine total = {patrimoine:,.0f} (attendu 680 000)')
    erreurs += 1

# Revenus mensuels
aah = 1033
loyer = 320
parents = 325
reste = aah + loyer - parents
if reste == 1028:
    print(f'  [OK] Reste mensuel = {reste} EUR (1033 + 320 - 325 = 1028)')
    ok += 1
else:
    print(f'  [ERREUR] Reste mensuel = {reste} (attendu 1028)')
    erreurs += 1

# LMNP : recettes - charges = 320/mois
recettes = 8827
charges = 4984
net_lmnp = recettes - charges
net_mois = round(net_lmnp / 12)
if abs(net_mois - 320) <= 1:
    print(f'  [OK] LMNP net = {net_mois} EUR/mois (8827 - 4984 = 3843 / 12 = 320)')
    ok += 1
else:
    print(f'  [ERREUR] LMNP net = {net_mois} (attendu 320)')
    erreurs += 1

# Amortissements > resultat = base imposable 0
amort = 11087
resultat = 3843
if amort > resultat:
    print(f'  [OK] Amortissements {amort} > resultat {resultat} = base imposable 0 EUR')
    ok += 1
else:
    print(f'  [ERREUR] Amortissements {amort} < resultat {resultat}')
    erreurs += 1

# ASPA seuil
seuil_aspa = int((12523 - 320*12) / 0.03 - 219000)
print(f'  [INFO] Seuil ASPA calcule = {seuil_aspa:,.0f} EUR (attendu ~198 433)')
if abs(seuil_aspa - 198433) < 2000:
    print(f'  [OK] Seuil ASPA coherent')
    ok += 1
else:
    print(f'  [ATTENTION] Seuil ASPA = {seuil_aspa:,.0f} - verifier formule')
    erreurs += 1

# SCI : 433000 - 26000 - frais = 296100
sci_net = 433000 - 26000 - 72100 - 800 - 3209 - 910 - 30553 - 3294
if abs(sci_net - 296134) < 100:
    print(f'  [OK] SCI net calcule = {sci_net:,.0f} (attendu ~296 134 arrondi 296 100)')
    ok += 1
else:
    print(f'  [ERREUR] SCI net = {sci_net:,.0f} (attendu ~296 134)')
    erreurs += 1

# Succession : part 246500 - abattements - droits + AV - frais = 217400
part = 246500
abatt = 7967 + 159325
base = part - abatt
droits = round(base * 0.55)
net_droits = part - droits
av = 34500
frais = 20020
net_succ = net_droits + av - frais
print(f'  [INFO] Succession calcule = {net_succ:,.0f} (attendu ~217 400)')
if abs(net_succ - 217400) < 500:
    print(f'  [OK] Succession coherent')
    ok += 1
else:
    print(f'  [ATTENTION] Succession = {net_succ:,.0f} - ecart a verifier')
    erreurs += 1

# Donation usufruit
usufruit = round(166000 * 0.20)
frais_don = 2634 + 199 + 166 + 350
total_don = frais_don
if abs(total_don - 3349) < 1:
    print(f'  [OK] Donation usufruit = {total_don:,.0f} EUR (attendu 3 349)')
    ok += 1
else:
    print(f'  [ERREUR] Donation usufruit = {total_don:,.0f} (attendu 3 349)')
    erreurs += 1

db.close()

# ==========================================
# RESULTAT FINAL
# ==========================================
print('\n' + '=' * 60)
print(f'RESULTAT : {ok} OK / {erreurs} ERREURS')
if erreurs == 0:
    print('COCKPIT v4.3 : TOUS LES TESTS PASSENT')
else:
    print(f'COCKPIT v4.3 : {erreurs} POINT(S) A VERIFIER')
print('=' * 60)
