import re
p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# 1. Ajouter les fonctions BoursoBank et Crypto avant def main()
new_pages = '''
def page_boursobank(profil, cap):
    import sqlite3, urllib.parse
    titre("BoursoBank - Connexion Tink")
    st.info("Ce module permet de connecter ton compte BoursoBank via Tink (DSP2).")
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS tink_config (id INTEGER PRIMARY KEY, client_id TEXT DEFAULT '', client_secret TEXT DEFAULT '', updated TEXT DEFAULT CURRENT_TIMESTAMP)")
    if not c.execute("SELECT id FROM tink_config").fetchone():
        c.execute("INSERT INTO tink_config DEFAULT VALUES")
    conn.commit()
    row = c.execute("SELECT client_id, client_secret FROM tink_config WHERE id=1").fetchone()
    conn.close()
    old_cid = row[0] if row else ""
    old_cs = row[1] if row else ""
    cid = st.text_input("Client ID Tink", value=old_cid)
    cs = st.text_input("Client Secret Tink", value=old_cs, type="password")
    if st.button("Enregistrer les cles"):
        conn = sqlite3.connect(DB_PATH)
        conn.execute("UPDATE tink_config SET client_id=?, client_secret=?, updated=CURRENT_TIMESTAMP WHERE id=1", (cid, cs))
        conn.commit(); conn.close()
        st.success("Cles enregistrees !")
    if cid and cs:
        redirect = "https://console.tink.com/callback"
        tink_url = f"https://link.tink.com/1.0/transactions/connect-accounts?client_id={cid}&redirect_uri={urllib.parse.quote(redirect)}&market=FR&locale=fr_FR"
        st.markdown(f'<a href="{tink_url}" target="_blank" style="display:inline-block;background:#1A6B4B;color:white;padding:10px 20px;border-radius:8px;text-decoration:none;font-weight:700;">Ouvrir Boursorama sur Tink</a>', unsafe_allow_html=True)
    auth_code = st.text_input("Code Tink (depuis URL)")
    if st.button("Synchroniser") and auth_code and cid and cs:
        try:
            import urllib.request, json
            data = json.dumps({"client_id":cid,"client_secret":cs,"grant_type":"authorization_code","code":auth_code}).encode()
            req = urllib.request.Request("https://api.tink.com/api/v1/oauth/token", data=data, headers={"Content-Type":"application/json"})
            resp = urllib.request.urlopen(req, timeout=10)
            token_data = json.loads(resp.read())
            token = token_data.get("access_token","")
            if not token:
                st.error(f"Pas de token: {token_data}")
            else:
                req2 = urllib.request.Request("https://api.tink.com/api/v1/accounts/list", headers={"Authorization":f"Bearer {token}"})
                resp2 = urllib.request.urlopen(req2, timeout=10)
                accounts = json.loads(resp2.read())
                if accounts.get("accounts"):
                    for acc in accounts["accounts"]:
                        st.success(f"{acc.get('name','?')} : {acc.get('balances',{}).get('booked',{}).get('amount',{}).get('value','?')}")
                else:
                    st.warning(f"Aucun compte. Debug: {accounts}")
        except Exception as e:
            st.error(f"Erreur: {e}")


def page_crypto(profil, cap):
    titre("Module Crypto")
    st.info("Poche separee du plan patrimonial.")
    c1, c2 = st.columns(2)
    with c1:
        mise = st.number_input("Mise (euros)", value=500.0, step=100.0)
        levier = st.number_input("Levier", value=1.0, step=1.0, min_value=1.0, max_value=10.0)
        prix_entree = st.number_input("Prix entree", value=70000.0, step=1000.0)
        prix_cible = st.number_input("Prix cible", value=150000.0, step=1000.0)
        duree_ans = st.number_input("Duree (annees)", value=3.0, step=0.5)
    with c2:
        position = mise * levier
        quantite = position / prix_entree if prix_entree > 0 else 0
        liquidation = prix_entree - (mise / quantite) if quantite > 0 and levier > 1 else 0
        valeur_cible = quantite * prix_cible
        gain_brut = valeur_cible - position
        funding = position * 0.15 * duree_ans if levier > 1 else 0
        gain_net = gain_brut - funding - max(0, (gain_brut - funding) * 0.30)
        kpi("Position", f"{position:,.0f} E", f"x{levier:.0f}", "bleu")
        if levier > 1:
            kpi("Liquidation", f"{liquidation:,.0f} E", "", "rouge")
            kpi("Funding", f"{funding:,.0f} E", "", "orange")
        kpi("Gain net", f"{gain_net:,.0f} E", f"x{(mise+gain_net)/mise:.1f}", "vert" if gain_net > 0 else "rouge")
    if levier > 3:
        alerte('rouge', f"Levier x{levier:.0f} = risque eleve. Recommande : x1 spot.")
    elif levier > 1:
        alerte('orange', f"Levier x{levier:.0f} : acceptable courte duree.")
    else:
        alerte('vert', "Spot sans levier : strategie la plus sure.")


'''

t = t.replace('def main():', new_pages + 'def main():')

# 2. Ajouter navigation
old_saisie_nav = '"Saisie capital",'
new_saisie_nav = '"BoursoBank",\n            "Crypto",\n            "Saisie capital",'
t = t.replace(old_saisie_nav, new_saisie_nav, 1)

# 3. Ajouter dispatch
old_saisie_disp = '"Saisie capital":        lambda: page_saisie(profil,cap),'
new_saisie_disp = '"BoursoBank":             lambda: page_boursobank(profil,cap),\n        "Crypto":                  lambda: page_crypto(profil,cap),\n        "Saisie capital":        lambda: page_saisie(profil,cap),'
t = t.replace(old_saisie_disp, new_saisie_disp, 1)

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print('Pages ajoutees:', t.count('lambda:'), 'pages')
