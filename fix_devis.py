src = open(r'C:\Users\BoulePiou\cockpit-raphael\app.py', encoding='utf-8').read()

src = src.replace(
    "                db4 = sqd.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')",
    "                db4 = db_wrapper.connect()"
)
src = src.replace(
    "                db5 = sqd.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')",
    "                db5 = db_wrapper.connect()"
)

import ast
try:
    ast.parse(src)
    open(r'C:\Users\BoulePiou\cockpit-raphael\app.py', 'w', encoding='utf-8').write(src)
    print("OK")
except SyntaxError as e:
    print(f"ERREUR ligne {e.lineno} : {e.msg}")
