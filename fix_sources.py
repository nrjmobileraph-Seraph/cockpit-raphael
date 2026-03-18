FICHIER = r"C:\Users\BoulePiou\cockpit-raphael\app.py"
with open(FICHIER, "r", encoding="utf-8") as f:
    contenu = f.read()

ancien = '''        _src_items = []
        if cap.get("av1", 0) > 0: _src_items.append(("AV1 Lucya Cardif", cap["av1"], "#C4922A"))
        if cap.get("av2", 0) > 0: _src_items.append(("AV2 Linxea Spirit", cap["av2"], "#D4A017"))
        if cap.get("av3", 0) > 0: _src_items.append(("AV3 Lucya Abeille", cap["av3"], "#BBA888"))
        if cap.get("livret_a", 0) > 0: _src_items.append(("Livret A", cap["livret_a"], "#4DFF99"))
        if cap.get("ldds", 0) > 0: _src_items.append(("LDDS", cap["ldds"], "#66CCAA"))
        if cap.get("lep", 0) > 0: _src_items.append(("LEP", cap["lep"], "#77DDBB"))
        _src_html = '<div style="display:flex;gap:10px;margin-bottom:16px;flex-wrap:wrap;">'
        for _sn, _sv, _sc in _src_items:
            _src_html += f'<div style="flex:1;min-width:100px;background:#1A0D12;border:1px solid {_sc};border-radius:10px;padding:10px;text-align:center;"><div style="color:{_sc};font-size:9px;text-transform:uppercase;letter-spacing:1px;">{_sn}</div><div style="color:#F0E6D8;font-size:16px;font-weight:700;margin-top:4px;">{_sv:,.0f} EUR</div></div>'
        _src_html += '</div>'
        # --- Alimentation du compte : quelles sources nourrissent le CC ---
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

        st.markdown('<div style="text-align:center;margin-bottom:6px;"><span style="color:#BBA888;font-size:10px;text-transform:uppercase;letter-spacing:3px;">SOURCES DU CAPITAL</span></div>', unsafe_allow_html=True)
        st.markdown(_src_html, unsafe_allow_html=True)'''

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

if ancien in contenu:
    contenu = contenu.replace(ancien, nouveau)
    with open(FICHIER, "w", encoding="utf-8") as f:
        f.write(contenu)
    print("OK - Nouveau systeme sources + fleches + total installe")
else:
    print("ERREUR - bloc ancien non trouve")
