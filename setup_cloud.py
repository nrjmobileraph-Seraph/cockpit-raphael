# Creer les fichiers necessaires pour Streamlit Cloud

# 1. requirements.txt
f = open('C:/Users/BoulePiou/cockpit-raphael/requirements.txt', 'w')
f.write('streamlit\npandas\npsycopg2-binary\n')
f.close()
print('requirements.txt cree')

# 2. .streamlit/secrets.toml
import os
os.makedirs('C:/Users/BoulePiou/cockpit-raphael/.streamlit', exist_ok=True)
f = open('C:/Users/BoulePiou/cockpit-raphael/.streamlit/secrets.toml', 'w')
f.write('[database]\n')
f.write('host = "db.zyizvlrwsatxqehhqiwh.supabase.co"\n')
f.write('port = 5432\n')
f.write('dbname = "postgres"\n')
f.write('user = "postgres"\n')
f.write('password = "Seraphetraph/62//26**"\n')
f.close()
print('secrets.toml cree')

print('Fichiers cloud prets')
