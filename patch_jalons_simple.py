p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

idx = t.find('def page_jalons(profil, cap):')
next_def = t.find(chr(10)+'def ', idx+10)

new_jalons = '''def page_jalons(profil, cap):
    from datetime import date
    import sqlite3
    today = date.today()
    st.subheader("PLANNING PATRIMONIAL - SUIVI EN TEMPS REEL")

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

    st.metric("CAPITAL REEL CUMULE", f"{capital_reel:,.0f} EUR", delta="Base sur les flux confirmes")
    st.divider()

    a_faire = [r for r in rows if r['fait'] == 0]
    fait = [r for r in rows if r['fait'] == 1]

    # Confirmations 1 mois
    for r in fait:
        if r.get('date_reelle') and r['montant'] > 0:
            try:
                dr = date.fromisoformat(r['date_reelle'])
                jours = (today - dr).days
                if jours >= 30 and r.get('confirme_1mois', 0) == 0:
                    ecart = (r.get('montant_reel', 0) or r['montant']) - r['montant']
                    st.warning(f"CONFIRMATION 1 MOIS : {r['action']} | Prevu: {r['montant']:,.0f} EUR | Reel: {r.get('montant_reel',0):,.0f} EUR | Ecart: {ecart:+,.0f} EUR")
                    c1, c2 = st.columns(2)
                    with c1:
                        if st.button("Confirmer", key=f"c1m_{r['id']}"):
                            db2 = sqlite3.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
                            db2.execute("UPDATE chronologie SET confirme_1mois=1, date_confirme_1mois=? WHERE id=?", (str(today), r['id']))
                            db2.commit(); db2.close(); st.rerun()
                    with c2:
                        nv = st.number_input("Corriger montant", value=float(r.get('montant_reel', 0) or r['montant']), key=f"corr1_{r['id']}")
                        if st.button("Corriger", key=f"fix1_{r['id']}"):
                            db2 = sqlite3.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
                            db2.execute("UPDATE chronologie SET montant_reel=? WHERE id=?", (nv, r['id']))
                            db2.commit(); db2.close(); st.rerun()
                if jours >= 180 and r.get('confirme_6mois', 0) == 0:
                    st.error(f"VERROUILLAGE 6 MOIS : {r['action']} | Montant: {r.get('montant_reel',0):,.0f} EUR")
                    c1, c2 = st.columns(2)
                    with c1:
                        if st.button("Verrouiller", key=f"c6m_{r['id']}"):
                            db2 = sqlite3.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
                            db2.execute("UPDATE chronologie SET confirme_6mois=1, date_confirme_6mois=? WHERE id=?", (str(today), r['id']))
                            db2.commit(); db2.close(); st.rerun()
                    with c2:
                        nv6 = st.number_input("Derniere correction", value=float(r.get('montant_reel', 0) or r['montant']), key=f"corr6_{r['id']}")
                        if st.button("Corriger et verrouiller", key=f"fix6_{r['id']}"):
                            db2 = sqlite3.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
                            db2.execute("UPDATE chronologie SET montant_reel=?, confirme_6mois=1, date_confirme_6mois=? WHERE id=?", (nv6, str(today), r['id']))
                            db2.commit(); db2.close(); st.rerun()
            except:
                pass

    # A venir
    st.subheader("A VENIR")
    for r in a_faire:
        try:
            dt = date.fromisoformat(r['date_cible'])
            jours = (dt - today).days
        except:
            jours = 0
        jours_txt = f"Dans {jours} jours" if jours > 0 else "Maintenant"
        if r['sens'] == 'entree':
            icone = "+"
        elif r['sens'] == 'sortie':
            icone = "-"
        else:
            icone = ""
        flux_txt = f"{icone}{r['montant']:,.0f} EUR" if r['montant'] > 0 else ""

        col1, col2, col3 = st.columns([4, 2, 1])
        with col1:
            st.write(f"**{r['action']}**")
            st.caption(f"{jours_txt} | {r['date_cible']}")
        with col2:
            if flux_txt:
                st.write(f"**{flux_txt}**")
        with col3:
            if r['montant'] > 0:
                pass
            elif r['sens'] == 'info':
                if st.button("Fait", key=f"fait_{r['id']}"):
                    db2 = sqlite3.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
                    db2.execute("UPDATE chronologie SET fait=1, date_reelle=? WHERE id=?", (str(today), r['id']))
                    db2.commit(); db2.close(); st.rerun()

        if r['montant'] > 0:
            with st.expander(f"Saisir le montant reel"):
                cd, cm = st.columns(2)
                with cd:
                    date_r = st.date_input("Date reelle", value=today, key=f"dr_{r['id']}")
                with cm:
                    montant_r = st.number_input("Montant reel (EUR)", value=float(r['montant']), key=f"mr_{r['id']}")
                ecart = montant_r - r['montant']
                if abs(ecart) > 0:
                    pct = ecart / r['montant'] * 100 if r['montant'] else 0
                    if abs(pct) > 5:
                        st.error(f"Ecart: {ecart:+,.0f} EUR ({pct:+.1f}%) - Verifiez le montant")
                    else:
                        st.warning(f"Ecart: {ecart:+,.0f} EUR ({pct:+.1f}%)")
                if st.button("Valider", key=f"val_{r['id']}"):
                    db2 = sqlite3.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
                    db2.execute("UPDATE chronologie SET fait=1, montant_reel=?, date_reelle=? WHERE id=?", (montant_r, str(date_r), r['id']))
                    db2.commit(); db2.close(); st.rerun()
        st.divider()

    # Deja fait
    if fait:
        st.subheader("DEJA FAIT")
        for r in fait:
            mr = r.get('montant_reel', 0) if r.get('montant_reel', 0) else r['montant']
            icone = "+" if r['sens'] == 'entree' else ("-" if r['sens'] == 'sortie' else "")
            flux_txt = f"{icone}{mr:,.0f} EUR" if mr > 0 else ""
            locks = ""
            if r.get('confirme_1mois'): locks += " [1M]"
            if r.get('confirme_6mois'): locks += " [6M]"
            st.write(f"{r.get('date_reelle', '') or r['date_cible']} | {r['action']} | {flux_txt}{locks}")

'''

t = t[:idx] + new_jalons + t[next_def:]

f = open(p, 'w', encoding='utf-8')
f.write(t)
f.close()
print('Page Jalons simplifiee installee')

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
