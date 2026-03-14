p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()
old_style = '[data-testid="stAppViewContainer"] { background:#0F1117; }'
new_style = '[data-testid="stAppViewContainer"] { background: linear-gradient(135deg, #0A0508 0%, #1A0A0A 30%, #0D0A15 70%, #0A0508 100%); }'
t = t.replace(old_style, new_style)
t = t.replace('#2D6A9F', '#8B6914')
t = t.replace('#CCDDFF', '#FFD699')
t = t.replace('#2D3A55', '#3A2A15')
t = t.replace('#0D2040', '#1A0A0A')
t = t.replace('#0D1020', '#0D0508')
t = t.replace('#1C2333', '#1A1015')
t = t.replace('#0A1020', '#0A0810')
f = open(p, 'w', encoding='utf-8')
f.write(t)
f.close()
print('Theme OK')
