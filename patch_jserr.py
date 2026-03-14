p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Cacher les erreurs JS Streamlit
old_css_end = '</style>'
hide_errors = """
  .stException { display:none !important; }
  .element-container iframe[title="streamlit_js_eval"] { display:none !important; }
  div[data-testid="stNotification"] { display:none !important; }
"""
if 'stException' not in t:
    t = t.replace(old_css_end, hide_errors + old_css_end, 1)

f = open(p, 'w', encoding='utf-8')
f.write(t)
f.close()
print('Erreur JS cachee OK')
