import sys
sys.path.insert(0, r'C:\Users\BoulePiou\cockpit-raphael')
import db_wrapper

# Creer table lmnp sur Supabase
conn = db_wrapper.connect()
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS lmnp (
    id SERIAL PRIMARY KEY,
    date_acquisition VARCHAR(20) DEFAULT '2026-04-28',
    valeur_acquisition NUMERIC DEFAULT 166000,
    valeur_terrain NUMERIC DEFAULT 16600,
    travaux NUMERIC DEFAULT 33000,
    loyer_brut_mensuel NUMERIC DEFAULT 920,
    charges_annuelles NUMERIC DEFAULT 4984,
    duree_amort_immeuble INTEGER DEFAULT 30,
    duree_amort_mobilier INTEGER DEFAULT 7,
    valeur_mobilier NUMERIC DEFAULT 10000,
    taux_irl_dernier NUMERIC DEFAULT 0.0243,
    date_derniere_revalorisation VARCHAR(20) DEFAULT '2025-01-01',
    updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
c.execute("INSERT INTO lmnp (id) VALUES (1) ON CONFLICT (id) DO NOTHING")
conn.commit()
conn.close()
print("OK - table lmnp creee sur Supabase")

# Investiguer jalons et parametres
src = open(r'C:\Users\BoulePiou\cockpit-raphael\app.py', encoding='utf-8').read()
import ast
tree = ast.parse(src)
for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef) and node.name in ('page_jalons', 'page_parametres'):
        print(f"Ligne {node.lineno} : {node.name}")
