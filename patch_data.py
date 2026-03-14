import sqlite3
db = sqlite3.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
c = db.cursor()

# Profil
c.execute("""UPDATE profil SET
    aah_mensuel=1033, pch_mensuel=0, loyer_net=448,
    taux_mdph=75, rendement_annuel=0.035, rail_mensuel=2760,
    date_naissance='1975-08-26', age_cible=92
    WHERE id=1""")

# Capital - repartition validee
c.execute("""INSERT INTO capital
    (date,cc,livret_a,ldds,lep,av1,av2,av3,
     av1_date_ouverture,av2_date_ouverture,av3_date_ouverture,
     av1_versements,av2_versements,av3_versements,
     av1_rendement,av2_rendement,av3_rendement,note)
    VALUES ('2026-03-11',
     500, 22950, 12000, 10000,
     109500, 109500, 128742,
     '2016-01-01','2026-01-01','2010-01-01',
     95000, 500, 110000,
     0.035, 0.035, 0.035,
     'Projection initiale validee 4 IA - Mars 2026')""")

db.commit()
db.close()
print('Capital:', 500+22950+12000+10000+109500+109500+128742)
print('Base mise a jour OK')
