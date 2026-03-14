p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Fix sidebar text visibility
old_sidebar = '[data-testid="stSidebar"] { background:#0D1020; }'
new_sidebar = '[data-testid="stSidebar"] { background:#0D1020; color:#DDDDDD; }\n  [data-testid="stSidebar"] .stRadio label { color:#DDDDDD !important; font-size:14px !important; }\n  [data-testid="stSidebar"] .stMarkdown { color:#DDDDDD !important; }'
t=t.replace(old_sidebar, new_sidebar)

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print('Sidebar fix OK')
