p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Fix deprecated use_container_width
t=t.replace('use_container_width=True', "width='stretch'")
t=t.replace('use_container_width=False', "width='content'")

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
count = t.count("width='stretch'") + t.count("width='content'")
print(f'Remplacements: {count}')
print('Warning fix OK')
