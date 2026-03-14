p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# 1. Rendre les items "DEJA FAIT" avec un fond vert visible
old_fait_display = '''            col_f, col_a = st.columns([5, 1])
            with col_f:
                st.write(f"{r.get('date_reelle', '') or r['date_cible']} | {r['action']} | {flux_txt}{locks}")
            with col_a:
                if not verrouille:
                    if st.button("Annuler", key=f"undo_{r['id']}"):'''

new_fait_display = '''            col_f, col_a = st.columns([5, 1])
            with col_f:
                st.markdown(f'<div style="background:#0A2010;border-left:4px solid #4DFF99;border-radius:0 6px 6px 0;padding:8px 14px;margin:4px 0;"><span style="color:#4DFF99;font-size:15px;font-weight:700;">FAIT</span> <span style="color:#F0E6D8;font-size:14px;">{r.get("date_reelle", "") or r["date_cible"]} | {r["action"]} | {flux_txt}{locks}</span></div>', unsafe_allow_html=True)
            with col_a:
                if not verrouille:
                    if st.button("Annuler", key=f"undo_{r['id']}"):'''

if old_fait_display in t:
    t = t.replace(old_fait_display, new_fait_display)
    print('Affichage FAIT rendu visible')
else:
    print('Section FAIT non trouvee')

# 2. Ajouter un flash dore quand on marque un jalon comme fait
# On ajoute du CSS animation
old_css = 'st.markdown("<style>.stException{display:none !important}</style>", unsafe_allow_html=True)'
new_css = '''st.markdown("<style>.stException{display:none !important} @keyframes flashGold{0%{background:#2A1800}50%{background:#FFD060}100%{background:#0A2010}} .flash-gold{animation:flashGold 1.5s ease-out;}</style>", unsafe_allow_html=True)'''

if old_css in t:
    t = t.replace(old_css, new_css)
    print('Animation flash doree ajoutee')

# 3. Grossir le bouton "Fait" dans la section A VENIR
old_fait_btn = '''            if st.button("Fait", key=f"fait_{r['id']}"):'''
new_fait_btn = '''            if st.button("Marquer FAIT", key=f"fait_{r['id']}"):'''
t = t.replace(old_fait_btn, new_fait_btn)
print('Bouton Fait renomme')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
