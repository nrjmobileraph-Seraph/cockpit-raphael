FICHIER = r"C:\Users\BoulePiou\cockpit-raphael\app.py"
with open(FICHIER, "r", encoding="utf-8") as f:
    contenu = f.read()

ancien = '''        # --- Sources du capital avec grand rectangle total au-dessus ---
        _poches = [
            ("AV1 Lucya Cardif", cap.get("av1", 0) or 0, "#C4922A"),
            ("AV2 Linxea Spirit", cap.get("av2", 0) or 0, "#D4A017"),
            ("AV3 Lucya Abeille", cap.get("av3", 0) or 0, "#BBA888"),
            ("Livret A", cap.get("livret_a", 0) or 0, "#4DFF99"),
            ("LDDS", cap.get("ldds", 0) or 0, "#66CCAA"),
            ("LEP", cap.get("lep", 0) or 0, "#77DDBB"),
        ]
        _poches_actives = [(n, v, c) for n, v, c in _poches if v > 0]
        _total_cap = sum(v for _, v, _ in _poches_actives)

        # Grand rectangle : montants en haut + carre TOTAL au milieu
        _g_html = '<div style="background:linear-gradient(145deg, #1A0D12 0%, #150A10 100%);border:2px solid #C4922A;border-radius:12px;padding:16px;margin-bottom:0;">'
        _g_html += '<div style="display:flex;align-items:flex-end;justify-content:center;gap:0;flex-wrap:nowrap;">'
        _nb = len(_poches_actives)
        _mid = _nb // 2
        for _idx, (_pn, _pv, _pc) in enumerate(_poches_actives):
            _g_html += f'<div style="flex:1;text-align:center;padding:4px;"><div style="color:{_pc};font-size:10px;text-transform:uppercase;">{_pn}</div><div style="color:#F0E6D8;font-size:14px;font-weight:700;">{_pv:,.0f}</div></div>'
            if _idx == _mid - 1:
                _g_html += f'<div style="min-width:120px;background:#0A0A0A;border:2px solid #FFD060;border-radius:10px;padding:10px;text-align:center;margin:0 8px;"><div style="color:#C4922A;font-size:9px;text-transform:uppercase;letter-spacing:2px;">TOTAL</div><div style="color:#FFD060;font-size:22px;font-weight:900;">{_total_cap:,.0f} EUR</div></div>'
        _g_html += '</div></div>'
        st.markdown(_g_html, unsafe_allow_html=True)

        # Fleches qui montent
        _fl_html = '<div style="display:flex;justify-content:center;gap:0;margin:0;padding:0;">'
        for _idx, (_pn, _pv, _pc) in enumerate(_poches_actives):
            _fl_html += f'<div style="flex:1;text-align:center;"><span style="color:{_pc};font-size:20px;">\\u2B06</span></div>'
            if _idx == _mid - 1:
                _fl_html += '<div style="min-width:120px;"></div>'
        _fl_html += '</div>'
        st.markdown(_fl_html, unsafe_allow_html=True)

        # Les 6 sources en bas
        _b_html = '<div style="display:flex;gap:8px;margin-bottom:16px;flex-wrap:nowrap;">'
        for _idx, (_pn, _pv, _pc) in enumerate(_poches_actives):
            _b_html += f'<div style="flex:1;min-width:80px;background:#1A0D12;border:1px solid {_pc};border-radius:10px;padding:10px;text-align:center;"><div style="color:{_pc};font-size:9px;text-transform:uppercase;letter-spacing:1px;">{_pn}</div><div style="color:#F0E6D8;font-size:15px;font-weight:700;margin-top:4px;">{_pv:,.0f} EUR</div></div>'
            if _idx == _mid - 1:
                _b_html += '<div style="min-width:120px;"></div>'
        _b_html += '</div>\\n' '''

nouveau = '''        # --- Sources du capital avec grand rectangle total au-dessus ---
        _poches = [
            ("AV1 Lucya Cardif", cap.get("av1", 0) or 0, "#C4922A"),
            ("AV2 Linxea Spirit", cap.get("av2", 0) or 0, "#D4A017"),
            ("AV3 Lucya Abeille", cap.get("av3", 0) or 0, "#BBA888"),
            ("Livret A", cap.get("livret_a", 0) or 0, "#4DFF99"),
            ("LDDS", cap.get("ldds", 0) or 0, "#66CCAA"),
            ("LEP", cap.get("lep", 0) or 0, "#77DDBB"),
        ]
        _poches_actives = [(n, v, c) for n, v, c in _poches if v > 0]
        _total_cap = sum(v for _, v, _ in _poches_actives)
        _nb = len(_poches_actives)
        _mid = _nb // 2

        # GRAND RECTANGLE : montants alignes + TOTAL au milieu
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
        st.markdown(_g_html, unsafe_allow_html=True)

        # FLECHES qui montent + fleches laterales vers TOTAL
        _fl_html = '<div style="display:flex;justify-content:center;align-items:center;gap:0;margin:2px 0;padding:0;">'
        for _idx, (_pn, _pv, _pc) in enumerate(_poches_actives):
            if _idx > 0 and _idx != _mid:
                _fl_html += '<div style="padding:0 4px;"></div>'
            if _idx == _mid:
                _fl_html += '<div style="min-width:130px;text-align:center;"><span style="color:#C4922A;font-size:14px;">\\u2B05</span><span style="color:#C4922A;font-size:10px;padding:0 4px;">\\u2795</span><span style="color:#C4922A;font-size:14px;">\\u27A1</span></div>'
                if _idx > 0:
                    _fl_html += '<div style="padding:0 4px;"></div>'
            _fl_html += f'<div style="flex:1;text-align:center;"><span style="color:{_pc};font-size:20px;">\\u2B06</span></div>'
        _fl_html += '</div>'
        st.markdown(_fl_html, unsafe_allow_html=True)

        # 6 RECTANGLES SOURCES en bas
        _b_html = '<div style="display:flex;gap:6px;margin-bottom:16px;flex-wrap:nowrap;">'
        for _idx, (_pn, _pv, _pc) in enumerate(_poches_actives):
            if _idx > 0 and _idx != _mid:
                _b_html += '<div style="display:flex;align-items:center;color:#665544;font-size:14px;padding:0 2px;"></div>'
            if _idx == _mid:
                _b_html += '<div style="min-width:130px;"></div>'
            _b_html += f'<div style="flex:1;min-width:80px;background:#1A0D12;border:1px solid {_pc};border-radius:10px;padding:10px;text-align:center;"><div style="color:{_pc};font-size:9px;text-transform:uppercase;letter-spacing:1px;">{_pn}</div><div style="color:#F0E6D8;font-size:15px;font-weight:700;margin-top:4px;">{_pv:,.0f} EUR</div></div>'
        _b_html += '</div>' '''

if ancien in contenu:
    contenu = contenu.replace(ancien, nouveau)
    with open(FICHIER, "w", encoding="utf-8") as f:
        f.write(contenu)
    print("OK - Rectangles sources restaures + fleches + plus + total")
else:
    print("ERREUR - bloc non trouve")
