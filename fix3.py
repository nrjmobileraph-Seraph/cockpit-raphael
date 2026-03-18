lines = open('app.py', 'r', encoding='utf-8').readlines()
out = []
for line in lines:
    if 'Montants' in line and 'venir' in line:
        continue
    out.append(line)
    if 'PLANCHER' in line and 'CIBLE' in line and 'BONUS' in line:
        new = '''        _left = [('AV1', cap['av1']), ('AV2', cap['av2']), ('AV3', cap['av3']), ('AV4', cap.get('av4', 0))]
        _right = [('Livret A', cap['livreta']), ('LDDS', cap['ldds']), ('LEP', cap['lep']), ('PEA', cap.get('pea', 0)), ('Crypto', cap.get('crypto', 0)), ('Crowdf.', cap.get('crowdfunding', 0))]
        _ltot = sum(v for _, v in _left)
        _rtot = sum(v for _, v in _right)
        _gtot = _ltot + _rtot
        _lhtml = ' <span style="color:#C4922A;">+</span> '.join(f'<span style="color:#FFD060;font-size:12px;font-weight:700;">{v:,.0f}</span>' for _, v in _left)
        _rhtml = ' <span style="color:#C4922A;">+</span> '.join(f'<span style="color:#FFD060;font-size:12px;font-weight:700;">{v:,.0f}</span>' for _, v in _right)
        st.markdown(f'<div style="background:#1A0D12;border:2px solid #C4922A;border-radius:10px;padding:12px 10px;margin:0 0 12px 0;display:flex;align-items:center;justify-content:center;flex-wrap:wrap;gap:6px;">{_lhtml} <span style="color:#C4922A;font-size:14px;">&#9654;</span> <span style="background:#2A1800;border:2px solid #FFD060;border-radius:8px;padding:6px 14px;color:#FFD060;font-size:16px;font-weight:900;">{_gtot:,.0f} \\u20ac</span> <span style="color:#C4922A;font-size:14px;">&#9664;</span> {_rhtml}</div>', unsafe_allow_html=True)
'''
        out.insert(-1, new)
open('app.py', 'w', encoding='utf-8').writelines(out)
print('OK cadre valeurs ajoute')
