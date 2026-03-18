FICHIER = r"C:\Users\BoulePiou\cockpit-raphael\app.py"
with open(FICHIER, "r", encoding="utf-8") as f:
    contenu = f.read()

# Inserer le bloc REVENUS juste avant PLANCHER/CIBLE/BONUS
cible = "        st.markdown('<div style=" + '"' + "display:flex;gap:12px;margin-bottom:16px;flex-wrap:wrap;" + '"'

revenus_bloc = '''        # --- SOURCES DE REVENUS : meme schema que capital ---
        _aah_m = profil.get('aah_mensuel', 625) or 625
        _pch_m = profil.get('pch_mensuel', 0) or 0
        _loyer_m = profil.get('loyer_net', 0) or 0
        _rdt_av = (cap.get('av1',0) + cap.get('av2',0) + cap.get('av3',0)) * profil.get('rendement_annuel', 0.0345) / 12
        _int_liv = (cap.get('livret_a',0) * 0.025 + cap.get('ldds',0) * 0.025 + cap.get('lep',0) * 0.04) / 12
        _rev_sources = [
            ("AAH", _aah_m, "#FFD060"),
            ("Loyers LMNP", _loyer_m, "#4DFF99"),
            ("PCH", _pch_m, "#66CCAA"),
            ("Rendement AV", round(_rdt_av, 0), "#C4922A"),
            ("Interets livrets", round(_int_liv, 0), "#77DDBB"),
        ]
        _rev_actives = [(n, v, c) for n, v, c in _rev_sources if v > 0]
        _rev_total = sum(v for _, v, _ in _rev_actives)
        _rev_nb = len(_rev_actives)
        _rev_mid = _rev_nb // 2

        # Grand rectangle revenus : montants + TOTAL
        _rv_html = '<div style="background:linear-gradient(145deg, #1A0D12 0%, #150A10 100%);border:2px solid #4DFF99;border-radius:12px;padding:16px;margin-bottom:2px;">'
        _rv_html += '<div style="display:flex;align-items:center;justify-content:center;gap:0;flex-wrap:nowrap;">'
        for _idx, (_rn, _rv, _rc) in enumerate(_rev_actives):
            if _idx > 0 and _idx != _rev_mid:
                _rv_html += '<div style="color:#665544;font-size:14px;padding:0 3px;">+</div>'
            if _idx == _rev_mid:
                _rv_html += f'<div style="color:#4DFF99;font-size:18px;padding:0 6px;">\\u27A1</div>'
                _rv_html += f'<div style="min-width:130px;background:#0A0A0A;border:2px solid #4DFF99;border-radius:10px;padding:10px;text-align:center;margin:0 4px;"><div style="color:#4DFF99;font-size:9px;text-transform:uppercase;letter-spacing:2px;">REVENUS/MOIS</div><div style="color:#4DFF99;font-size:22px;font-weight:900;">{_rev_total:,.0f} EUR</div></div>'
                if _idx > 0:
                    _rv_html += f'<div style="color:#4DFF99;font-size:18px;padding:0 6px;">\\u2B05</div>'
            _rv_html += f'<div style="flex:1;text-align:center;padding:2px;"><div style="color:#F0E6D8;font-size:14px;font-weight:700;">{_rv:,.0f}</div></div>'
        _rv_html += '</div></div>'
        st.markdown(_rv_html, unsafe_allow_html=True)

        # Fleches revenus
        _rvf_html = '<div style="display:flex;justify-content:center;align-items:center;gap:0;margin:2px 0;padding:0;">'
        for _idx, (_rn, _rv, _rc) in enumerate(_rev_actives):
            if _idx > 0 and _idx != _rev_mid:
                _rvf_html += '<div style="padding:0 3px;"></div>'
            if _idx == _rev_mid:
                _rvf_html += '<div style="min-width:130px;"></div>'
            _rvf_html += f'<div style="flex:1;text-align:center;"><span style="color:{_rc};font-size:20px;">\\u2B06</span></div>'
        _rvf_html += '</div>'
        st.markdown(_rvf_html, unsafe_allow_html=True)

        # Rectangles revenus en bas dans un cadre
        _rvb_html = '<div style="display:flex;gap:6px;flex-wrap:nowrap;">'
        for _idx, (_rn, _rv, _rc) in enumerate(_rev_actives):
            if _idx > 0 and _idx != _rev_mid:
                _rvb_html += '<div style="padding:0 2px;"></div>'
            if _idx == _rev_mid:
                _rvb_html += '<div style="min-width:130px;"></div>'
            _rvb_html += f'<div style="flex:1;min-width:100px;background:#1A0D12;border:1px solid {_rc};border-radius:10px;padding:10px;text-align:center;"><div style="color:{_rc};font-size:9px;text-transform:uppercase;letter-spacing:1px;">{_rn}</div><div style="color:#F0E6D8;font-size:15px;font-weight:700;margin-top:4px;">{_rv:,.0f} EUR</div></div>'
        _rvb_html += '</div>'
        st.markdown('<div style="border:2px solid #4DFF99;border-radius:12px;padding:14px;margin-bottom:16px;background:#0A0A0A;">' + _rvb_html + '</div>', unsafe_allow_html=True)

'''

if cible in contenu:
    idx = contenu.index(cible)
    contenu = contenu[:idx] + revenus_bloc + contenu[idx:]
    with open(FICHIER, "w", encoding="utf-8") as f:
        f.write(contenu)
    print("OK - Bloc REVENUS insere avant PLANCHER/CIBLE/BONUS")
else:
    print("ERREUR - cible non trouvee")
