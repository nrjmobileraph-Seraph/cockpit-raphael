FICHIER = r"C:\Users\BoulePiou\cockpit-raphael\app.py"
with open(FICHIER, "r", encoding="utf-8") as f:
    contenu = f.read()

modifs = 0

ancien_parents = 'color:#C4922A;font-size:18px;font-family:Garamond,Georgia,serif;font-style:italic;letter-spacing:2px;'
nouveau_parents = 'color:#C4922A;font-size:16px;font-family:Garamond,Georgia,serif;font-style:italic;letter-spacing:1px;line-height:1.2;'
if ancien_parents in contenu:
    contenu = contenu.replace(ancien_parents, nouveau_parents)
    modifs += 1
    print("[1/2] OK - Parents hauteur fixee")

ancien_poches = '            ("AAH", _aah_m, "#FFD060"),\n            ("Loyers LMNP", _loyer_m, "#4DFF99"),\n        ]'
nouveau_poches = '            ("AV4 Bourso Vie", cap.get("av4", 0) or 0, "#E8C547"),\n            ("PEA Bourse", cap.get("pea", 0) or 0, "#5599FF"),\n            ("Crypto", cap.get("crypto", 0) or 0, "#FF9933"),\n            ("Crowdfunding", cap.get("crowdfunding", 0) or 0, "#CC66FF"),\n            ("AAH", _aah_m, "#FFD060"),\n            ("PCH", _pch_m, "#AADDFF"),\n            ("Loyers LMNP", _loyer_m, "#FF7777"),\n            ("RVD", _rvd_m, "#FF66AA"),\n            ("ASPA", _aspa_m, "#DDAAFF"),\n        ]'

if ancien_poches in contenu:
    contenu = contenu.replace(ancien_poches, nouveau_poches)
    # Ajouter les variables manquantes
    if '_pch_m' not in contenu.split('_poches')[0]:
        contenu = contenu.replace("_loyer_m = profil.get('loyer_net', 0) or 0", "_loyer_m = profil.get('loyer_net', 0) or 0\n        _pch_m = profil.get('pch_mensuel', 0) or 0\n        _rvd_m = profil.get('rvd_mensuel', 0) or 0\n        _aspa_m = profil.get('aspa_mensuelle', 0) or 0")
    modifs += 1
    print("[2/2] OK - 15 sources installees")
else:
    print("[2/2] ERREUR")

with open(FICHIER, "w", encoding="utf-8") as f:
    f.write(contenu)
print(f"Termine ! {modifs}/2")
