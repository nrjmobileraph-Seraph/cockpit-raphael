import db_wrapper

print('=== TEST CONNEXION SUPABASE ===')
try:
    conn = db_wrapper.connect()
    c = conn.cursor()
    
    c.execute('SELECT cc+livret_a+ldds+lep+av1+av2+av3 as total FROM capital ORDER BY date DESC LIMIT 1')
    r = c.fetchone()
    print(f'Capital : {list(r.values())[0]:,.0f} EUR')
    
    c.execute('SELECT COUNT(*) as nb FROM chronologie')
    print(f'Jalons : {c.fetchone()["nb"]}')
    
    c.execute('SELECT COUNT(*) as nb FROM aah_suivi')
    print(f'AAH : {c.fetchone()["nb"]} annees')
    
    c.execute('SELECT COUNT(*) as nb FROM devis_artisans')
    print(f'Devis : {c.fetchone()["nb"]}')
    
    c.execute('SELECT loyer_net, rail_mensuel, aah_mensuel FROM profil LIMIT 1')
    p = c.fetchone()
    print(f'Profil : loyer={p["loyer_net"]}, rail={p["rail_mensuel"]}, aah={p["aah_mensuel"]}')
    
    conn.close()
    print('SUPABASE : CONNEXION STABLE ET DONNEES OK')
except Exception as e:
    print(f'ERREUR : {e}')
