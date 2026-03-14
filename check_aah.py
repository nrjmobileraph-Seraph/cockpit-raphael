import psycopg2, psycopg2.extras
conn = psycopg2.connect(host='aws-1-eu-west-1.pooler.supabase.com', port=6543, dbname='postgres', user='postgres.zyizvlrwsatxqehhqiwh', password='Seraphetraph/62//26**', cursor_factory=psycopg2.extras.RealDictCursor)
c = conn.cursor()
c.execute('SELECT mois, montant_prevu FROM aah_suivi ORDER BY mois ASC')
for r in c.fetchall():
    print(r['mois'], '=', r['montant_prevu'])
conn.close()
