p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()
old = 'background: linear-gradient(135deg, #0A0508 0%, #1A0A0A 30%, #0D0A15 70%, #0A0508 100%);'
new = 'background: linear-gradient(rgba(10,5,8,0.85), rgba(26,10,10,0.85)), url("/app/static/fond.png") center/cover fixed;'
t = t.replace(old, new)
f = open(p, 'w', encoding='utf-8')
f.write(t)
f.close()
print('Fond image OK')
