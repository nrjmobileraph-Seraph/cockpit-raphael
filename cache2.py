with open('C:/Users/BoulePiou/cockpit-raphael/app.py', 'r', encoding='utf-8') as f:
    code = f.read()
code = code.replace('def get_lmnp():', '@st.cache_data(ttl=300)\ndef get_lmnp():')
code = code.replace('def get_historique_surplus():', '@st.cache_data(ttl=300)\ndef get_historique_surplus():')
code = code.replace('def calculer_alertes(', '@st.cache_data(ttl=300)\ndef calculer_alertes(')
with open('C:/Users/BoulePiou/cockpit-raphael/app.py', 'w', encoding='utf-8') as f:
    f.write(code)
import ast
ast.parse(code)
print('SUCCES')
