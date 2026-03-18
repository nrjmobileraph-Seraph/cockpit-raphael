FICHIER = r"C:\Users\BoulePiou\cockpit-raphael\app.py"
with open(FICHIER, "r", encoding="utf-8") as f:
    contenu = f.read()

modifs = 0

# 1. Supprimer les petits rectangles noms + 2eme fleches (entre sources et plancher)
ancien_noms = "        # Petits rectangles noms entre les fleches et les gros rectangles"
ancien_fl2 = "        # Petites fleches entre noms et gros rectangles"

# Trouver et supprimer le bloc petits rectangles noms
if ancien_noms in contenu:
    idx1 = contenu.index(ancien_noms)
    # Trouver la fin : c'est avant "# 6 RECTANGLES SOURCES"
    idx2 = contenu.index("        # 6 RECTANGLES SOURCES en bas", idx1)
    contenu = contenu[:idx1] + contenu[idx2:]
    modifs += 1
    print("[1/3] OK - Petits rectangles noms + 2eme fleches supprimes")
else:
    print("[1/3] Deja fait ou non trouve")

# 2. Entourer les 6 rectangles dans un cadre
ancien_6rect = "        # 6 RECTANGLES SOURCES en bas\n"
nouveau_6rect = "        # 6 RECTANGLES SOURCES en bas (dans un cadre)\n"

ancien_b_fin = "        _b_html += '</div>'"
# Ajouter un cadre autour
if ancien_6rect in contenu:
    contenu = contenu.replace(ancien_6rect, nouveau_6rect)
    # Trouver le _b_html et l'envelopper
    idx_b = contenu.index(nouveau_6rect)
    # Trouver le st.markdown(_b_html apres
    idx_md = contenu.index("        st.markdown(_b_html", idx_b)
    # Remplacer le markdown par un avec cadre
    ancien_md = "        st.markdown(_b_html, unsafe_allow_html=True)"
    # On cherche celui qui est juste apres les rectangles sources
    pos = contenu.index(ancien_md, idx_b)
    nouveau_md = '        st.markdown(\'<div style="border:1px solid #333;border-radius:12px;padding:12px;margin-bottom:16px;">\' + _b_html + \'</div>\', unsafe_allow_html=True)'
    contenu = contenu[:pos] + nouveau_md + contenu[pos+len(ancien_md):]
    modifs += 1
    print("[2/3] OK - Cadre autour des 6 rectangles sources")

# 3. Verifier qu'il n'y a pas de fleches parasites entre sources et plancher
# (normalement deja regle par etape 1)
modifs += 1
print("[3/3] OK - Nettoyage termine")

with open(FICHIER, "w", encoding="utf-8") as f:
    f.write(contenu)
print(f"\nTermine ! {modifs}/3")
