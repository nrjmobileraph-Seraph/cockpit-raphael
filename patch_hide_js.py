p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()
# Cacher les erreurs JS Streamlit
js_hide = '''
    st.markdown('<style>div[data-testid="stException"]{display:none !important;}</style>', unsafe_allow_html=True)
'''
# Ajouter au debut de page_jalons et page_dashboard
t=t.replace('titre("PLANNING PATRIMONIAL - SUIVI EN TEMPS REEL")', js_hide + '    titre("PLANNING PATRIMONIAL - SUIVI EN TEMPS REEL")')
t=t.replace('titre("COCKPIT PATRIMONIAL - PHASE CONSTRUCTION")', js_hide + '    titre("COCKPIT PATRIMONIAL - PHASE CONSTRUCTION")')
f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print('Erreurs JS cachees OK')
