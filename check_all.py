import sys
sys.path.insert(0, r'C:\Users\BoulePiou\cockpit-raphael')
import db_wrapper

print("=== CONTROLE SUPABASE ===")
tables = ['profil', 'capital', 'chronologie', 'aah_suivi', 'devis_artisans', 'lmnp']
conn = db_wrapper.connect()
c = conn.cursor()
ok = 0
for t in tables:
    try:
        c.execute(f"SELECT COUNT(*) as n FROM {t}")
        row = c.fetchone()
        n = row['n'] if row else 0
        print(f"  OK  {t} : {n} ligne(s)")
        ok += 1
    except Exception as e:
        print(f"  ERREUR  {t} : {e}")
conn.close()
print(f"\n{ok}/{len(tables)} tables accessibles sur Supabase")

print("\n=== CONTROLE PAGES (import) ===")
import importlib, types, unittest.mock as mock

# Mock streamlit pour eviter l'interface graphique
import streamlit as st_real
mocks = ['write','markdown','columns','metric','button','selectbox','number_input',
         'text_input','form','form_submit_button','expander','subheader','caption',
         'progress','divider','line_chart','date_input','checkbox','info','success',
         'warning','error','rerun','sidebar','set_page_config','stop']
for m in mocks:
    setattr(st_real, m, mock.MagicMock())
st_real.session_state = mock.MagicMock()
st_real.columns = mock.MagicMock(return_value=[mock.MagicMock(), mock.MagicMock(), mock.MagicMock()])

import app
profil = {'nom':'Raphael','date_naissance':'1975-08-26','age_cible':92,'capital_cible':50000,
          'taux_mdph':75,'aah_mensuel':1033,'loyer_net':320,'rail_mensuel':2760,
          'rendement_annuel':0.035,'pch_mensuel':0,'rvd_mensuel':450,'mdph_80plus':0}
cap = {'CC':500,'Livret A':22950,'LDDS':12000,'LEP':10000,'AV1':130000,'AV2':130000,'AV3':155550}

pages = [
    ('dashboard', lambda: app.page_dashboard(profil, cap)),
    ('lmnp',      lambda: app.page_lmnp(profil, cap)),
    ('caf_pch',   lambda: app.page_caf_pch(profil, cap)),
    ('succession',lambda: app.page_succession(profil, cap)),
    ('jalons',    lambda: app.page_jalons(profil, cap)),
    ('simulateur',lambda: app.page_simulateur(profil, cap)),
    ('arva',      lambda: app.page_arva(profil, cap)),
    ('parametres',lambda: app.page_parametres(profil, cap)),
    ('inflation', lambda: app.page_inflation(profil, cap)),
    ('senior',    lambda: app.page_senior(profil, cap)),
    ('export',    lambda: app.page_export(profil, cap)),
]

ok2 = 0
for nom, fn in pages:
    try:
        fn()
        print(f"  OK  {nom}")
        ok2 += 1
    except Exception as e:
        print(f"  CRASH  {nom} : {e}")

print(f"\n{ok2}/{len(pages)} pages sans erreur")
