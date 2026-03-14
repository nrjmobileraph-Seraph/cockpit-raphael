p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
lines=f.readlines()
f.close()
for i in range(len(lines)):
    if 'sidebar' in lines[i] and ('radio' in lines[i] or 'selectbox' in lines[i] or 'option_menu' in lines[i]):
        for j in range(max(0,i-5), min(i+20, len(lines))):
            print(f'{j+1}: {lines[j].rstrip()[:120]}')
        print('---')
        break
