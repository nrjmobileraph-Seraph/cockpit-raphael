p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()
lines=t.split(chr(10))
start=0
end=0
for i,l in enumerate(lines):
    if 'def page_annexe' in l: start=i; break
for i in range(start+1, len(lines)):
    if lines[i].startswith('def '): end=i; break
print(f'page_annexe: lignes {start+1} a {end}')
print(f'Taille: {end-start} lignes')
print()
for i in range(start, min(start+30, end)):
    print(f'{i+1}: {lines[i][:100]}')
