FICHIER = r"C:\Users\BoulePiou\cockpit-raphael\app.py"
with open(FICHIER, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Supprimer lignes 526-538 (les petits rectangles noms + commentaire fleches vide)
# index 525 a 538
debut = None
fin = None
for i, l in enumerate(lines):
    if "# Petits rectangles noms entre les fleches" in l:
        debut = i
    if debut is not None and "# 6 RECTANGLES SOURCES en bas" in l:
        fin = i
        break

if debut is not None and fin is not None:
    lines = lines[:debut] + ["\n"] + lines[fin:]
    with open(FICHIER, "w", encoding="utf-8") as f:
        f.writelines(lines)
    print(f"OK - Petits rectangles noms supprimes (lignes {debut+1}-{fin})")
else:
    print(f"ERREUR debut={debut} fin={fin}")
