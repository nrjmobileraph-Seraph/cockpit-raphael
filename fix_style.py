FICHIER = r"C:\Users\BoulePiou\cockpit-raphael\app.py"
with open(FICHIER, "r", encoding="utf-8") as f:
    contenu = f.read()

modifs = 0

# 1. Petits rectangles noms : plus gros, meme taille
ancien_nm = "padding:2px 8px;"
nouveau_nm = "padding:6px 12px;"
if ancien_nm in contenu:
    contenu = contenu.replace(ancien_nm, nouveau_nm)
ancien_nm2 = 'font-size:9px;text-transform:uppercase;letter-spacing:1px;">{_short}'
nouveau_nm2 = 'font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1px;">{_short}'
if ancien_nm2 in contenu:
    contenu = contenu.replace(ancien_nm2, nouveau_nm2)
    modifs += 1
    print("[1/3] OK - Petits rectangles noms plus gros")

# 2. Dans le grand rectangle : remplacer + entre les 2 groupes par fleches
ancien_plus_mid = """                if _idx > 0:
                    _g_html += '<div style="color:#665544;font-size:16px;padding:0 4px;">+</div>'"""
nouveau_fleche_mid = """                if _idx > 0:
                    _g_html += '<div style="color:#C4922A;font-size:18px;padding:0 6px;">\\u27A1</div>'"""
if ancien_plus_mid in contenu:
    contenu = contenu.replace(ancien_plus_mid, nouveau_fleche_mid, 1)
    modifs += 1
    print("[2a/3] OK - Fleche droite vers TOTAL")

# Fleche gauche : le + avant le TOTAL (cote gauche)
ancien_plus_gauche = """            if _idx > 0 and _idx != _mid:
                _g_html += '<div style="color:#665544;font-size:16px;padding:0 4px;">+</div>'"""
nouveau_plus_gauche = """            if _idx > 0 and _idx != _mid:
                _g_html += '<div style="color:#665544;font-size:14px;padding:0 3px;">+</div>'"""
# On garde les + entre les montants du meme cote, mais on change la fleche vers TOTAL
# Chercher la fleche cote AV3 -> TOTAL
ancien_mid_block = """            if _idx == _mid:
                _g_html += f'<div style="min-width:130px;background:#0A0A0A;border:2px solid #FFD060;border-radius:10px;padding:10px;text-align:center;margin:0 10px;"><div style="color:#C4922A;font-size:9px;text-transform:uppercase;letter-spacing:2px;">TOTAL</div><div style="color:#FFD060;font-size:22px;font-weight:900;">{_total_cap:,.0f} EUR</div></div>'"""
nouveau_mid_block = """            if _idx == _mid:
                _g_html += '<div style="color:#C4922A;font-size:18px;padding:0 6px;">\\u2B05</div>'
                _g_html += f'<div style="min-width:130px;background:#0A0A0A;border:2px solid #FFD060;border-radius:10px;padding:10px;text-align:center;margin:0 4px;"><div style="color:#C4922A;font-size:9px;text-transform:uppercase;letter-spacing:2px;">TOTAL</div><div style="color:#FFD060;font-size:22px;font-weight:900;">{_total_cap:,.0f} EUR</div></div>'"""
if ancien_mid_block in contenu:
    contenu = contenu.replace(ancien_mid_block, nouveau_mid_block)
    modifs += 1
    print("[2b/3] OK - Fleches gauche/droite vers TOTAL")

# 3. Parents d'Amour : elegant, plus gros, belle police
ancien_parents = '<div style="color:#BBA888;font-size:11px;text-transform:uppercase;">Pour mes Parents d Amour...</div>'
nouveau_parents = '<div style="color:#C4922A;font-size:18px;font-family:Garamond,Georgia,serif;font-style:italic;letter-spacing:2px;">Pour mes Parents d Amour...</div>'
if ancien_parents in contenu:
    contenu = contenu.replace(ancien_parents, nouveau_parents)
    modifs += 1
    print("[3/3] OK - Parents d'Amour elegant et plus gros")
else:
    print("[3/3] ERREUR - Parents non trouve")

with open(FICHIER, "w", encoding="utf-8") as f:
    f.write(contenu)
print(f"\nTermine ! {modifs} modifications.")
