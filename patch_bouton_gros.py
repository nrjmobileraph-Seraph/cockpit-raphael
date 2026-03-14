p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Rendre le bouton Marquer FAIT plus gros - ajouter du CSS
old_css = 'st.markdown("<style>.stException{display:none !important} @keyframes flashGold'
new_css = 'st.markdown("<style>.stException{display:none !important} div.stButton>button{font-size:16px !important;font-weight:700 !important;} @keyframes flashGold{0%{background:#1A0D12;box-shadow:none}25%{background:#FFD060;box-shadow:0 0 30px #FFD060}50%{background:#C4922A;box-shadow:0 0 20px #C4922A}100%{background:#0A2010;box-shadow:0 0 5px #4DFF99}} .flash-gold{animation:flashGold 2s ease-out;'

t = t.replace(old_css, new_css)
print('Boutons grossis + flash renforce')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
