p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Remplacer la page jalons par la version chronologie
old_jalons = 'def page_jalons(profil, cap):'
new_jalons = '''def page_jalons(profil, cap):
    from datetime import datetime, date
    titre("CHRONOLOGIE COMPLETE - PILOTAGE AUTOMATIQUE")
    age = age_actuel(profil)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    try:
        rows = c.execute("SELECT date_cible,age_cible,action,montant,sens,categorie,auto,fait,note FROM chronologie ORDER BY date_cible").fetchall()
    except:
        rows = []
    conn.close()
    if not rows:
        st.warning("Aucune action en chronologie. Lancer patch_chrono.py.")
        return
    # Stats
    total = len(rows)
    faits = sum(1 for r in rows if r[7])
    auto = sum(1 for r in rows if r[6])
    st.markdown(f'<div style="background:#140810;border-radius:10px;padding:14px;margin-bottom:14px;"><div style="color:#E0D0B8;font-size:13px;">{faits}/{total} actions realisees | {auto} automatiques | {total-faits} restantes</div></div>', unsafe_allow_html=True)
    # Filtres
    cats = list(set(r[5] for r in rows))
    cats.sort()
    filtre = st.multiselect("Filtrer par categorie", cats, default=cats)
    for r in rows:
        dt_s, age_j, action, montant, sens, cat, is_auto, fait, note = r
        if cat not in filtre:
            continue
        try:
            dt = datetime.strptime(dt_s, '%Y-%m-%d')
            delta_j = (dt - datetime.today()).days
        except:
            delta_j = 0
        if fait:
            badge_col = "#1A6B4B"; badge_txt = "FAIT"; bg = "#0A1A0A"
        elif delta_j < 0:
            badge_col = "#CC3333"; badge_txt = "EN RETARD"; bg = "#2A0A0A"
        elif delta_j < 90:
            badge_col = "#CC3333"; badge_txt = "URGENT"; bg = "#2A0A0A"
        elif delta_j < 365:
            badge_col = "#D4A017"; badge_txt = f"{delta_j}j"; bg = "#1A1008"
        else:
            ans = delta_j / 365.25
            badge_col = "#C4922A"; badge_txt = f"{ans:.1f}ans"; bg = "#140810"
        auto_tag = " | AUTO" if is_auto else ""
        montant_tag = ""
        if montant > 0:
            if sens == "entree":
                montant_tag = f'<span style="color:#4DFF99;margin-left:10px;">+{montant:,.0f} EUR</span>'
            elif sens == "sortie":
                montant_tag = f'<span style="color:#FF7777;margin-left:10px;">-{montant:,.0f} EUR</span>'
            elif sens == "transfert":
                montant_tag = f'<span style="color:#FFD060;margin-left:10px;">{montant:,.0f} EUR</span>'
            elif sens == "perte":
                montant_tag = f'<span style="color:#FF7777;margin-left:10px;">{montant:,.0f} EUR/mois</span>'
        st.markdown(f'<div style="display:flex;align-items:flex-start;gap:12px;padding:10px 14px;background:{bg};border-radius:8px;margin:4px 0;border-left:3px solid {badge_col};"><div style="background:{badge_col};color:white;border-radius:6px;padding:3px 8px;font-size:11px;font-weight:700;white-space:nowrap;flex-shrink:0;">{badge_txt}</div><div><div style="color:#F0E6D8;font-size:13px;font-weight:600;">{action}{montant_tag}<span style="color:#C4922A;font-size:11px;margin-left:8px;">{cat}{auto_tag}</span></div><div style="color:#D0C0A8;font-size:12px;">{dt_s} | {age_j:.1f} ans | {note}</div></div></div>', unsafe_allow_html=True)
    return
def page_jalons_old(profil, cap):'''

t = t.replace(old_jalons, new_jalons, 1)

f = open(p, 'w', encoding='utf-8')
f.write(t)
f.close()
print('Page chronologie OK')
