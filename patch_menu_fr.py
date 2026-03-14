p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Renommer les pages du menu
renames = [
    ("Moteur ARVA", "Calcul de la Rente"),
    ("Suivi AV x 3 contrats", "Assurances-Vie (3 contrats)"),
    ("Simulateurs de scénarios", "Simuler des Scenarios"),
    ("Fiscal & CAF", "Impots et Aides"),
    ("Impostions de déclaration", "Declaration Fiscale"),
    ("Impositions de déclaration", "Declaration Fiscale"),
    ("Impostions de declaration", "Declaration Fiscale"),
    ("LMNP & IRL", "Location Meublee (LMNP)"),
    ("Jalons & Actions", "Planning et Actions"),
    ("AAH / CAF / PCH", "Allocations (AAH)"),
    ("Inflation", "Impact Inflation"),
    ("Succession", "Succession et Heritage"),
    ("Mode Senior", "Retraite et Senior"),
    ("Exportation de Bilan d", "Exporter le Bilan"),
    ("Exportation de Bilan", "Exporter le Bilan"),
    ("BoursoBank", "Banque (BoursoBank)"),
    ("Crypto", "Crypto"),
    ("Annexe - Référence", "Guide Complet (Annexe)"),
    ("Annexe - Reference", "Guide Complet (Annexe)"),
    ("Saisie capital", "Modifier le Capital"),
]

n = 0
for old, new in renames:
    if old in t:
        t = t.replace(old, new)
        n += 1
        print(f'{old} -> {new}')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print(f'Total: {n} renommages')

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
