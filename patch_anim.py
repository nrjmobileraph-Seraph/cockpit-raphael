p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# 1. Cards: marron -> rouge sombre profond avec reflet
t = t.replace('background:#1A1015;', 'background:linear-gradient(145deg, #1A0D12 0%, #150A10 100%);')

# 2. Bordures: brun -> cuivre chaud
t = t.replace('border-color:#3A2A15;', 'border-color:#4A2020;')
t = t.replace('#3A2A15', '#3A1520')

# 3. Ajouter animations hover sur les boutons et cards
old_css_end = '</style>'
animations = """
  .kpi { transition: transform 0.2s ease, box-shadow 0.3s ease; }
  .kpi:hover { transform: translateY(-3px); box-shadow: 0 6px 20px rgba(139,105,20,0.3); }
  .stRadio label { transition: all 0.2s ease !important; padding: 4px 8px !important; border-radius: 6px !important; }
  .stRadio label:hover { background: rgba(139,105,20,0.15) !important; padding-left: 14px !important; }
  button { transition: all 0.2s ease !important; }
  button:hover { transform: scale(1.03) !important; box-shadow: 0 4px 15px rgba(139,105,20,0.4) !important; }
  .poche-row { transition: all 0.2s ease; }
  .poche-row:hover { background: rgba(139,105,20,0.1); padding-left: 6px; }
  div[data-testid="stDecoration"] { display: none !important; }
  iframe[title="streamlit_translation"] { display: none !important; }
  #MainMenu { visibility: hidden !important; }
  footer { visibility: hidden !important; }
  div[data-testid="stToolbar"] { display: none !important; }
"""
if 'translateY' not in t:
    t = t.replace(old_css_end, animations + old_css_end, 1)

f = open(p, 'w', encoding='utf-8')
f.write(t)
f.close()
print('Animations + couleurs OK')
