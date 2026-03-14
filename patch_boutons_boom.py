p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# 1. CSS pour gros boutons + animation explosion
old_css = 'st.markdown("<style>.stException{display:none !important}'
new_css = '''st.markdown("<style>.stException{display:none !important} div.stButton>button{font-size:18px !important;font-weight:800 !important;padding:10px 24px !important;border-radius:8px !important;transition:all 0.3s !important;} div.stButton>button:hover{transform:scale(1.1) !important;box-shadow:0 0 20px rgba(255,208,96,0.6) !important;}'''

t = t.replace(old_css, new_css)
print('CSS boutons grossis')

# 2. Remplacer "Marquer FAIT" par un texte plus gros avec emoji
t = t.replace('"Marquer FAIT"', '"FAIT"')
print('Bouton FAIT simplifie')

# 3. Ajouter une animation quand on arrive dans DEJA FAIT
old_deja = '        st.subheader("DEJA FAIT")'
new_deja = '''        st.markdown('<div style="background:linear-gradient(90deg,#0A2010,#1A4A2A,#0A2010);border:2px solid #4DFF99;border-radius:10px;padding:14px;text-align:center;margin:20px 0;"><span style="font-size:24px;color:#4DFF99;font-weight:900;letter-spacing:4px;">DEJA FAIT</span></div>', unsafe_allow_html=True)'''

t = t.replace(old_deja, new_deja)
print('Titre DEJA FAIT rendu visible')

# 4. Grossir le bandeau vert de chaque item fait
old_bandeau = 'font-size:15px;font-weight:700;">FAIT</span>'
new_bandeau = 'font-size:20px;font-weight:900;letter-spacing:3px;text-shadow:0 0 10px #4DFF99;">FAIT</span>'

t = t.replace(old_bandeau, new_bandeau)
print('Bandeau FAIT grossi avec glow')

# 5. Grossir le bouton Annuler
old_annuler = 'st.button("Annuler"'
new_annuler = 'st.button("ANNULER"'
t = t.replace(old_annuler, new_annuler)
print('Bouton ANNULER grossi')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
