p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()
old_css_end = '</style>'
force_all = """
  * { color-scheme: dark; }
  body, p, span, div, li, td, th, label, input, textarea, select, summary, details, code, pre, a, h1, h2, h3, h4, h5, h6 { color: #F0E6D8 !important; }
  .stAlert p, .stAlert span { color: inherit !important; }
  input, textarea, select { background: #1A1015 !important; border-color: #4A2020 !important; }
  [data-testid="stMarkdownContainer"] { color: #F0E6D8 !important; }
  .stTabs [data-baseweb="tab"] { color: #E0D0B8 !important; }
  .stTabs [aria-selected="true"] { color: #FFD060 !important; }
"""
if 'color-scheme: dark' not in t:
    t = t.replace(old_css_end, force_all + old_css_end, 1)
f = open(p, 'w', encoding='utf-8')
f.write(t)
f.close()
print('Texte final OK')
