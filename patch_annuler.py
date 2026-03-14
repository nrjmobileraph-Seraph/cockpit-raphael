p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Trouver la section DEJA FAIT dans page_jalons et ajouter un bouton annuler
old_fait = """    if fait:
        titre("DEJA FAIT")
        for r in fait:
            mr = r.get('montant_reel', 0) if r.get('montant_reel', 0) else r['montant']
            icone = "+" if r['sens'] == 'entree' else ("-" if r['sens'] == 'sortie' else "")
            flux_txt = f"{icone}{mr:,.0f} EUR" if mr > 0 else ""
            locks = ""
            if r.get('confirme_1mois'): locks += " [1M]"
            if r.get('confirme_6mois'): locks += " [6M]"
            st.write(f"{r.get('date_reelle', '') or r['date_cible']} | {r['action']} | {flux_txt}{locks}")"""

new_fait = """    if fait:
        titre("DEJA FAIT")
        for r in fait:
            mr = r.get('montant_reel', 0) if r.get('montant_reel', 0) else r['montant']
            icone = "+" if r['sens'] == 'entree' else ("-" if r['sens'] == 'sortie' else "")
            flux_txt = f"{icone}{mr:,.0f} EUR" if mr > 0 else ""
            locks = ""
            if r.get('confirme_1mois'): locks += " [1M]"
            if r.get('confirme_6mois'): locks += " [6M]"
            verrouille = r.get('confirme_6mois', 0) == 1
            col_f, col_a = st.columns([5, 1])
            with col_f:
                st.write(f"{r.get('date_reelle', '') or r['date_cible']} | {r['action']} | {flux_txt}{locks}")
            with col_a:
                if not verrouille:
                    if st.button("Annuler", key=f"undo_{r['id']}"):
                        db_u = sqlite3.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
                        db_u.execute("UPDATE chronologie SET fait=0, montant_reel=0, date_reelle='' WHERE id=?", (r['id'],))
                        db_u.commit()
                        db_u.close()
                        st.rerun()"""

if old_fait in t:
    t = t.replace(old_fait, new_fait)
    print('Bouton Annuler ajoute')
else:
    print('Section DEJA FAIT non trouvee exacte - recherche...')
    if 'DEJA FAIT' in t:
        print('DEJA FAIT present mais format different')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
