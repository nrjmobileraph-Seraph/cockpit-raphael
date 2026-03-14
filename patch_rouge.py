p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Sidebar: rouge sang profond comme la larme
t = t.replace('linear-gradient(180deg, #080510 0%, #050308 50%, #030206 100%)', 'linear-gradient(180deg, #2A0810 0%, #1E0610 50%, #150510 100%)')

f = open(p, 'w', encoding='utf-8')
f.write(t)
f.close()
print('Sidebar rouge sang OK')
