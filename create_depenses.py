import sys
sys.path.append('C:/Users/BoulePiou/cockpit-raphael')
import db_wrapper
conn = db_wrapper.connect()
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS depenses (
    id SERIAL PRIMARY KEY,
    date TEXT NOT NULL,
    montant REAL NOT NULL,
    categorie TEXT NOT NULL,
    priorite TEXT DEFAULT 'essentiel',
    description TEXT DEFAULT '',
    source TEXT DEFAULT 'manuel',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)""")
conn.commit()
conn.close()
print('SUCCES')
