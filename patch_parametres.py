p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

idx = t.find('def page_export(profil, cap):')

new_params = '''def page_parametres(profil, cap):
    import sqlite3
    st.subheader("PARAMETRES DU COCKPIT")
    st.caption("Parametres figes par defaut. Modifiables avec double confirmation.")

    st.subheader("Profil financier")
    col1, col2 = st.columns(2)
    with col1:
        rail = st.number_input("Rail mensuel (EUR)", value=float(profil['rail_mensuel']), step=100.0, key="p_rail")
        aah = st.number_input("AAH mensuelle reference (EUR)", value=float(profil['aah_mensuel']), step=50.0, key="p_aah")
        loyer = st.number_input("Loyer net LMNP (EUR/mois)", value=float(profil['loyer_net']), step=10.0, key="p_loyer")
        taux_mdph = st.number_input("Taux MDPH (%)", value=int(profil['taux_mdph']), step=5, key="p_mdph")
    with col2:
        rendement = st.number_input("Rendement annuel (%)", value=float(profil['rendement_annuel'])*100, step=0.1, key="p_rend")
        age_cible = st.number_input("Age cible (ans)", value=int(profil['age_cible']), step=1, key="p_age")
        capital_cible = st.number_input("Capital cible final (EUR)", value=int(profil['capital_cible']), step=5000, key="p_cap_cible")

    # Detecter changements
    changes = []
    if rail != profil['rail_mensuel']: changes.append(f"Rail : {profil['rail_mensuel']:,.0f} -> {rail:,.0f}")
    if aah != profil['aah_mensuel']: changes.append(f"AAH : {profil['aah_mensuel']:,.0f} -> {aah:,.0f}")
    if loyer != profil['loyer_net']: changes.append(f"Loyer : {profil['loyer_net']:,.0f} -> {loyer:,.0f}")
    if abs(rendement/100 - profil['rendement_annuel']) > 0.001: changes.append(f"Rendement : {profil['rendement_annuel']*100:.1f}% -> {rendement:.1f}%")
    if age_cible != profil['age_cible']: changes.append(f"Age cible : {profil['age_cible']} -> {age_cible}")
    if capital_cible != profil['capital_cible']: changes.append(f"Capital cible : {profil['capital_cible']:,} -> {capital_cible:,}")
    if taux_mdph != profil['taux_mdph']: changes.append(f"MDPH : {profil['taux_mdph']}% -> {taux_mdph}%")

    if changes:
        st.divider()
        st.warning("Modifications detectees :")
        for ch in changes:
            st.write(f"  {ch}")

        # Double confirmation
        if 'confirm_step' not in st.session_state:
            st.session_state.confirm_step = 0

        if st.session_state.confirm_step == 0:
            if st.button("Etape 1 : Je veux modifier ces parametres"):
                st.session_state.confirm_step = 1
                st.rerun()
        elif st.session_state.confirm_step == 1:
            st.error("ATTENTION : ces parametres impactent TOUS les calculs du cockpit.")
            if st.button("Etape 2 : JE CONFIRME la modification"):
                db = sqlite3.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
                db.execute("""UPDATE profil SET
                    rail_mensuel=?, aah_mensuel=?, loyer_net=?,
                    rendement_annuel=?, age_cible=?, capital_cible=?,
                    taux_mdph=?
                    WHERE id=1""",
                    (rail, aah, loyer, rendement/100, age_cible, capital_cible, taux_mdph))
                db.commit()
                db.close()
                st.session_state.confirm_step = 0
                st.success("Parametres enregistres avec succes")
                st.rerun()
            if st.button("Annuler"):
                st.session_state.confirm_step = 0
                st.rerun()
    else:
        st.success("Aucune modification detectee - parametres inchanges")

    st.divider()
    st.subheader("Poches de capital")
    db2 = sqlite3.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
    db2.row_factory = sqlite3.Row
    c2 = db2.cursor()
    c2.execute("SELECT * FROM capital ORDER BY date DESC LIMIT 1")
    cap_row = dict(c2.fetchone())
    db2.close()

    col_a, col_b = st.columns(2)
    with col_a:
        cc = st.number_input("Compte courant", value=float(cap_row['cc']), step=100.0, key="pc_cc")
        livret_a = st.number_input("Livret A", value=float(cap_row['livret_a']), step=500.0, key="pc_la")
        ldds = st.number_input("LDDS", value=float(cap_row['ldds']), step=500.0, key="pc_ldds")
        lep = st.number_input("LEP", value=float(cap_row['lep']), step=500.0, key="pc_lep")
    with col_b:
        av1 = st.number_input("AV1", value=float(cap_row['av1']), step=1000.0, key="pc_av1")
        av2 = st.number_input("AV2", value=float(cap_row['av2']), step=1000.0, key="pc_av2")
        av3 = st.number_input("AV3", value=float(cap_row['av3']), step=1000.0, key="pc_av3")

    total_new = cc + livret_a + ldds + lep + av1 + av2 + av3
    st.metric("Total apres modification", f"{total_new:,.0f} EUR")

    cap_changes = abs(total_new - 461000) > 1
    if cap_changes:
        st.warning(f"Capital modifie : {461000:,.0f} -> {total_new:,.0f} EUR (ecart {total_new-461000:+,.0f})")
        if 'cap_confirm' not in st.session_state:
            st.session_state.cap_confirm = 0
        if st.session_state.cap_confirm == 0:
            if st.button("Etape 1 : Je veux modifier le capital"):
                st.session_state.cap_confirm = 1
                st.rerun()
        elif st.session_state.cap_confirm == 1:
            st.error("ATTENTION : ceci modifie la base de tout le plan patrimonial.")
            if st.button("Etape 2 : JE CONFIRME le nouveau capital"):
                db3 = sqlite3.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
                from datetime import date
                db3.execute("""INSERT INTO capital
                    (date, cc, livret_a, ldds, lep, av1, av2, av3,
                     av1_rendement, av2_rendement, av3_rendement, note)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, 0.035, 0.035, 0.035, 'Modification parametres')""",
                    (str(date.today()), cc, livret_a, ldds, lep, av1, av2, av3))
                db3.commit()
                db3.close()
                st.session_state.cap_confirm = 0
                st.success(f"Capital enregistre : {total_new:,.0f} EUR")
                st.rerun()
            if st.button("Annuler modification capital"):
                st.session_state.cap_confirm = 0
                st.rerun()

    st.divider()
    st.subheader("Backup et restauration")
    import os
    backup_dir = 'C:/Users/BoulePiou/cockpit-raphael/backups'
    if os.path.exists(backup_dir):
        backups = sorted(os.listdir(backup_dir), reverse=True)
        st.write(f"**{len(backups)} backups disponibles**")
        for b in backups[:5]:
            st.caption(b)
    if st.button("Faire un backup maintenant"):
        import shutil
        from datetime import datetime
        os.makedirs(backup_dir, exist_ok=True)
        bp = os.path.join(backup_dir, f'cockpit_manual_{datetime.now().strftime("%Y%m%d_%H%M%S")}.db')
        shutil.copy2('C:/Users/BoulePiou/cockpit-raphael/cockpit.db', bp)
        st.success(f"Backup cree")

    st.divider()
    if os.path.exists(backup_dir):
        backups_list = sorted(os.listdir(backup_dir), reverse=True)
        if backups_list:
            st.warning("ATTENTION : restaurer un backup ecrase toutes les donnees actuelles.")
            choix = st.selectbox("Choisir un backup", backups_list, key="restore_bk")
            if st.button("Restaurer ce backup"):
                import shutil
                shutil.copy2(os.path.join(backup_dir, choix), 'C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
                st.success(f"Backup restaure. Rechargez la page.")
                st.rerun()

'''

t = t[:idx] + new_params + '\n' + t[idx:]

# Ajouter Parametres dans le menu
old_menu = '"Saisie capital"'
new_menu = '"Parametres","Saisie capital"'
if old_menu in t and '"Parametres"' not in t:
    t = t.replace(old_menu, new_menu)
    print('Menu Parametres ajoute')

# Ajouter le routage
old_route = 'if page=="Saisie capital"'
new_route = 'if page=="Parametres": page_parametres(profil,cap)\n    elif page=="Saisie capital"'
if 'page=="Parametres"' not in t:
    t = t.replace(old_route, new_route)
    print('Routage Parametres ajoute')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print('Page Parametres avec double confirmation installee')

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
