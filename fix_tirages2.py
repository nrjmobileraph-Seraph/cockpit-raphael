FICHIER = r"C:\Users\BoulePiou\cockpit-raphael\app.py"
with open(FICHIER, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Remplacer les lignes 477-490 (index 476-489)
# Trouver debut et fin
debut = None
fin = None
for i, l in enumerate(lines):
    if "# GRAND RECTANGLE : montants alignes + TOTAL au milieu" in l:
        debut = i
    if debut is not None and i > debut and "st.markdown(_g_html, unsafe_allow_html=True)" in l:
        fin = i
        break

if debut is not None and fin is not None:
    indent = "        "
    new_lines = [
        indent + "# Calculer les tirages mensuels par poche\n",
        indent + '_tirage = {"av1": 0, "av2": 0, "av3": 0, "livret_a": 0, "ldds": 0, "lep": 0}\n',
        indent + "try:\n",
        indent + "    _pi, _pi_src = pioche_ce_mois(profil, cap)\n",
        indent + "    if not phase_0:\n",
        indent + '        if "Livret" in _pi_src and cap.get("livret_a", 0) >= _pi:\n',
        indent + '            _tirage["livret_a"] = _pi\n',
        indent + '        elif "AV1" in _pi_src:\n',
        indent + '            _tirage["av1"] = _pi\n',
        indent + "except:\n",
        indent + "    _pi = 0\n",
        indent + "_tirages_list = []\n",
        indent + "for _pn, _pv, _pc in _poches_actives:\n",
        indent + '    _key = "av1" if "AV1" in _pn else "av2" if "AV2" in _pn else "av3" if "AV3" in _pn else "livret_a" if "Livret" in _pn else "ldds" if "LDDS" in _pn else "lep"\n',
        indent + "    _tirages_list.append(_tirage.get(_key, 0))\n",
        indent + "_total_tirage = sum(_tirages_list)\n",
        indent + "\n",
        indent + "# GRAND RECTANGLE : tirages calcules + TOTAL au milieu\n",
        indent + '_g_html = \'<div style="background:linear-gradient(145deg, #1A0D12 0%, #150A10 100%);border:2px solid #C4922A;border-radius:12px;padding:16px;margin-bottom:2px;">\'\n',
        indent + '_g_html += \'<div style="display:flex;align-items:center;justify-content:center;gap:0;flex-wrap:nowrap;">\'\n',
        indent + "for _idx, (_pn, _pv, _pc) in enumerate(_poches_actives):\n",
        indent + "    _tir = _tirages_list[_idx] if _idx < len(_tirages_list) else 0\n",
        indent + "    if _idx > 0 and _idx != _mid:\n",
        indent + '        _g_html += \'<div style="color:#665544;font-size:14px;padding:0 3px;">+</div>\'\n',
        indent + "    if _idx == _mid:\n",
        indent + '        _g_html += \'<div style="color:#C4922A;font-size:18px;padding:0 6px;">\\u27A1</div>\'\n',
        indent + '        _tot_col = "#4DFF99" if _total_tirage > 0 else "#665544"\n',
        indent + "        _g_html += f'<div style=\"min-width:130px;background:#0A0A0A;border:2px solid #FFD060;border-radius:10px;padding:10px;text-align:center;margin:0 4px;\"><div style=\"color:#C4922A;font-size:9px;text-transform:uppercase;letter-spacing:2px;\">TOTAL</div><div style=\"color:{_tot_col};font-size:22px;font-weight:900;\">{_total_tirage:,.0f} EUR</div></div>'\n",
        indent + "        if _idx > 0:\n",
        indent + '            _g_html += \'<div style="color:#C4922A;font-size:18px;padding:0 6px;">\\u2B05</div>\'\n',
        indent + '    _tir_col = "#4DFF99" if _tir > 0 else "#665544"\n',
        indent + '    _tir_txt = f"{_tir:,.0f}" if _tir > 0 else "0"\n',
        indent + "    _g_html += f'<div style=\"flex:1;text-align:center;padding:2px;\"><div style=\"color:{_tir_col};font-size:14px;font-weight:700;\">{_tir_txt}</div></div>'\n",
        indent + '_g_html += \'</div></div>\'\n',
        indent + "st.markdown(_g_html, unsafe_allow_html=True)\n",
    ]
    lines = lines[:debut] + new_lines + lines[fin+1:]
    with open(FICHIER, "w", encoding="utf-8") as f:
        f.writelines(lines)
    print(f"OK - Lignes {debut+1}-{fin+1} remplacees par tirages calcules")
else:
    print(f"ERREUR - debut={debut} fin={fin}")
