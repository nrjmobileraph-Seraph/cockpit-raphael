import re, ast
src = open(r'C:\Users\BoulePiou\cockpit-raphael\app.py', encoding='utf-8').read()
src, n = re.subn(r"(sq|sq2|sqd|sqlite3)\.connect\s*\(\s*['\"][^'\"]*cockpit\.db[^'\"]*['\"]\s*\)", "db_wrapper.connect()", src)
print(f"{n} remplacements")
ast.parse(src)
open(r'C:\Users\BoulePiou\cockpit-raphael\app.py', 'w', encoding='utf-8').write(src)
print("OK")
