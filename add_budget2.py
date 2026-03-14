with open('C:/Users/BoulePiou/cockpit-raphael/app.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Trouver la ligne "titre("COCKPIT PATRIMONIAL - PHASE CONSTRUCTION")"
insert_at = None
for i, line in enumerate(lines):
    if 'COCKPIT PATRIMONIAL - PHASE CONSTRUCTION' in line:
        insert_at = i
        break

if insert_at:
    budget_code = [
        '    import calendar\n',
        '    _today = date.today()\n',
        '    _jdm = calendar.monthrange(_today.year, _today.month)[1]\n',
        '    _bj = int(profil["rail_mensuel"] / _jdm)\n',
        '    _rm = int(profil["rail_mensuel"] - _bj * (_today.day - 1))\n',
        '    _jr = _jdm - _today.day + 1\n',
        "    st.markdown(f'<div style=\"display:flex;gap:16px;margin-bottom:16px;\"><div style=\"flex:1;background:#1A0D12;border:2px solid #4DFF99;border-radius:12px;padding:16px;text-align:center;\"><div style=\"color:#BBA888;font-size:11px;\">BUDGET AUJOURD HUI</div><div style=\"color:#4DFF99;font-size:36px;font-weight:900;\">{_bj} EUR</div><div style=\"color:#CCBBAA;font-size:12px;\">par jour</div></div><div style=\"flex:1;background:#1A0D12;border:2px solid #FFD060;border-radius:12px;padding:16px;text-align:center;\"><div style=\"color:#BBA888;font-size:11px;\">RESTE CE MOIS</div><div style=\"color:#FFD060;font-size:36px;font-weight:900;\">{_rm} EUR</div><div style=\"color:#CCBBAA;font-size:12px;\">sur {_jr} jours</div></div></div>', unsafe_allow_html=True)\n",
    ]
    for j, bl in enumerate(budget_code):
        lines.insert(insert_at + j, bl)
    print(f'Insere a la ligne {insert_at}')

with open('C:/Users/BoulePiou/cockpit-raphael/app.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)

import ast
with open('C:/Users/BoulePiou/cockpit-raphael/app.py', 'r', encoding='utf-8') as f:
    ast.parse(f.read())
print('SUCCES')
