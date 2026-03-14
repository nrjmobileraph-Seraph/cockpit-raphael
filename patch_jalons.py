p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Expanders text color fix
old_css_end = '</style>'
expander_fix = """
  .streamlit-expanderHeader { color:#F0E6D8 !important; font-size:15px !important; }
  .streamlit-expanderContent { color:#DDCCBB !important; }
  details summary span { color:#F0E6D8 !important; }
  details div { color:#DDCCBB !important; }
  .stExpander { border-color:#4A2020 !important; }
"""
if 'expanderHeader' not in t:
    t = t.replace(old_css_end, expander_fix + old_css_end, 1)

f = open(p, 'w', encoding='utf-8')
f.write(t)
f.close()
print('Jalons lisibles OK')
