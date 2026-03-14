with open('C:/Users/BoulePiou/cockpit-raphael/app.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Trouver le debut de page_dashboard et ajouter budget jour/mois en haut
old = '    titre("COCKPIT PATRIMONIAL - PHASE CONSTRUCTION")'
new = '''    import calendar
    today = date.today()
    jours_dans_mois = calendar.monthrange(today.year, today.month)[1]
    jour_actuel = today.day
    budget_mois = profil['rail_mensuel']
    budget_jour = int(budget_mois / jours_dans_mois)
    depense_estimee = budget_jour * (jour_actuel - 1)
    reste_mois = int(budget_mois - depense_estimee)
    st.markdown(f'<div style="display:flex;gap:16px;margin-bottom:16px;"><div style="flex:1;background:#1A0D12;border:2px solid #4DFF99;border-radius:12px;padding:16px;text-align:center;"><div style="color:#BBA888;font-size:11px;text-transform:uppercase;">BUDGET AUJOURD HUI</div><div style="color:#4DFF99;font-size:36px;font-weight:900;">{budget_jour} EUR</div><div style="color:#CCBBAA;font-size:12px;">par jour ce mois</div></div><div style="flex:1;background:#1A0D12;border:2px solid #FFD060;border-radius:12px;padding:16px;text-align:center;"><div style="color:#BBA888;font-size:11px;text-transform:uppercase;">RESTE CE MOIS</div><div style="color:#FFD060;font-size:36px;font-weight:900;">{reste_mois} EUR</div><div style="color:#CCBBAA;font-size:12px;">sur {jours_dans_mois - jour_actuel + 1} jours restants</div></div></div>', unsafe_allow_html=True)
    titre("COCKPIT PATRIMONIAL - PHASE CONSTRUCTION")'''
code = code.replace(old, new)

with open('C:/Users/BoulePiou/cockpit-raphael/app.py', 'w', encoding='utf-8') as f:
    f.write(code)

import ast
ast.parse(code)
print('SUCCES')
