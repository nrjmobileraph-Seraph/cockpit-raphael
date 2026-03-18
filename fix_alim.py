FICHIER = r"C:\Users\BoulePiou\cockpit-raphael\app.py"
with open(FICHIER, "r", encoding="utf-8") as f:
    contenu = f.read()

modifs = 0

# 1. SUPPRIMER le bloc PROCHAINS MOUVEMENTS
debut_mv = "        # --- Prochains mouvements (depuis chronologie) ---"
fin_mv = "        _src_items = []"

if debut_mv in contenu:
    idx_start = contenu.index(debut_mv)
    idx_end = contenu.index(fin_mv)
    contenu = contenu[:idx_start] + fin_mv + contenu[idx_end + len(fin_mv):]
    modifs += 1
    print("[1/2] OK - PROCHAINS MOUVEMENTS supprime")
else:
    print("[1/2] DEJA FAIT ou non trouve")

# 2. INSERER box ALIMENTATION DU COMPTE au-dessus de SOURCES DU CAPITAL
ancien_sources_titre = "        st.markdown('<div style=" + '"text-align:center;margin-bottom:6px;"><span style="color:#BBA888;font-size:10px;text-transform:uppercase;letter-spacing:3px;">SOURCES DU CAPITAL</span></div>' + "', unsafe_allow_html=True)"

box_alim = '''        # --- Alimentation du compte courant ---
        _alim_html = '<div style="background:linear-gradient(145deg, #1A0D12 0%, #150A10 100%);border:2px solid #C4922A;border-radius:12px;padding:16px;margin-bottom:16px;">'
        _alim_html += '<div style="color:#C4922A;font-size:11px;text-transform:uppercase;letter-spacing:3px;text-align:center;margin-bottom:12px;">ALIMENTATION DU COMPTE</div>'
        _alim_html += '<div style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center;">'
        _alim_sources = [
            ("Livret A", cap.get("livret_a", 0), "#4DFF99"),
            ("AV1 Lucya Cardif", cap.get("av1", 0), "#C4922A"),
            ("AV2 Linxea Spirit", cap.get("av2", 0), "#D4A017"),
        ]
        for _an, _av, _ac in _alim_sources:
            if _av > 0:
                _alim_html += f'<div style="display:flex;align-items:center;gap:8px;padding:6px 12px;background:#0A0A0A;border:1px solid {_ac};border-radius:8px;"><span style="color:{_ac};font-size:11px;">{_an}</span><span style="color:#FFD060;font-size:16px;">\\u2192</span><span style="color:#4DFF99;font-size:11px;font-weight:700;">CC</span></div>'
        _alim_html += '</div></div>'
        st.markdown(_alim_html, unsafe_allow_html=True)

'''

if ancien_sources_titre in contenu:
    contenu = contenu.replace(ancien_sources_titre, box_alim + ancien_sources_titre)
    modifs += 1
    print("[2/2] OK - Box ALIMENTATION DU COMPTE inseree")
else:
    print("[2/2] ERREUR - titre SOURCES non trouve")

with open(FICHIER, "w", encoding="utf-8") as f:
    f.write(contenu)

print(f"\nTermine ! {modifs}/2 modifications.")
print("Relance : streamlit run app.py")
