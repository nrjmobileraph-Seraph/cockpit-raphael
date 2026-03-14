p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Trouver la ligne avec l'age dans le sidebar
old_age = "st.markdown(f\"**Age :** {age:.1f} ans\")"
new_age = '''st.markdown(f"**Age :** {age:.1f} ans")
        st.markdown('<div style="background:#0A2010;border:1px solid #1A6B4B;border-radius:6px;padding:8px 12px;margin:4px 0;text-align:center;"><span style="color:#4DFF99;font-size:11px;font-weight:700;letter-spacing:1px;">PLAN OPERATIONNEL</span><br><span style="color:#BBA888;font-size:10px;">Garanti jusqu&#39;a 92 ans</span></div>', unsafe_allow_html=True)'''

if old_age in t:
    t = t.replace(old_age, new_age)
    print('Badge ajoute dans le sidebar')
else:
    # Essayer variante
    old_age2 = 'st.markdown(f"**Age :** {age:.1f} ans")'
    if old_age2 in t:
        t = t.replace(old_age2, new_age)
        print('Badge ajoute dans le sidebar (variante)')
    else:
        print('Ligne age non trouvee - on cherche...')
        for i, l in enumerate(t.split(chr(10))):
            if 'Age' in l and 'age' in l and 'markdown' in l:
                print(f'Ligne {i+1}: {l.strip()[:80]}')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
