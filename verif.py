import sqlite3, math
db = sqlite3.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
c = db.cursor()
row = c.execute("SELECT cc,livret_a,ldds,lep,av1,av2,av3 FROM capital ORDER BY id DESC LIMIT 1").fetchone()
C = sum(row)
print(f'Capital total: {C:,.0f} EUR')
print(f'  CC={row[0]:.0f} LA={row[1]:.0f} LDDS={row[2]:.0f} LEP={row[3]:.0f}')
print(f'  AV1={row[4]:.0f} AV2={row[5]:.0f} AV3={row[6]:.0f}')

r = 0.035
r_m = (1+r)**(1/12)-1
mois = 497
facteur = (1+r_m)**mois
annuite = (facteur-1)/r_m
W = (C*facteur - 50000)/annuite
print(f'ARVA: {W:,.0f} EUR/mois (rail=2760)')
print(f'Ecart: {W-2760:+,.0f} EUR')

# Trajectoire
from datetime import datetime
dn = datetime(1975,8,26)
age = (datetime.today()-dn).days/365.25
print(f'Age: {age:.1f} ans')
print(f'Mois restants: {mois}')

C0 = 393192.0
aah = 1033; loyer = 448; rail = 2760
pioche_p1 = rail - aah - loyer
def A(n): return ((1+r)**n-1)/r_m if r_m>0 else n
def P(n): return (1+r)**n
traj = C0*P(age-50) - pioche_p1*A(age-50)
print(f'Trajectoire theorique: {traj:,.0f} EUR')
print(f'Ecart capital vs traj: {(C-traj)/traj*100:+.1f}%')

db.close()
print('Verification OK')
