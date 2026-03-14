import psycopg2

conn = psycopg2.connect(
    host='db.zyizvlrwsatxqehhqiwh.supabase.co',
    port=5432,
    dbname='postgres',
    user='postgres',
    password='Seraphetraph/62//26**'
)
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS profil (
    id SERIAL PRIMARY KEY,
    nom TEXT DEFAULT 'Raphael',
    date_naissance TEXT DEFAULT '1975-08-26',
    age_cible INTEGER DEFAULT 92,
    capital_cible INTEGER DEFAULT 50000,
    taux_mdph INTEGER DEFAULT 75,
    aah_mensuel REAL DEFAULT 1033,
    loyer_net REAL DEFAULT 320,
    rail_mensuel REAL DEFAULT 2760,
    rendement_annuel REAL DEFAULT 0.035,
    updated TEXT DEFAULT '',
    pch_mensuel REAL DEFAULT 0,
    rvd_mensuel REAL DEFAULT 450,
    mdph_80plus INTEGER DEFAULT 0
)""")
print('Table profil creee')

c.execute("""CREATE TABLE IF NOT EXISTS capital (
    id SERIAL PRIMARY KEY,
    date TEXT DEFAULT CURRENT_DATE::TEXT,
    cc REAL DEFAULT 500,
    livret_a REAL DEFAULT 22950,
    ldds REAL DEFAULT 12000,
    lep REAL DEFAULT 10000,
    av1 REAL DEFAULT 130000,
    av2 REAL DEFAULT 130000,
    av3 REAL DEFAULT 155550,
    pv_latentes_av1 REAL DEFAULT 0,
    pv_latentes_av2 REAL DEFAULT 0,
    pv_latentes_av3 REAL DEFAULT 0,
    note TEXT DEFAULT '',
    updated TEXT DEFAULT '',
    av1_date_ouverture TEXT DEFAULT '2016-01-01',
    av2_date_ouverture TEXT DEFAULT '2026-01-01',
    av3_date_ouverture TEXT DEFAULT '2010-01-01',
    av1_versements REAL DEFAULT 95000,
    av2_versements REAL DEFAULT 500,
    av3_versements REAL DEFAULT 110000,
    av1_rendement REAL DEFAULT 0.035,
    av2_rendement REAL DEFAULT 0.035,
    av3_rendement REAL DEFAULT 0.035
)""")
print('Table capital creee')

c.execute("""CREATE TABLE IF NOT EXISTS chronologie (
    id SERIAL PRIMARY KEY,
    date_cible TEXT,
    age_cible REAL,
    action TEXT,
    montant REAL DEFAULT 0,
    sens TEXT DEFAULT 'info',
    categorie TEXT DEFAULT 'jalon',
    auto INTEGER DEFAULT 0,
    fait INTEGER DEFAULT 0,
    note TEXT DEFAULT '',
    montant_reel REAL DEFAULT 0,
    date_reelle TEXT DEFAULT '',
    confirme_1mois INTEGER DEFAULT 0,
    date_confirme_1mois TEXT DEFAULT '',
    confirme_6mois INTEGER DEFAULT 0,
    date_confirme_6mois TEXT DEFAULT ''
)""")
print('Table chronologie creee')

c.execute("""CREATE TABLE IF NOT EXISTS aah_suivi (
    id SERIAL PRIMARY KEY,
    mois TEXT UNIQUE,
    montant_prevu REAL DEFAULT 0,
    montant_reel REAL DEFAULT 0,
    date_saisie TEXT DEFAULT '',
    note TEXT DEFAULT ''
)""")
print('Table aah_suivi creee')

c.execute("""CREATE TABLE IF NOT EXISTS devis_artisans (
    id SERIAL PRIMARY KEY,
    corps_metier TEXT,
    artisan TEXT DEFAULT '',
    devis_montant REAL DEFAULT 0,
    paye_montant REAL DEFAULT 0,
    statut TEXT DEFAULT 'a_faire',
    date_devis TEXT DEFAULT '',
    date_paiement TEXT DEFAULT '',
    note TEXT DEFAULT ''
)""")
print('Table devis_artisans creee')

conn.commit()
conn.close()
print('Toutes les tables creees sur Supabase OK')
