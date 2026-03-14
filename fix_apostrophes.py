p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
lines=f.readlines()
f.close()
fixed=0
for i in range(len(lines)):
    # Remplacer les apostrophes francaises dans les f-strings par des entites HTML
    if "aujourd'hui" in lines[i] and 'st.markdown' in lines[i]:
        lines[i]=lines[i].replace("aujourd'hui", "aujourd&#39;hui")
        fixed+=1
    if "d'achat" in lines[i] and 'st.markdown' in lines[i]:
        lines[i]=lines[i].replace("d'achat", "d&#39;achat")
        fixed+=1
    if "d'un" in lines[i] and 'st.markdown' in lines[i]:
        lines[i]=lines[i].replace("d'un", "d&#39;un")
        fixed+=1
    if "l'ensemble" in lines[i] and 'st.markdown' in lines[i]:
        lines[i]=lines[i].replace("l'ensemble", "l&#39;ensemble")
        fixed+=1
    if "n'est" in lines[i] and 'st.markdown' in lines[i]:
        lines[i]=lines[i].replace("n'est", "n&#39;est")
        fixed+=1
    if "qu'" in lines[i] and 'st.markdown' in lines[i]:
        lines[i]=lines[i].replace("qu'", "qu&#39;")
        fixed+=1
    if "l'" in lines[i] and 'st.markdown' in lines[i] and "l&#39;" not in lines[i]:
        # Trop dangereux, on skip
        pass
f=open(p,'w',encoding='utf-8')
f.writelines(lines)
f.close()
print(f'Apostrophes corrigees: {fixed}')
import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {e}')
