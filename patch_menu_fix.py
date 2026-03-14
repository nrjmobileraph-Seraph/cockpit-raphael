p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Remettre les noms originaux et juste clarifier les abreviations
renames = [
    ("Calcul de la Rente", "Moteur ARVA (Rente)"),
    ("Assurances-Vie (3 contrats)", "Suivi AV x 3 contrats"),
    ("Simuler des Scenarios", "Simulateurs de scenarios"),
    ("Impots et Aides", "Fiscal & CAF"),
    ("Declaration Fiscale", "Imposition & Declaration"),
    ("Location Meublee (LMNP)", "LMNP (Location Meublee) & IRL"),
    ("Planning et Actions", "Jalons & Actions"),
    ("Allocations (AAH)", "AAH / CAF / PCH (Allocations)"),
    ("Impact Inflation", "Inflation"),
    ("Succession et Heritage", "Succession"),
    ("Retraite et Senior", "Mode Senior"),
    ("Exporter le Bilan", "Exportation de Bilan"),
    ("Banque (BoursoBank)", "BoursoBank"),
    ("Guide Complet (Annexe)", "Annexe - Reference"),
    ("Modifier le Capital", "Saisie capital"),
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
print(f'Total: {n} corrections')

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
