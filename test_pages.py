import db_wrapper
import traceback

print('=' * 60)
print('TEST CROISE - SIMULATION CHAQUE PAGE')
print('=' * 60)

conn = db_wrapper.connect()
c = conn.cursor()
ok = 0
err = 0

# Simuler les donnees que chaque page utilise

# 1. Dashboard
print('\n--- page_dashboard ---')
try:
    c.execute('SELECT * FROM chronologie ORDER BY date_cible ASC')
    rows = c.fetchall()
    c.execute('SELECT cc+livret_a+ldds+lep+av1+av2+av3 as total FROM capital ORDER BY date DESC LIMIT 1')
    cap = c.fetchone()
    print(f'  [OK] {len(rows)} jalons, capital {cap["total"]:,.0f}'); ok+=1
except Exception as e:
    print(f'  [ERR] {e}'); err+=1

# 2. ARVA
print('\n--- page_arva ---')
try:
    c.execute('SELECT rail_mensuel, rendement_annuel, age_cible, loyer_net, aah_mensuel FROM profil LIMIT 1')
    p = c.fetchone()
    print(f'  [OK] rail={p["rail_mensuel"]} rend={p["rendement_annuel"]}'); ok+=1
except Exception as e:
    print(f'  [ERR] {e}'); err+=1

# 3. Suivi AV
print('\n--- page_suivi_av ---')
try:
    c.execute('SELECT av1, av2, av3, av1_rendement, av2_rendement, av3_rendement, av1_versements, av2_versements, av3_versements, av1_date_ouverture, av2_date_ouverture, av3_date_ouverture FROM capital ORDER BY date DESC LIMIT 1')
    r = c.fetchone()
    print(f'  [OK] AV1={r["av1"]:,.0f} AV2={r["av2"]:,.0f} AV3={r["av3"]:,.0f}'); ok+=1
except Exception as e:
    print(f'  [ERR] {e}'); err+=1

# 4. Simulateur
print('\n--- page_simulateur ---')
try:
    c.execute('SELECT * FROM profil LIMIT 1')
    c.fetchone()
    c.execute('SELECT * FROM capital ORDER BY date DESC LIMIT 1')
    c.fetchone()
    print(f'  [OK] Donnees presentes'); ok+=1
except Exception as e:
    print(f'  [ERR] {e}'); err+=1

# 5. Fiscal
print('\n--- page_fiscal ---')
try:
    c.execute('SELECT loyer_net, aah_mensuel, rail_mensuel FROM profil LIMIT 1')
    c.fetchone()
    print(f'  [OK]'); ok+=1
except Exception as e:
    print(f'  [ERR] {e}'); err+=1

# 6. Impots
print('\n--- page_impots ---')
try:
    c.execute('SELECT * FROM profil LIMIT 1')
    c.fetchone()
    print(f'  [OK]'); ok+=1
except Exception as e:
    print(f'  [ERR] {e}'); err+=1

# 7. LMNP
print('\n--- page_lmnp ---')
try:
    c.execute('SELECT * FROM devis_artisans ORDER BY id')
    dev = c.fetchall()
    print(f'  [OK] {len(dev)} devis'); ok+=1
except Exception as e:
    print(f'  [ERR] {e}'); err+=1

# 8. Jalons
print('\n--- page_jalons ---')
try:
    c.execute('SELECT * FROM chronologie WHERE fait=0 ORDER BY date_cible ASC')
    avenir = c.fetchall()
    c.execute('SELECT * FROM chronologie WHERE fait=1 ORDER BY date_cible ASC')
    faits = c.fetchall()
    print(f'  [OK] {len(avenir)} a venir, {len(faits)} faits'); ok+=1
except Exception as e:
    print(f'  [ERR] {e}'); err+=1

# 9. AAH/CAF/PCH
print('\n--- page_caf_pch ---')
try:
    c.execute('SELECT * FROM aah_suivi ORDER BY mois ASC')
    aah = c.fetchall()
    print(f'  [OK] {len(aah)} annees AAH'); ok+=1
except Exception as e:
    print(f'  [ERR] {e}'); err+=1

# 10. Inflation
print('\n--- page_inflation ---')
try:
    c.execute('SELECT rail_mensuel FROM profil LIMIT 1')
    c.fetchone()
    print(f'  [OK]'); ok+=1
except Exception as e:
    print(f'  [ERR] {e}'); err+=1

# 11. Succession
print('\n--- page_succession ---')
try:
    c.execute('SELECT * FROM profil LIMIT 1')
    c.fetchone()
    print(f'  [OK]'); ok+=1
except Exception as e:
    print(f'  [ERR] {e}'); err+=1

# 12. Senior
print('\n--- page_senior ---')
try:
    c.execute('SELECT age_cible, taux_mdph, aah_mensuel FROM profil LIMIT 1')
    c.fetchone()
    print(f'  [OK]'); ok+=1
except Exception as e:
    print(f'  [ERR] {e}'); err+=1

# 13. Export
print('\n--- page_export ---')
try:
    c.execute('SELECT * FROM profil LIMIT 1')
    c.execute('SELECT * FROM capital ORDER BY date DESC LIMIT 1')
    print(f'  [OK]'); ok+=1
except Exception as e:
    print(f'  [ERR] {e}'); err+=1

# 14. BoursoBank
print('\n--- page_boursobank ---')
try:
    c.execute('SELECT cc, livret_a, ldds, lep FROM capital ORDER BY date DESC LIMIT 1')
    c.fetchone()
    print(f'  [OK]'); ok+=1
except Exception as e:
    print(f'  [ERR] {e}'); err+=1

# 15. Crypto
print('\n--- page_crypto ---')
try:
    c.execute('SELECT * FROM profil LIMIT 1')
    c.fetchone()
    print(f'  [OK]'); ok+=1
except Exception as e:
    print(f'  [ERR] {e}'); err+=1

# 16. Annexe
print('\n--- page_annexe ---')
try:
    c.execute('SELECT * FROM profil LIMIT 1')
    c.execute('SELECT * FROM capital ORDER BY date DESC LIMIT 1')
    c.execute('SELECT * FROM chronologie ORDER BY date_cible ASC')
    c.execute('SELECT * FROM aah_suivi ORDER BY mois ASC')
    c.execute('SELECT * FROM devis_artisans ORDER BY id ASC')
    print(f'  [OK] Toutes tables accessibles'); ok+=1
except Exception as e:
    print(f'  [ERR] {e}'); err+=1

# 17. Parametres
print('\n--- page_parametres ---')
try:
    c.execute('SELECT * FROM profil LIMIT 1')
    p = c.fetchone()
    c.execute('SELECT * FROM capital ORDER BY date DESC LIMIT 1')
    cap = c.fetchone()
    print(f'  [OK] Profil + Capital accessibles'); ok+=1
except Exception as e:
    print(f'  [ERR] {e}'); err+=1

# 18. Saisie capital
print('\n--- page_saisie ---')
try:
    c.execute('SELECT * FROM capital ORDER BY date DESC LIMIT 1')
    c.fetchone()
    print(f'  [OK]'); ok+=1
except Exception as e:
    print(f'  [ERR] {e}'); err+=1

conn.close()

print(f'\n{"="*60}')
print(f'RESULTAT : {ok} OK / {err} ERREURS')
if err == 0:
    print('TOUTES LES PAGES ONT ACCES AUX DONNEES')
else:
    print(f'{err} page(s) avec probleme de donnees')
print('='*60)
