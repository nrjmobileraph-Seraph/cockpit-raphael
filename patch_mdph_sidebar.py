p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Trouver le badge actuel et le rendre dynamique
old_badge = "st.markdown('<div style=" + '"' + "background:#0A2010"
# On va remplacer la section MDPH du sidebar
old_mdph = 'st.markdown(f"**MDPH :** {profil[' + "'" + 'taux_mdph' + "'" + ']}%")'

new_mdph = '''mdph80 = profil.get('mdph_80plus', 0)
        st.markdown(f"**MDPH :** {profil['taux_mdph']}%")
        if mdph80:
            st.markdown('<div style="background:#0A2010;border:1px solid #4DFF99;border-radius:6px;padding:6px 10px;text-align:center;"><span style="color:#4DFF99;font-size:10px;font-weight:700;">AAH A VIE</span></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div style="background:#2A1800;border:1px solid #D4A017;border-radius:6px;padding:6px 10px;text-align:center;"><span style="color:#FFD060;font-size:10px;font-weight:700;">AAH STOP 64 ANS</span></div>', unsafe_allow_html=True)'''

if old_mdph in t:
    t = t.replace(old_mdph, new_mdph)
    print('Sidebar MDPH dynamique installe')
else:
    print('Ligne MDPH non trouvee, recherche...')
    for i, l in enumerate(t.split(chr(10))):
        if 'taux_mdph' in l and 'markdown' in l:
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
