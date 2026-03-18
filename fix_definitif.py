import shutil
shutil.copy2("app.py", "app_backup_definitive.py")
print("Backup cree: app_backup_definitive.py")

with open("app.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

bl = pl = None
for i, line in enumerate(lines):
    if "BUDGET AUJOURD" in line:
        bl = i
    if bl is not None and pl is None and "PLANCHER" in line and i > bl:
        pl = i
        break

if bl is None or pl is None:
    print("ERREUR: marqueurs non trouves")
    exit(1)

print(f"Zone a remplacer: L{bl+1} a L{pl+1} ({pl-bl-1} lignes)")

code = []
code.append("")
code.append("        # === REVENUS MENSUELS ===")
code.append('        _rev = [("AAH", profil["aah_mensuel"]),("Loyers LMNP", profil["loyer_net"]),("RVD", profil.get("rvd_mensuel", 0)),("ASPA", profil.get("aspa_mensuelle", 0)),("Revenus pro", profil.get("revenus_pro", 0)),("Autres rentes", profil.get("autres_rentes", 0))]')
code.append("        _rtot = sum(v for _, v in _rev)")
code.append("        _rc = ''")
code.append("        for _n, _v in _rev:")
code.append("            _vc = '#4DFF99' if _v > 0 else '#665544'")
code.append('            _rc += f\'<div style="flex:1 1 calc(16% - 8px);min-width:85px;max-width:130px;background:#0A1E12;border:1px solid #1A6B4B;border-radius:8px;padding:6px 4px;text-align:center;"><div style="color:#BBA888;font-size:8px;text-transform:uppercase;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">{_n}</div><div style="color:{_vc};font-size:14px;font-weight:900;margin-top:2px;">{_v:,.0f}</div></div>\'')
code.append('        st.markdown(f\'<div style="margin:12px 0;"><div style="background:#0A1E12;border:2px solid #4DFF99;border-radius:10px;padding:10px;text-align:center;margin-bottom:4px;"><div style="color:#BBA888;font-size:9px;text-transform:uppercase;">REVENUS / MOIS</div><div style="color:#4DFF99;font-size:22px;font-weight:900;">{_rtot:,.0f} EUR</div></div><div style="display:flex;gap:5px;flex-wrap:wrap;justify-content:center;">{_rc}</div></div>\', unsafe_allow_html=True)')
code.append("")
code.append("        # === POCHES CAPITAL ===")
code.append('        _pch = [("AV1 Cardif", cap["av1"]),("AV2 Spirit", cap["av2"]),("AV3 Abeille", cap["av3"]),("AV4 Bourso", cap.get("av4", 0)),("Livret A", cap["livret_a"]),("LDDS", cap["ldds"]),("LEP", cap["lep"]),("PEA", cap.get("pea", 0)),("Crypto", cap.get("crypto", 0)),("Crowdf.", cap.get("crowdfunding", 0))]')
code.append("        _ptot = sum(v for _, v in _pch)")
code.append("        _pc = ''")
code.append("        for _n, _v in _pch:")
code.append("            _vc = '#FFD060' if _v > 0 else '#665544'")
code.append('            _pc += f\'<div style="flex:1 1 calc(10% - 5px);min-width:85px;max-width:120px;background:#1A0D12;border:1px solid #C4922A;border-radius:8px;padding:6px 4px;text-align:center;"><div style="color:#BBA888;font-size:8px;text-transform:uppercase;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">{_n}</div><div style="color:{_vc};font-size:14px;font-weight:900;margin-top:2px;">{_v:,.0f}</div></div>\'')
code.append('        st.markdown(f\'<div style="margin:8px 0 16px 0;"><div style="background:#1A0D12;border:2px solid #C4922A;border-radius:10px;padding:10px;text-align:center;margin-bottom:4px;"><div style="color:#BBA888;font-size:9px;text-transform:uppercase;">CAPITAL TOTAL</div><div style="color:#FFD060;font-size:22px;font-weight:900;">{_ptot:,.0f} EUR</div></div><div style="display:flex;gap:5px;flex-wrap:wrap;justify-content:center;">{_pc}</div></div>\', unsafe_allow_html=True)')
code.append("")

new = lines[:bl+1]
for c in code:
    new.append(c + "\n")
new.extend(lines[pl:])

with open("app.py", "w", encoding="utf-8") as f:
    f.writelines(new)
print(f"OK DEFINITIF - Revenus + Capital inseres proprement")
print(f"Backup dans: app_backup_definitive.py")
