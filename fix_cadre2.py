FICHIER = r"C:\Users\BoulePiou\cockpit-raphael\app.py"
with open(FICHIER, "r", encoding="utf-8") as f:
    contenu = f.read()

ancien = "        _b_html += '</div>'"

# On veut ajouter l'affichage avec cadre juste apres
nouveau = """        _b_html += '</div>'
        st.markdown('<div style="border:1px solid #333;border-radius:12px;padding:12px;margin-bottom:16px;">' + _b_html + '</div>', unsafe_allow_html=True)"""

# Remplacer seulement la premiere occurrence (celle des sources, pas d'autres)
idx = contenu.index("        # 6 RECTANGLES SOURCES en bas")
pos = contenu.index(ancien, idx)
contenu = contenu[:pos] + nouveau + contenu[pos+len(ancien):]

with open(FICHIER, "w", encoding="utf-8") as f:
    f.write(contenu)
print("OK - Rectangles sources affiches dans un cadre")
