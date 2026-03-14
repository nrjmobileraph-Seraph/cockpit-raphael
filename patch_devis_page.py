p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Trouver page_lmnp
idx = t.find('def page_lmnp(profil, cap):')
# Trouver juste apres le premier st.subheader ou titre de cette page
# On va ajouter le suivi devis a la fin de page_lmnp, avant le next def
next_def = t.find(chr(10)+'def ', idx+10)

# Inserer le bloc devis juste avant la fin de page_lmnp
devis_block = '''
    # SUIVI DEVIS ARTISANS
    st.divider()
    st.subheader("SUIVI DEVIS ARTISANS - Budget 33 000 EUR")
    import sqlite3 as sqd
    dbd = sqd.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
    dbd.row_factory = sqd.Row
    cd = dbd.cursor()
    cd.execute("SELECT * FROM devis_artisans ORDER BY id ASC")
    devis = [dict(r) for r in cd.fetchall()]
    dbd.close()

    total_devis = sum(d['devis_montant'] for d in devis)
    total_paye = sum(d['paye_montant'] for d in devis)
    reste = 33000 - total_devis
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Total devis", f"{total_devis:,.0f} EUR", delta=f"sur 33 000 EUR")
    with c2:
        st.metric("Deja paye", f"{total_paye:,.0f} EUR")
    with c3:
        couleur_reste = "normal" if reste >= 0 else "inverse"
        st.metric("Marge restante", f"{reste:,.0f} EUR", delta="OK" if reste >= 0 else "DEPASSEMENT", delta_color=couleur_reste)

    if total_devis > 0:
        st.progress(min(int(total_devis / 33000 * 100), 100))

    for d in devis:
        icone = "a]" if d['statut'] == 'a_faire' else ("en cours" if d['statut'] == 'en_cours' else "fait")
        with st.expander(f"{d['corps_metier']} | Devis: {d['devis_montant']:,.0f} EUR | {d['statut']}"):
            st.caption(d['note'])
            ca, cm, cs = st.columns(3)
            with ca:
                artisan = st.text_input("Artisan", value=d['artisan'], key=f"art_{d['id']}")
            with cm:
                montant_d = st.number_input("Montant devis (EUR)", value=float(d['devis_montant']), key=f"dev_{d['id']}")
            with cs:
                statut_d = st.selectbox("Statut", ["a_faire", "en_cours", "devis_recu", "signe", "paye"], index=["a_faire", "en_cours", "devis_recu", "signe", "paye"].index(d['statut']) if d['statut'] in ["a_faire", "en_cours", "devis_recu", "signe", "paye"] else 0, key=f"st_{d['id']}")
            paye_d = st.number_input("Montant paye (EUR)", value=float(d['paye_montant']), key=f"pay_{d['id']}")
            if st.button("Enregistrer", key=f"sav_{d['id']}"):
                db4 = sqd.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
                db4.execute("UPDATE devis_artisans SET artisan=?, devis_montant=?, statut=?, paye_montant=? WHERE id=?",
                           (artisan, montant_d, statut_d, paye_d, d['id']))
                db4.commit()
                db4.close()
                st.success(f"{d['corps_metier']} mis a jour")
                st.rerun()

    with st.expander("Ajouter un corps de metier"):
        nc, nm = st.columns(2)
        with nc:
            new_corps = st.text_input("Nom du poste", key="new_corps")
        with nm:
            new_note = st.text_input("Note", key="new_note_corps")
        if st.button("Ajouter", key="add_corps"):
            if new_corps:
                db5 = sqd.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
                db5.execute("INSERT INTO devis_artisans (corps_metier, note) VALUES (?,?)", (new_corps, new_note))
                db5.commit()
                db5.close()
                st.rerun()

    if total_devis > 33000:
        st.error(f"ATTENTION : les devis depassent le budget de {total_devis - 33000:,.0f} EUR. Renegocier ou ajuster le plan.")
    elif total_devis > 29700:
        st.warning(f"Budget utilise a plus de 90% ({total_devis/33000*100:.0f}%). Attention a la marge.")

'''

t = t[:next_def] + devis_block + t[next_def:]

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print('Suivi devis artisans ajoute dans LMNP')

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
