p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

print(f'Lignes : {t.count(chr(10))}')
print(f'Fonctions : {t.count("def ")}')
print()

# Verifier les pages
pages = ['page_dashboard','page_arva','page_suivi_av','page_simulateur',
         'page_fiscal','page_impots','page_lmnp','page_jalons',
         'page_caf_pch','page_inflation','page_succession','page_senior',
         'page_export','page_boursobank','page_crypto','page_annexe',
         'page_parametres','page_saisie']
print('=== PAGES ===')
for pg in pages:
    if f'def {pg}' in t:
        print(f'  [OK] {pg}')
    else:
        print(f'  [ABSENT] {pg}')

# Verifier CSS
print('\n=== CSS ===')
print(f'  Bordeaux (#2A0A12) : {"OUI" if "#2A0A12" in t or "#1a0a12" in t else "ABSENT"}')
print(f'  Or (#FFD060) : {"OUI" if "#FFD060" in t else "ABSENT"}')
print(f'  Fond sombre : {"OUI" if "background" in t.lower() and "#0" in t else "ABSENT"}')
print(f'  Boutons styles : {"OUI" if "stButton" in t else "ABSENT"}')

# Verifier splash
print('\n=== SPLASH ===')
print(f'  Connexion : {"OUI" if "C O N N E X I O N" in t else "ABSENT"}')
print(f'  session_state.connected : {"OUI" if "connected" in t else "ABSENT"}')

# Verifier erreurs JS cachees
print(f'\n=== DIVERS ===')
print(f'  stException cache : {"OUI" if "stException" in t else "ABSENT"}')
print(f'  Banniere 2026..2067 : {"OUI" if "2067" in t else "ABSENT"}')
