src = open(r'C:\Users\BoulePiou\cockpit-raphael\app.py', encoding='utf-8').read()

# Fix 1 : connexion principale devis (lignes ~1013-1015)
src = src.replace(
    "    import sqlite3 as sqd\n    dbd = sqd.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')\n    dbd.row_factory = sqd.Row\n    cd = dbd.cursor()",
    "    dbd = db_wrapper.connect()\n    cd = dbd.cursor()"
)

# Fix 2 : connexion save devis (ligne ~1049)
src = src.replace(
    "                db4 = sqd.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')",
    "                db4 = db_wrapper.connect()"
)

open(r'C:\Users\BoulePiou\cockpit-raphael\app.py', 'w', encoding='utf-8').write(src)
print("OK - corrections appliquees")
