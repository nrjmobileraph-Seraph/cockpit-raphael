FICHIER = r"C:\Users\BoulePiou\cockpit-raphael\app.py"
with open(FICHIER, "r", encoding="utf-8") as f:
    contenu = f.read()

modifs = 0

# 1. Fleche gauche : inverser (les montants vont VERS le total)
# AV3 -> TOTAL : la fleche doit pointer vers la droite
ancien_fg = "                _g_html += '<div style=" + '"' + "color:#C4922A;font-size:18px;padding:0 6px;" + '"' + ">\\u2B05</div>'"
nouveau_fg = "                _g_html += '<div style=" + '"' + "color:#C4922A;font-size:18px;padding:0 6px;" + '"' + ">\\u27A1</div>'"

# Plan B : chercher directement les caracteres unicode
if "\\u2B05" in contenu and "\\u27A1" in contenu:
    # u2B05 = fleche gauche, u27A1 = fleche droite
    # On veut : gauche du total = fleche droite (vers total), droite du total = fleche gauche (vers total)
    # Actuellement c'est l'inverse, on swap
    contenu = contenu.replace("\\u2B05", "TEMP_PLACEHOLDER")
    contenu = contenu.replace("\\u27A1", "\\u2B05")
    contenu = contenu.replace("TEMP_PLACEHOLDER", "\\u27A1")
    modifs += 1
    print("[1/2] OK - Fleches inversees (montants -> TOTAL)")
elif "\\u2B05" in contenu:
    contenu = contenu.replace("\\u2B05", "\\u27A1")
    modifs += 1
    print("[1/2] OK - Fleche gauche inversee")
else:
    print("[1/2] Fleches non trouvees")

# 2. Rectangles en bas : forcer meme taille pour tous (min-width plus grand)
ancien_rect = 'min-width:80px;background:#1A0D12;border:1px solid {_pc}'
nouveau_rect = 'min-width:120px;background:#1A0D12;border:1px solid {_pc}'
if ancien_rect in contenu:
    contenu = contenu.replace(ancien_rect, nouveau_rect)
    modifs += 1
    print("[2/2] OK - Rectangles tous meme taille")
else:
    print("[2/2] ERREUR - rectangles non trouves")

with open(FICHIER, "w", encoding="utf-8") as f:
    f.write(contenu)
print(f"\nTermine ! {modifs}/2")
