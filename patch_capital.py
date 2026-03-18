import shutil

f = r"C:\Users\BoulePiou\cockpit-raphael\app.py"
shutil.copy2(f, f + ".bak3")
lines = open(f, "r", encoding="utf-8").readlines()

plancher_idx = None
for i, line in enumerate(lines):
    if "PLANCHER" in line and "CIBLE" in line and "BONUS" in line and "st.markdown" in line:
        plancher_idx = i
        break
plancher_line = lines[plancher_idx] if plancher_idx is not None else ""

cap_start = None
cap_render = None
for i, line in enumerate(lines):
    if "_cap_items" in line and "AV1 Cardif" in line:
        cap_start = i
    if cap_start is not None and i > cap_start and "_ch}</div>" in line and "st.markdown" in line:
        cap_render = i
        break

print(f"PLANCHER: ligne {plancher_idx+1 if plancher_idx is not None else None}")
print(f"Capital: lignes {cap_start+1 if cap_start is not None else None} a {cap_render+1 if cap_render is not None else None}")

if cap_start is None or cap_render is None:
    print("ERREUR: sections non trouvees")
    exit(1)

SP = "        "
new_cap_lines = []
new_cap_lines.append(SP + '# === POCHES CAPITAL : cartes + fleches + grand rectangle ===\n')
new_cap_lines.append(SP + '_cap_items = [("AV1 Cardif", cap["av1"]),("AV2 Spirit", cap["av2"]),("AV3 Abeille", cap["av3"]),("AV4 Bourso", cap.get("av4", 0)),("Livret A", cap["livret_a"]),("LDDS", cap["ldds"]),("LEP", cap["lep"]),("PEA", cap.get("pea", 0)),("Crypto", cap.get("crypto", 0)),("Crowdfunding", cap.get("crowdfunding", 0))]\n')
new_cap_lines.append(SP + '_cap_total = sum(v for _, v in _cap_items)\n')
new_cap_lines.append(SP + '_cards = ""\n')
new_cap_lines.append(SP + 'for _n, _v in _cap_items:\n')
new_cap_lines.append(SP + '    _vc = "#FFD060" if _v > 0 else "#665544"\n')
new_cap_lines.append(SP + '    _cards += f\'<div style="flex:1;min-width:85px;text-align:center;"><div style="background:#1A0D12;border:1px solid #C4922A;border-radius:8px;padding:6px 3px;"><span style="color:#BBA888;font-size:9px;">{_n}</span><br><span style="color:{_vc};font-size:13px;font-weight:bold;">{_v:,.0f} \\u20ac</span></div></div>\'\\n')
new_cap_lines.append(SP + 'st.markdown(f\'<div style="display:flex;gap:5px;align-items:flex-start;margin:0 0 0 0;flex-wrap:wrap;">{_cards}</div>\', unsafe_allow_html=True)\\n')
new_cap_lines.append(SP + '_arrows = ""\n')
new_cap_lines.append(SP + 'for _ in _cap_items:\n')
new_cap_lines.append(SP + '    _arrows += \'<div style="flex:1;min-width:85px;text-align:center;color:#C4922A;font-size:18px;line-height:1;">\\u25BC</div>\'\\n')
new_cap_lines.append(SP + 'st.markdown(f\'<div style="display:flex;gap:5px;margin:0;flex-wrap:wrap;">{_arrows}</div>\', unsafe_allow_html=True)\\n')
new_cap_lines.append(SP + '_mid = len(_cap_items) // 2\n')
new_cap_lines.append(SP + '_vals = ""\n')
new_cap_lines.append(SP + 'for _idx, (_n, _v) in enumerate(_cap_items):\n')
new_cap_lines.append(SP + '    _vc = "#FFD060" if _v > 0 else "#665544"\n')
new_cap_lines.append(SP + '    _vals += f\'<div style="flex:1;min-width:85px;text-align:center;"><span style="color:{_vc};font-size:12px;font-weight:bold;">{_v:,.0f}</span></div>\'\\n')
new_cap_lines.append(SP + '    if _idx == _mid - 1: _vals += f\'<div style="min-width:100px;text-align:center;background:#2A1800;border:2px solid #FFD060;border-radius:8px;padding:6px 10px;"><span style="color:#FFD060;font-size:10px;">TOTAL</span><br><span style="color:#FFD060;font-size:16px;font-weight:900;">{_cap_total:,.0f} \\u20ac</span></div>\'\\n')
new_cap_lines.append(SP + 'st.markdown(f\'<div style="background:#1A0D12;border:2px solid #C4922A;border-radius:10px;padding:10px 5px;margin:0 0 12px 0;display:flex;gap:5px;align-items:center;flex-wrap:wrap;">{_vals}</div>\', unsafe_allow_html=True)\\n')
new_cap_lines.append("\n")

new_lines = []
for i in range(plancher_idx):
    new_lines.append(lines[i])
# Skip plancher line
for i in range(plancher_idx + 1, cap_start):
    new_lines.append(lines[i])
# Insert new capital section
for nl in new_cap_lines:
    new_lines.append(nl)
# Insert PLANCHER after capital
if plancher_line:
    new_lines.append(plancher_line)
# Rest of file
for i in range(cap_render + 1, len(lines)):
    new_lines.append(lines[i])

open(f, "w", encoding="utf-8").writelines(new_lines)
print("OK - Capital refait + PLANCHER deplace en dessous!")
