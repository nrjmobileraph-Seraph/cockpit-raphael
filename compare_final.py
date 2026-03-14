import sqlite3, psycopg2, psycopg2.extras

print('=' * 60)
print('COMPARAISON LOCAL vs SERVEUR')
print('=' * 60)

# Serveur
srv = psycopg2.connect(host='aws-1-eu-west-1.pooler.supabase.com', port=6543, dbname='postgres', user='postgres.zyizvlrwsatxqehhqiwh', password='Seraphetraph/62//26**', cursor_factory=psycopg2.extras.RealDictCursor)
sc = srv.cursor()

# Local (backup)
import os, glob
backup_dir = 'C:/Users/BoulePiou/cockpit-raphael/backups'
backups = sorted(glob.glob(os.path.join(backup_dir, '*.db')))
if backups:
    loc = sqlite3.connect(backups[-1])
    loc.row_factory = sqlite3.Row
    lc = loc.cursor()
    print(f'Backup local : {os.path.basename(backups[-1])}')
else:
    print('Pas de backup local trouve')
    exit()

ok = 0
err = 0

# 1. PROFIL
print('\n--- PROFIL ---')
sc.execute('SELECT * FROM profil LIMIT 1')
sp = dict(sc.fetchone())
lc.execute('SELECT * FROM profil WHERE id=1')
lp = dict(lc.fetchone())
for k in ['rail_mensuel','aah_mensuel','loyer_net','taux_mdph','age_cible','rendement_annuel','capital_cible']:
    sv = sp.get(k)
    lv = lp.get(k)
    if sv == lv:
        print(f'  [OK] {k} : local={lv} serveur={sv}'); ok+=1
    else:
        print(f'  [DIFF] {k} : local={lv} serveur={sv}'); err+=1

# 2. CAPITAL
print('\n--- CAPITAL ---')
sc.execute('SELECT cc,livret_a,ldds,lep,av1,av2,av3 FROM capital ORDER BY date DESC LIMIT 1')
scap = dict(sc.fetchone())
lc.execute('SELECT cc,livret_a,ldds,lep,av1,av2,av3 FROM capital ORDER BY date DESC LIMIT 1')
lcap = dict(lc.fetchone())
for k in ['cc','livret_a','ldds','lep','av1','av2','av3']:
    if scap[k] == lcap[k]:
        print(f'  [OK] {k} : {scap[k]:,.0f}'); ok+=1
    else:
        print(f'  [DIFF] {k} : local={lcap[k]} serveur={scap[k]}'); err+=1

stot = sum(scap.values())
ltot = sum(lcap.values())
print(f'  Total local={ltot:,.0f} serveur={stot:,.0f}')

# 3. JALONS
print('\n--- JALONS ---')
sc.execute('SELECT action, montant, sens FROM chronologie ORDER BY date_cible ASC')
srows = sc.fetchall()
lc.execute('SELECT action, montant, sens FROM chronologie ORDER BY date_cible ASC')
lrows = [dict(r) for r in lc.fetchall()]
print(f'  Local : {len(lrows)} jalons | Serveur : {len(srows)} jalons')
if len(srows) == len(lrows):
    print(f'  [OK] Meme nombre'); ok+=1
    for i in range(len(srows)):
        if srows[i]['action'] != lrows[i]['action'] or srows[i]['montant'] != lrows[i]['montant']:
            print(f'  [DIFF] Jalon {i+1} : local={lrows[i]["action"][:40]} serveur={srows[i]["action"][:40]}')
            err+=1
        else:
            ok+=1
else:
    print(f'  [DIFF] Nombre different'); err+=1

# 4. AAH
print('\n--- AAH ---')
sc.execute('SELECT mois, montant_prevu FROM aah_suivi ORDER BY mois ASC')
saah = sc.fetchall()
lc.execute('SELECT mois, montant_prevu FROM aah_suivi ORDER BY mois ASC')
laah = [dict(r) for r in lc.fetchall()]
for i in range(min(len(saah), len(laah))):
    sm = saah[i]['montant_prevu']
    lm = laah[i]['montant_prevu']
    smois = saah[i]['mois']
    lmois = laah[i]['mois']
    if sm == lm:
        print(f'  [OK] {smois} : {sm}'); ok+=1
    else:
        print(f'  [DIFF] local {lmois}={lm} serveur {smois}={sm}'); err+=1

# 5. DEVIS
print('\n--- DEVIS ---')
sc.execute('SELECT corps_metier, devis_montant FROM devis_artisans ORDER BY id ASC')
sdev = sc.fetchall()
lc.execute('SELECT corps_metier, devis_montant FROM devis_artisans ORDER BY id ASC')
ldev = [dict(r) for r in lc.fetchall()]
if len(sdev) == len(ldev):
    print(f'  [OK] {len(sdev)} corps de metier identiques'); ok+=1
else:
    print(f'  [DIFF] local={len(ldev)} serveur={len(sdev)}'); err+=1

srv.close()
loc.close()

print(f'\n{"="*60}')
print(f'COMPARAISON : {ok} IDENTIQUES / {err} DIFFERENCES')
if err == 0:
    print('LOCAL ET SERVEUR SONT 100% IDENTIQUES')
else:
    print(f'{err} difference(s) a corriger')
print('='*60)
