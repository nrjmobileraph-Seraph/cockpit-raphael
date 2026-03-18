import re

path = r"C:\Users\BoulePiou\cockpit-raphael\app.py"
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Find the BUDGET AUJOURD HUI / RESTE CE MOIS line (the anchor BEFORE our section)
start = None
for i, l in enumerate(lines):
    if "BUDGET AUJOURD" in l and "RESTE CE MOIS" in l:
        start = i + 1  # line after BUDGET
        break

# Find where the next major section starts after our block (titre or similar)
end = None
if start:
    for i in range(start, min(start + 100, len(lines))):
        if "titre(" in lines[i] or "st.subheader" in lines[i] or ("# ===" in lines[i] and "COCKPIT" in lines[i].upper()):
            end = i
            break

if start and end:
    # Skip blank lines right after BUDGET
    while start < end and lines[start].strip() == "":
        start += 1
    print(f"Section a remplacer: lignes {start+1} a {end} (indices {start}-{end-1})")
    print(f"Premiere ligne: {lines[start][:80].strip()}")
    print(f"Derniere ligne: {lines[end-1][:80].strip()}")
    print(f"Ligne APRES: {lines[end][:80].strip()}")
else:
    print(f"start={start}, end={end} - pattern non trouve")
    # Fallback: search for our broken block
    for i, l in enumerate(lines):
        if "REVENUS MENSUELS : cartes" in l or "PLANCHER" in l:
            print(f"  L{i+1}: {l[:80].strip()}")
