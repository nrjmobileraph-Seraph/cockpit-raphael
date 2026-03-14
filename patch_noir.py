p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Sidebar: virer tout marron -> noir pur avec leger reflet violet
t = t.replace('linear-gradient(180deg, #12060A 0%, #0D0408 50%, #080205 100%)', 'linear-gradient(180deg, #080510 0%, #050308 50%, #030206 100%)')

# Animations plus visibles
old_hover = 'padding-left: 14px !important;'
new_hover = 'padding-left: 14px !important; color:#FFD060 !important; text-shadow: 0 0 8px rgba(196,146,42,0.5);'
t = t.replace(old_hover, new_hover)

# Bouton pulse plus gros
t = t.replace('50% { transform: scale(0.96); }', '50% { transform: scale(0.92); box-shadow: 0 0 15px rgba(196,146,42,0.6); }')

# Transition page plus visible
t = t.replace('animation: fadeSlideIn 0.4s ease-out;', 'animation: fadeSlideIn 0.6s ease-out;')
t = t.replace('0% { opacity:0; transform:translateY(15px); }', '0% { opacity:0; transform:translateY(30px) scale(0.98); }')

f = open(p, 'w', encoding='utf-8')
f.write(t)
f.close()
print('Sidebar noir + anim forte OK')
