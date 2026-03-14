p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Trouver le debut du dashboard Phase 0, juste apres le titre
old = '        titre("COCKPIT PATRIMONIAL - PHASE CONSTRUCTION")'
new = '''        titre("COCKPIT PATRIMONIAL - PHASE CONSTRUCTION")

        # Capital reel cumule depuis les jalons
        import sqlite3 as sq
        db_j = sq.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
        db_j.row_factory = sq.Row
        c_j = db_j.cursor()
        c_j.execute("SELECT * FROM chronologie ORDER BY date_cible ASC")
        rows_j = [dict(r) for r in c_j.fetchall()]
        db_j.close()
        capital_reel = 0
        for rj in rows_j:
            if rj['fait'] == 1 and rj['montant'] > 0:
                mr = rj['montant_reel'] if rj['montant_reel'] else rj['montant']
                if rj['sens'] == 'entree': capital_reel += mr
                elif rj['sens'] == 'sortie': capital_reel -= mr
        objectif_capital = 461000
        pct = int(capital_reel / objectif_capital * 100) if objectif_capital > 0 else 0
        barre_col = "#4DFF99" if pct >= 80 else ("#FFD060" if pct >= 30 else "#FF7777")
        cr1, cr2 = st.columns([2, 1])
        with cr1:
            st.metric("CAPITAL REEL CUMULE", f"{capital_reel:,.0f} EUR", delta=f"{pct}% de l objectif")
        with cr2:
            st.metric("OBJECTIF JANVIER 2027", f"{objectif_capital:,.0f} EUR")
        st.progress(min(pct, 100))'''

t = t.replace(old, new)

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print('Capital reel ajoute au dashboard')

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
