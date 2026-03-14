"""
COCKPIT PATRIMONIAL — RAPHAËL
Sprint 1+2 : Dashboard corrigé + Suivi AV + Impôts + Surplus automatique
"""

import streamlit as st
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import db_wrapper
import math
from datetime import date, datetime
from pathlib import Path

st.set_page_config(
    page_title="Cockpit Patrimonial — Raphaël",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Header natif Streamlit (bouton sidebar visible)

st.markdown("""<style>
[data-testid="collapsedControl"] { display: none !important; }
header[data-testid="stHeader"] { background: #0A0508 !important; border: none !important; }
.stButton button, div.stButton > button, [data-testid="baseButton-secondary"], [data-testid="baseButton-primary"] {
    background-color: #2A0A12 !important; color: #FFD060 !important; border: 2px solid #C4922A !important;
    font-weight: 800 !important; border-radius: 8px !important; transition: all 0.3s !important;
}
.stButton button:hover, div.stButton > button:hover {
    background-color: #3A0A15 !important; color: #FFFFFF !important; border: 2px solid #FFD060 !important;
    box-shadow: 0 0 25px rgba(196,146,42,0.8) !important;
}
.stException {display:none !important}
[data-testid="stAppViewContainer"] { background: #0A0508 !important; }
[data-testid="stApp"] { background: #0A0508 !important; }
.main .block-container { background: #0A0508 !important; }
.main { background: #0A0508 !important; }
.stApp { background: #0A0508 !important; }
section.main > div { background: #0A0508 !important; }
[data-testid="stSidebar"] { background: linear-gradient(180deg, #2A0810 0%, #1E0610 50%, #150510 100%) !important; color:#FFFFFF; border-right: 1px solid rgba(196,146,42,0.3) !important; border-radius: 0 16px 16px 0 !important; }
[data-testid="stSidebar"] * { color: #F0E6D8 !important; }
[data-testid="stSidebar"] .stRadio label { padding: 6px 12px !important; border-radius: 8px !important; margin: 2px 0 !important; transition: all 0.2s ease !important; }
[data-testid="stSidebar"] .stRadio label:hover { background: rgba(196,146,42,0.2) !important; padding-left: 16px !important; }
[data-testid="stSidebar"] .stRadio label span { color: #E8D5B5 !important; font-size: 14px !important; font-weight: 500 !important; }
.kpi { background:linear-gradient(145deg, #1A0D12 0%, #150A10 100%); border-radius:12px; padding:18px 20px; border-left:4px solid #C4922A; margin-bottom:6px; }
.kpi.vert  { border-left-color:#1A6B4B; }
.kpi.orange{ border-left-color:#D4A017; }
.kpi.rouge { border-left-color:#CC3333; }
.kpi.bleu  { border-left-color:#C4922A; }
.kpi-label { font-size:11px; color:#BBA888; text-transform:uppercase; letter-spacing:1px; margin-bottom:2px; }
.kpi-val   { font-size:26px; font-weight:800; color:#FFF; line-height:1.1; }
.kpi-sub   { font-size:12px; color:#CCBBAA; margin-top:3px; }
.alerte-r  { background:#2A0F0F; border:1px solid #CC3333; border-radius:8px; padding:10px 14px; color:#FF7777; margin:4px 0; font-size:13px; }
.alerte-o  { background:#2A1E0A; border:1px solid #D4A017; border-radius:8px; padding:10px 14px; color:#FFD060; margin:4px 0; font-size:13px; }
.alerte-v  { background:#0A1E12; border:1px solid #1A6B4B; border-radius:8px; padding:10px 14px; color:#4DFF99; margin:4px 0; font-size:13px; }
.box       { background:linear-gradient(145deg, #1A0D12 0%, #150A10 100%); border-radius:10px; padding:16px 20px; margin:8px 0; }
.titre     { font-size:16px; font-weight:700; color:#FFD4A0; border-bottom:1px solid #2A0A12; padding-bottom:6px; margin:18px 0 10px 0; }
.poche-row { display:flex; align-items:center; gap:10px; padding:6px 0; border-bottom:1px solid #1A2030; }
.badge     { border-radius:50%; width:26px; height:26px; display:flex; align-items:center; justify-content:center; font-size:11px; font-weight:800; flex-shrink:0; }
.av-card   { background:linear-gradient(145deg, #1A0D12 0%, #150A10 100%); border-radius:10px; padding:14px 18px; border-top:3px solid #C4922A; margin-bottom:8px; }
.av-card.danger { border-top-color:#CC3333; }
.av-card.warn   { border-top-color:#D4A017; }
.av-card.ok     { border-top-color:#1A6B4B; }
.surplus-box { background:#0A2010; border:2px solid #1A6B4B; border-radius:10px; padding:16px 20px; margin:12px 0; }
.kpi { transition: transform 0.2s ease, box-shadow 0.3s ease; }
.kpi:hover { transform: translateY(-4px) scale(1.01); box-shadow: 0 8px 25px rgba(196,146,42,0.5); }
* { color-scheme: dark; }
body, p, span, div, li, td, th, label, input, textarea, select { color: #F0E6D8 !important; }
.alerte-r, .alerte-r * { color: #FF7777 !important; }
.alerte-o, .alerte-o * { color: #FFD060 !important; }
.alerte-v, .alerte-v * { color: #4DFF99 !important; }
input, textarea, select { background: #1A1015 !important; border-color: #4A2020 !important; }
div[data-testid="stDecoration"] { display: none !important; }
#MainMenu { visibility: hidden !important; }
footer { visibility: hidden !important; }
div[data-testid="stToolbar"] { display: none !important; }
section[data-testid="stSidebar"] { background: linear-gradient(180deg, #2A0810 0%, #1E0610 50%, #150510 100%) !important; }
section[data-testid="stSidebar"] * { color: #F0E6D8 !important; }
header[data-testid="stHeader"] { background: #0A0508 !important; border: none !important; }
</style>""", unsafe_allow_html=True)

def init_db():
    pass

def get_profil():
    conn = db_wrapper.connect()
    c = conn.cursor()
    row = c.execute("SELECT * FROM profil WHERE id=1").fetchone()
    cols = [d[0] for d in c.description]
    conn.close()
    return dict(zip(cols, row)) if row else {}

def get_capital():
    conn = db_wrapper.connect()
    c = conn.cursor()
    row = c.execute("SELECT * FROM capital ORDER BY id DESC LIMIT 1").fetchone()
    cols = [d[0] for d in c.description]
    conn.close()
    return dict(zip(cols, row)) if row else {}

def save_capital(d):
    conn = db_wrapper.connect()
    c = conn.cursor()
    c.execute("""INSERT INTO capital
        (date,cc,livret_a,ldds,lep,av1,av2,av3,
         av1_date_ouverture,av2_date_ouverture,av3_date_ouverture,
         av1_versements,av2_versements,av3_versements,
         av1_rendement,av2_rendement,av3_rendement,note)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
        (date.today().isoformat(),
         d['cc'],d['livret_a'],d['ldds'],d['lep'],
         d['av1'],d['av2'],d['av3'],
         d['av1_do'],d['av2_do'],d['av3_do'],
         d['av1_v'],d['av2_v'],d['av3_v'],
         d['av1_r'],d['av2_r'],d['av3_r'],d.get('note','')))
    conn.commit()
    conn.close()

def save_profil(d):
    conn = db_wrapper.connect()
    c = conn.cursor()
    c.execute("""UPDATE profil SET aah_mensuel=?,pch_mensuel=?,loyer_net=?,
        taux_mdph=?,rendement_annuel=?,rail_mensuel=?,updated=CURRENT_TIMESTAMP
        WHERE id=1""",
        (d['aah'],d['pch'],d['loyer'],d['mdph'],d['rendement']/100,d['rail']))
    conn.commit()
    conn.close()

def save_surplus(montant, destination, note):
    conn = db_wrapper.connect()
    c = conn.cursor()
    c.execute("INSERT INTO surplus_affectation (montant,destination,note) VALUES (?,?,?)",
              (montant, destination, note))
    conn.commit()
    conn.close()

def get_historique_surplus():
    conn = db_wrapper.connect()
    c = conn.cursor()
    rows = c.execute("SELECT date,montant,destination,note FROM surplus_affectation ORDER BY id DESC LIMIT 10").fetchall()
    conn.close()
    return rows

def age_actuel(profil):
    dn = datetime.strptime(profil['date_naissance'], '%Y-%m-%d')
    return (datetime.today() - dn).days / 365.25

def mois_restants(profil):
    dn = datetime.strptime(profil['date_naissance'], '%Y-%m-%d')
    jours = (datetime.today() - dn).days
    return max(0, int((profil['age_cible'] * 365.25 - jours) / 30.44))

def capital_total(cap):
    return sum(cap[k] for k in ['cc','livret_a','ldds','lep','av1','av2','av3'])

def arva(capital, mois, rendement, cible=50000):
    if mois <= 0: return 0.0
    r_m = (1 + rendement) ** (1/12) - 1
    if r_m == 0: return max(0,(capital - cible) / mois)
    facteur = (1 + r_m) ** mois
    annuite = (facteur - 1) / r_m
    return round(max(0, (capital * facteur - cible) / annuite), 2)

def rendement_pondere(cap):
    taux = {'cc':0.0,'livret_a':0.024,'ldds':0.024,'lep':0.035,'av1':0.035,'av2':0.035,'av3':0.035}
    tot = capital_total(cap)
    if tot == 0: return 0
    return sum(cap[k] * taux[k] for k in taux) / tot

def trajectoire_theorique(profil, age):
    C0, r = 393192.0, profil['rendement_annuel']
    rail = profil['rail_mensuel']
    aah = profil['aah_mensuel'] + profil.get('pch_mensuel', 0)
    loyer = profil['loyer_net']
    r_m = (1 + r) ** (1/12) - 1
    def A(n): return ((1+r)**n - 1) / r_m if r_m > 0 else n
    def P(n): return (1+r)**n
    pioche_p1 = rail - aah - loyer
    if age <= 64:
        n = age - 50
        return C0 * P(n) - pioche_p1 * A(n)
    else:
        immo = 205000 * (1.015**14)
        C64 = C0 * P(14) - pioche_p1 * A(14) + immo
        return C64 * P(age-64) - rail * A(age-64)

def pv_latentes(cap, av):
    return max(0, cap[av] - cap[f'{av}_versements'])

def abattement_dispo(cap, av):
    try:
        do = datetime.strptime(cap[f'{av}_date_ouverture'], '%Y-%m-%d')
        return 4600.0 if (datetime.today()-do).days/365.25 >= 8 else 0.0
    except: return 0.0

def rachat_max_sans_ir(cap, av):
    val = cap[av]; vers = cap[f'{av}_versements']
    pv = max(0, val - vers)
    if pv == 0: return val
    ab = abattement_dispo(cap, av)
    if ab == 0: return 0.0
    taux = pv / val
    return round(ab / taux, 2) if taux > 0 else val

def phase(age):
    if age < 64: return 1, "Phase 1 — AAH + Loyer + Pioche"
    elif age < 75: return 2, "Phase 2 — Pioche AV seule"
    else: return 3, "Phase 3 — Pioche AV + RVD"

def pioche_ce_mois(profil, cap):
    age = age_actuel(profil)
    rail = profil['rail_mensuel']
    aah = profil['aah_mensuel'] + profil.get('pch_mensuel',0)
    loyer = profil['loyer_net']
    ph, _ = phase(age)
    if ph == 1:
        pioche = rail - aah - loyer
        src = "Livret A" if cap['livret_a'] > pioche*3 else "AV1"
    elif ph == 2:
        pioche = rail
        src = "AV1"
    else:
        pioche = rail - profil.get('rvd_mensuel',450)
        src = "AV1"
    return pioche, src

def calculer_alertes(profil, cap):
    alertes = []
    age = age_actuel(profil)
    mois = mois_restants(profil)
    C = capital_total(cap)
    traj = trajectoire_theorique(profil, age)
    W = arva(C, mois, profil['rendement_annuel'])
    rail = profil['rail_mensuel']
    if traj > 0:
        ecart = (C - traj) / traj * 100
        if ecart < -10: alertes.append(('rouge', f'🔴 Capital inférieur de {abs(ecart):.1f}% à la trajectoire. Réduire la pioche immédiatement.'))
        elif ecart < -5: alertes.append(('orange', f'⚠️ Capital inférieur de {abs(ecart):.1f}% à la trajectoire. Surveiller.'))
        elif ecart > 15: alertes.append(('vert', f'✅ Capital supérieur de {ecart:.1f}% à la trajectoire. Surplus disponible.'))
    buffer = cap['livret_a'] + cap['ldds']
    if buffer > 20000:
        alertes.append(('orange', f'⚠️ Buffer livrets {buffer:,.0f}€ > 16 560€ cible. Réinjecter {buffer-16560:,.0f}€ en AV1.'))
    rp = rendement_pondere(cap)
    if rp < 0.033:
        alertes.append(('rouge', f'🔴 Rendement pondéré {rp*100:.2f}% trop bas. Réduire le buffer livrets.'))
    for av in ['av1','av2','av3']:
        r = cap.get(f'{av}_rendement', 0.035)
        if r < 0.025: alertes.append(('rouge', f'🔴 {av.upper()} rendement {r*100:.1f}% critique. Contacter assureur.'))
        elif r < 0.028: alertes.append(('orange', f'⚠️ {av.upper()} rendement {r*100:.1f}% < 2,8%. Surveiller.'))
    if age >= 74:
        swr = (rail*12)/C*100
        if swr > 9: alertes.append(('rouge', f'🔴 SWR Phase 3 = {swr:.1f}% > 9%. Souscrire RVD immédiatement.'))
    if age < 60:
        ans = 60 - age
        if ans < 2: alertes.append(('rouge', f'🔴 MDPH : {ans:.1f} ans avant 60 ans. Dépôt dossier URGENT.'))
        elif ans < 3: alertes.append(('orange', f'⚠️ MDPH : {ans:.1f} ans avant la deadline.'))
    if cap['cc'] < 1000:
        alertes.append(('orange', f'⚠️ CC bas ({cap["cc"]:,.0f}€). Renflouer depuis Livret A.'))
    if not alertes:
        alertes.append(('vert', '✅ Aucune alerte. Trajectoire nominale.'))
    return alertes

def kpi(label, val, sub="", couleur="bleu"):
    st.markdown(f'<div class="kpi {couleur}"><div class="kpi-label">{label}</div><div class="kpi-val">{val}</div><div class="kpi-sub">{sub}</div></div>', unsafe_allow_html=True)

def alerte(niveau, msg):
    cls = {'rouge':'alerte-r','orange':'alerte-o','vert':'alerte-v'}.get(niveau,'alerte-o')
    st.markdown(f'<div class="{cls}">{msg}</div>', unsafe_allow_html=True)

def titre(t):
    st.markdown(f'<div class="titre">{t}</div>', unsafe_allow_html=True)

def graphe(pts):
    try:
        import plotly.graph_objects as go
        ages = list(pts.keys())
        vals = [max(v,-50000) for v in pts.values()]
        cols = ['#1A6B4B' if v>=50000 else '#CC3333' for v in pts.values()]
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=ages,y=vals,mode='lines+markers',
            line=dict(color='#C4922A',width=2),marker=dict(color=cols,size=8),
            text=[f"{v:,.0f}€" for v in pts.values()],
            hovertemplate='%{x} ans : %{text}<extra></extra>'))
        fig.add_hline(y=50000,line_dash="dash",line_color="#D4A017",annotation_text="Cible 50k€")
        fig.add_hline(y=0,line_dash="dot",line_color="#CC3333")
        fig.update_layout(plot_bgcolor='#140810',paper_bgcolor='#140810',
            font_color='#CCC',height=270,margin=dict(t=20,b=0,l=0,r=0),
            xaxis=dict(gridcolor='#2A0A12'),yaxis=dict(gridcolor='#2A0A12'))
        st.plotly_chart(fig, use_container_width=True)
    except: pass

def page_dashboard(profil, cap):
    age = age_actuel(profil)
    mois = mois_restants(profil)
    C = capital_total(cap)
    W = arva(C, mois, profil['rendement_annuel'])
    traj = trajectoire_theorique(profil, age)
    rp = rendement_pondere(cap)
    ph_num, ph_label = phase(age)
    pioche, src = pioche_ce_mois(profil, cap)
    rail = profil['rail_mensuel']
    ecart_traj = (C-traj)/traj*100 if traj>0 else 0
    ecart_arva = W - rail

    bg = {'1':'#1A0D12','2':'#2A1800','3':'#200A0A'}.get(str(ph_num),'#1A0D12')
    st.markdown(f'<div style="background:{bg};border-radius:8px;padding:10px 16px;margin-bottom:14px;font-size:14px;color:#DDD;">📍 {ph_label} · {age:.1f} ans · {mois} mois jusqu\'à 92 ans</div>', unsafe_allow_html=True)

    # ── BLOC FLUX MENSUEL COMPLET ──
    cc_val = cap['cc']
    aah_m = profil['aah_mensuel']
    pch_m = profil.get('pch_mensuel', 0)
    loyer_m = profil['loyer_net']
    rvd_m = profil.get('rvd_mensuel', 0) if ph_num == 3 else 0
    entrees_auto = aah_m + pch_m + loyer_m + rvd_m
    manque = rail - entrees_auto  # ce qu'il faut piocher en capital
    cc_apres = cc_val - manque  # CC prévu fin de mois si on ne renfloue pas
    besoin_virement = max(0, manque) if cc_val < manque * 2 else 0  # virement depuis livret si CC trop bas

    cc_border = "#CC3333" if cc_val < 1000 else ("#D4A017" if cc_val < manque*2 else "#1A6B4B")

    # Build HTML without indentation (Streamlit treats 4+ spaces as code block)
    pch_line = f"<br>PCH : +{int(pch_m)}€" if pch_m > 0 else ""
    loyer_line = f"<br>Loyer LMNP : +{int(loyer_m)}€" if loyer_m > 0 else ""
    rvd_line = f"<br>RVD : +{int(rvd_m)}€" if rvd_m > 0 else ""
    cc_msg = "CC suffisant" if cc_val >= manque*2 else f"Virer {int(besoin_virement+manque)}€ depuis Livret A"
    flux_html = f'<div style="background:#1A0D12;border-radius:14px;padding:20px 24px;border:2px solid {cc_border};margin-bottom:14px;">'
    flux_html += '<div style="color:#BBA888;font-size:12px;text-transform:uppercase;letter-spacing:1px;margin-bottom:14px;">FLUX MENSUEL COMPLET — CE MOIS</div>'
    flux_html += '<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px;">'
    flux_html += f'<div style="background:#150A10;border-radius:10px;padding:14px;"><div style="color:#BBA888;font-size:11px;margin-bottom:6px;">ENTREES AUTOMATIQUES</div><div style="color:#4DFF99;font-size:22px;font-weight:800;">+{entrees_auto:,.0f} €</div><div style="color:#CCBBAA;font-size:12px;margin-top:6px;line-height:1.8;">AAH : +{aah_m:,.0f}€{pch_line}{loyer_line}{rvd_line}</div></div>'
    flux_html += f'<div style="background:#150A10;border-radius:10px;padding:14px;"><div style="color:#BBA888;font-size:11px;margin-bottom:6px;">A PIOCHER EN CAPITAL</div><div style="color:#FF9944;font-size:22px;font-weight:800;">-{manque:,.0f} €</div><div style="color:#CCBBAA;font-size:12px;margin-top:6px;line-height:1.8;">Rail {rail:,.0f}€ - Entrees {entrees_auto:,.0f}€<br>Depuis : <b style="color:#FFF;">{src}</b><br>{cc_msg}</div></div>'
    flux_html += f'<div style="background:#150A10;border-radius:10px;padding:14px;border:1px solid {cc_border};"><div style="color:#BBA888;font-size:11px;margin-bottom:6px;">COMPTE COURANT</div><div style="color:#FFF;font-size:28px;font-weight:900;">{cc_val:,.0f} €</div><div style="color:#CCBBAA;font-size:12px;margin-top:6px;line-height:1.8;">Solde actuel<br>Apres depenses : ~{max(0,cc_val-manque):,.0f}€<br>Seuil mini conseille : {int(manque*2):,}€</div></div>'
    flux_html += '</div>'
    flux_html += f'<div style="margin-top:12px;background:#1A2A1A;border-radius:8px;padding:10px 14px;color:#4DFF99;font-size:13px;font-weight:600;">Rail mensuel : {entrees_auto:,.0f}€ auto + {manque:,.0f}€ a piocher = <b>{rail:,.0f}€/mois</b> total</div>'
    flux_html += '</div>'
    st.markdown(flux_html, unsafe_allow_html=True)

    titre("💶 CE MOIS — QUE FAIRE ?")
    c1,c2,c3 = st.columns(3)
    coul = "vert" if abs(ecart_arva)<100 else ("orange" if ecart_arva>-300 else "rouge")
    with c1: kpi("PIOCHE CE MOIS", f"{pioche:,.0f} €", f"Source : {src} · Rail total : {rail:,.0f}€/mois", coul)
    with c2: kpi("ARVA — PIOCHE OPTIMALE", f"{W:,.0f} €/mois", f"Écart vs rail : {ecart_arva:+.0f}€", coul)
    with c3:
        surplus = max(0,(W-rail)*12) if W>rail else 0
        if surplus>0: kpi("SURPLUS ANNUEL", f"{surplus:,.0f} €","→ Affecter dans Moteur ARVA","vert")
        else: kpi("SURPLUS ANNUEL","0 €","Trajectoire nominale","bleu")

    titre("📊 5 INDICATEURS CLÉS")
    k1,k2,k3,k4,k5 = st.columns(5)
    cc = "vert" if ecart_traj>=0 else ("orange" if ecart_traj>-10 else "rouge")
    with k1: kpi("Capital total",f"{C:,.0f} €",f"Traj. : {traj:,.0f}€ ({ecart_traj:+.1f}%)",cc)
    with k2: kpi("Rail mensuel",f"{rail:,.0f} €/mois",f"ARVA recommande : {W:,.0f}€",coul)
    with k3:
        cr = "vert" if rp>=0.0336 else ("orange" if rp>=0.033 else "rouge")
        kpi("Rendement pondéré",f"{rp*100:.3f} %","Cible : ≥ 3,365%",cr)
    with k4:
        if age>=74:
            swr=(rail*12)/C*100
            cs="vert" if swr<7.5 else("orange" if swr<9 else "rouge")
            kpi("SWR Phase 3",f"{swr:.1f} %","Seuil : > 9%",cs)
        else: kpi("SWR Phase 3","N/A",f"Actif dans {75-age:.0f} ans","bleu")
    with k5: kpi("Mois restants",f"{mois}",f"{mois/12:.1f} ans jusqu'à 92","bleu")

    titre("🚨 ALERTES")
    for niv,msg in calculer_alertes(profil,cap):
        alerte(niv,msg)

    titre("💰 RÉPARTITION DU CAPITAL — ORDRE DE PIOCHE (CC EN PREMIER)")
    col_g,col_d = st.columns([3,1])
    poches=[
        ("1","CC",        cap['cc'],       "#CC3333","0%",  "Vie quotidienne"),
        ("2","Livret A",  cap['livret_a'], "#C4922A","2,4%","Buffer 6 mois"),
        ("3","LDDS",      cap['ldds'],     "#1A4A7F","2,4%","Buffer complémentaire"),
        ("4","AV1",       cap['av1'],      "#1A6B4B","3,5%","Abattement disponible"),
        ("5","AV2",       cap['av2'],      "#27A06E","3,5%","Abattement en 2034"),
        ("6","AV3",       cap['av3'],      "#0F5C3A","3,5%","Réserve stratégique"),
        ("7★","LEP",      cap['lep'],      "#1C3A5E","3,5%","DERNIER — ne jamais piocher en premier"),
    ]
    with col_g:
        try:
            import plotly.graph_objects as go
            fig = go.Figure(go.Bar(
                x=[f"{p[1]} ({p[4]})" for p in poches],
                y=[p[2] for p in poches],
                marker_color=[p[3] for p in poches],
                text=[f"{p[2]:,.0f}€" for p in poches],
                textposition='outside'))
            fig.update_layout(plot_bgcolor='#140810',paper_bgcolor='#140810',
                font_color='#CCC',showlegend=False,height=250,
                yaxis=dict(gridcolor='#2A0A12'),margin=dict(t=20,b=0,l=0,r=0))
            st.plotly_chart(fig,use_container_width=True)
        except:
            for p in poches: st.write(f"{p[0]}. {p[1]}: {p[2]:,.0f}€")
    with col_d:
        for num,nom,val,col,taux,desc in poches:
            pct=val/C*100 if C>0 else 0
            st.markdown(f'<div class="poche-row"><div class="badge" style="background:{col};color:white;">{num}</div><div style="flex:1;"><div style="color:#DDD;font-size:13px;font-weight:600;">{nom} <span style="color:#888;font-size:11px;">{taux}</span></div><div style="color:#AAA;font-size:11px;">{val:,.0f}€ · {pct:.1f}%</div></div></div>',unsafe_allow_html=True)

    titre("📅 PROCHAIN JALON")
    jalons=[(50,"Départ","bleu"),(55,"Bilan Phase 1","bleu"),(58,"Abattement AV2 disponible","vert"),
            (60,"⚠️ DEADLINE MDPH","rouge"),(62,"Simulation vente immo","orange"),
            (64,"★ TRANSITION — Vente T3 + AAH s'arrête","rouge"),(73,"⚠️ Dernier moment RVD","rouge"),
            (75,"Activation RVD +450€/mois","vert"),(80,"Bilan dépendance","orange"),
            (85,"Bilan succession Anne-Lyse","orange"),(92,"Cible 50 000€","vert")]
    p = next(((a,l,c) for a,l,c in jalons if a>age),None)
    if p:
        aj,lj,cj=p; ans=aj-age
        bgs={'rouge':'#2A0A0A','orange':'#2A1800','vert':'#0A2010','bleu':'#0A1020'}
        bds={'rouge':'#CC3333','orange':'#D4A017','vert':'#1A6B4B','bleu':'#C4922A'}
        st.markdown(f'<div style="background:{bgs.get(cj,"#1A0D12")};border-radius:8px;padding:14px 18px;border-left:4px solid {bds.get(cj,"#C4922A")};"><div style="color:#888;font-size:11px;text-transform:uppercase;">Prochain jalon</div><div style="color:#FFF;font-size:17px;font-weight:700;margin:4px 0;">{lj}</div><div style="color:#AAA;font-size:13px;">À {aj} ans · dans <b>{ans:.1f} années</b></div></div>',unsafe_allow_html=True)

def page_arva(profil, cap):
    titre("🧮 MOTEUR ARVA — CALCUL ANNUEL")
    age=age_actuel(profil); mois=mois_restants(profil)
    C=capital_total(cap); W=arva(C,mois,profil['rendement_annuel']); rail=profil['rail_mensuel']
    coul='#1A6B4B' if abs(W-rail)<200 else '#D4A017'
    st.markdown(f'<div style="background:#1A0D12;border-radius:12px;padding:24px;text-align:center;margin-bottom:20px;"><div style="color:#888;font-size:12px;text-transform:uppercase;">ARVA — Pioche optimale pour 50 000€ à 92 ans</div><div style="color:{coul};font-size:56px;font-weight:900;line-height:1;">{W:,.0f} €</div><div style="color:#AAA;font-size:15px;margin-top:6px;">par mois · écart vs rail : <b style="color:{"#4DFF99" if W>=rail else "#FF6666"}">{W-rail:+.0f}€</b></div></div>',unsafe_allow_html=True)
    col1,col2=st.columns(2)
    with col1:
        titre("Simuler avec d'autres paramètres")
        cap_s=st.number_input("Capital (€)",value=float(C),step=1000.0)
        mois_s=st.number_input("Mois restants",value=mois,step=1)
        rend_s=st.number_input("Rendement (%/an)",value=profil['rendement_annuel']*100,step=0.1,format="%.2f")
        cible_s=st.number_input("Capital cible 92 ans (€)",value=50000.0,step=1000.0)
    with col2:
        W2=arva(cap_s,int(mois_s),rend_s/100,cible_s)
        r_m=(1+rend_s/100)**(1/12)-1
        titre("Résultat")
        st.code(f"W_opt = {W2:,.2f} €/mois\nRail  = {rail:,.0f} €/mois\nÉcart = {W2-rail:+.0f} €\n\nFormule:\nW = Capital × r_m / [1−(1+r_m)^(−n)]\nr_m = {r_m*100:.5f}%\nn   = {int(mois_s)} mois",language="")
    titre("Sensibilité au rendement")
    rows=[]
    for rt in [2.5,2.8,3.0,3.2,3.5,3.8,4.0]:
        wt=arva(cap_s,int(mois_s),rt/100,cible_s)
        rows.append(f"| {rt:.1f}% | **{wt:,.0f} €** | {wt-rail:+.0f} € | {'✅' if wt>=rail else '⚠️'} |")
    st.markdown("| Rendement | Pioche ARVA | Écart rail | Statut |\n|---|---|---|---|\n"+"\n".join(rows))
    if W>rail+100:
        surplus_an=(W-rail)*12
        titre("✨ SURPLUS DÉTECTÉ — AFFECTATION")
        st.markdown(f'<div class="surplus-box"><div style="color:#4DFF99;font-size:18px;font-weight:700;">Surplus annuel : {surplus_an:,.0f} €</div><div style="color:#AAA;font-size:13px;margin-top:4px;">Le plan génère plus que nécessaire. Affecter ce surplus ?</div></div>',unsafe_allow_html=True)
        dest=st.radio("Destination :",["RVD (à constituer avant 64 ans)","AV3 (réserve stratégique)","Laisser en CC","Anticiper travaux parents"])
        note_s=st.text_input("Note")
        if st.button("💾 Valider",type="primary"):
            save_surplus(surplus_an,dest,note_s)
            st.success(f"✅ {surplus_an:,.0f}€ affectés : {dest}")
    hist=get_historique_surplus()
    if hist:
        titre("Historique affectations")
        for d,m,dst,n in hist:
            st.markdown(f"**{d}** · {m:,.0f}€ → {dst}"+(f" · {n}" if n else ""))

def page_suivi_av(profil, cap):
    titre("📋 SUIVI AV × 3 CONTRATS")
    for av,nom in [('av1','AV Contrat 1 — Abattement disponible'),('av2','AV Contrat 2 — Ouvert 2026'),('av3','AV Contrat 3 — Réserve')]:
        val=cap[av]; vers=cap[f'{av}_versements']; pv=pv_latentes(cap,av)
        ab=abattement_dispo(cap,av); rmax=rachat_max_sans_ir(cap,av)
        r_av=cap.get(f'{av}_rendement',0.035); do_s=cap.get(f'{av}_date_ouverture','2020-01-01')
        tpv=pv/val*100 if val>0 else 0
        try:
            do=datetime.strptime(do_s,'%Y-%m-%d'); anc=(datetime.today()-do).days/365.25
            d8=do.replace(year=do.year+8).strftime('%d/%m/%Y')
        except: anc=0; d8="?"
        cc2="ok" if r_av>=0.03 else("warn" if r_av>=0.028 else "danger")
        cr2="#1A6B4B" if r_av>=0.03 else("#D4A017" if r_av>=0.028 else "#CC3333")
        st.markdown(f'<div class="av-card {cc2}"><div style="display:flex;justify-content:space-between;"><div><div style="color:#FFF;font-size:15px;font-weight:700;">{nom}</div><div style="color:#888;font-size:12px;">{do_s} · {anc:.1f} ans</div></div><div style="text-align:right;"><div style="color:{cr2};font-size:20px;font-weight:800;">{r_av*100:.2f}%</div><div style="color:#888;font-size:11px;">rendement</div></div></div><div style="display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:12px;"><div><div style="color:#888;font-size:11px;">Valeur rachat</div><div style="color:#FFF;font-weight:700;">{val:,.0f}€</div></div><div><div style="color:#888;font-size:11px;">PV latentes</div><div style="color:#FFF;font-weight:700;">{pv:,.0f}€ ({tpv:.1f}%)</div></div><div><div style="color:#888;font-size:11px;">Abattement 8 ans</div><div style="color:{"#4DFF99" if ab>0 else "#FF6666"};font-weight:700;">{"✅ "+str(int(ab))+"€" if ab>0 else "❌ "+d8}</div></div><div><div style="color:#888;font-size:11px;">Rachat max sans IR</div><div style="color:{"#4DFF99" if rmax>0 else "#FF6666"};font-weight:700;">{f"{rmax:,.0f}€" if rmax>0 else "Attendre"}</div></div></div></div>',unsafe_allow_html=True)
    titre("📐 TOTAUX 3 CONTRATS")
    c1,c2,c3=st.columns(3)
    tot_av=cap['av1']+cap['av2']+cap['av3']
    tot_pv=sum(pv_latentes(cap,av) for av in ['av1','av2','av3'])
    tot_r=sum(rachat_max_sans_ir(cap,av) for av in ['av1','av2','av3'])
    with c1: kpi("Total AV",f"{tot_av:,.0f} €",f"{tot_av/capital_total(cap)*100:.1f}% du capital","bleu")
    with c2: kpi("PV latentes totales",f"{tot_pv:,.0f} €","","orange")
    with c3: kpi("Rachat max sans IR",f"{tot_r:,.0f} €","Abattements 8 ans cumulés","vert")
    titre("Stratégie rachat — 1er janvier")
    st.markdown("1. **AV1** → cristalliser 4 600€ PV → IR = 0€ · PS 17,2% si PV > abattement\n2. Si AV2 ≥ 8 ans (après 2034) → 4 600€ supplémentaires\n3. Vérifier marge CAF avant chaque rachat\n4. Réinvestir la part capital immédiatement → nouveau prix de revient")

def page_simulateur(profil, cap):
    titre("🔬 SIMULATEUR DE SCÉNARIOS")
    C=capital_total(cap); r=profil['rendement_annuel']; rail=profil['rail_mensuel']
    aah=profil['aah_mensuel']; loyer=profil['loyer_net']
    def sim(C0,rend,rail_s,aah_s,loyer_s,rvd=450,ehpad=0):
        r_m=(1+rend)**(1/12)-1
        def A(n): return ((1+rend)**n-1)/r_m if r_m>0 else n
        def P(n): return (1+rend)**n
        pp1=rail_s-aah_s-loyer_s; immo=205000*(1.015**14)
        C64=C0*P(14)-pp1*A(14)+immo; C75=C64*P(11)-rail_s*A(11)
        C92=C75*P(17)-(rail_s-rvd+ehpad)*A(17)
        pts={}
        for age in [50,56,60,64,70,75,80,85,90,92]:
            n=age-50
            if age<=64: v=C0*P(n)-pp1*A(n)
            elif age<=75: v=C64*P(age-64)-rail_s*A(age-64)
            else: v=C75*P(age-75)-(rail_s-rvd+ehpad)*A(age-75)
            pts[age]=round(v,0)
        return round(C92,0),pts
    t1,t2,t3,t4,t5,t6=st.tabs(["Base","MDPH+PCH","Seq. Returns","EHPAD+APA","Rendement","Comparaison"])
    base_c92,base_pts=sim(C,r,rail,aah,loyer)
    with t1:
        kpi("C92 — Base",f"{base_c92:,.0f} €","✅ Cible atteinte" if base_c92>=50000 else "⚠️ Cible non atteinte","vert" if base_c92>=50000 else "rouge")
        graphe(base_pts)
    with t2:
        pch=st.slider("PCH (€/mois)",0,1500,500,50)
        c92b,ptsb=sim(C,r,rail,aah+pch,loyer)
        kpi(f"C92 — MDPH+PCH {pch}€",f"{c92b:,.0f} €",f"Gain vs base : +{c92b-base_c92:,.0f}€","vert" if c92b>=50000 else "rouge")
        graphe(ptsb)
    with t3:
        rb=st.slider("Rendement 64→67 ans (%)",1.0,3.5,2.0,0.1)/100
        r_mb=(1+rb)**(1/12)-1
        def Ab(n): return ((1+rb)**n-1)/r_mb if r_mb>0 else n
        r_m=(1+r)**(1/12)-1
        def Ar(n): return ((1+r)**n-1)/r_m if r_m>0 else n
        pp1=rail-aah-loyer; immo=205000*(1.015**14)
        C64=C*(1+r)**14-pp1*Ar(14)+immo
        C67=C64*(1+rb)**3-rail*Ab(3)
        C75=C67*(1+r)**8-rail*Ar(8)
        C92sor=C75*(1+r)**17-rail*Ar(17)
        kpi(f"C92 — Seq.Returns r={rb*100:.1f}%",f"{C92sor:,.0f} €",f"Perte vs base : {C92sor-base_c92:+,.0f}€","vert" if C92sor>=50000 else "rouge")
        alerte('orange',"💡 Solution : garder 3 ans de pioche en livrets à 64 ans (99 360€) avant de racheter les AV.")
    with t4:
        eb=st.slider("EHPAD brut (€/mois)",1500,4000,2000,100)
        apa=st.slider("APA reçue (€/mois)",0,1700,700,50)
        net=eb-apa; c92e,ptse=sim(C,r,rail,aah,loyer,ehpad=net)
        kpi(f"C92 — EHPAD {eb}€ − APA {apa}€ = {net}€ net",f"{c92e:,.0f} €","GIR2≈700€APA · GIR1≈1200€APA","vert" if c92e>=50000 else("orange" if c92e>0 else "rouge"))
        graphe(ptse)
    with t5:
        rd=st.slider("Rendement (%/an)",2.0,4.0,2.8,0.1)/100
        c92d,ptsd=sim(C,rd,rail,aah,loyer)
        kpi(f"C92 — {rd*100:.1f}%/an",f"{c92d:,.0f} €","Critique si < 2,8%","vert" if c92d>=50000 else "rouge")
        graphe(ptsd)
    with t6:
        titre("Comparaison rapide")
        c92_pch,_=sim(C,r,rail,aah+500,loyer)
        c92_r,_=sim(C,0.028,rail,aah,loyer)
        c92_e,_=sim(C,r,rail,aah,loyer,ehpad=1300)
        sc=[("Base",base_c92),("MDPH+PCH 500€",c92_pch),("Rendement 2,8%",c92_r),("EHPAD net 1300€",c92_e)]
        try:
            import plotly.graph_objects as go
            fig=go.Figure(go.Bar(x=[s[0] for s in sc],y=[s[1] for s in sc],
                marker_color=['#1A6B4B' if s[1]>=50000 else '#CC3333' for s in sc],
                text=[f"{s[1]:,.0f}€" for s in sc],textposition='outside'))
            fig.add_hline(y=50000,line_dash="dash",line_color="#D4A017",annotation_text="Cible")
            fig.update_layout(plot_bgcolor='#140810',paper_bgcolor='#140810',font_color='#CCC',
                height=320,margin=dict(t=20,b=0,l=0,r=0),yaxis=dict(gridcolor='#2A0A12'))
            st.plotly_chart(fig,use_container_width=True)
        except: pass

def page_impots(profil, cap):
    titre("📄 DÉCLARATION D'IMPÔTS — RÉCAPITULATIF")
    year=st.number_input("Année fiscale",value=datetime.today().year-1,step=1)
    titre("Cases à remplir sur impots.gouv.fr")
    cases=[
        ("1AS","AAH — pensions","NE PAS REMPLIR","L'AAH n'est pas imposable. Laisser vide.",False),
        ("4BA","LMNP résultat BIC net","0 €","Résultat = 0€ grâce aux amortissements. À confirmer avec expert-comptable.",True),
        ("2TR","PV assurance-vie imposables","Voir calcul ci-dessous","Uniquement les plus-values, pas le capital remboursé.",True),
        ("2OP","Option PFU — À COCHER","✅ COCHER","Cocher pour que les prélèvements sociaux soient calculés à la source.",True),
    ]
    for cn,lb,vl,nt,imp in cases:
        bg="#1A2C1A" if imp else "#1A0D12"; bd="#1A6B4B" if imp else "#2D3A55"
        st.markdown(f'<div style="background:{bg};border:1px solid {bd};border-radius:8px;padding:10px 14px;margin:4px 0;"><div style="display:flex;justify-content:space-between;align-items:center;"><div><span style="color:#888;font-size:12px;font-family:monospace;margin-right:10px;">CASE {cn}</span><span style="color:#DDD;font-size:13px;">{lb}</span></div><div style="color:#FFF;font-weight:700;">{vl}</div></div><div style="color:#888;font-size:12px;margin-top:4px;">💡 {nt}</div></div>',unsafe_allow_html=True)
    titre("Calcul PV AV imposables")
    c1,c2=st.columns(2)
    with c1:
        r1=st.number_input("Rachat AV1 (€)",value=15000.0,step=500.0)
        tp1=st.number_input("Taux PV AV1 (%)",value=5.0,step=0.5)
        r3=st.number_input("Rachat AV3 (€)",value=0.0,step=500.0)
        tp3=st.number_input("Taux PV AV3 (%)",value=8.0,step=0.5)
    with c2:
        pv1=r1*tp1/100; pv3=r3*tp3/100; tpv=pv1+pv3
        ab=abattement_dispo(cap,'av1')+abattement_dispo(cap,'av3')
        pvi=max(0,tpv-ab); ps=pvi*0.172
        st.markdown(f'<div style="background:#1A0D12;border-radius:8px;padding:16px;"><div style="color:#888;font-size:12px;margin-bottom:8px;">RÉSULTAT {int(year)}</div><div style="color:#DDD;margin:3px 0;">PV AV1 : <b>{pv1:,.0f}€</b></div><div style="color:#DDD;margin:3px 0;">PV AV3 : <b>{pv3:,.0f}€</b></div><div style="color:#DDD;margin:3px 0;">Abattements : <b>−{min(tpv,ab):,.0f}€</b></div><div style="color:#DDD;margin:3px 0;">PV imposable : <b>{pvi:,.0f}€</b></div><div style="color:#1A6B4B;font-size:16px;font-weight:700;margin-top:8px;">IR : 0 € (TMI 0%)</div><div style="color:{"#1A6B4B" if ps<300 else "#D4A017"};">PS 17,2% : <b>{ps:.0f}€</b></div><div style="color:#4DFF99;font-size:20px;font-weight:800;">Total : {ps:.0f} €</div></div>',unsafe_allow_html=True)
    titre("Texte à copier-coller lors de la déclaration")
    aah_an=profil['aah_mensuel']*12
    texte=f"""DÉCLARATION {int(year)} — RAPHAËL

FORMULAIRE 2042 :
• Case 1AS : NE PAS REMPLIR (AAH non imposable)
• Case 4BA : 0 € (résultat LMNP nul)
• Case 2TR : {pvi:,.0f} € (PV nettes après abattement)
• Case 2OP : COCHER

FISCAL :
• PV encaissées : {tpv:,.0f} €
• Abattements 8 ans : {min(tpv,ab):,.0f} €
• PV imposables : {pvi:,.0f} €
• IR : 0 € · PS : {ps:.0f} €
• TOTAL IMPÔTS : {ps:.0f} €

LMNP (formulaire 2031 + liasse 2033) :
• Résultat BIC : 0 € (à confirmer expert-comptable)
"""
    st.code(texte,language="")

def page_fiscal(profil, cap):
    titre("💶 FISCAL & CAF")
    aah=profil['aah_mensuel']
    seuil=st.number_input("Seuil ressources CAF Isère (€/an)",value=12396.0,step=100.0)
    titre("Tax-Gain Harvesting — Chaque 1er Janvier")
    st.info("✨ IR = 0€ toute la vie → cristalliser 4 600€ de PV AV chaque année = opération gratuite à ne jamais manquer")
    c1,c2=st.columns(2)
    with c1:
        rachat=st.number_input("Rachat AV1 prévu (€)",value=15000.0,step=500.0)
        tpv=st.number_input("Taux PV AV1 (%)",value=5.0,step=0.5)/100
        pv=rachat*tpv; ab=abattement_dispo(cap,'av1'); pvi=max(0,pv-ab); ps=pvi*0.172
    with c2:
        st.markdown(f'<div style="background:#1A0D12;border-radius:8px;padding:16px;"><div style="color:#DDD;margin:3px 0;">Rachat : <b>{rachat:,.0f}€</b></div><div style="color:#DDD;margin:3px 0;">PV : <b>{pv:,.0f}€</b> · Abattement : <b>−{min(pv,ab):,.0f}€</b></div><div style="color:#DDD;margin:3px 0;">PV imposable : <b>{pvi:,.0f}€</b></div><div style="color:#1A6B4B;font-size:16px;font-weight:700;margin-top:8px;">IR : 0 €</div><div style="color:{"#1A6B4B" if ps<300 else "#D4A017"};">PS 17,2% : <b>{ps:.0f}€</b></div><div style="color:#4DFF99;font-size:20px;font-weight:800;">Total fiscal : {ps:.0f} €</div></div>',unsafe_allow_html=True)
    titre("Vérification CAF avant rachat")
    rev_caf=aah*12+pv; marge=seuil-rev_caf
    alerte("vert" if marge>500 else("orange" if marge>0 else "rouge"),
           f"Ressources CAF estimées : {rev_caf:,.0f}€/an · Marge : {marge:+,.0f}€")
    if marge<0: alerte('rouge',"🔴 BLOQUER le rachat. Contacter CAF Isère avant toute action.")
    st.caption("⚠️ Seules les PLUS-VALUES comptent pour la CAF, pas le capital.")

def page_saisie(profil, cap):
    titre("✏️ MISE À JOUR ANNUELLE")
    st.info("📅 À faire chaque 1er janvier avec les relevés de vos assureurs.")
    with st.form("cap_form"):
        titre("Poches sécurité")
        c1,c2,c3,c4=st.columns(4)
        with c1: cc=st.number_input("CC (€)",value=float(cap['cc']),step=100.0)
        with c2: liva=st.number_input("Livret A (€)",value=float(cap['livret_a']),step=100.0)
        with c3: ldds=st.number_input("LDDS (€)",value=float(cap['ldds']),step=100.0)
        with c4: lep=st.number_input("LEP ★ (€)",value=float(cap['lep']),step=100.0)
        titre("Assurances-Vie")
        ca1,ca2,ca3=st.columns(3)
        with ca1:
            st.markdown("**AV1**")
            av1=st.number_input("Valeur AV1 (€)",value=float(cap['av1']),step=500.0)
            av1v=st.number_input("Versements AV1 (€)",value=float(cap['av1_versements']),step=500.0)
            av1r=st.number_input("Rend. AV1 (%)",value=float(cap['av1_rendement'])*100,step=0.1,format="%.2f")
            av1d=st.text_input("Ouverture AV1",value=cap['av1_date_ouverture'])
        with ca2:
            st.markdown("**AV2**")
            av2=st.number_input("Valeur AV2 (€)",value=float(cap['av2']),step=500.0)
            av2v=st.number_input("Versements AV2 (€)",value=float(cap['av2_versements']),step=500.0)
            av2r=st.number_input("Rend. AV2 (%)",value=float(cap['av2_rendement'])*100,step=0.1,format="%.2f")
            av2d=st.text_input("Ouverture AV2",value=cap['av2_date_ouverture'])
        with ca3:
            st.markdown("**AV3**")
            av3=st.number_input("Valeur AV3 (€)",value=float(cap['av3']),step=500.0)
            av3v=st.number_input("Versements AV3 (€)",value=float(cap['av3_versements']),step=500.0)
            av3r=st.number_input("Rend. AV3 (%)",value=float(cap['av3_rendement'])*100,step=0.1,format="%.2f")
            av3d=st.text_input("Ouverture AV3",value=cap['av3_date_ouverture'])
        note=st.text_input("Note",placeholder="ex: Relevé janvier 2027")
        total=cc+liva+ldds+lep+av1+av2+av3
        st.info(f"**Total capital : {total:,.0f} €**")
        if st.form_submit_button("💾 Enregistrer",type="primary"):
            save_capital({'cc':cc,'livret_a':liva,'ldds':ldds,'lep':lep,
                'av1':av1,'av2':av2,'av3':av3,
                'av1_do':av1d,'av2_do':av2d,'av3_do':av3d,
                'av1_v':av1v,'av2_v':av2v,'av3_v':av3v,
                'av1_r':av1r/100,'av2_r':av2r/100,'av3_r':av3r/100,'note':note})
            st.success("✅ Capital mis à jour !")
            st.rerun()
    titre("⚙️ PARAMÈTRES PROFIL")
    with st.form("prof_form"):
        c1,c2,c3=st.columns(3)
        with c1:
            aah=st.number_input("AAH (€/mois)",value=float(profil['aah_mensuel']),step=1.0)
            pch=st.number_input("PCH (€/mois)",value=float(profil.get('pch_mensuel',0)),step=50.0)
        with c2:
            loyer=st.number_input("Loyer LMNP net (€/mois)",value=float(profil['loyer_net']),step=1.0)
            mdph=st.number_input("Taux MDPH (%)",value=int(profil['taux_mdph']),step=5)
        with c3:
            rail=st.number_input("Rail (€/mois)",value=float(profil['rail_mensuel']),step=10.0)
            rend=st.number_input("Rendement AV (%/an)",value=float(profil['rendement_annuel']*100),step=0.1,format="%.2f")
        if st.form_submit_button("💾 Sauvegarder",type="primary"):
            save_profil({'aah':aah,'pch':pch,'loyer':loyer,'mdph':mdph,'rail':rail,'rendement':rend})
            st.success("✅ Paramètres mis à jour !")
            st.rerun()


# ─── HELPERS DB LMNP ─────────────────────────────────────────────────────────
def get_lmnp():
    conn = db_wrapper.connect()
    c = conn.cursor()
    row = c.execute("SELECT * FROM lmnp WHERE id=1").fetchone()
    cols = [d[0] for d in c.description]
    conn.close()
    return dict(zip(cols, row)) if row else {}

def save_lmnp(d):
    conn = db_wrapper.connect()
    c = conn.cursor()
    c.execute("""UPDATE lmnp SET date_acquisition=?,valeur_acquisition=?,valeur_terrain=?,
        travaux=?,loyer_brut_mensuel=?,charges_annuelles=?,
        duree_amort_immeuble=?,duree_amort_mobilier=?,valeur_mobilier=?,
        taux_irl_dernier=?,date_derniere_revalorisation=?,updated=CURRENT_TIMESTAMP
        WHERE id=1""",
        (d['date_acq'],d['val_acq'],d['terrain'],d['travaux'],
         d['loyer_brut'],d['charges'],d['amort_imm'],d['amort_mob'],
         d['mobilier'],d['irl']/100,d['date_reval']))
    conn.commit(); conn.close()

def calcul_lmnp(lm):
    """Calcule amortissements, résultat, années restantes."""
    from datetime import datetime
    try:
        acq = datetime.strptime(lm['date_acquisition'], '%Y-%m-%d')
        annees_ecoules = (datetime.today() - acq).days / 365.25
    except:
        annees_ecoules = 15
    val_amort = lm['valeur_acquisition'] - lm['valeur_terrain'] + lm['travaux']
    amort_imm_annuel = val_amort / lm['duree_amort_immeuble']
    amort_mob_annuel = lm['valeur_mobilier'] / lm['duree_amort_mobilier']
    annees_restantes_mob = max(0, lm['duree_amort_mobilier'] - annees_ecoules)
    annees_restantes_imm = max(0, lm['duree_amort_immeuble'] - annees_ecoules)
    amort_mob_actuel = amort_mob_annuel if annees_restantes_mob > 0 else 0
    amort_total = amort_imm_annuel + amort_mob_actuel
    loyer_annuel = lm['loyer_brut_mensuel'] * 12
    resultat = loyer_annuel - lm['charges_annuelles'] - amort_total
    return {
        'loyer_annuel': loyer_annuel,
        'charges': lm['charges_annuelles'],
        'amort_imm': amort_imm_annuel,
        'amort_mob': amort_mob_actuel,
        'amort_total': amort_total,
        'resultat': resultat,
        'annees_restantes_imm': annees_restantes_imm,
        'annees_restantes_mob': annees_restantes_mob,
        'annees_ecoules': annees_ecoules,
    }

def nouveau_loyer_irl(loyer_actuel, taux_irl):
    return round(loyer_actuel * (1 + taux_irl), 2)

# ─── PAGE LMNP ────────────────────────────────────────────────────────────────
def page_lmnp(profil, cap):
    lm = get_lmnp()
    res = calcul_lmnp(lm)
    titre("🏠 MODULE LMNP — T3 MEYLAN")

    # Statut fiscal
    coul_res = "vert" if abs(res['resultat']) < 500 else ("orange" if res['resultat'] < 2000 else "rouge")
    signe = "+" if res['resultat'] > 0 else ""
    c1,c2,c3,c4 = st.columns(4)
    with c1: kpi("Loyer brut annuel", f"{res['loyer_annuel']:,.0f} €", f"{lm['loyer_brut_mensuel']:,.0f}€/mois", "bleu")
    with c2: kpi("Amortissements", f"{res['amort_total']:,.0f} €/an", f"Imm. {res['amort_imm']:,.0f}€ + Mob. {res['amort_mob']:,.0f}€", "bleu")
    with c3: kpi("Résultat BIC", f"{signe}{res['resultat']:,.0f} €", "Cible : 0€ (AAH maintenue)", coul_res)
    with c4:
        ann_imm = res['annees_restantes_imm']
        coul_a = "vert" if ann_imm > 5 else ("orange" if ann_imm > 2 else "rouge")
        kpi("Amort. immeuble restant", f"{ann_imm:.1f} ans", f"Fin : ~{2025+int(ann_imm)}", coul_a)

    # Alerte résultat
    if res['resultat'] > 500:
        alerte('orange', f"⚠️ Résultat LMNP positif ({res['resultat']:,.0f}€). Impact potentiel sur AAH. Vérifier avec expert-comptable.")
    elif abs(res['resultat']) <= 500:
        alerte('vert', f"✅ Résultat LMNP ≈ 0€ ({res['resultat']:+.0f}€). AAH maintenue taux plein.")

    if res['annees_restantes_imm'] < 3:
        alerte('rouge', f"🔴 Amortissements immeuble épuisés dans {res['annees_restantes_imm']:.1f} ans. Résultat LMNP va devenir positif. Prévoir avec expert-comptable.")
    elif res['annees_restantes_imm'] < 5:
        alerte('orange', f"⚠️ Amortissements immeuble épuisés dans {res['annees_restantes_imm']:.1f} ans. Anticiper.")

    titre("🔢 DÉTAIL CALCUL FISCAL")
    lmnp_detail = f'<div style="background:#1A0D12;border-radius:10px;padding:16px 20px;font-family:monospace;font-size:13px;line-height:2;"><span style="color:#4DFF99;">Loyer brut annuel</span> <span style="color:#FFF;float:right;">+ {res["loyer_annuel"]:,.0f} €</span><br><span style="color:#FF7777;">Charges annuelles</span> <span style="color:#FFF;float:right;">- {lm["charges_annuelles"]:,.0f} €</span><br><span style="color:#FF7777;">Amort. immeuble</span> <span style="color:#FFF;float:right;">- {res["amort_imm"]:,.0f} €</span><br><span style="color:#FF7777;">Amort. mobilier</span> <span style="color:#FFF;float:right;">- {res["amort_mob"]:,.0f} €</span><br><div style="border-top:1px solid #2A0A12;margin:8px 0;"></div><span style="color:#FFD060;font-weight:700;">Resultat BIC</span> <span style="color:#FFD060;font-weight:700;float:right;">= {res["resultat"]:,.0f} €</span></div>'
    st.markdown(lmnp_detail, unsafe_allow_html=True)

    titre("📈 REVALORISATION LOYER IRL")
    try:
        from datetime import datetime
        date_rev = datetime.strptime(lm['date_derniere_revalorisation'], '%Y-%m-%d')
        mois_depuis = (datetime.today() - date_rev).days / 30.44
    except:
        mois_depuis = 13
    loyer_actuel = lm['loyer_brut_mensuel']
    nouveau = nouveau_loyer_irl(loyer_actuel, lm['taux_irl_dernier'])
    hausse = nouveau - loyer_actuel

    if mois_depuis > 12:
        alerte('orange', f"⚠️ Dernière revalorisation il y a {mois_depuis:.0f} mois. Revalorisation due !")
    else:
        alerte('vert', f"✅ Dernière revalorisation il y a {mois_depuis:.0f} mois. Prochaine dans {12-mois_depuis:.0f} mois.")

    c1,c2,c3 = st.columns(3)
    with c1: kpi("Loyer actuel", f"{loyer_actuel:,.2f} €/mois", "", "bleu")
    with c2:
        irl_pct = lm['taux_irl_dernier']*100
        kpi("IRL dernier trimestre", f"+{irl_pct:.2f} %", "À mettre à jour chaque trimestre", "orange")
    with c3: kpi("Nouveau loyer calculé", f"{nouveau:,.2f} €/mois", f"Hausse : +{hausse:.2f}€/mois (+{hausse*12:.0f}€/an)", "vert")

    st.markdown(f'<div style="background:#0A2010;border:1px solid #1A6B4B;border-radius:8px;padding:12px 16px;margin:8px 0;font-size:13px;color:#4DFF99;">COURRIER AU LOCATAIRE : A compter du [date], votre loyer est revalorise a <b>{nouveau:.2f}€/mois</b> conformement a l indice IRL du [trimestre] publie par l INSEE (indice : +{irl_pct:.2f}%).</div>', unsafe_allow_html=True)

    titre("⚙️ PARAMÈTRES LMNP")
    with st.form("lmnp_form"):
        c1,c2 = st.columns(2)
        with c1:
            date_acq = st.text_input("Date acquisition (AAAA-MM-JJ)", value=lm['date_acquisition'])
            val_acq  = st.number_input("Valeur acquisition (€)", value=float(lm['valeur_acquisition']), step=1000.0)
            terrain  = st.number_input("Part terrain non amortissable (€)", value=float(lm['valeur_terrain']), step=1000.0)
            travaux  = st.number_input("Travaux amortissables (€)", value=float(lm['travaux']), step=500.0)
            mobilier = st.number_input("Valeur mobilier (€)", value=float(lm['valeur_mobilier']), step=500.0)
        with c2:
            loyer_b  = st.number_input("Loyer brut mensuel (€)", value=float(lm['loyer_brut_mensuel']), step=10.0)
            charges  = st.number_input("Charges annuelles (€)", value=float(lm['charges_annuelles']), step=100.0)
            amort_i  = st.number_input("Durée amort. immeuble (ans)", value=int(lm['duree_amort_immeuble']), step=1)
            amort_m  = st.number_input("Durée amort. mobilier (ans)", value=int(lm['duree_amort_mobilier']), step=1)
            irl      = st.number_input("IRL dernier trimestre (%)", value=float(lm['taux_irl_dernier']*100), step=0.01, format="%.2f")
            date_rev2= st.text_input("Date dernière revalorisation", value=lm['date_derniere_revalorisation'])
        if st.form_submit_button("💾 Sauvegarder LMNP", type="primary"):
            save_lmnp({'date_acq':date_acq,'val_acq':val_acq,'terrain':terrain,'travaux':travaux,
                'loyer_brut':loyer_b,'charges':charges,'amort_imm':amort_i,'amort_mob':amort_m,
                'mobilier':mobilier,'irl':irl,'date_reval':date_rev2})
            st.success("✅ LMNP mis à jour !"); st.rerun()

# ─── PAGE JALONS ──────────────────────────────────────────────────────────────
def page_jalons(profil, cap):
    from datetime import datetime, date
    titre("📅 CALENDRIER JALONS — COMPTE À REBOURS")

    age = age_actuel(profil)
    dn  = datetime.strptime(profil['date_naissance'], '%Y-%m-%d')

    jalons_complets = [
        (50,  "📍 Départ du plan",
               "Ouvrir AV n°2 (500€ minimum). Simulateur MaPrimeRénov ANAH pour travaux parents.",
               ["Ouvrir AV2 Linxea Spirit 2 ✓", "Simuler MaPrimeRénov en ligne", "Valider capital initial 393 192€"]),
        (55,  "📊 Bilan mi-parcours Phase 1",
               "Vérifier trajectoire. Ajuster pioche si besoin.",
               ["Relever capital réel", "Comparer à trajectoire théorique", "ARVA recalculé"]),
        (58,  "✅ Abattement AV2 disponible",
               "AV2 atteint 8 ans → 4 600€ de PV supplémentaires exonérées. Passer de 4 600€ à 9 200€/an de PV exo.",
               ["Vérifier date ouverture AV2", "Mettre à jour stratégie rachat", "Tax-Gain Harvesting × 2 contrats"]),
        (60,  "🔴 DEADLINE MDPH — CRITIQUE",
               "Dossier MDPH doit être DÉPOSÉ avant 60 ans. Si raté → irréversible. PCH potentielle +282 000€ sur C92.",
               ["Dossier médical complet", "Certificat médical spécialisé", "Dépôt MDPH 38 (Grenoble)", "Suivi dossier"]),
        (62,  "🏠 Simulation vente immo",
               "Commencer les estimations du T3 Meylan. Anticiper la réinvestissement de 252k€.",
               ["Estimation agences (3 minimum)", "Vérifier fiscalité PV immo (>22 ans = exo)", "Anticiper frais notaire"]),
        (64,  "⭐ TRANSITION MAJEURE",
               "AAH s'arrête + vendre T3 + réinjecter 252k€ en AV. ARVA recalcule tout. Phase 2 démarre.",
               ["Vente T3 finalisée", "252k€ injectés AV3", "ARVA Phase 2 calculé", "Buffer 3 ans livrets constitué"]),
        (73,  "⚠️ Dernier moment RVD",
               "Si RVD pas encore souscrite → ALERTE ROUGE. 2 ans avant activation. Dernier moment absolu.",
               ["Comparer offres rentes viagères", "Souscrire RVD 50 000€", "Vérifier conditions activation"]),
        (75,  "💰 Activation RVD",
               "+450€/mois garantis à vie. Pioche AV réduite à 2 310€/mois. Phase 3 démarre.",
               ["RVD activée automatiquement", "Mise à jour cockpit pioche", "ARVA Phase 3 recalculé"]),
        (80,  "🏥 Bilan dépendance",
               "Activer mode sénior. Évaluer besoin EHPAD. Simuler coût net APA.",
               ["Bilan autonomie (GIR)", "Simulation EHPAD − APA", "Mise à jour testament/mandat"]),
        (85,  "📜 Bilan succession",
               "Anne-Lyse : capital résiduel estimé. AV hors succession vérifiées.",
               ["Capital résiduel calculé", "AV bénéficiaires vérifiés", "Testament à jour"]),
    ]

    # Actions urgentes maintenant
    titre("🚨 ACTIONS URGENTES MAINTENANT")
    actions_now = [
        ("IMMÉDIAT", "Simuler MaPrimeRénov ANAH", "Récupérer ~11 400€ avant travaux parents", "#CC3333"),
        ("CETTE SEMAINE", "Ouvrir AV n°2 (500€ min)", "Démarrer l'horloge 8 ans → abattement dispo en 2034", "#D4A017"),
        ("CETTE SEMAINE", "RDV médecin → dossier MDPH ≥80%", "PCH potentielle +282 000€ sur C92", "#D4A017"),
        ("CE MOIS", "CAF Isère — seuil ressources exact", "Calibrer les rachats AV sans risquer l'AAH", "#D4A017"),
        ("< 3 MOIS", "Notaire : testament + mandat + donation NP", "3 actes en 1 RDV", "#C4922A"),
        ("< 3 MOIS", "Dépôt dossier MDPH complet", "IRRÉVERSIBLE si raté avant 60 ans", "#CC3333"),
        ("< 6 MOIS", "Souscrire RVD 50 000€", "Essentielle Phase 3 — à constituer maintenant", "#CC3333"),
        ("< 6 MOIS", "Réduire buffer livrets à 16 560€", "OBLIGATOIRE sinon C92 = −15 000€", "#CC3333"),
    ]
    for delai, action, enjeu, col in actions_now:
        st.markdown(f'<div style="display:flex;align-items:flex-start;gap:12px;padding:10px 14px;background:#1A0D12;border-radius:8px;margin:4px 0;border-left:3px solid {col};"><div style="background:{col};color:white;border-radius:6px;padding:3px 8px;font-size:11px;font-weight:700;white-space:nowrap;flex-shrink:0;">{delai}</div><div><div style="color:#FFF;font-size:13px;font-weight:600;">{action}</div><div style="color:#BBA888;font-size:12px;">{enjeu}</div></div></div>', unsafe_allow_html=True)

    titre("📅 TOUS LES JALONS — COMPTE À REBOURS")
    for age_j, label, desc, checklist in jalons_complets:
        ans_restants = age_j - age
        if ans_restants < 0:
            statut = "✅ PASSÉ"
            bg = "#0A1A0A"; bd = "#1A6B4B"; ct = "#4DFF99"
        elif ans_restants < 1:
            statut = f"🔴 DANS {ans_restants*12:.0f} MOIS"
            bg = "#2A0A0A"; bd = "#CC3333"; ct = "#FF7777"
        elif ans_restants < 3:
            statut = f"⚠️ DANS {ans_restants:.1f} ANS"
            bg = "#2A1800"; bd = "#D4A017"; ct = "#FFD060"
        else:
            statut = f"⏳ DANS {ans_restants:.1f} ANS"
            bg = "#1A0D12"; bd = "#2D3A55"; ct = "#AAAAAA"

        # Date cible
        date_cible = dn.replace(year=dn.year + age_j)
        date_str = date_cible.strftime('%B %Y')

        with st.expander(f"{label} — {age_j} ans ({date_str}) — {statut}"):
            st.markdown(f'<div style="color:#AAA;font-size:13px;margin-bottom:10px;">{desc}</div>', unsafe_allow_html=True)
            st.markdown("**Checklist :**")
            for item in checklist:
                st.markdown(f"- {item}")

# ─── PAGE CAF/PCH ─────────────────────────────────────────────────────────────
def page_caf_pch(profil, cap):
    titre("🏛️ MODULE AAH / CAF / PCH")

    aah = profil['aah_mensuel']
    pch = profil.get('pch_mensuel', 0)

    # PCH simulator
    titre("1. Simulateur PCH — Impact si MDPH ≥ 80%")
    st.info("La PCH (Prestation Compensation Handicap) est cumulable avec l'AAH si taux ≥ 80%.")

    c1,c2 = st.columns(2)
    with c1:
        pch_sim = st.slider("PCH simulée (€/mois)", 0, 1500, 500, 50)
        C = capital_total(cap)
        r = profil['rendement_annuel']
        rail = profil['rail_mensuel']
        loyer = profil['loyer_net']
        mois = mois_restants(profil)

        # Calcul C92 sans et avec PCH
        def c92_simple(aah_s, pch_s):
            r_m = (1+r)**(1/12)-1
            def A(n): return ((1+r)**n-1)/r_m if r_m>0 else n
            def P(n): return (1+r)**n
            pp1 = rail - aah_s - pch_s - loyer
            immo = 205000*(1.015**14)
            C64 = C*P(14)-pp1*A(14)+immo
            C75 = C64*P(11)-rail*A(11)
            return round(C75*P(17)-(rail-450)*A(17), 0)

        c92_base = c92_simple(aah, 0)
        c92_pch  = c92_simple(aah, pch_sim)
        gain = c92_pch - c92_base

    with c2:
        coul_g = "vert" if gain > 0 else "rouge"
        st.markdown(f'<div style="background:#1A0D12;border-radius:10px;padding:16px;"><div style="color:#BBA888;font-size:12px;margin-bottom:8px;">IMPACT PCH {pch_sim}€/MOIS</div><div style="color:#CCBBAA;margin:4px 0;">C92 sans PCH : <b>{c92_base:,.0f}€</b></div><div style="color:#4DFF99;font-size:18px;font-weight:700;">C92 avec PCH : {c92_pch:,.0f}€</div><div style="color:#4DFF99;font-size:22px;font-weight:900;margin-top:8px;">Gain : +{gain:,.0f} €</div><div style="color:#CCBBAA;font-size:12px;margin-top:4px;">sur 42 ans</div></div>', unsafe_allow_html=True)

    titre("2. Vérification CAF avant rachat AV")
    seuil = st.number_input("Seuil ressources CAF Isère (€/an) — à confirmer", value=12396.0, step=100.0)
    rachat = st.number_input("Rachat AV prévu ce mois (€)", value=10000.0, step=500.0)
    taux_pv = st.number_input("Taux PV dans ce rachat (%)", value=5.0, step=0.5)/100
    pv_generees = rachat * taux_pv
    ressources_caf = aah*12 + pch*12 + pv_generees
    marge = seuil - ressources_caf

    pch_caf = f"<div style='color:#CCBBAA;margin:3px 0;'>PCH : +{int(pch*12)}€/an</div>" if pch > 0 else ""
    marge_col = "#4DFF99" if marge > 500 else ("#FFD060" if marge > 0 else "#FF6666")
    marge_txt = "SECURISE" if marge > 500 else ("SURVEILLER" if marge > 0 else "BLOQUER LE RACHAT")
    caf_html = f'<div style="background:#1A0D12;border-radius:10px;padding:16px;margin-top:8px;"><div style="color:#BBA888;font-size:12px;margin-bottom:8px;">CALCUL RESSOURCES CAF</div><div style="color:#CCBBAA;margin:3px 0;">AAH : +{aah*12:,.0f}€/an</div>{pch_caf}<div style="color:#CCBBAA;margin:3px 0;">PV rachat AV : +{pv_generees:,.0f}€</div><div style="border-top:1px solid #2A0A12;margin:8px 0;"></div><div style="color:#FFF;font-weight:700;">Total ressources : {ressources_caf:,.0f}€/an</div><div style="color:#FFF;">Seuil CAF : {seuil:,.0f}€/an</div><div style="color:{marge_col};font-size:18px;font-weight:700;margin-top:8px;">Marge : {marge:+,.0f}€ - {marge_txt}</div></div>'
    st.markdown(caf_html, unsafe_allow_html=True)

    if marge < 0:
        alerte('rouge', "🔴 Ce rachat mettrait les ressources CAF au-dessus du seuil. AAH risque d'être révisée. NE PAS RACHETER. Contacter CAF Isère avant toute action.")
    st.caption("Rappel : seules les PLUS-VALUES AV comptent pour la CAF. Le capital remboursé ne compte pas.")

    titre("3. Scénarios AAH — Impact sur le plan")
    scenarios_aah = [
        ("MDPH 75% — AAH s'arrête à 64 ans", 64, 0),
        ("MDPH ≥80% — AAH jusqu'à 67 ans", 67, 0),
        ("MDPH ≥80% + PCH 300€/mois", 67, 300),
        ("MDPH ≥80% + PCH 500€/mois", 67, 500),
        ("MDPH ≥80% + PCH 800€/mois", 67, 800),
    ]
    rows = []
    for label, age_fin, pch_s in scenarios_aah:
        c92_s = c92_simple(aah + pch_s, 0)
        gain_s = c92_s - c92_base
        ok = "✅" if c92_s >= 50000 else "⚠️"
        rows.append(f"| {label} | {c92_s:,.0f}€ | {gain_s:+,.0f}€ | {ok} |")
    header = "| Scénario | C92 | Gain vs base | |\n|---|---|---|---|"
    st.markdown(header + "\n" + "\n".join(rows))


# ─── PAGE INFLATION ───────────────────────────────────────────────────────────
def page_inflation(profil, cap):
    titre("📈 MODULE INFLATION — POUVOIR D'ACHAT RÉEL")

    C = capital_total(cap)
    r = profil['rendement_annuel']
    rail = profil['rail_mensuel']
    aah = profil['aah_mensuel']
    loyer = profil['loyer_net']

    inf = st.slider("Taux d'inflation annuel (%)", 0.0, 4.0, 1.5, 0.1) / 100
    st.markdown(f'<div style="background:#1A0D12;border-radius:8px;padding:12px 16px;margin:8px 0;color:#CCBBAA;font-size:13px;">Avec une inflation de <b>{inf*100:.1f}%/an</b>, 2 760€/mois aujourd hui vaudront <b>{rail*(1+inf)**10:,.0f}€/mois dans 10 ans</b> et <b>{rail*(1+inf)**20:,.0f}€/mois dans 20 ans</b> en pouvoir d achat reel.</div>', unsafe_allow_html=True)

    r_m = (1+r)**(1/12)-1
    def A(n): return ((1+r)**n-1)/r_m if r_m>0 else n
    def P(n): return (1+r)**n
    pp1 = rail - aah - loyer
    immo = 205000*(1.015**14)
    C64 = C*P(14)-pp1*A(14)+immo
    C75 = C64*P(11)-rail*A(11)
    C92_nom = C75*P(17)-(rail-450)*A(17)

    # En valeur réelle (déflatée)
    pts_nom = {}; pts_reel = {}
    for age in [50,56,60,64,70,75,80,85,90,92]:
        n = age-50
        if age<=64: v=C*P(n)-pp1*A(n)
        elif age<=75: v=C64*P(age-64)-rail*A(age-64)
        else: v=C75*P(age-75)-(rail-450)*A(age-75)
        pts_nom[age]=round(v,0)
        pts_reel[age]=round(v/(1+inf)**n, 0)

    c1,c2 = st.columns(2)
    with c1:
        kpi("C92 nominal", f"{C92_nom:,.0f} €", "Valeur face aux billets", "bleu")
    with c2:
        c92_reel = pts_reel[92]
        coul = "vert" if c92_reel >= 50000 else "orange"
        kpi("C92 en pouvoir d'achat réel", f"{c92_reel:,.0f} €", f"Ce que valent ces euros en 2026 · inflation {inf*100:.1f}%/an", coul)

    titre("Trajectoire nominale vs réelle")
    try:
        import plotly.graph_objects as go
        ages = list(pts_nom.keys())
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=ages, y=list(pts_nom.values()), name="Nominal",
            line=dict(color='#C4922A',width=2), mode='lines+markers'))
        fig.add_trace(go.Scatter(x=ages, y=list(pts_reel.values()), name="Pouvoir d'achat réel",
            line=dict(color='#D4A017',width=2,dash='dash'), mode='lines+markers'))
        fig.add_hline(y=50000, line_dash="dot", line_color="#1A6B4B", annotation_text="Cible 50k€")
        fig.update_layout(plot_bgcolor='#140810',paper_bgcolor='#140810',font_color='#CCC',
            height=300,margin=dict(t=20,b=0,l=0,r=0),
            xaxis=dict(gridcolor='#2A0A12'),yaxis=dict(gridcolor='#2A0A12'),
            legend=dict(bgcolor='#140810'))
        st.plotly_chart(fig, use_container_width=True)
    except: pass

    titre("💡 Option : Rail indexé sur inflation")
    st.markdown("Et si on augmentait la pioche de 1,5%/an pour maintenir le pouvoir d'achat ?")

    # Rail croissant
    r_m2 = (1+r)**(1/12)-1
    rail_croissant_c92 = None
    c_sim = C; rail_sim = rail
    for annee in range(42):
        croissance = rail_sim * (1+inf) / 12
        c_sim = c_sim * (1+r)**(1/12) - croissance
    c_sim_final = c_sim
    coul_croiss = "vert" if c_sim_final >= 50000 else "rouge"
    kpi(f"C92 avec rail +{inf*100:.1f}%/an", f"{c_sim_final:,.0f} €",
        f"Rail à 92 ans : {rail*(1+inf)**42:,.0f}€/mois · Faisable si capital suffisant", coul_croiss)



def main():
    if 'connected' not in st.session_state:
        st.session_state.connected = False
    if 'menu_ouvert' not in st.session_state:
        st.session_state.menu_ouvert = True
    if not st.session_state.connected:
        st.markdown('<style>section[data-testid="stSidebar"]{display:none!important;}</style>', unsafe_allow_html=True)
        st.markdown('<div style="text-align:center;padding:80px 0 20px 0;"><span style="font-family:Garamond,Georgia,serif;font-size:72px;font-weight:300;font-style:italic;letter-spacing:20px;background:linear-gradient(90deg, #8B0000, #C4922A, #FFD060, #C4922A, #8B0000);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">COCKPIT</span></div>', unsafe_allow_html=True)
        st.markdown('<div style="text-align:center;"><span style="font-family:Garamond,Georgia,serif;font-size:28px;letter-spacing:10px;background:linear-gradient(90deg, #665544, #BBA888, #C4922A, #BBA888, #665544);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">P A T R I M O N I A L</span></div>', unsafe_allow_html=True)
        st.markdown('<div style="text-align:center;padding:30px 0;"><span style="font-family:Garamond,Georgia,serif;font-size:18px;color:#BBA888;font-style:italic;letter-spacing:4px;">2026 &middot;&middot;&middot; 2067</span></div>', unsafe_allow_html=True)
        st.markdown('<div style="text-align:center;padding:0 0 40px 0;"><span style="font-family:Georgia,serif;font-size:14px;color:#665544;">v4.4 &mdash; Raphael</span></div>', unsafe_allow_html=True)
        c1, c2, c3 = st.columns([3, 2, 3])
        with c2:
            if st.button("C O N N E X I O N", use_container_width=True):
                st.session_state.connected = True
                st.rerun()
        return
    init_db()
    try:
        profil=get_profil(); cap=get_capital()
    except Exception as e:
        st.error(f"Erreur connexion base : {e}")
        st.stop()
    if not profil or not cap:
        st.error("Erreur base de donnees."); return
    age=age_actuel(profil); C=capital_total(cap)
    if st.session_state.menu_ouvert:
        # Sidebar ouverte — bouton ❮ en haut de la sidebar
        st.markdown(f'<style>section[data-testid="stSidebar"]{{display:block!important;visibility:visible!important;}}</style>', unsafe_allow_html=True)
        with st.sidebar:
            if st.button("❮", key="btn_fermer"):
                st.session_state.menu_ouvert = False
                st.rerun()
            st.markdown('<div style="text-align:center;padding:10px 0;"><span style="font-family:Garamond,Georgia,serif;font-size:24px;color:#FFD060;font-weight:700;">COCKPIT</span></div>', unsafe_allow_html=True)
            st.markdown(f'<div style="color:#CCBBAA;font-size:13px;text-align:center;margin-bottom:12px;">{age:.1f} ans | {C:,.0f} EUR<br>Rail {profil["rail_mensuel"]:,.0f} EUR</div>', unsafe_allow_html=True)
            al=calculer_alertes(profil,cap)
            nr=sum(1 for n,_ in al if n=='rouge')
            no=sum(1 for n,_ in al if n=='orange')
            if nr: st.markdown(f'<div style="color:#FF7777;text-align:center;font-size:12px;">{nr} alerte(s) rouge(s)</div>', unsafe_allow_html=True)
            elif no: st.markdown(f'<div style="color:#FFD060;text-align:center;font-size:12px;">{no} alerte(s) orange</div>', unsafe_allow_html=True)
            else: st.markdown('<div style="color:#4DFF99;text-align:center;font-size:12px;">Aucune alerte</div>', unsafe_allow_html=True)
            st.markdown("---")
            page=st.radio("Navigation",[
                "Dashboard",
                "Moteur ARVA",
                "Suivi AV x 3",
                "Simulateur",
                "Fiscal & CAF",
                "Impots",
                "LMNP & IRL",
                "Jalons",
                "AAH / PCH",
                "Inflation",
                "Saisie capital",
            ], label_visibility="collapsed")
            st.markdown("---")
            st.caption("v4.4")
    else:
        # Sidebar fermee — petit bouton ❯ meme position que ❮
        st.markdown('<style>section[data-testid="stSidebar"]{display:none!important;}</style>', unsafe_allow_html=True)
        if st.button("❯", key="btn_ouvrir"):
            st.session_state.menu_ouvert = True
            st.rerun()
        page = st.session_state.get("_last_page", "Dashboard")
    st.session_state["_last_page"] = page
    {
        "Dashboard":      lambda: page_dashboard(profil,cap),
        "Moteur ARVA":    lambda: page_arva(profil,cap),
        "Suivi AV x 3":  lambda: page_suivi_av(profil,cap),
        "Simulateur":     lambda: page_simulateur(profil,cap),
        "Fiscal & CAF":   lambda: page_fiscal(profil,cap),
        "Impots":         lambda: page_impots(profil,cap),
        "LMNP & IRL":     lambda: page_lmnp(profil,cap),
        "Jalons":         lambda: page_jalons(profil,cap),
        "AAH / PCH":      lambda: page_caf_pch(profil,cap),
        "Inflation":      lambda: page_inflation(profil,cap),
        "Saisie capital": lambda: page_saisie(profil,cap),
    }[page]()

if __name__=="__main__":
    main()
