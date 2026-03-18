FICHIER = r"C:\Users\BoulePiou\cockpit-raphael\app.py"
with open(FICHIER, "r", encoding="utf-8") as f:
    contenu = f.read()

modifs = 0

# 1. Poches capital : afficher TOUT meme a 0
ancien1 = "_poches_actives = [(n, v, c) for n, v, c in _poches if v > 0]"
nouveau1 = "_poches_actives = [(n, v, c) for n, v, c in _poches]"
if ancien1 in contenu:
    contenu = contenu.replace(ancien1, nouveau1, 1)
    modifs += 1
    print("[1/2] OK - Poches : tout affiche")

# 2. Revenus : afficher TOUT meme a 0
ancien2 = "_rev_actives = [(n, v, c) for n, v, c in _revenus if v > 0]"
nouveau2 = "_rev_actives = [(n, v, c) for n, v, c in _revenus]"
if ancien2 in contenu:
    contenu = contenu.replace(ancien2, nouveau2, 1)
    modifs += 1
    print("[2/2] OK - Revenus : tout affiche")

with open(FICHIER, "w", encoding="utf-8") as f:
    f.write(contenu)
print(f"\nTermine ! {modifs}/2")
