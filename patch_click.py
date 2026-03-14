p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# 1. Sidebar: changer le fond marron -> rouge sombre elegant
t = t.replace('linear-gradient(180deg, #1A0A0F 0%, #120810 50%, #0A0508 100%)', 'linear-gradient(180deg, #12060A 0%, #0D0408 50%, #080205 100%)')

# 2. Ajouter animation au clic (pulse)
old_css_end = '</style>'
click_anim = """
  @keyframes pulse { 0% { transform: scale(1); } 50% { transform: scale(0.96); } 100% { transform: scale(1); } }
  button:active { animation: pulse 0.15s ease !important; }
  .kpi:active { animation: pulse 0.2s ease; }
  .stRadio label:active { animation: pulse 0.15s ease !important; background: rgba(204,51,51,0.2) !important; }
  [data-testid="stSidebar"] { border-right: 1px solid rgba(139,105,20,0.2) !important; }
  [data-testid="stSidebar"] .stRadio label { color:#CCBBAA !important; }
"""
if 'pulse' not in t:
    t = t.replace(old_css_end, click_anim + old_css_end, 1)

f = open(p, 'w', encoding='utf-8')
f.write(t)
f.close()
print('Sidebar + click anim OK')
