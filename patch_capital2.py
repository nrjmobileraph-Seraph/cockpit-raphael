import sqlite3
db = sqlite3.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
c = db.cursor()

# Nouveau capital: 475 000 EUR
# Repartition proportionnelle ajustee
c.execute("""INSERT INTO capital
    (date,cc,livret_a,ldds,lep,av1,av2,av3,
     av1_date_ouverture,av2_date_ouverture,av3_date_ouverture,
     av1_versements,av2_versements,av3_versements,
     av1_rendement,av2_rendement,av3_rendement,note)
    VALUES ('2026-03-12',
     500, 22950, 12000, 10000,
     130000, 130000, 169550,
     '2016-01-01','2026-01-01','2010-01-01',
     95000, 500, 110000,
     0.035, 0.035, 0.035,
     'Capital corrige 475 000 EUR - SCI 291800 + Succession 217400 - travaux 33000 - donation 1200')""")

db.commit()
db.close()
print('Capital:', 500+22950+12000+10000+130000+130000+169550)
print('Base mise a jour OK')
