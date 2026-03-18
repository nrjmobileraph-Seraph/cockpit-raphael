import shutil
shutil.copy2("app.py", "app.py.bak2")
with open("app.py", "r", encoding="utf-8") as f:
    lines = f.readlines()
bl = pl = None
for i, line in enumerate(lines):
    if "BUDGET AUJOURD" in line: bl = i
    if bl is not None and pl is None and "PLANCHER" in line and i > bl: pl = i; break
if bl is None or pl is None:
    print("ERREUR: marqueurs non trouves"); exit(1)

code = []
code.append("")
code.append("        # === ETAGE 3 : REVENUS MENSUELS ===")
code.append('        _rev = [("AAH", profil["aah_mensuel"]),("Loyers LMNP", profil["loyer_net"]),("RVD", profil.get("rvd_mensuel", 0)),("ASPA", profil.get("aspa_mensuelle", 0)),("Revenus pro", profil.get("revenus_pro", 0)),("Autres rentes", profil.get("autres_rentes", 0))]')
code.append("        _rtot = sum(v for _, v in _rev)")
code.append("        _rmid = len(_rev) // 2")
s1 = '        _rg = \' + \'.join(f\'<span style="color:#4DFF99;font-weight:700;">{v:,.0f}</span>\' for _, v in _rev[:_rmid])'
s2 = '        _rd = \' + \'.join(f\'<span style="color:#4DFF99;font-weight:700;">{v:,.0f}</span>\' for _, v in _rev[_rmid:])'
code.append(s1)
code.append(s2)
code.append("        _rc = ''")
code.append("        for _n, _v in _rev:")
code.append('            _rc += f\'<div style="flex:1;min-width:100px;max-width:160px;background:#0A1E12;border:1px solid #1A6B4B;border-radius:8px;padding:8px 6px;text-align:center;"><div style="color:#BBA888;font-size:9px;text-transform:uppercase;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">{_n}</div><div style="color:#4DFF99;font-size:18px;font-weight:900;margin-top:4px;">{_v:,.0f} EUR</div></div>\'')
code.append('        _ra = \'\'.join(\'<div style="text-align:center;flex:1;color:#4DFF99;font-size:18px;">&#9650;</div>\' for _ in _rev)')
code.append('        st.markdown(f\'<div style="margin:16px 0;"><div style="background:#0A1E12;border:2px solid #4DFF99;border-radius:10px;padding:12px 16px;display:flex;align-items:center;justify-content:center;gap:8px;flex-wrap:wrap;"><div style="color:#BBA888;font-size:11px;">{_rg}</div><div style="color:#FFF;font-size:11px;">&#10132;</div><div style="background:#1A6B4B;border-radius:8px;padding:8px 16px;text-align:center;"><div style="color:#BBA888;font-size:9px;text-transform:uppercase;">REVENUS / MOIS</div><div style="color:#4DFF99;font-size:22px;font-weight:900;">{_rtot:,.0f} EUR</div></div><div style="color:#FFF;font-size:11px;">&#10132;</div><div style="color:#BBA888;font-size:11px;">{_rd}</div></div><div style="display:flex;gap:4px;margin:4px 0;padding:0 10px;">{_ra}</div><div style="border:1px solid #1A6B4B;border-radius:10px;padding:10px;display:flex;gap:6px;flex-wrap:wrap;justify-content:center;">{_rc}</div></div>\', unsafe_allow_html=True)')
code.append("")
code.append("        # === ETAGE 4 : POCHES CAPITAL (10 rectangles compacts) ===")
code.append('        _pch = [("AV1 Lucya Cardif", cap["av1"]),("AV2 Linxea Spirit", cap["av2"]),("AV3 Lucya Abeille", cap["av3"]),("AV4 Boursorama", cap.get("av4", 0)),("Livret A", cap["livret_a"]),("LDDS", cap["ldds"]),("LEP", cap["lep"]),("PEA", cap.get("pea", 0)),("Crypto", cap.get("crypto", 0)),("Crowdfunding", cap.get("crowdfunding", 0))]')
code.append("        _ptot = sum(v for _, v in _pch)")
code.append("        _pmid = len(_pch) // 2")
code.append('        _tg = \' + \'.join(f\'<span style="color:#C4922A;font-weight:700;">0</span>\' for _ in _pch[:_pmid])')
code.append('        _td = \' + \'.join(f\'<span style="color:#C4922A;font-weight:700;">0</span>\' for _ in _pch[_pmid:])')
code.append("        _pc = ''")
code.append("        for _n, _v in _pch:")
code.append("            _vc = '#FFD060' if _v > 0 else '#665544'")
code.append('            _pc += f\'<div style="flex:1 1 calc(20% - 8px);min-width:85px;max-width:120px;background:#1A0D12;border:1px solid #C4922A;border-radius:8px;padding:6px 4px;text-align:center;"><div style="color:#BBA888;font-size:8px;text-transform:uppercase;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">{_n}</div><div style="color:{_vc};font-size:14px;font-weight:900;margin-top:2px;">{_v:,.0f}</div></div>\'')
code.append('        _pa = \'\'.join(\'<div style="text-align:center;flex:1;color:#C4922A;font-size:18px;">&#9650;</div>\' for _ in _pch)')
code.append('        st.markdown(f\'<div style="margin:8px 0 16px 0;"><div style="background:#1A0D12;border:2px solid #C4922A;border-radius:10px;padding:12px 16px;display:flex;align-items:center;justify-content:center;gap:8px;flex-wrap:wrap;"><div style="color:#BBA888;font-size:11px;">{_tg}</div><div style="color:#FFF;font-size:11px;">&#10132;</div><div style="background:#3A2010;border-radius:8px;padding:8px 16px;text-align:center;"><div style="color:#BBA888;font-size:9px;text-transform:uppercase;">CAPITAL TOTAL</div><div style="color:#FFD060;font-size:22px;font-weight:900;">{_ptot:,.0f} EUR</div></div><div style="color:#FFF;font-size:11px;">&#10132;</div><div style="color:#BBA888;font-size:11px;">{_td}</div></div><div style="display:flex;gap:4px;margin:4px 0;padding:0 10px;">{_pa}</div><div style="border:1px solid #C4922A;border-radius:10px;padding:8px;display:flex;gap:5px;flex-wrap:wrap;justify-content:center;">{_pc}</div></div>\', unsafe_allow_html=True)')
code.append("")

new = lines[:bl+1]
for c in code:
    new.append(c + "\n")
new.extend(lines[pl:])
with open("app.py", "w", encoding="utf-8") as f:
    f.writelines(new)
print(f"OK - Etage 3+4 inseres entre L{bl+1} et L{pl+1}")
