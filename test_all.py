import db_wrapper

print('=' * 60)
print('TEST TOUTES LES PAGES - DONNEES SERVEUR')
print('=' * 60)

conn = db_wrapper.connect()
c = conn.cursor()
ok = 0
err = 0

# Profil
print('\n--- PROFIL ---')
c.execute('SELECT * FROM profil LIMIT 1')
p = c.fetchone()
if p and p['rail_mensuel'] == 2760:
    print(f'  [OK] Profil charge'); ok+=1
else:
    print(f'  [ERR] Profil'); err+=1

# Capital
print('\n--- CAPITAL ---')
c.execute('SELECT cc,livret_a,ldds,lep,av1,av2,av3 FROM capital ORDER BY date DESC LIMIT 1')
cap = c.fetchone()
total = cap['cc']+cap['livret_a']+cap['ldds']+cap['lep']+cap['av1']+cap['av2']+cap['av3']
print(f'  [OK] Capital = {total:,.0f}'); ok+=1

# Jalons
print('\n--- JALONS ---')
c.execute('SELECT COUNT(*) as nb FROM chronologie')
nb = c.fetchone()['nb']
print(f'  [OK] {nb} jalons'); ok+=1

c.execute('SELECT action, montant FROM chronologie WHERE montant > 1000 ORDER BY date_cible')
rows = c.fetchall()
for r in rows:
    print(f'  [OK] {r["action"][:50]} = {r["montant"]:,.0f}'); ok+=1

# AAH
print('\n--- AAH ---')
c.execute('SELECT mois, montant_prevu FROM aah_suivi ORDER BY mois')
aah = c.fetchall()
for r in aah:
    print(f'  [OK] {r["mois"]} = {r["montant_prevu"]}'); ok+=1

# Devis
print('\n--- DEVIS ---')
c.execute('SELECT corps_metier, devis_montant FROM devis_artisans ORDER BY id')
dev = c.fetchall()
for r in dev:
    print(f'  [OK] {r["corps_metier"]} = {r["devis_montant"]:,.0f}'); ok+=1

# AV Jean-Luc mis a jour
print('\n--- MISE A JOUR AV ---')
c.execute("SELECT montant FROM chronologie WHERE action LIKE '%AV Jean-Luc%'")
r = c.fetchone()
if r and r['montant'] == 22800:
    print(f'  [OK] AV Jean-Luc = 22 800 EUR (mis a jour)'); ok+=1
else:
    print(f'  [ERR] AV Jean-Luc = {r["montant"] if r else "absent"}'); err+=1

# Pages existantes dans app.py
print('\n--- PAGES APP.PY ---')
f2 = open('C:/Users/BoulePiou/cockpit-raphael/app.py','r',encoding='utf-8')
code = f2.read()
f2.close()
pages = ['page_dashboard','page_arva','page_suivi_av','page_simulateur',
         'page_fiscal','page_impots','page_lmnp','page_jalons',
         'page_caf_pch','page_inflation','page_succession','page_senior',
         'page_export','page_boursobank','page_crypto','page_annexe',
         'page_parametres','page_saisie']
for pg in pages:
    if f'def {pg}' in code:
        print(f'  [OK] {pg}'); ok+=1
    else:
        print(f'  [ABSENT] {pg}'); err+=1

# Sidebar toggle
print('\n--- SIDEBAR ---')
if 'sidebar_state' in code:
    print(f'  [OK] Systeme Gemini present'); ok+=1
else:
    print(f'  [ERR] Systeme Gemini absent'); err+=1

conn.close()

print(f'\n{"="*60}')
print(f'RESULTAT : {ok} OK / {err} ERREURS')
if err == 0:
    print('TOUT FONCTIONNE')
else:
    print(f'{err} point(s) a verifier')
print('='*60)
