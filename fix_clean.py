FICHIER = r"C:\Users\BoulePiou\cockpit-raphael\app.py"
with open(FICHIER, "r", encoding="utf-8") as f:
    contenu = f.read()

ancien = "        # GRAND RECTANGLE : montants avec labels + TOTAL au milieu"
fin_ancien = "        st.markdown(_g_html, unsafe_allow_html=True)"

idx1 = contenu.index(ancien)
idx2 = contenu.index(fin_ancien, idx1) + len(fin_ancien)

nouveau = '''        # GRAND RECTANGLE : montants + TOTAL au milieu
        _g_html = '<div style="background:linear-gradient(145deg, #1A0D12 0%, #150A10 100%);border:2px solid #C4922A;border-radius:12px;padding:16px;margin-bottom:2px;">'
        _g_html += '<div style="display:flex;align-items:center;justify-content:center;gap:0;flex-wrap:nowrap;">'
        for _idx, (_pn, _pv, _pc) in enumerate(_poches_actives):
            if _idx > 0 and _idx != _mid:
                _g_html += '<div style="color:#665544;font-size:16px;padding:0 4px;">+</div>'
            if _idx == _mid:
                _g_html += f'<div style="min-width:130px;background:#0A0A0A;border:2px solid #FFD060;border-radius:10px;padding:10px;text-align:center;margin:0 10px;"><div style="color:#C4922A;font-size:9px;text-transform:uppercase;letter-spacing:2px;">TOTAL</div><div style="color:#FFD060;font-size:22px;font-weight:900;">{_total_cap:,.0f} EUR</div></div>'
                if _idx > 0:
                    _g_html += '<div style="color:#665544;font-size:16px;padding:0 4px;">+</div>'
            _g_html += f'<div style="flex:1;text-align:center;padding:2px;"><div style="color:#F0E6D8;font-size:14px;font-weight:700;">{_pv:,.0f}</div></div>'
        _g_html += '</div></div>'
        st.markdown(_g_html, unsafe_allow_html=True)'''

contenu = contenu[:idx1] + nouveau + contenu[idx2:]

with open(FICHIER, "w", encoding="utf-8") as f:
    f.write(contenu)
print("OK - Grand rectangle propre")
