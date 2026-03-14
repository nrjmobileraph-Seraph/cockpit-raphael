import ast
src = open(r'C:\Users\BoulePiou\cockpit-raphael\app.py', encoding='utf-8').read()
src, n = __import__('re').subn(r'db_wrapper\.connect\(DB_PATH\)', 'db_wrapper.connect()', src)
print(f"{n} remplacements")
ast.parse(src)
open(r'C:\Users\BoulePiou\cockpit-raphael\app.py', 'w', encoding='utf-8').write(src)
print("OK")
