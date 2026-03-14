p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

old = '''    with st.sidebar:
        st.markdown("## Cockpit Raphael")
        st.markdown(f"**Age :** {age:.1f} ans")'''

new = '''    with st.sidebar:
        try:
            st.markdown("## Cockpit Raphael")
            st.markdown(f"**Age :** {age:.1f} ans")'''

t = t.replace(old, new)

# Fermer le try avant le radio
old2 = '''        st.markdown("---")
        page=st.radio("Navigation",['''

new2 = '''        st.markdown("---")
        except:
            st.markdown("## Cockpit Raphael")
        page=st.radio("Navigation",['''

t = t.replace(old2, new2)

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print('Sidebar protege')

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
