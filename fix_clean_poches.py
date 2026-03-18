FICHIER = r"C:\Users\BoulePiou\cockpit-raphael\app.py"
with open(FICHIER, "r", encoding="utf-8") as f:
    contenu = f.read()

modifs = 0

# 1. Enlever AAH, PCH, Loyers, RVD, ASPA des poches capital
lignes_a_virer = [
    '            ("AAH", _aah_m, "#FFD060"),\n',
    '            ("PCH", _pch_m, "#AADDFF"),\n',
    '            ("Loyers LMNP", _loyer_m, "#FF7777"),\n',
    '            ("RVD", _rvd_m, "#FF66AA"),\n',
    '            ("ASPA", _aspa_m, "#DDAAFF"),\n',
]
for l in lignes_a_virer:
    if l in contenu:
        contenu = contenu.replace(l, "")
        modifs += 1

# 2. Enlever les variables inutiles dans le bloc capital
bloc_vars = """        _aah_m = profil.get('aah_mensuel', 625) or 625
        _loyer_m = profil.get('loyer_net', 0) or 0
        _pch_m = profil.get('pch_mensuel', 0) or 0
        _rvd_m = profil.get('rvd_mensuel', 0) or 0
        _aspa_m = profil.get('aspa_mensuelle', 0) or 0
        _poches"""
bloc_vars_clean = "        _poches"
if bloc_vars in contenu:
    contenu = contenu.replace(bloc_vars, bloc_vars_clean)
    modifs += 1

# 3. Remettre AV4 apres AV3 (avant Livret A)
# Deja dans le bon ordre

with open(FICHIER, "w", encoding="utf-8") as f:
    f.write(contenu)
print(f"OK - {modifs} lignes nettoyees des poches capital")
