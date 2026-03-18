from db_wrapper import ConnectionWrapper
c = ConnectionWrapper()
cur = c.cursor()
cur._cursor.execute('SELECT date_cible, action, montant, sens, fait FROM chronologie WHERE fait=1 ORDER BY date_cible DESC LIMIT 5')
print("=== FAITS ===")
for r in cur._cursor.fetchall():
    print(dict(r))
cur._cursor.execute('SELECT date_cible, action, montant, sens, fait FROM chronologie WHERE fait=0 ORDER BY date_cible ASC LIMIT 8')
print("=== A VENIR ===")
for r in cur._cursor.fetchall():
    print(dict(r))
c.close()
