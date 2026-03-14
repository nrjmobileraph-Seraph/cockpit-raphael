p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Texte trop sombre -> plus clair partout
t = t.replace('color:#888;', 'color:#BBA888;')
t = t.replace('color:#777;', 'color:#BBA888;')
t = t.replace('color:#AAA;', 'color:#DDCCBB;')
t = t.replace('color:#999;', 'color:#CCBBAA;')
t = t.replace('color:#555;', 'color:#998877;')
t = t.replace('color:#DDD;', 'color:#F0E6D8;')

f = open(p, 'w', encoding='utf-8')
f.write(t)
f.close()
print('Textes eclaircis OK')
