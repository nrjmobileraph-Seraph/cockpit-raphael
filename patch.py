import re
p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()
t=t.replace('v3.0','v4.1').replace('Sprint 1-3','Sprint 1-4')
print('Pages avant:',t.count('lambda:'))
f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print('Version patch OK')
