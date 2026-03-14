p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Trouver le CSS global des boutons et changer la couleur par defaut
old_btn = 'div.stButton>button{font-size:18px !important;font-weight:800 !important;padding:10px 24px !important;border-radius:8px !important;transition:all 0.3s !important;}'
new_btn = 'div.stButton>button{font-size:18px !important;font-weight:800 !important;padding:10px 24px !important;border-radius:8px !important;transition:all 0.3s !important;background:#2A0A12 !important;color:#FFD060 !important;border:2px solid #C4922A !important;}'

if old_btn in t:
    t = t.replace(old_btn, new_btn)
    print('Tous les boutons en bordeaux/or')
else:
    print('CSS boutons non trouve - recherche...')
    if 'font-size:18px' in t:
        print('CSS present mais format different')

# Hover aussi en dore
old_hover = 'div.stButton>button:hover{transform:scale(1.1) !important;box-shadow:0 0 20px rgba(255,208,96,0.6) !important;}'
new_hover = 'div.stButton>button:hover{transform:scale(1.1) !important;box-shadow:0 0 25px rgba(196,146,42,0.8) !important;background:#3A0A15 !important;color:#FFFFFF !important;border:2px solid #FFD060 !important;}'

if old_hover in t:
    t = t.replace(old_hover, new_hover)
    print('Hover en dore lumineux')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
