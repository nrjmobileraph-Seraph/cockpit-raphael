with open('C:/Users/BoulePiou/cockpit-raphael/app.py', 'r', encoding='utf-8') as f:
    code = f.read()

pages = {
    'page_dashboard': 'Tableau de bord',
    'page_arva': 'Moteur ARVA',
    'page_suivi_av': 'Suivi AV',
    'page_simulateur': 'Simulateur',
    'page_fiscal': 'Fiscal',
    'page_impots': 'Impots',
    'page_lmnp': 'LMNP',
    'page_jalons': 'Jalons',
    'page_caf_pch': 'AAH/PCH',
    'page_inflation': 'Inflation',
    'page_succession': 'Succession',
    'page_senior': 'Senior',
    'page_export': 'Export bilan',
    'page_boursobank': 'BoursoBank',
    'page_crypto': 'Crypto',
    'page_annexe': 'Annexe',
    'page_parametres': 'Parametres',
    'page_saisie': 'Saisie capital',
}
print('=== PAGES ===')
for func, nom in pages.items():
    defini = f'def {func}(' in code
    appele = func in code.split('def main')[1] if 'def main' in code else False
    taille = 0
    if defini:
        start = code.find(f'def {func}(')
        next_def = code.find('\ndef ', start + 10)
        if next_def > 0:
            taille = next_def - start
    status = 'OK' if defini and taille > 100 else ('VIDE' if taille < 100 else 'MANQUE')
    print(f'  {nom:20s} : {status:6s} ({taille} chars)')

print(f'\nTotal lignes : {len(code.splitlines())}')
