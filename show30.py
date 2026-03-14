p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
lines=f.readlines()
f.close()

# Montrer lignes 30-65 pour voir ou commence le code Gemini
for j in range(28, 65):
    print(f'{j+1}: {lines[j].rstrip()[:120]}')
