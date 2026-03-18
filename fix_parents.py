FICHIER = r"C:\Users\BoulePiou\cockpit-raphael\app.py"
with open(FICHIER, "r", encoding="utf-8") as f:
    contenu = f.read()

ancien = '''                <div style="color:#BBA888;font-size:22px;font-weight:700;letter-spacing:2px;">Pour mes Parents d Amour...</div>
                <div style="color:#FF7777;font-size:36px;font-weight:900;">{reste_vivre} EUR</div>
                <div style="color:#DDCCBB;font-size:12px;">&nbsp;</div>'''

nouveau = '''                <div style="color:#BBA888;font-size:11px;text-transform:uppercase;">Pour mes Parents d Amour...</div>
                <div style="color:#FF7777;font-size:36px;font-weight:900;">{versement_parents} EUR</div>
                <div style="color:#DDCCBB;font-size:12px;">par mois</div>'''

if ancien in contenu:
    contenu = contenu.replace(ancien, nouveau)
    with open(FICHIER, "w", encoding="utf-8") as f:
        f.write(contenu)
    print("OK - Parents d'Amour harmonise avec les autres KPI")
else:
    print("ERREUR - bloc non trouve")
