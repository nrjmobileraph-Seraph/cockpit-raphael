src = open(r'C:\Users\BoulePiou\cockpit-raphael\app.py', encoding='utf-8').read()

src = src.replace(
    "        import sqlite3 as sq\n        db_j = sq.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')\n        db_j.row_factory = sq.Row\n        c_j = db_j.cursor()",
    "        db_j = db_wrapper.connect()\n        c_j = db_j.cursor()"
)

open(r'C:\Users\BoulePiou\cockpit-raphael\app.py', 'w', encoding='utf-8').write(src)
print("OK")
