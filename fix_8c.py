FICHIER = r"C:\Users\BoulePiou\cockpit-raphael\app.py"
with open(FICHIER, "r", encoding="utf-8") as f:
    contenu = f.read()

ancien = '            ("LEP", cap.get("lep", 0) or 0, "#77DDBB"),\n        ]'
nouveau = '            ("LEP", cap.get("lep", 0) or 0, "#77DDBB"),\n            ("AAH", _aah_m, "#FFD060"),\n            ("Loyers LMNP", _loyer_m, "#4DFF99"),\n        ]'

if ancien in contenu:
    contenu = contenu.replace(ancien, nouveau)
    with open(FICHIER, "w", encoding="utf-8") as f:
        f.write(contenu)
    print("OK - AAH + Loyers LMNP ajoutes")
else:
    print("ERREUR")
