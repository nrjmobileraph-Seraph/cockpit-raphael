p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# 1. Trouver page_caf_pch et ajouter saisie AAH
idx = t.find('def page_caf_pch(profil, cap):')
next_def = t.find(chr(10)+'def ', idx+10)
old_caf = t[idx:next_def]

new_caf = '''def page_caf_pch(profil, cap):
    from datetime import date
    import sqlite3
    today = date.today()
    annee = str(today.year)

    st.subheader("AAH / CAF / PCH")

    # Lire AAH suivi
    db = sqlite3.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
    db.row_factory = sqlite3.Row
    c = db.cursor()
    c.execute("SELECT * FROM aah_suivi ORDER BY mois ASC")
    rows = [dict(r) for r in c.fetchall()]
    db.close()

    # AAH annee en cours
    aah_courante = None
    for r in rows:
        if r['mois'] == annee:
            aah_courante = r
            break

    st.subheader("AAH - Suivi annuel")

    if aah_courante:
        prevu = aah_courante['montant_prevu']
        reel = aah_courante['montant_reel']
        affiche = reel if reel > 0 else prevu

        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("AAH prevue " + annee, f"{prevu:,.0f} EUR/mois")
        with c2:
            st.metric("AAH reelle " + annee, f"{reel:,.0f} EUR/mois" if reel > 0 else "Pas encore saisie")
        with c3:
            st.metric("AAH utilisee dans les calculs", f"{affiche:,.0f} EUR/mois")

        st.divider()
        st.write("**Saisir le montant AAH reel pour cette annee :**")
        nouveau = st.number_input("Montant AAH mensuel reel (EUR)", value=float(reel if reel > 0 else prevu), key="aah_saisie")
        if st.button("Enregistrer AAH " + annee):
            db2 = sqlite3.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
            db2.execute("UPDATE aah_suivi SET montant_reel=?, date_saisie=? WHERE mois=?", (nouveau, str(today), annee))
            db2.commit()
            db2.close()
            st.success(f"AAH {annee} enregistree : {nouveau:,.0f} EUR/mois")
            st.rerun()
    else:
        st.info(f"Pas de prevision AAH pour {annee}")

    # Tableau complet
    st.divider()
    st.subheader("Historique AAH prevu vs reel")
    for r in rows:
        reel_txt = f"{r['montant_reel']:,.0f} EUR" if r['montant_reel'] > 0 else "—"
        prevu_txt = f"{r['montant_prevu']:,.0f} EUR"
        ecart = ""
        if r['montant_reel'] > 0 and r['montant_reel'] != r['montant_prevu']:
            diff = r['montant_reel'] - r['montant_prevu']
            ecart = f" (ecart: {diff:+,.0f} EUR)"
        st.write(f"**{r['mois']}** | Prevu: {prevu_txt} | Reel: {reel_txt}{ecart}")
        if r.get('note'):
            st.caption(r['note'])

    # PCH
    st.divider()
    st.subheader("PCH - Prestation Compensation Handicap")
    pch = profil.get('pch_mensuel', 0)
    st.metric("PCH mensuelle", f"{pch:,.0f} EUR/mois")
    st.caption("La PCH est versee par le departement pour compenser les consequences du handicap.")

    # Resume
    st.divider()
    st.subheader("Resume mensuel")
    aah_m = 0
    if aah_courante:
        aah_m = aah_courante['montant_reel'] if aah_courante['montant_reel'] > 0 else aah_courante['montant_prevu']
    loyer = profil.get('loyer_net', 0)
    parents = 325
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("AAH", f"+{aah_m:,.0f} EUR")
    with c2:
        st.metric("Loyers LMNP", f"+{loyer:,.0f} EUR")
    with c3:
        st.metric("Versement parents", f"-{parents:,.0f} EUR")
    with c4:
        reste = aah_m + loyer - parents
        st.metric("Reste pour vivre", f"{reste:,.0f} EUR")

'''

t = t[:idx] + new_caf + t[next_def:]

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print('Page AAH/CAF/PCH mise a jour')

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
