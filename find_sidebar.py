p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
lines=f.readlines()
f.close()

# Trouver la ligne with st.sidebar
for i, l in enumerate(lines):
    if 'with st.sidebar:' in l:
        print(f'Sidebar trouve ligne {i+1}')
        # Montrer 5 lignes avant et 30 apres
        for j in range(max(0,i-2), min(i+30, len(lines))):
            print(f'{j+1}: {lines[j].rstrip()[:120]}')
        break
