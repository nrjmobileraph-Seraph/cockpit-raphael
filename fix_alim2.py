FICHIER = r"C:\Users\BoulePiou\cockpit-raphael\app.py"
with open(FICHIER, "r", encoding="utf-8") as f:
    contenu = f.read()

# SUPPRIMER l'ancien bloc ALIMENTATION DU COMPTE
ancien_debut = "        # --- Alimentation du compte courant ---"
ancien_fin = "        st.markdown('<div style=" + '"' + "text-align:center;margin-bottom:6px;"

if ancien_debut in contenu:
    idx_start = contenu.index(ancien_debut)
    idx_end = contenu.index(ancien_fin, idx_start)
    contenu = contenu[:idx_start] + contenu[idx_end:]
    print("[1/2] OK - Ancien bloc ALIMENTATION supprime")
else:
    print("[1/2] Ancien bloc non trouve, on continue")

# INSERER le nouveau bloc adaptatif
cible = "        st.markdown('<div style=" + '"' + "text-align:center;margin-bottom:6px;"

nouveau = '''        # --- Alimentation du compte : quelles sources nourrissent le CC ---
        _flux = []
        if cap.get("livret_a", 0) > 0: _flux.append(("Livret A", "#4DFF99"))
        if cap.get("ldds", 0) > 0: _flux.append(("LDDS", "#66CCAA"))
        if cap.get("lep", 0) > 0: _flux.append(("LEP", "#77DDBB"))
        if cap.get("av1", 0) > 0: _flux.append(("AV1", "#C4922A"))
        if cap.get("av2", 0) > 0: _flux.append(("AV2", "#D4A017"))
        if cap.get("av3", 0) > 0: _flux.append(("AV3", "#BBA888"))
        if _flux:
            _f_html = '<div style="background:#1A0D12;border:2px solid #C4922A;border-radius:12px;padding:12px;margin-bottom:12px;text-align:center;">'
            _f_html += '<div style="display:flex;align-items:center;justify-content:center;gap:8px;flex-wrap:wrap;">'
            for _i, (_fn, _fc) in enumerate(_flux):
                _f_html += f'<span style="color:{_fc};font-size:13px;font-weight:700;padding:4px 10px;border:1px solid {_fc};border-radius:6px;">{_fn}</span>'
                _f_html += '<span style="color:#FFD060;font-size:16px;">\\u2192</span>'
            _f_html += '<span style="color:#4DFF99;font-size:15px;font-weight:900;padding:4px 14px;border:2px solid #4DFF99;border-radius:8px;">COMPTE COURANT</span>'
            _f_html += '</div></div>'
            st.markdown(_f_html, unsafe_allow_html=True)

'''

if cible in contenu:
    contenu = contenu.replace(cible, nouveau + cible, 1)
    print("[2/2] OK - Nouveau bloc adaptatif insere")
else:
    print("[2/2] ERREUR - cible non trouvee")

with open(FICHIER, "w", encoding="utf-8") as f:
    f.write(contenu)
print("Relance : streamlit run app.py")
