FICHIER = r"C:\Users\BoulePiou\cockpit-raphael\app.py"
with open(FICHIER, "r", encoding="utf-8") as f:
    contenu = f.read()

modifs = 0

# 1. Supprimer le bloc REVENUS qu'on vient d'ajouter
debut_rev = "        # --- SOURCES DE REVENUS : meme schema que capital ---"
fin_rev = "        st.markdown('<div style=" + '"' + "border:2px solid #4DFF99"
if debut_rev in contenu:
    idx1 = contenu.index(debut_rev)
    # Trouver la fin du bloc : le markdown avec cadre vert
    idx2 = contenu.index("background:#0A0A0A;\">' + _rvb_html + '</div>'", idx1)
    idx2 = contenu.index("\n", idx2) + 1
    # Chercher la ligne vide apres
    while idx2 < len(contenu) and contenu[idx2] == "\n":
        idx2 += 1
    contenu = contenu[:idx1] + contenu[idx2:]
    modifs += 1
    print("[1/2] OK - Bloc revenus supprime")

# 2. Ajouter AAH et Loyers LMNP dans _poches_actives
ancien_poches = '''        _poches_actives = [
            ("AV1 Lucya Cardif", cap.get('av1',0), "#C4922A"),
            ("AV2 Linxea Spirit", cap.get('av2',0), "#FFD060"),
            ("AV3 Lucya Abeille", cap.get('av3',0), "#FFAA33"),
            ("Livret A", cap.get('livret_a',0), "#77DDBB"),
            ("LDDS", cap.get('ldds',0), "#66CCAA"),
            ("LEP", cap.get('lep',0), "#4DFF99"),
        ]'''
nouveau_poches = '''        _aah_m = profil.get('aah_mensuel', 625) or 625
        _loyer_m = profil.get('loyer_net', 0) or 0
        _poches_actives = [
            ("AV1 Lucya Cardif", cap.get('av1',0), "#C4922A"),
            ("AV2 Linxea Spirit", cap.get('av2',0), "#FFD060"),
            ("AV3 Lucya Abeille", cap.get('av3',0), "#FFAA33"),
            ("Livret A", cap.get('livret_a',0), "#77DDBB"),
            ("LDDS", cap.get('ldds',0), "#66CCAA"),
            ("LEP", cap.get('lep',0), "#4DFF99"),
            ("AAH", _aah_m, "#FFD060"),
            ("Loyers LMNP", _loyer_m, "#4DFF99"),
        ]'''
if ancien_poches in contenu:
    contenu = contenu.replace(ancien_poches, nouveau_poches)
    modifs += 1
    print("[2/2] OK - AAH + Loyers LMNP ajoutes aux poches")
else:
    print("[2/2] ERREUR - poches non trouvees")

with open(FICHIER, "w", encoding="utf-8") as f:
    f.write(contenu)
print(f"\nTermine ! {modifs}/2")
