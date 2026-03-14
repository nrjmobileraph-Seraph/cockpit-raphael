import psycopg2, psycopg2.extras

conn = psycopg2.connect(host='aws-1-eu-west-1.pooler.supabase.com', port=6543, dbname='postgres', user='postgres.zyizvlrwsatxqehhqiwh', password='Seraphetraph/62//26**', cursor_factory=psycopg2.extras.RealDictCursor)
c = conn.cursor()

# Mettre a jour le jalon AV Jean-Luc
c.execute("UPDATE chronologie SET montant=22800 WHERE action LIKE '%AV Jean-Luc%'")
conn.commit()
print('AV Jean-Luc mis a jour : 22 800 EUR')

# Recalculer le capital total
# Ancien: 513 500 - 52 424 = 461 076
# Nouveau: 513 500 - 11 700 = 501 800 entrees, - 52 424 = 449 376
# Ou plus simple: 461 000 - 11 700 = 449 300
ancien_av = 34500
nouveau_av = 22800
diff = ancien_av - nouveau_av
print(f'Difference : -{diff:,.0f} EUR')
print(f'Nouveau capital net : {461000 - diff:,.0f} EUR')

# Verifier
c.execute("SELECT montant FROM chronologie WHERE action LIKE '%AV Jean-Luc%'")
r = c.fetchone()
print(f'Verification : AV Jean-Luc = {r["montant"]:,.0f} EUR')

conn.close()
