FICHIER = r"C:\Users\BoulePiou\cockpit-raphael\app.py"
with open(FICHIER, "r", encoding="utf-8") as f:
    lines = f.readlines()

modifs = 0

# 1. Supprimer les fleches parasites (_fl2_html) - lignes qui contiennent _fl2
# Chercher le bloc _fl2_html
debut_fl2 = None
fin_fl2 = None
for i, l in enumerate(lines):
    if "_fl2_html" in l and debut_fl2 is None:
        debut_fl2 = i
    if debut_fl2 is not None and "st.markdown(_fl2_html" in l:
        fin_fl2 = i
        break

if debut_fl2 is not None and fin_fl2 is not None:
    lines = lines[:debut_fl2] + lines[fin_fl2+1:]
    modifs += 1
    print(f"[1/2] OK - Fleches parasites supprimees (lignes {debut_fl2+1}-{fin_fl2+1})")
else:
    print("[1/2] Fleches non trouvees")

# 2. Cadre plus visible autour des sources
for i, l in enumerate(lines):
    if 'border:1px solid #333;border-radius:12px;padding:12px;margin-bottom:16px;' in l:
        lines[i] = l.replace(
            'border:1px solid #333;border-radius:12px;padding:12px;margin-bottom:16px;',
            'border:2px solid #C4922A;border-radius:12px;padding:14px;margin-bottom:16px;background:#0A0A0A;'
        )
        modifs += 1
        print(f"[2/2] OK - Cadre dore visible autour des sources (ligne {i+1})")
        break

with open(FICHIER, "w", encoding="utf-8") as f:
    f.writelines(lines)
print(f"\nTermine ! {modifs}/2")
