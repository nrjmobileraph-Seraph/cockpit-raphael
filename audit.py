with open('C:/Users/BoulePiou/cockpit-raphael/app.py', 'r', encoding='utf-8') as f:
    code = f.read()

import ast
try:
    ast.parse(code)
    print('ast.parse : PASS')
except Exception as e:
    print(f'ast.parse : ERREUR {e}')

lines = code.splitlines()
print(f'Lignes : {len(lines)}')
print(f'sqlite3 : {code.count("sqlite3")}')
print(f'DB_PATH : {code.count("DB_PATH")}')
print(f'BoulePiou : {code.count("BoulePiou")}')
print(f'db_wrapper.connect() : {code.count("db_wrapper.connect()")}')
print(f'Pages : {code.count("def page_")}')
print(f'sidebar_state : {code.count("sidebar_state")}')
print(f'CONNEXION : {code.count("C O N N E X I O N")}')
print(f'FFD060 : {code.count("FFD060")}')

# Verifier chaque page est appelee dans main
pages = ['page_dashboard','page_arva','page_suivi_av','page_simulateur','page_fiscal','page_impots','page_lmnp','page_jalons','page_caf_pch','page_inflation','page_succession','page_senior','page_export','page_boursobank','page_crypto','page_annexe','page_parametres','page_saisie']
print()
print('=== PAGES ===')
for p in pages:
    defini = f'def {p}(' in code
    appele = f'{p}(profil,cap)' in code or f'{p}(profil, cap)' in code
    print(f'  {p}: {"DEF" if defini else "MANQUE"} | {"APPELE" if appele else "NON APPELE"}')

# Verifier connexions restantes
print()
print('=== CONNEXIONS DB ===')
for i, line in enumerate(lines, 1):
    if 'connect(' in line and ('sqlite' in line or 'sq.' in line or 'sqd.' in line or 'sq2.' in line):
        print(f'  PROBLEME L{i}: {line.strip()[:80]}')
ok = True
for i, line in enumerate(lines, 1):
    if 'connect(' in line and ('sqlite' in line or 'sq.' in line or 'sqd.' in line or 'sq2.' in line):
        ok = False
if ok:
    print('  TOUTES les connexions sont db_wrapper.connect() - OK')

# Verifier HTML sans unsafe_allow_html
print()
print('=== HTML SANS UNSAFE ===')
html_ok = True
for i, line in enumerate(lines, 1):
    s = line.strip()
    if 'st.markdown(' in s and ('<div' in s or '<span' in s or '<style' in s) and 'unsafe_allow_html' not in s:
        print(f'  PROBLEME L{i}: {s[:80]}')
        html_ok = False
if html_ok:
    print('  TOUS les st.markdown HTML ont unsafe_allow_html - OK')

print()
print('=== AUDIT TERMINE ===')
