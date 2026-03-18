FICHIER = r"C:\Users\BoulePiou\cockpit-raphael\app.py"
with open(FICHIER, "r", encoding="utf-8") as f:
    contenu = f.read()

ancien = '''        _poches = [
            ("AV1 Lucya Cardif", cap.get("av1", 0) or 0, "#C4922A"),
            ("AV2 Linxea Spirit", cap.get("av2", 0) or 0, "#D4A017"),
            ("AV3 Lucya Abeille", cap.get("av3", 0) or 0, "#BBA888"),
            ("Livret A", cap.get("livret_a", 0) or 0, "#4DFF99"),
            ("LDDS", cap.get("ldds", 0) or 0, "#66CCAA"),
            ("LEP", cap.get("lep", 0) or 0, "#77DDBB"),
        ]
        _poches_actives = [(n, v, c) for n, v, c in _poches if v > 0]'''

nouveau = '''        _aah_m = profil.get('aah_mensuel', 625) or 625
        _loyer_m = profil.get('loyer_net', 0) or 0
        _poches = [
            ("AV1 Lucya Cardif", cap.get("av1", 0) or 0, "#C4922A"),
            ("AV2 Linxea Spirit", cap.get("av2", 0) or 0, "#D4A017"),
            ("AV3 Lucya Abeille", cap.get("av3", 0) or 0, "#BBA888"),
            ("Livret A", cap.get("livret_a", 0) or 0, "#4DFF99"),
            ("LDDS", cap.get("ldds", 0) or 0, "#66CCAA"),
            ("LEP", cap.get("lep", 0) or 0, "#77DDBB"),
            ("AAH", _aah_m, "#FFD060"),
            ("Loyers LMNP", _loyer_m, "#4DFF99"),
        ]
        _poches_actives = [(n, v, c) for n, v, c in _poches if v > 0]'''

if ancien in contenu:
    contenu = contenu.replace(ancien, nouveau)
    with open(FICHIER, "w", encoding="utf-8") as f:
        f.write(contenu)
    print("OK - AAH + Loyers LMNP ajoutes aux poches")
else:
    print("ERREUR - bloc non trouve")
