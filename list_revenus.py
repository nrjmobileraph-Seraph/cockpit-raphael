FICHIER = r"C:\Users\BoulePiou\cockpit-raphael\app.py"
with open(FICHIER, "r", encoding="utf-8") as f:
    contenu = f.read()

# Chercher toutes les sources de revenus mentionnees
import re
sources = set()
for mot in ["aah", "loyer", "pch", "aspa", "rvd", "arva", "rendement", "interet", "pension", "rente", "allocation"]:
    for m in re.finditer(r'["\'](' + mot + r'[^"\']*)["\']', contenu, re.IGNORECASE):
        sources.add(m.group(1))

print("=== SOURCES DE REVENUS TROUVEES ===")
for s in sorted(sources):
    print(f"  - {s}")

# Afficher les valeurs du profil
for ligne in contenu.split("\n"):
    if any(x in ligne for x in ["aah_mensuel", "loyer_net", "pch_mensuel", "rvd_mensuel", "rail_mensuel"]):
        if "=" in ligne or ":" in ligne:
            print(ligne.strip()[:100])
