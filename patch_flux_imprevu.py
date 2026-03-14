p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Ajouter le formulaire d'ajout de flux juste apres le titre de page_jalons
old = '    st.subheader("PLANNING PATRIMONIAL - SUIVI EN TEMPS REEL")'
new = '''    st.subheader("PLANNING PATRIMONIAL - SUIVI EN TEMPS REEL")

    with st.expander("Ajouter un flux impреvu"):
        import sqlite3 as sq2
        from datetime import date as dt2
        col_n, col_s = st.columns(2)
        with col_n:
            nom_flux = st.text_input("Description", placeholder="Ex: Remboursement CAF, aide exceptionnelle...")
        with col_s:
            sens_flux = st.selectbox("Type", ["entree", "sortie", "info"])
        col_m, col_d, col_c = st.columns(3)
        with col_m:
            montant_flux = st.number_input("Montant (EUR)", value=0.0, min_value=0.0, key="flux_mt")
        with col_d:
            date_flux = st.date_input("Date", value=dt2.today(), key="flux_dt")
        with col_c:
            cat_flux = st.selectbox("Categorie", ["impреvu", "caf", "sante", "famille", "administratif", "autre"])
        note_flux = st.text_input("Note (optionnel)", key="flux_note")
        deja_fait = st.checkbox("Deja encaisse/paye", value=True)
        if st.button("Ajouter ce flux"):
            if nom_flux:
                db3 = sq2.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
                age_val = 50.5
                fait_val = 1 if deja_fait else 0
                mr_val = montant_flux if deja_fait else 0
                dr_val = str(date_flux) if deja_fait else ''
                db3.execute("""INSERT INTO chronologie
                    (date_cible, age_cible, action, montant, sens, categorie, auto, fait, note, montant_reel, date_reelle)
                    VALUES (?,?,?,?,?,?,0,?,?,?,?)""",
                    (str(date_flux), age_val, nom_flux, montant_flux, sens_flux, cat_flux, fait_val, note_flux, mr_val, dr_val))
                db3.commit()
                db3.close()
                st.success(f"Flux ajoute : {nom_flux} | {sens_flux} | {montant_flux:,.0f} EUR")
                st.rerun()
            else:
                st.error("Donnez un nom au flux")'''

t = t.replace(old, new)

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print('Formulaire flux imprevu ajoute')

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
