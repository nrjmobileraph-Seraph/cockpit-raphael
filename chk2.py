from db_wrapper import ConnectionWrapper
c = ConnectionWrapper()
cur = c.cursor()
cur._cursor.execute('SELECT column_name FROM information_schema.columns WHERE table_name=%s ORDER BY ordinal_position', ('chronologie',))
[print(r['column_name']) for r in cur._cursor.fetchall()]
c.close()
