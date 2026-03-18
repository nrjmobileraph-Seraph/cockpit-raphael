FICHIER = r"C:\Users\BoulePiou\cockpit-raphael\app.py"
with open(FICHIER, "r", encoding="utf-8") as f:
    contenu = f.read()

ancien_fleches_fin = '''        st.markdown(_fl_html, unsafe_allow_html=True)

        # 6 RECTANGLES SOURCES en bas'''

nouveau = '''        st.markdown(_fl_html, unsafe_allow_html=True)

        # Petits rectangles noms entre les fleches et les gros rectangles
        _nm_html = '<div style="display:flex;gap:6px;margin:2px 0;flex-wrap:nowrap;">'
        for _idx, (_pn, _pv, _pc) in enumerate(_poches_actives):
            if _idx > 0 and _idx != _mid:
                _nm_html += '<div style="display:flex;align-items:center;padding:0 2px;"></div>'
            if _idx == _mid:
                _nm_html += '<div style="min-width:130px;"></div>'
            _short = _pn.split()[0] if len(_pn) > 8 else _pn
            _nm_html += f'<div style="flex:1;text-align:center;"><div style="display:inline-block;background:{_pc}22;border:1px solid {_pc};border-radius:4px;padding:2px 8px;"><span style="color:{_pc};font-size:9px;text-transform:uppercase;letter-spacing:1px;">{_short}</span></div></div>'
        _nm_html += '</div>'
        st.markdown(_nm_html, unsafe_allow_html=True)

        # Petites fleches entre noms et gros rectangles
        _fl2_html = '<div style="display:flex;justify-content:center;align-items:center;gap:0;margin:0;padding:0;">'
        for _idx, (_pn, _pv, _pc) in enumerate(_poches_actives):
            if _idx > 0 and _idx != _mid:
                _fl2_html += '<div style="padding:0 2px;"></div>'
            if _idx == _mid:
                _fl2_html += '<div style="min-width:130px;"></div>'
            _fl2_html += f'<div style="flex:1;text-align:center;"><span style="color:{_pc};font-size:16px;">\\u2B06</span></div>'
        _fl2_html += '</div>'
        st.markdown(_fl2_html, unsafe_allow_html=True)

        # 6 RECTANGLES SOURCES en bas'''

if ancien_fleches_fin in contenu:
    contenu = contenu.replace(ancien_fleches_fin, nouveau)
    with open(FICHIER, "w", encoding="utf-8") as f:
        f.write(contenu)
    print("OK - Petits rectangles noms + 2eme fleches ajoutes")
else:
    print("ERREUR - bloc non trouve")
