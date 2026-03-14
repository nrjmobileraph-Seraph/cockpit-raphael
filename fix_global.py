src = open(r'C:\Users\BoulePiou\cockpit-raphael\app.py', encoding='utf-8').read()

src = src.replace(
    "db3 = sq2.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')",
    "db3 = db_wrapper.connect()"
)

open(r'C:\Users\BoulePiou\cockpit-raphael\app.py', 'w', encoding='utf-8').write(src)
print("OK - toutes corrections appliquees")
