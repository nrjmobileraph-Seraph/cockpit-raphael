import sqlite3, psycopg2

# Source locale
local = sqlite3.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')
local.row_factory = sqlite3.Row

# Destination Supabase
cloud = psycopg2.connect(
    host='db.zyizvlrwsatxqehhqiwh.supabase.co',
    port=5432, dbname='postgres', user='postgres',
    password='Seraphetraph/62//26**'
)
cc = cloud.cursor()

# 1. Profil
r = dict(local.execute("SELECT * FROM profil WHERE id=1").fetchone())
cc.execute("""INSERT INTO profil (nom, date_naissance, age_cible, capital_cible, taux_mdph,
    aah_mensuel, loyer_net, rail_mensuel, rendement_annuel, pch_mensuel, rvd_mensuel, mdph_80plus)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
    (r['nom'], r['date_naissance'], r['age_cible'], r['capital_cible'], r['taux_mdph'],
     r['aah_mensuel'], r['loyer_net'], r['rail_mensuel'], r['rendement_annuel'],
     r.get('pch_mensuel',0), r.get('rvd_mensuel',450), r.get('mdph_80plus',0)))
print('Profil migre')

# 2. Capital
r = dict(local.execute("SELECT * FROM capital ORDER BY date DESC LIMIT 1").fetchone())
cc.execute("""INSERT INTO capital (date, cc, livret_a, ldds, lep, av1, av2, av3,
    av1_date_ouverture, av2_date_ouverture, av3_date_ouverture,
    av1_versements, av2_versements, av3_versements,
    av1_rendement, av2_rendement, av3_rendement, note)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
    (r['date'], r['cc'], r['livret_a'], r['ldds'], r['lep'], r['av1'], r['av2'], r['av3'],
     r['av1_date_ouverture'], r['av2_date_ouverture'], r['av3_date_ouverture'],
     r['av1_versements'], r['av2_versements'], r['av3_versements'],
     r['av1_rendement'], r['av2_rendement'], r['av3_rendement'], r['note']))
print('Capital migre')

# 3. Chronologie
rows = local.execute("SELECT * FROM chronologie ORDER BY date_cible ASC").fetchall()
for r in rows:
    r = dict(r)
    cc.execute("""INSERT INTO chronologie (date_cible, age_cible, action, montant, sens, categorie,
        auto, fait, note, montant_reel, date_reelle, confirme_1mois, date_confirme_1mois,
        confirme_6mois, date_confirme_6mois)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
        (r['date_cible'], r['age_cible'], r['action'], r['montant'], r['sens'], r['categorie'],
         r['auto'], r['fait'], r['note'], r.get('montant_reel',0), r.get('date_reelle',''),
         r.get('confirme_1mois',0), r.get('date_confirme_1mois',''),
         r.get('confirme_6mois',0), r.get('date_confirme_6mois','')))
print(f'Chronologie migree : {len(rows)} jalons')

# 4. AAH
rows = local.execute("SELECT * FROM aah_suivi ORDER BY mois ASC").fetchall()
for r in rows:
    r = dict(r)
    cc.execute("""INSERT INTO aah_suivi (mois, montant_prevu, montant_reel, date_saisie, note)
        VALUES (%s,%s,%s,%s,%s)""",
        (r['mois'], r['montant_prevu'], r['montant_reel'], r.get('date_saisie',''), r.get('note','')))
print(f'AAH migree : {len(rows)} annees')

# 5. Devis
rows = local.execute("SELECT * FROM devis_artisans ORDER BY id ASC").fetchall()
for r in rows:
    r = dict(r)
    cc.execute("""INSERT INTO devis_artisans (corps_metier, artisan, devis_montant, paye_montant, statut, note)
        VALUES (%s,%s,%s,%s,%s,%s)""",
        (r['corps_metier'], r.get('artisan',''), r['devis_montant'], r['paye_montant'], r['statut'], r.get('note','')))
print(f'Devis migres : {len(rows)} corps de metier')

cloud.commit()

# Verification
cc.execute("SELECT COUNT(*) FROM chronologie")
nb_j = cc.fetchone()[0]
cc.execute("SELECT cc+livret_a+ldds+lep+av1+av2+av3 FROM capital ORDER BY date DESC LIMIT 1")
cap = cc.fetchone()[0]

cloud.close()
local.close()

print(f'\nVERIFICATION SUPABASE :')
print(f'  Jalons : {nb_j}')
print(f'  Capital : {cap:,.0f} EUR')
print(f'  Migration complete OK')
