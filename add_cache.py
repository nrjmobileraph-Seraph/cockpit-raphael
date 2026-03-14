with open('C:/Users/BoulePiou/cockpit-raphael/app.py', 'r', encoding='utf-8') as f:
    code = f.read()
code = code.replace('def get_profil():', '@st.cache_data(ttl=300)\ndef get_profil():')
code = code.replace('def get_capital():', '@st.cache_data(ttl=300)\ndef get_capital():')
with open('C:/Users/BoulePiou/cockpit-raphael/app.py', 'w', encoding='utf-8') as f:
    f.write(code)
import ast
ast.parse(code)
print('SUCCES')
