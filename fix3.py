with open('C:/Users/BoulePiou/cockpit-raphael/app.py', 'r', encoding='utf-8') as f:
    code = f.read()

code = code.replace('        # Capital reel cumule depuis les jalons\n                db_j = db_wrapper.connect()', '        # Capital reel cumule depuis les jalons\n        db_j = db_wrapper.connect()')

with open('C:/Users/BoulePiou/cockpit-raphael/app.py', 'w', encoding='utf-8') as f:
    f.write(code)

import ast
ast.parse(code)
print(f'ast.parse : PASS')
print(f'Pages : {code.count("def page_")}')
print(f'sqlite3 : {code.count("sqlite3")}')
print(f'BoulePiou : {code.count("BoulePiou")}')
print('SUCCES')
