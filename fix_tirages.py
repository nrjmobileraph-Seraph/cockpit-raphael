FICHIER = r"C:\Users\BoulePiou\cockpit-raphael\app.py"
with open(FICHIER, "r", encoding="utf-8") as f:
    contenu = f.read()

# Remplacer les montants dans le grand rectangle : au lieu des soldes, mettre les tirages calcules
ancien = '''        # GRAND RECTANGLE : montants alignes + TOTAL au milieu
        _g_html = '<div style="background:linear-gradient(145deg, #1A0D12 0%, #150A10 100%);border:2px solid #C4922A;border-radius:12px;padding:16px;margin-bottom:2px;">'
        _g_html += '<div style="display:flex;align-items:center;justify-content:center;gap:0;flex-wrap:nowrap;">'
        for _idx, (_pn, _pv, _pc) in enumerate(_poches_actives):
            if _idx > 0 and _idx != _mid:
                _g_html += '<div style="color:#665544;font-size:14px;padding:0 3px;">+</div>'
            if _idx == _mid:
                _g_html += '<div style="color:#C4922A;font-size:18px;padding:0 6px;">\\u27A1</div>'
                _g_html += f'<div style="min-width:130px;background:#0A0A0A;border:2px solid #FFD060;border-radius:10px;padding:10px;text-align:center;margin:0 4px;"><div style="color:#C4922A;font-size:9px;text-transform:uppercase;letter-spacing:2px;">TOTAL</div><div style="color:#FFD060;font-size:22px;font-weight:900;">{_total_cap:,.0f} EUR</div></div>'
                if _idx > 0:
                    _g_html += '<div style="color:#C4922A;font-size:18px;padding:0 6px;">\\u2B05</div>'
            _g_html += f'<div style="flex:1;text-align:center;padding:2px;"><div style="color:#F0E6D8;font-size:14px;font-weight:700;">{_pv:,.0f}</div></div>'
        _g_html += '</div></div>'
        st.markdown(_g_html, unsafe_allow_html=True)'''

nouveau = '''        # Calculer les tirages mensuels par poche
        _tirage = {"av1": 0, "av2": 0, "av3": 0, "livret_a": 0, "ldds": 0, "lep": 0}
        try:
            _pi, _pi_src = pioche_ce_mois(profil, cap)
            if not phase_0:
                if _pi_src == "Livret A" and cap.get("livret_a", 0) >= _pi:
                    _tirage["livret_a"] = _pi
                elif _pi_src == "AV1":
                    _tirage["av1"] = _pi
                else:
                    _tirage["av1"] = _pi
        except:
            _pi = 0

        _tirages_list = []
        for _pn, _pv, _pc in _poches_actives:
            _key = "av1" if "AV1" in _pn else "av2" if "AV2" in _pn else "av3" if "AV3" in _pn else "livret_a" if "Livret" in _pn else "ldds" if "LDDS" in _pn else "lep"
            _tirages_list.append(_tirage.get(_key, 0))
        _total_tirage = sum(_tirages_list)

        # GRAND RECTANGLE : tirages + TOTAL au milieu
        _g_html = '<div style="background:linear-gradient(145deg, #1A0D12 0%, #150A10 100%);border:2px solid #C4922A;border-radius:12px;padding:16px;margin-bottom:2px;">'
        _g_html += '<div style="display:flex;align-items:center;justify-content:center;gap:0;flex-wrap:nowrap;">'
        for _idx, (_pn, _pv, _pc) in enumerate(_poches_actives):
            _tir = _tirages_list[_idx] if _idx < len(_tirages_list) else 0
            if _idx > 0 and _idx != _mid:
                _g_html += '<div style="color:#665544;font-size:14px;padding:0 3px;">+</div>'
            if _idx == _mid:
                _g_html += '<div style="color:#C4922A;font-size:18px;padding:0 6px;">\\u27A1</div>'
                _tot_col = "#4DFF99" if _total_tirage > 0 else "#665544"
                _g_html += f'<div style="min-width:130px;background:#0A0A0A;border:2px solid #FFD060;border-radius:10px;padding:10px;text-align:center;margin:0 4px;"><div style="color:#C4922A;font-size:9px;text-transform:uppercase;letter-spacing:2px;">TOTAL</div><div style="color:{_tot_col};font-size:22px;font-weight:900;">{_total_tirage:,.0f} EUR</div></div>'
                if _idx > 0:
                    _g_html += '<div style="color:#C4922A;font-size:18px;padding:0 6px;">\\u2B05</div>'
            _tir_col = "#4DFF99" if _tir > 0 else "#665544"
            _tir_txt = f"{_tir:,.0f}" if _tir > 0 else "0"
            _g_html += f'<div style="flex:1;text-align:center;padding:2px;"><div style="color:{_tir_col};font-size:14px;font-weight:700;">{_tir_txt}</div></div>'
        _g_html += '</div></div>'
        st.markdown(_g_html, unsafe_allow_html=True)'''

if ancien in contenu:
    contenu = contenu.replace(ancien, nouveau)
    with open(FICHIER, "w", encoding="utf-8") as f:
        f.write(contenu)
    print("OK - Grand rectangle avec tirages calcules")
else:
    print("ERREUR - bloc non trouve")
