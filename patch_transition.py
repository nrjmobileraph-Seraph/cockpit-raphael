p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

old_css_end = '</style>'
page_transition = """
  @keyframes fadeSlideIn { 0% { opacity:0; transform:translateY(15px); } 100% { opacity:1; transform:translateY(0); } }
  .main .block-container { animation: fadeSlideIn 0.4s ease-out; }
  @keyframes sideGlow { 0% { box-shadow: inset -2px 0 8px rgba(139,105,20,0); } 50% { box-shadow: inset -2px 0 8px rgba(139,105,20,0.3); } 100% { box-shadow: inset -2px 0 8px rgba(139,105,20,0); } }
  .stRadio label[data-checked="true"] { animation: sideGlow 1.5s ease infinite; }
"""
if 'fadeSlideIn' not in t:
    t = t.replace(old_css_end, page_transition + old_css_end, 1)

f = open(p, 'w', encoding='utf-8')
f.write(t)
f.close()
print('Page transition OK')
