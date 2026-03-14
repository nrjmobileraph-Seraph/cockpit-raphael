from PIL import Image
import base64, io

# Reduire l'image pour le fond
img = Image.open('C:/Users/BoulePiou/cockpit-raphael/fond.png')
img = img.resize((960, 1440), Image.LANCZOS)
buf = io.BytesIO()
img.save(buf, format='JPEG', quality=40)
b64 = base64.b64encode(buf.getvalue()).decode()

p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

old = "url(\"/app/static/fond.png\") center/cover fixed;"
new = "url(\"data:image/jpeg;base64," + b64 + "\") center/cover fixed;"
t = t.replace(old, new)

f = open(p, 'w', encoding='utf-8')
f.write(t)
f.close()
print('Image fond integree OK')
print(f'Taille base64: {len(b64)//1024}KB')
