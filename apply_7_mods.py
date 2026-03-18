# The file is too large to recreate character-by-character in the sandbox.
# Instead, I'll create a patch script that Raphaël can run locally.
# This is the most reliable approach.

cat > /tmp/apply_7_mods.py << 'PYTHON_SCRIPT'
#!/usr/bin/env python3
"""
apply_7_mods.py — Applique les 7 modifications sur app_cockpit_v49.py
Usage: python apply_7_mods.py
Produit: app_cockpit_v50.py dans le même dossier
"""
import os, sys

# Chercher le fichier source
src = None
for candidate in ['app_cockpit_v49.py', os.path.expanduser(r'~\cockpit-raphael\app_cockpit_v49.py'), 
                   r'C:\Users\BoulePiou\cockpit-raphael\app_cockpit_v49.py']:
    if os.path.exists(candidate):
        src = candidate
        break

if not src:
    print("ERREUR: app_cockpit_v49.py introuvable!")
    print("Placez ce script dans C:\\Users\\BoulePiou\\cockpit-raphael\\ et relancez")
    sys.exit(1)

with open(src, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"Fichier source: {src} ({len(content)} caractères)")
mods = 0

# ═══════════════════════════════════════════════════════════
# MOD 1: Résultat ARVA → HTML table propre
# ═══════════════════════════════════════════════════════════
OLD = '''        titre("Résultat")
        st.code(f"W_opt = {W2:,.2f} €/mois\\nRail  = {rail:,.0f} €/mois\\nÉcart = {W2-rail:+.0f} €\\n\\nFormule:\\nW = Capital × r_m / [1−(1+r_m)^(−n)]\\nr_m = {r_m*100:.5f}%\\nn   = {int(mois_s)} mois",language="")'''

NEW = '''        titre("Résultat")
        ecart_col = "#4DFF99" if W2 >= rail else "#FF7777"
        st.markdown(f\'\'\'<div style="background:#1A0D12;border:1px solid #C4922A;border-radius:10px;padding:16px;font-size:14px;">
<table style="width:100%;border-collapse:collapse;">
<tr><td style="color:#BBA888;padding:6px 0;">W_opt</td><td style="color:#4DFF99;font-weight:800;text-align:right;padding:6px 0;">{W2:,.2f} EUR/mois</td></tr>
<tr><td style="color:#BBA888;padding:6px 0;">Rail</td><td style="color:#FFD060;font-weight:700;text-align:right;padding:6px 0;">{rail:,.0f} EUR/mois</td></tr>
<tr style="border-top:1px solid #333;"><td style="color:#BBA888;padding:6px 0;">Ecart</td><td style="color:{ecart_col};font-weight:800;text-align:right;padding:6px 0;">{W2-rail:+.0f} EUR</td></tr>
</table>
<div style="border-top:1px solid #2A0A12;margin:10px 0;"></div>
<div style="color:#BBA888;font-size:12px;">W = Capital x r_m / [1-(1+r_m)^(-n)]</div>
<div style="color:#BBA888;font-size:12px;">r_m = {r_m*100:.5f}% | n = {int(mois_s)} mois</div>
</div>\'\'\', unsafe_allow_html=True)'''

if OLD in content:
    content = content.replace(OLD, NEW)
    mods += 1; print("MOD 1: Résultat ARVA → HTML table ✅")
else:
    print("MOD 1: ❌ PATTERN NON TROUVÉ")

# ═══════════════════════════════════════════════════════════
# MOD 2: Sensibilité → HTML table couleurs
# ═══════════════════════════════════════════════════════════
OLD2 = """    titre("Sensibilité au rendement")
    rows=[]
    for rt in [2.5,2.8,3.0,3.2,3.5,3.8,4.0]:
        wt=arva(cap_s,int(mois_s),rt/100,cible_s)
        rows.append(f"| {rt:.1f}% | **{wt:,.0f} €** | {wt-rail:+.0f} € | {'✅' if wt>=rail else '⚠️'} |")
    st.markdown("| Rendement | Pioche ARVA | Écart rail | Statut |\\n|---|---|---|---|\\n"+"\\n".join(rows))"""

NEW2 = '''    titre("Sensibilité au <u>rendement</u>")
    rend_actuel = rend_s
    sens_html = '<div style="background:#1A0D12;border-radius:10px;padding:16px;margin:8px 0;overflow-x:auto;"><table style="width:100%;border-collapse:collapse;font-size:13px;">'
    sens_html += '<tr><th style="text-align:left;padding:8px;color:#BBA888;border-bottom:1px solid #C4922A;">Rendement</th><th style="text-align:right;padding:8px;color:#BBA888;border-bottom:1px solid #C4922A;">Pioche ARVA</th><th style="text-align:right;padding:8px;color:#BBA888;border-bottom:1px solid #C4922A;">Ecart rail</th><th style="text-align:center;padding:8px;color:#BBA888;border-bottom:1px solid #C4922A;">Statut</th></tr>'
    for rt in [2.5,2.8,3.0,3.2,3.5,3.8,4.0]:
        wt=arva(cap_s,int(mois_s),rt/100,cible_s)
        ecart_rt = wt - rail
        col_w = "#4DFF99" if ecart_rt >= 0 else ("#FFD060" if ecart_rt > -200 else "#FF7777")
        statut_rt = "OK" if wt >= rail else "ALERTE"
        statut_col = "#4DFF99" if wt >= rail else "#FF7777"
        is_current = abs(rt - rend_actuel) < 0.05
        bg_row = "background:rgba(196,146,42,0.15);" if is_current else ""
        marker = " ◄" if is_current else ""
        sens_html += f'<tr style="border-bottom:1px solid #1A1A1A;{bg_row}"><td style="padding:6px 8px;color:#F0E6D8;font-weight:{"700" if is_current else "400"};">{rt:.1f}%{marker}</td><td style="text-align:right;padding:6px 8px;color:{col_w};font-weight:700;">{wt:,.0f} EUR</td><td style="text-align:right;padding:6px 8px;color:{col_w};">{ecart_rt:+,.0f} EUR</td><td style="text-align:center;padding:6px 8px;color:{statut_col};font-weight:700;">{statut_rt}</td></tr>'
    sens_html += '</table></div>'
    st.markdown(sens_html, unsafe_allow_html=True)'''

if OLD2 in content:
    content = content.replace(OLD2, NEW2)
    mods += 1; print("MOD 2: Sensibilité → HTML table ✅")
else:
    print("MOD 2: ❌ PATTERN NON TROUVÉ")

# ═══════════════════════════════════════════════════════════
# MOD 3: Navigation header bigger
# ═══════════════════════════════════════════════════════════
OLD3 = '        page=st.radio("Navigation",['
NEW3 = '''        st.markdown('<div style="color:#FFD060;font-size:20px;font-weight:900;letter-spacing:3px;margin-bottom:8px;text-transform:uppercase;">NAVIGATION</div>', unsafe_allow_html=True)
        page=st.radio("\\u200b",['''

if OLD3 in content:
    content = content.replace(OLD3, NEW3)
    mods += 1; print("MOD 3: Navigation header ✅")
else:
    print("MOD 3: ❌ PATTERN NON TROUVÉ")

# ═══════════════════════════════════════════════════════════
# MOD 4: ARVA renamed
# ═══════════════════════════════════════════════════════════
OLD4 = '"Moteur ARVA (Rente)"'
NEW4 = '"ARVA (Rente Vie Autonome)"'
n = content.count(OLD4)
if n > 0:
    content = content.replace(OLD4, NEW4)
    mods += 1; print(f"MOD 4: ARVA renamed ({n}x) ✅")
else:
    print("MOD 4: ❌ PATTERN NON TROUVÉ")

# ═══════════════════════════════════════════════════════════
# MOD 5: Simulator tabs renamed + PCH info
# ═══════════════════════════════════════════════════════════
OLD5 = '    t1,t2,t3,t4,t5,t6=st.tabs(["Base","MDPH+PCH","Seq. Returns","EHPAD+APA","Rendement","Comparaison"])'
NEW5 = '    t1,t2,t3,t4,t5,t6=st.tabs(["Plan de base","Avec aide MDPH+PCH","Seq. Returns","EHPAD+APA","Rendement","Comparaison"])'
if OLD5 in content:
    content = content.replace(OLD5, NEW5)
    mods += 1; print("MOD 5: Tabs renamed ✅")
else:
    print("MOD 5: ❌ PATTERN NON TROUVÉ")

OLD5b = '        pch=st.slider("PCH (€/mois)",0,1500,500,50)'
NEW5b = '''        pch=st.slider("PCH (€/mois)",0,1500,500,50)
        st.info("**PCH** = Prestation de Compensation du Handicap, versée par le département (MDPH). Montant selon le plan d\\'aide personnalisé. Non imposable.")'''
if OLD5b in content:
    content = content.replace(OLD5b, NEW5b, 1)
    print("MOD 5b: PCH info box ✅")
else:
    print("MOD 5b: ❌ PCH slider non trouvé")

# ═══════════════════════════════════════════════════════════
# MOD 6: Stratégies non retenues → expander
# ═══════════════════════════════════════════════════════════
OLD6 = '    titre("3. Placements NON retenus (19)")\n    non_retenus = ['
NEW6 = '    with st.expander("3. Placements NON retenus (19) — cliquer pour voir", expanded=False):\n        non_retenus = ['
OLD6b = '    for p in non_retenus:\n        st.markdown(f"- {p}")\n    titre("4'
NEW6b = '        for p in non_retenus:\n            st.markdown(f"- {p}")\n    titre("4'

if OLD6 in content:
    content = content.replace(OLD6, NEW6, 1)
    if OLD6b in content:
        content = content.replace(OLD6b, NEW6b, 1)
    mods += 1; print("MOD 6: Non retenus → expander ✅")
else:
    print("MOD 6: ❌ PATTERN NON TROUVÉ")

# ═══════════════════════════════════════════════════════════
# MOD 7: Ajustement manuel cash (Phase 3 dashboard)
# ═══════════════════════════════════════════════════════════
OLD7 = '''        cc_border = "#CC3333" if cc_val < 1000 else ("#D4A017" if cc_val < manque*2 else "#1A6B4B")
        st.markdown(f\'<div style="background:linear-gradient(145deg, #1A0D12 0%, #150A10 100%);border:2px solid {cc_border};border-radius:12px;padding:20px;text-align:center;margin-bottom:16px;"><div style="color:#BBA888;font-size:12px;text-transform:uppercase;letter-spacing:1px;">COMPTE COURANT</div><div style="color:#4DFF99;font-size:42px;font-weight:900;margin:8px 0;">{cc_val:,.0f} EUR</div><div style="color:#FFD060;font-size:14px;font-weight:600;">Alimente ce mois-ci de {manque:,.0f} EUR</div></div>\', unsafe_allow_html=True)'''

NEW7 = '''        # Ajustement manuel cash (concept Gemini)
        if 'ajustement_cash' not in st.session_state:
            st.session_state.ajustement_cash = 0.0
        cc_effectif = cc_val + st.session_state.ajustement_cash
        cc_border = "#CC3333" if cc_effectif < 1000 else ("#D4A017" if cc_effectif < manque*2 else "#1A6B4B")
        adj_c1, adj_c2, adj_c3 = st.columns(3)
        with adj_c1:
            st.markdown(f\'<div style="background:#1A0D12;border:1px solid #333;border-radius:8px;padding:10px;text-align:center;"><div style="color:#BBA888;font-size:10px;">SOLDE FINARY</div><div style="color:#CCBBAA;font-size:20px;font-weight:700;">{cc_val:,.0f} EUR</div></div>\', unsafe_allow_html=True)
        with adj_c2:
            new_adj = st.number_input("Ajustement (+/-)", value=float(st.session_state.ajustement_cash), step=50.0, key="adj_cash_input")
            if new_adj != st.session_state.ajustement_cash:
                st.session_state.ajustement_cash = new_adj
                st.rerun()
        with adj_c3:
            st.markdown(f\'<div style="background:#1A0D12;border:2px solid {cc_border};border-radius:8px;padding:10px;text-align:center;"><div style="color:#BBA888;font-size:10px;">CASH EFFECTIF</div><div style="color:#4DFF99;font-size:20px;font-weight:900;">{cc_effectif:,.0f} EUR</div></div>\', unsafe_allow_html=True)
        st.markdown(f\'<div style="background:linear-gradient(145deg, #1A0D12 0%, #150A10 100%);border:2px solid {cc_border};border-radius:12px;padding:20px;text-align:center;margin-bottom:16px;"><div style="color:#BBA888;font-size:12px;text-transform:uppercase;letter-spacing:1px;">COMPTE COURANT</div><div style="color:#4DFF99;font-size:42px;font-weight:900;margin:8px 0;">{cc_effectif:,.0f} EUR</div><div style="color:#FFD060;font-size:14px;font-weight:600;">Alimente ce mois-ci de {manque:,.0f} EUR</div></div>\', unsafe_allow_html=True)'''

if OLD7 in content:
    content = content.replace(OLD7, NEW7)
    mods += 1; print("MOD 7: Ajustement manuel cash ✅")
else:
    print("MOD 7: ❌ PATTERN NON TROUVÉ")

# ═══════════════════════════════════════════════════════════
# Version update
# ═══════════════════════════════════════════════════════════
content = content.replace('# v4.7.7', '# v5.0 — 7 modifications applied')
content = content.replace('v4.9 - Mars 2026', 'v5.0 - Mars 2026')
content = content.replace('v4.9 &mdash; Raphael', 'v5.0 &mdash; Raphael')

# Write output
out = os.path.join(os.path.dirname(src), 'app_cockpit_v50.py')
with open(out, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n{'='*50}")
print(f"RÉSULTAT: {mods}/7 modifications appliquées")
print(f"Fichier créé: {out}")
print(f"Taille: {len(content)} caractères")
print(f"\nPour lancer: streamlit run app_cockpit_v50.py")
PYTHON_SCRIPT

echo "Script créé: /tmp/apply_7_mods.py"
wc -l /tmp/apply_7_mods.py
