p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

idx = t.find('def page_jalons(profil, cap):')
next_def = t.find(chr(10)+'def ', idx+10)

new_jalons = '''def page_jalons(profil, cap):
    from datetime import date, timedelta
    import sqlite3
    today = date.today()
    titre("PLANNING PATRIMONIAL - SUIVI EN TEMPS REEL")

    db = sqlite3.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
    db.row_factory = sqlite3.Row
    c = db.cursor()
    c.execute("SELECT * FROM chronologie ORDER BY date_cible ASC")
    rows = [dict(r) for r in c.fetchall()]
    db.close()

    capital_reel = 0
    for r in rows:
        if r['fait'] == 1 and r['montant'] > 0:
            mr = r['montant_reel'] if r['montant_reel'] else r['montant']
            if r['sens'] == 'entree':
                capital_reel += mr
            elif r['sens'] == 'sortie':
                capital_reel -= mr

    st.markdown(f'<div style="background:linear-gradient(145deg, #1A0D12 0%, #150A10 100%);border:2px solid #1A6B4B;border-radius:12px;padding:20px;text-align:center;margin-bottom:20px;"><div style="color:#BBA888;font-size:12px;text-transform:uppercase;">CAPITAL REEL CUMULE</div><div style="color:#4DFF99;font-size:42px;font-weight:900;">{capital_reel:,.0f} EUR</div><div style="color:#DDCCBB;font-size:13px;">Base sur les flux confirmes</div></div>', unsafe_allow_html=True)

    a_faire = [r for r in rows if r['fait'] == 0]
    fait = [r for r in rows if r['fait'] == 1]

    a_confirmer_1m = []
    a_confirmer_6m = []
    for r in fait:
        if r.get('date_reelle') and r['montant'] > 0:
            try:
                dr = date.fromisoformat(r['date_reelle'])
                jours = (today - dr).days
                if jours >= 30 and r.get('confirme_1mois',0) == 0:
                    a_confirmer_1m.append(r)
                if jours >= 180 and r.get('confirme_6mois',0) == 0:
                    a_confirmer_6m.append(r)
            except:
                pass

    if a_confirmer_1m:
        titre("CONFIRMATION 1 MOIS")
        for r in a_confirmer_1m:
            ecart = (r.get('montant_reel',0) or r['montant']) - r['montant']
            st.markdown(f'<div style="background:#2A1800;border:2px solid #D4A017;border-radius:8px;padding:12px;margin:8px 0;"><span style="color:#FFD060;font-weight:700;">{r["action"]}</span><br><span style="color:#F0E6D8;">Prevu: {r["montant"]:,.0f} EUR | Reel: {r.get("montant_reel",0):,.0f} EUR | Ecart: {ecart:+,.0f} EUR</span></div>', unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Confirmer 1 mois", key=f"c1m_{r['id']}"):
                    db2 = sqlite3.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
                    db2.execute("UPDATE chronologie SET confirme_1mois=1, date_confirme_1mois=? WHERE id=?", (str(today), r['id']))
                    db2.commit(); db2.close(); st.rerun()
            with col2:
                nv = st.number_input("Corriger", value=float(r.get('montant_reel',0) or r['montant']), key=f"corr1_{r['id']}")
                if st.button("Corriger", key=f"fix1_{r['id']}"):
                    db2 = sqlite3.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
                    db2.execute("UPDATE chronologie SET montant_reel=? WHERE id=?", (nv, r['id']))
                    db2.commit(); db2.close(); st.rerun()

    if a_confirmer_6m:
        titre("VERROUILLAGE 6 MOIS")
        for r in a_confirmer_6m:
            st.markdown(f'<div style="background:#1A0A0A;border:2px solid #CC3333;border-radius:8px;padding:12px;margin:8px 0;"><span style="color:#FF7777;font-weight:700;">{r["action"]}</span><br><span style="color:#F0E6D8;">Montant final: {r.get("montant_reel",0):,.0f} EUR</span></div>', unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Verrouiller", key=f"c6m_{r['id']}"):
                    db2 = sqlite3.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
                    db2.execute("UPDATE chronologie SET confirme_6mois=1, date_confirme_6mois=? WHERE id=?", (str(today), r['id']))
                    db2.commit(); db2.close(); st.rerun()
            with col2:
                nv6 = st.number_input("Derniere correction", value=float(r.get('montant_reel',0) or r['montant']), key=f"corr6_{r['id']}")
                if st.button("Corriger et verrouiller", key=f"fix6_{r['id']}"):
                    db2 = sqlite3.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
                    db2.execute("UPDATE chronologie SET montant_reel=?, confirme_6mois=1, date_confirme_6mois=? WHERE id=?", (nv6, str(today), r['id']))
                    db2.commit(); db2.close(); st.rerun()

    titre("A VENIR")
    for r in a_faire:
        try:
            dt = date.fromisoformat(r['date_cible'])
            jours = (dt - today).days
        except:
            jours = 0
        badge = "#4DFF99" if r['sens']=="entree" else ("#FF7777" if r['sens']=="sortie" else "#FFD060")
        flux_txt = f"+{r['montant']:,.0f}" if r['sens']=="entree" else (f"-{r['montant']:,.0f}" if r['sens']=="sortie" else "")
        jours_txt = f"Dans {jours} jours" if jours > 0 else "Maintenant"

        st.markdown(f'<div style="background:#140810;border-left:3px solid {badge};border-radius:0 8px 8px 0;padding:12px 16px;margin:6px 0;"><div style="display:flex;justify-content:space-between;"><div><span style="color:#F0E6D8;font-size:14px;font-weight:600;">{r["action"]}</span><br><span style="color:#BBA888;font-size:11px;">{jours_txt} | {r["date_cible"]}</span></div><div style="text-align:right;"><span style="color:{badge};font-size:16px;font-weight:700;">{flux_txt} EUR</span></div></div></div>', unsafe_allow_html=True)

        if r['montant'] > 0:
            with st.expander(f"Saisir : {r['action'][:50]}"):
                cd, cm = st.columns(2)
                with cd:
                    date_r = st.date_input("Date reelle", value=today, key=f"dr_{r['id']}")
                with cm:
                    montant_r = st.number_input("Montant reel (EUR)", value=float(r['montant']), key=f"mr_{r['id']}")
                ecart = montant_r - r['montant']
                if abs(ecart) > 0:
                    pct = ecart/r['montant']*100 if r['montant'] else 0
                    coul = "#FF7777" if abs(pct) > 5 else "#FFD060"
                    st.markdown(f'<div style="color:{coul};font-size:14px;font-weight:700;">Ecart: {ecart:+,.0f} EUR ({pct:+.1f}%)</div>', unsafe_allow_html=True)
                if st.button("Valider", key=f"val_{r['id']}"):
                    db2 = sqlite3.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
                    db2.execute("UPDATE chronologie SET fait=1, montant_reel=?, date_reelle=? WHERE id=?", (montant_r, str(date_r), r['id']))
                    db2.commit(); db2.close(); st.rerun()
        elif r['sens'] == 'info':
            if st.button("Fait", key=f"fait_{r['id']}"):
                db2 = sqlite3.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
                db2.execute("UPDATE chronologie SET fait=1, date_reelle=? WHERE id=?", (str(today), r['id']))
                db2.commit(); db2.close(); st.rerun()

    if fait:
        titre("DEJA FAIT")
        for r in fait:
            mr = r.get('montant_reel',0) if r.get('montant_reel',0) else r['montant']
            flux_txt = f"+{mr:,.0f}" if r['sens']=="entree" else (f"-{mr:,.0f}" if r['sens']=="sortie" else "")
            locks = ""
            if r.get('confirme_1mois'): locks += " [1M]"
            if r.get('confirme_6mois'): locks += " [6M]"
            st.markdown(f'<div style="color:#4DFF99;font-size:13px;padding:4px 16px;">{r.get("date_reelle","") or r["date_cible"]} | {r["action"]} | {flux_txt} EUR{locks}</div>', unsafe_allow_html=True)

'''

t = t[:idx] + new_jalons + t[next_def:]

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print('Page Jalons installee')

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
