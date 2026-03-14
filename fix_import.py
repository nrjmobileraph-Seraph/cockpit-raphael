src = open(r'C:\Users\BoulePiou\cockpit-raphael\app.py', encoding='utf-8').read()

ajout = 'import sys, os\nsys.path.append(os.path.dirname(os.path.abspath(__file__)))\nimport db_wrapper\n'

if 'import db_wrapper' not in src:
    src = src.replace('import math', ajout + 'import math', 1)
    import ast
    ast.parse(src)
    open(r'C:\Users\BoulePiou\cockpit-raphael\app.py', 'w', encoding='utf-8').write(src)
    print('OK - db_wrapper ajoute')
else:
    print('db_wrapper deja present')
