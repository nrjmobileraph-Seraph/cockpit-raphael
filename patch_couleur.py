p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Boutons dans les teintes bordeaux/or de la photo
t = t.replace('background:#1A4A2A !important;color:#4DFF99 !important;border:2px solid #4DFF99 !important;', 'background:#2A0A12 !important;color:#FFD060 !important;border:2px solid #C4922A !important;')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print('Boutons en bordeaux/or')
