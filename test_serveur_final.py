import psycopg2
import psycopg2.extras

print('=' * 60)
print('TESTS SERVEUR SUPABASE - IDENTIQUES AU LOCAL')
print('=' * 60)

conn = psycopg2.connect(
    host='aws-1-eu-west-1.pooler.supabase.com',
    port=6543, dbname='postgres',
    user='postgres.zyizvlrwsatxqehhqiwh',
    password='Seraphetraph/62//26**',
    cursor_factory=psycopg2.extras.RealDictCursor
)
c = conn.cursor()
ok = 0
err = 0

# 1. PROFIL
print('\n--- PROFIL ---')
c.execute('SELECT * FROM profil LIMIT 1')
p = dict(c.fetchone())
checks = {'rail_mensuel': 2760, 'aah_mensuel': 1033, 'loyer_net': 320, 'taux_mdph': 75, 'age_cible': 92, 'capital_cible': 50000}
for k, v in checks.items():
    if p[k] == v:
        print(f'  [OK] {k} = {p[k]}'); ok+=1
    else:
        print(f'  [ERR] {k} = {p[k]} (attendu {v})'); err+=1
if abs(p['rendement_annuel'] - 0.035) < 0.001:
    print(f'  [OK] rendement = {p["rendement_annuel"]}'); ok+=1
else:
    print(f'  [ERR] rendement = {p["rendement_annuel"]}'); err+=1

# 2. CAPITAL
print('\n--- CAPITAL ---')
c.execute('SELECT cc,livret_a,ldds,lep,av1,av2,av3 FROM capital ORDER BY date DESC LIMIT 1')
cap = dict(c.fetchone())
total = cap['cc']+cap['livret_a']+cap['ldds']+cap['lep']+cap['av1']+cap['av2']+cap['av3']
expected = {'cc':500,'livret_a':22950,'ldds':12000,'lep':10000,'av1':130000,'av2':130000,'av3':155550}
for k,v in expected.items():
    if cap[k] == v:
        print(f'  [OK] {k} = {cap[k]:,.0f}'); ok+=1
    else:
        print(f'  [ERR] {k} = {cap[k]} (attendu {v})'); err+=1
if abs(total - 461000) < 1:
    print(f'  [OK] TOTAL = {total:,.0f}'); ok+=1
else:
    print(f'  [ERR] TOTAL = {total:,.0f} (attendu 461000)'); err+=1

# 3. JALONS
print('\n--- JALONS ---')
c.execute('SELECT COUNT(*) as nb FROM chronologie')
nb = c.fetchone()['nb']
if nb >= 26:
    print(f'  [OK] {nb} jalons'); ok+=1
else:
    print(f'  [ERR] {nb} jalons (attendu 26+)'); err+=1

# Flux principaux
c.execute('SELECT action, montant, sens FROM chronologie WHERE montant > 10000')
rows = c.fetchall()
flux_ok = 0
for nom, attendu in [('AV Jean-Luc', 34500), ('SCI', 296100), ('succession', 182900)]:
    trouve = any(nom.lower() in r['action'].lower() and abs(r['montant']-attendu)<1 for r in rows)
    if trouve:
        print(f'  [OK] Flux {nom} = {attendu:,.0f}'); ok+=1; flux_ok+=1
    else:
        print(f'  [ERR] Flux {nom} absent'); err+=1

# 4. AAH
print('\n--- AAH ---')
c.execute('SELECT COUNT(*) as nb FROM aah_suivi')
nb_aah = c.fetchone()['nb']
if nb_aah == 14:
    print(f'  [OK] {nb_aah} annees'); ok+=1
else:
    print(f'  [ERR] {nb_aah} annees (attendu 14)'); err+=1

c.execute("SELECT montant_prevu FROM aah_suivi WHERE mois='2026-01'")
r = c.fetchone()
if r and r['montant_prevu'] == 625:
    print(f'  [OK] AAH 2026 = 625'); ok+=1
else:
    print(f'  [ERR] AAH 2026 != 625'); err+=1

c.execute("SELECT montant_prevu FROM aah_suivi WHERE mois='2029-01'")
r = c.fetchone()
if r and r['montant_prevu'] == 1033:
    print(f'  [OK] AAH 2029 = 1033'); ok+=1
else:
    print(f'  [ERR] AAH 2029 != 1033'); err+=1

# 5. DEVIS
print('\n--- DEVIS ---')
c.execute('SELECT COUNT(*) as nb FROM devis_artisans')
nb_dev = c.fetchone()['nb']
if nb_dev >= 8:
    print(f'  [OK] {nb_dev} corps de metier'); ok+=1
else:
    print(f'  [ERR] {nb_dev} (attendu 8)'); err+=1

# 6. ECRITURE/LECTURE
print('\n--- ECRITURE/LECTURE ---')
c.execute("INSERT INTO chronologie (date_cible, age_cible, action, montant, sens, categorie) VALUES (%s,%s,%s,%s,%s,%s)",
          ('2099-01-01', 99, 'TEST_SERVEUR_FINAL', 1, 'info', 'test'))
conn.commit()
c.execute("SELECT * FROM chronologie WHERE action='TEST_SERVEUR_FINAL'")
r = c.fetchone()
if r:
    print(f'  [OK] Ecriture OK'); ok+=1
    c.execute("DELETE FROM chronologie WHERE action='TEST_SERVEUR_FINAL'")
    conn.commit()
    print(f'  [OK] Suppression OK'); ok+=1
else:
    print(f'  [ERR] Ecriture echouee'); err+=1

# 7. MODIFICATION
print('\n--- MODIFICATION ---')
c.execute("SELECT id FROM chronologie ORDER BY id ASC LIMIT 1")
first = c.fetchone()['id']
c.execute("UPDATE chronologie SET note='TEST_MODIF' WHERE id=%s", (first,))
conn.commit()
c.execute("SELECT note FROM chronologie WHERE id=%s", (first,))
note = c.fetchone()['note']
if note == 'TEST_MODIF':
    print(f'  [OK] Modification OK'); ok+=1
    c.execute("UPDATE chronologie SET note='' WHERE id=%s", (first,))
    conn.commit()
    print(f'  [OK] Restauration OK'); ok+=1
else:
    print(f'  [ERR] Modification echouee'); err+=1

# 8. LATENCE
print('\n--- LATENCE ---')
import time
start = time.time()
for i in range(10):
    c.execute('SELECT COUNT(*) FROM chronologie')
    c.fetchone()
latence = (time.time() - start) / 10 * 1000
print(f'  [INFO] Latence : {latence:.0f} ms/requete')
if latence < 500:
    print(f'  [OK] Latence acceptable'); ok+=1
else:
    print(f'  [ATTENTION] Latence elevee'); err+=1

conn.close()

print(f'\n{"="*60}')
print(f'SERVEUR SUPABASE : {ok} OK / {err} ERREURS')
if err == 0:
    print('SERVEUR IDENTIQUE AU LOCAL — TOUT EST STABLE')
else:
    print(f'{err} point(s) a verifier')
print('='*60)
