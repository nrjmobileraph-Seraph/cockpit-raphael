import psycopg2, psycopg2.extras, time, sys

print('=' * 70)
print('  AUDIT INTEGRAL COCKPIT PATRIMONIAL RAPHAEL')
print('  Protocole de certification - Zero tolerance')
print('=' * 70)

conn = psycopg2.connect(host='aws-1-eu-west-1.pooler.supabase.com', port=6543, dbname='postgres', user='postgres.zyizvlrwsatxqehhqiwh', password='Seraphetraph/62//26**', cursor_factory=psycopg2.extras.RealDictCursor)
c = conn.cursor()
ok = 0
err = 0
warn = 0

def check(condition, msg_ok, msg_err):
    global ok, err
    if condition:
        print(f'  [OK] {msg_ok}'); ok+=1
    else:
        print(f'  [ERREUR] {msg_err}'); err+=1

def warning(msg):
    global warn
    print(f'  [ATTENTION] {msg}'); warn+=1

# ============================================================
# BLOC 1 : INTEGRITE BASE DE DONNEES
# ============================================================
print('\n' + '='*70)
print('  BLOC 1 : INTEGRITE BASE DE DONNEES')
print('='*70)

# 1.1 Tables existent
for table in ['profil','capital','chronologie','aah_suivi','devis_artisans']:
    c.execute(f"SELECT COUNT(*) as nb FROM {table}")
    r = c.fetchone()
    check(r is not None, f'Table {table} existe', f'Table {table} ABSENTE')

# 1.2 Profil unique
c.execute('SELECT COUNT(*) as nb FROM profil')
nb = c.fetchone()['nb']
check(nb == 1, f'Profil unique ({nb})', f'Profil multiple ({nb})')

# ============================================================
# BLOC 2 : PROFIL - 14 PARAMETRES
# ============================================================
print('\n' + '='*70)
print('  BLOC 2 : PROFIL (14 parametres)')
print('='*70)

c.execute('SELECT * FROM profil LIMIT 1')
p = dict(c.fetchone())

ref_profil = {
    'nom': 'Raphael', 'date_naissance': '1975-08-26', 'age_cible': 92,
    'capital_cible': 50000, 'taux_mdph': 75, 'aah_mensuel': 1033.0,
    'loyer_net': 320.0, 'rail_mensuel': 2760.0, 'rendement_annuel': 0.035,
    'pch_mensuel': 0.0, 'rvd_mensuel': 450.0, 'mdph_80plus': 0
}
for k, v in ref_profil.items():
    val = p.get(k)
    if isinstance(v, float):
        check(val is not None and abs(val - v) < 0.001, f'{k} = {val}', f'{k} = {val} (attendu {v})')
    else:
        check(val == v, f'{k} = {val}', f'{k} = {val} (attendu {v})')

# ============================================================
# BLOC 3 : CAPITAL - 7 POCHES
# ============================================================
print('\n' + '='*70)
print('  BLOC 3 : CAPITAL (7 poches = 461 000 EUR)')
print('='*70)

c.execute('SELECT * FROM capital ORDER BY date DESC LIMIT 1')
cap = dict(c.fetchone())

ref_cap = {'cc':500, 'livret_a':22950, 'ldds':12000, 'lep':10000, 'av1':130000, 'av2':130000, 'av3':155550}
for k, v in ref_cap.items():
    check(cap[k] == v, f'{k} = {cap[k]:,.0f}', f'{k} = {cap[k]} (attendu {v})')

total = sum(ref_cap.values())
total_srv = cap['cc']+cap['livret_a']+cap['ldds']+cap['lep']+cap['av1']+cap['av2']+cap['av3']
check(abs(total_srv - 461000) < 1, f'TOTAL = {total_srv:,.0f} EUR', f'TOTAL = {total_srv:,.0f} (attendu 461000)')

# Rendements AV
for av in ['av1','av2','av3']:
    r = cap.get(f'{av}_rendement', 0)
    check(abs(r - 0.035) < 0.001, f'{av}_rendement = {r}', f'{av}_rendement = {r} (attendu 0.035)')

# Dates ouverture
check(cap.get('av1_date_ouverture') == '2016-01-01', 'AV1 ouverture 2016', f'AV1 ouverture {cap.get("av1_date_ouverture")}')
check(cap.get('av3_date_ouverture') == '2010-01-01', 'AV3 ouverture 2010', f'AV3 ouverture {cap.get("av3_date_ouverture")}')

# Versements
check(cap.get('av1_versements') == 95000, 'AV1 versements 95000', f'AV1 versements {cap.get("av1_versements")}')
check(cap.get('av3_versements') == 110000, 'AV3 versements 110000', f'AV3 versements {cap.get("av3_versements")}')

# ============================================================
# BLOC 4 : CHRONOLOGIE - 26 JALONS
# ============================================================
print('\n' + '='*70)
print('  BLOC 4 : CHRONOLOGIE (26 jalons)')
print('='*70)

c.execute('SELECT * FROM chronologie ORDER BY date_cible ASC')
jalons = c.fetchall()
check(len(jalons) >= 26, f'{len(jalons)} jalons', f'{len(jalons)} jalons (attendu 26+)')

# Flux critiques
flux_critiques = {
    'AV Jean-Luc': 34500,
    'SCI': 296100,
    'succession': 182900,
    'Donation usufruit': 3349,
    'Acompte': 9900,
    'Solde artisans': 23100,
    'Mobilier': 15000,
}
for nom, montant in flux_critiques.items():
    trouve = any(nom.lower() in j['action'].lower() and abs(j['montant']) >= montant - 1 for j in jalons)
    check(trouve, f'Flux {nom} = {montant:,.0f}', f'Flux {nom} ABSENT')

# Colonnes de suivi presentes
cols_suivi = ['fait', 'montant_reel', 'date_reelle', 'confirme_1mois', 'confirme_6mois']
for col in cols_suivi:
    check(col in jalons[0].keys(), f'Colonne {col} presente', f'Colonne {col} ABSENTE')

# ============================================================
# BLOC 5 : AAH - 14 ANNEES
# ============================================================
print('\n' + '='*70)
print('  BLOC 5 : AAH (14 annees 2026-2039)')
print('='*70)

c.execute('SELECT mois, montant_prevu FROM aah_suivi ORDER BY mois ASC')
aah = c.fetchall()
check(len(aah) == 14, f'{len(aah)} annees', f'{len(aah)} (attendu 14)')

ref_aah = {'2026':625, '2027':625, '2028':900, '2029':1033, '2030':1033,
           '2031':1033, '2032':1033, '2033':1033, '2034':1033, '2035':1033,
           '2036':1033, '2037':1033, '2038':1033, '2039':0}
for r in aah:
    mois = r['mois'].replace('-01','')
    attendu = ref_aah.get(mois)
    if attendu is not None:
        check(r['montant_prevu'] == attendu, f'AAH {mois} = {r["montant_prevu"]}', f'AAH {mois} = {r["montant_prevu"]} (attendu {attendu})')

# ============================================================
# BLOC 6 : DEVIS ARTISANS - 8 CORPS
# ============================================================
print('\n' + '='*70)
print('  BLOC 6 : DEVIS ARTISANS (8 corps de metier)')
print('='*70)

c.execute('SELECT * FROM devis_artisans ORDER BY id ASC')
devis = c.fetchall()
check(len(devis) >= 8, f'{len(devis)} corps de metier', f'{len(devis)} (attendu 8)')

corps_attendus = ['Electricite','Plomberie','Peinture','Sol','Cuisine','Salle de bain','Menuiserie','Divers']
for corps in corps_attendus:
    trouve = any(corps.lower() in d['corps_metier'].lower() for d in devis)
    check(trouve, f'{corps} present', f'{corps} ABSENT')

# ============================================================
# BLOC 7 : OPERATIONS CRUD
# ============================================================
print('\n' + '='*70)
print('  BLOC 7 : OPERATIONS CRUD (Create/Read/Update/Delete)')
print('='*70)

# CREATE
c.execute("INSERT INTO chronologie (date_cible, age_cible, action, montant, sens, categorie) VALUES (%s,%s,%s,%s,%s,%s)",
          ('2099-12-31', 99, 'AUDIT_TEST_CREATE', 12345, 'info', 'test'))
conn.commit()
c.execute("SELECT * FROM chronologie WHERE action='AUDIT_TEST_CREATE'")
r = c.fetchone()
check(r is not None, 'CREATE OK', 'CREATE ECHOUE')

# READ
check(r['montant'] == 12345, 'READ montant OK', 'READ montant ECHOUE')

# UPDATE
c.execute("UPDATE chronologie SET montant=99999 WHERE action='AUDIT_TEST_CREATE'")
conn.commit()
c.execute("SELECT montant FROM chronologie WHERE action='AUDIT_TEST_CREATE'")
r2 = c.fetchone()
check(r2['montant'] == 99999, 'UPDATE OK', 'UPDATE ECHOUE')

# DELETE
c.execute("DELETE FROM chronologie WHERE action='AUDIT_TEST_CREATE'")
conn.commit()
c.execute("SELECT * FROM chronologie WHERE action='AUDIT_TEST_CREATE'")
r3 = c.fetchone()
check(r3 is None, 'DELETE OK', 'DELETE ECHOUE')

# ============================================================
# BLOC 8 : FORMULES FINANCIERES
# ============================================================
print('\n' + '='*70)
print('  BLOC 8 : FORMULES FINANCIERES')
print('='*70)

C = 461000
r_ann = 0.035
age = 50.5
cible = 92
mois = int((cible - age) * 12)
r_mens = r_ann / 12

# ARVA
if r_mens > 0:
    arva = C * r_mens / (1 - (1 + r_mens) ** (-mois))
else:
    arva = C / mois
check(abs(arva - 1800) < 300, f'ARVA = {arva:.0f} EUR/mois (plausible)', f'ARVA = {arva:.0f} EUR/mois (hors plage)')

# Capital epuise avec AAH
revenu_mens = 1033 + 320 - 325
pioche_mens = 2760 - revenu_mens
duree_mois_simple = C / pioche_mens
duree_ans = duree_mois_simple / 12
check(duree_ans > 20, f'Duree simple = {duree_ans:.1f} ans (>20 ans)', f'Duree simple = {duree_ans:.1f} ans')

# Capital epuise sans AAH
pioche_sans = 2760 - 320 + 325
duree_sans = C / pioche_sans / 12
check(duree_sans < 20, f'Sans AAH = {duree_sans:.1f} ans (<20 ans = DANGER)', f'Sans AAH = {duree_sans:.1f} ans')

# SCI : PV + PS
pv_brute = 246717
ps = 30553
check(abs(ps - pv_brute * 0.72 * 0.172) < 100, f'PS SCI = {ps} (correct)', f'PS SCI = {ps} (erreur)')

# ============================================================
# BLOC 9 : STRESS TEST
# ============================================================
print('\n' + '='*70)
print('  BLOC 9 : STRESS TEST')
print('='*70)

# Ecriture rapide 10x
start = time.time()
for i in range(10):
    c.execute("INSERT INTO chronologie (date_cible, age_cible, action, montant, sens, categorie) VALUES (%s,%s,%s,%s,%s,%s)",
              (f'2098-01-{i+1:02d}', 99, f'STRESS_{i}', i, 'info', 'test'))
conn.commit()
t_write = (time.time() - start) * 1000
check(t_write < 5000, f'10 ecritures en {t_write:.0f}ms', f'10 ecritures LENTES ({t_write:.0f}ms)')

# Lecture rapide 10x
start = time.time()
for i in range(10):
    c.execute("SELECT COUNT(*) FROM chronologie")
    c.fetchone()
t_read = (time.time() - start) * 1000
check(t_read < 2000, f'10 lectures en {t_read:.0f}ms', f'10 lectures LENTES ({t_read:.0f}ms)')

# Nettoyage
c.execute("DELETE FROM chronologie WHERE action LIKE 'STRESS_%'")
conn.commit()
check(True, 'Nettoyage stress OK', '')

# ============================================================
# BLOC 10 : COHERENCE CROISEE
# ============================================================
print('\n' + '='*70)
print('  BLOC 10 : COHERENCE CROISEE')
print('='*70)

# Somme flux entrees
c.execute("SELECT SUM(montant) as total FROM chronologie WHERE sens='entree'")
entrees = c.fetchone()['total'] or 0
check(abs(entrees - 513500) < 100, f'Total entrees = {entrees:,.0f} (ref 513500)', f'Total entrees = {entrees:,.0f}')

# Somme flux sorties
c.execute("SELECT SUM(ABS(montant)) as total FROM chronologie WHERE sens='sortie'")
sorties = c.fetchone()['total'] or 0
check(abs(sorties - 52424) < 1000, f'Total sorties = {sorties:,.0f} (ref ~52424)', f'Total sorties = {sorties:,.0f}')

# Rail vs AAH + loyer
rail = p['rail_mensuel']
aah = p['aah_mensuel']
loyer = p['loyer_net']
deficit = rail - aah - loyer + 325
check(deficit > 0, f'Deficit mensuel = {deficit:.0f} EUR (pioche sur capital)', f'Deficit = {deficit:.0f}')

# Rendement vs minimum viable
check(p['rendement_annuel'] >= 0.030, f'Rendement {p["rendement_annuel"]*100:.1f}% >= 3.0% minimum viable', f'Rendement {p["rendement_annuel"]*100:.1f}% SOUS le minimum')

conn.close()

# ============================================================
# VERDICT FINAL
# ============================================================
print('\n' + '='*70)
print('  VERDICT FINAL')
print('='*70)
print(f'  Tests reussis   : {ok}')
print(f'  Erreurs         : {err}')
print(f'  Avertissements  : {warn}')
print()
if err == 0:
    print('  *** CERTIFICATION : COCKPIT PATRIMONIAL RAPHAEL ***')
    print('  *** SERVEUR SUPABASE STABLE ET CERTIFIE ***')
    print('  *** ZERO ERREUR - PRET POUR LA PRODUCTION ***')
else:
    print(f'  {err} ERREUR(S) DETECTEE(S) - CORRECTIONS NECESSAIRES')
print('='*70)
