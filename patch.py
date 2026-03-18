import shutil
f = r"C:\Users\BoulePiou\cockpit-raphael\app.py"
shutil.copy2(f, f + ".bak")
c = open(f, "r", encoding="utf-8").read()
for rev in ["REVENUS / MOIS", "REVENUS MOIS", "REVENUS/MOIS"]:
    old = '<div style="background:#0A1E12;border:2px solid #4DFF99;border-radius:10px;padding:10px;text-align:center;margin-bottom:4px"><div style="color:#BBA888;font-size:9px;text-transform:uppercase">' + rev + '</div><div style="color:#4DFF99;font-size:22px;font-weight:900">{rtot:.0f} EUR</div></div>'
    if old in c:
        c = c.replace(old, "")
        print("REVENUS supprime")
        break
old2 = '<div style="background:#1A0D12;border:2px solid #C4922A;border-radius:10px;padding:10px;text-align:center;margin-bottom:4px"><div style="color:#BBA888;font-size:9px;text-transform:uppercase">CAPITAL TOTAL</div><div style="color:#FFD060;font-size:22px;font-weight:900">{ptot:.0f} EUR</div></div>'
if old2 in c:
    c = c.replace(old2, "")
    print("CAPITAL TOTAL supprime")
open(f, "w", encoding="utf-8").write(c)
print("OK - Termine!")
