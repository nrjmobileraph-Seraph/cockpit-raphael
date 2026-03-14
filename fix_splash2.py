src = open(r'C:\Users\BoulePiou\cockpit-raphael\app.py', encoding='utf-8').read()

ancien = '''if st.session_state.sidebar_state == "collapsed":'''

nouveau = '''if st.session_state.get('connected', False):
 if st.session_state.sidebar_state == "collapsed":'''

src = src.replace(ancien, nouveau, 1)

import ast
try:
    ast.parse(src)
    open(r'C:\Users\BoulePiou\cockpit-raphael\app.py', 'w', encoding='utf-8').write(src)
    print("OK - syntaxe valide - fichier sauvegarde")
except SyntaxError as e:
    print(f"ERREUR syntaxe ligne {e.lineno} : {e.msg} - fichier NON modifie")
