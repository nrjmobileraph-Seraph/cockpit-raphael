p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Sidebar: brun -> rouge sombre elegant comme la photo
t = t.replace('background:#0D0508;', 'background: linear-gradient(180deg, #1A0A0F 0%, #120810 50%, #0A0508 100%);')

# Supprimer la barre blanche en haut (header Streamlit)
old_css_end = '</style>'
header_hide = '  header[data-testid="stHeader"] { background:transparent !important; border:none !important; }\n  '
if 'stHeader' not in t:
    t = t.replace(old_css_end, header_hide + old_css_end, 1)

f = open(p, 'w', encoding='utf-8')
f.write(t)
f.close()
print('Sidebar + header fix OK')
