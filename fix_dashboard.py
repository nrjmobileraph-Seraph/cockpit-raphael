# fix_dashboard.py - 3 modifs dashboard Phase 0
import os

FICHIER = r"C:\Users\BoulePiou\cockpit-raphael\app.py"

with open(FICHIER, "r", encoding="utf-8") as f:
    contenu = f.read()

modifs = 0

ancien_plancher = '''        st.markdown('<div style="display:flex;gap:12px;margin-bottom:16px;flex-wrap:wrap;"><div style="flex:1;min-width:110px;background:#1A0D12;border:2px solid #FF7777;border-radius:10px;padding:8px;text-align:center;"><div style="color:#BBA888;font-size:9px;text-transform:uppercase;">PLANCHER</div><div style="color:#FF7777;font-size:18px;font-weight:900;">2 200 EUR</div></div><div style="flex:1;min-width:110px;background:#1A0D12;border:2px solid #FFD060;border-radius:10px;padding:8px;text-align:center;"><div style="color:#BBA888;font-size:9px;text-transform:uppercase;">CIBLE</div><div style="color:#FFD060;font-size:18px;font-weight:900;">2 500 EUR</div></div><div style="flex:1;min-width:110px;background:#1A0D12;border:2px solid #4DFF99;border-radius:10px;padding:8px;text-align:center;"><div style="color:#BBA888;font-size:9px;text-transform:uppercase;">BONUS</div><div style="color:#4DFF99;font-size:18px;font-weight:900;">2 700 EUR</div></div></div>', unsafe_allow_html=True)'''

source_box = '        _src_items = []\n'
source_box += '        if cap.get("av1", 0) > 0: _src_items.append(("AV1 Lucya Cardif", cap["av1"], "#C4922A"))\n'
source_box += '        if cap.get("av2", 0) > 0: _src_items.append(("AV2 Linxea Spirit", cap["av2"], "#D4A017"))\n'
source_box += '        if cap.get("av3", 0) > 0: _src_items.append(("AV3 Lucya Abeille", cap["av3"], "#BBA888"))\n'
source_box += '        if cap.get("livret_a", 0) > 0: _src_items.append(("Livret A", cap["livret_a"], "#4DFF99"))\n'
source_box += '        if cap.get("ldds", 0) > 0: _src_items.append(("LDDS", cap["ldds"], "#66CCAA"))\n'
source_box += '        if cap.get("lep", 0) > 0: _src_items.append(("LEP", cap["lep"], "#77DDBB"))\n'
source_box += '        _src_html = \'<div style="display:flex;gap:10px;margin-bottom:16px;flex-wrap:wrap;">\'\n'
source_box += '        for _sn, _sv, _sc in _src_items:\n'
source_box += '            _src_html += f\'<div style="flex:1;min-width:100px;background:#1A0D12;border:1px solid {_sc};border-radius:10px;padding:10px;text-align:center;"><div style="color:{_sc};font-size:9px;text-transform:uppercase;letter-spacing:1px;">{_sn}</div><div style="color:#F0E6D8;font-size:16px;font-weight:700;margin-top:4px;">{_sv:,.0f} EUR</div></div>\'\n'
source_box += '        _src_html += \'</div>\'\n'
source_box += '        st.markdown(\'<div style="text-align:center;margin-bottom:6px;"><span style="color:#BBA888;font-size:10px;text-transform:uppercase;letter-spacing:3px;">SOURCES DU CAPITAL</span></div>\', unsafe_allow_html=True)\n'
source_box += '        st.markdown(_src_html, unsafe_allow_html=True)\n\n'

if ancien_plancher in contenu:
    contenu = contenu.replace(ancien_plancher, source_box + ancien_plancher)
    modifs += 1
    print("[1/2] OK - SOURCE DU CAPITAL inseree au-dessus de PLANCHER/CIBLE/BONUS")
else:
    print("[1/2] ERREUR - bloc PLANCHER non trouve")

ancien_parents = '<div style="color:#BBA888;font-size:11px;text-transform:uppercase;">Pour mes Parents d Amour...</div>'
nouveau_parents = '<div style="color:#BBA888;font-size:22px;font-weight:700;letter-spacing:2px;">Pour mes Parents d Amour...</div>'

if ancien_parents in contenu:
    contenu = contenu.replace(ancien_parents, nouveau_parents)
    modifs += 1
    print("[2/2] OK - Parents d Amour 2x plus gros")
else:
    print("[2/2] ERREUR - bloc Parents non trouve")

with open(FICHIER, "w", encoding="utf-8") as f:
    f.write(contenu)

print(f"\nTermine ! {modifs}/2 modifications appliquees.")
print("Relance : streamlit run app.py")
