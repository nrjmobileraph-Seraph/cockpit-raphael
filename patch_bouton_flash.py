p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# 1. Remplacer le simple bouton FAIT par un st.markdown + bouton stylise
# On va ajouter du CSS specifique pour les boutons FAIT
old_css_start = 'div.stButton>button{font-size:18px'
new_css_start = '''div.stButton>button[kind="secondary"]{font-size:18px;background:#1A4A2A !important;color:#4DFF99 !important;border:2px solid #4DFF99 !important;} div.stButton>button{font-size:18px'''

t = t.replace(old_css_start, new_css_start)
print('Boutons FAIT colores en vert')

# 2. Ajouter animation flash plein ecran au clic
old_flash = '@keyframes flashGold{0%{background:#1A0D12;box-shadow:none}25%{background:#FFD060;box-shadow:0 0 30px #FFD060}50%{background:#C4922A;box-shadow:0 0 20px #C4922A}100%{background:#0A2010;box-shadow:0 0 5px #4DFF99}} .flash-gold{animation:flashGold 2s ease-out;'

new_flash = '@keyframes flashGold{0%{background:#1A0D12}15%{background:#FFD060}30%{background:#FFFFFF}50%{background:#FFD060}70%{background:#4DFF99}100%{background:#0A2010}} @keyframes screenFlash{0%{opacity:0}10%{opacity:1}30%{opacity:0.8}100%{opacity:0}} .screen-flash{position:fixed;top:0;left:0;width:100vw;height:100vh;background:#FFD060;z-index:9999;pointer-events:none;animation:screenFlash 1.5s ease-out forwards;} .flash-gold{animation:flashGold 2s ease-out;'

t = t.replace(old_flash, new_flash)
print('Animation flash plein ecran ajoutee')

# 3. Renommer bouton FAIT plus explicite
t = t.replace('st.button("FAIT"', 'st.button("MARQUER FAIT"')
print('Bouton renomme MARQUER FAIT')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
