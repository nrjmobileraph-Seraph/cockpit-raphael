import shutil
path = r"C:\Users\BoulePiou\cockpit-raphael\app.py"
shutil.copy2(path, path + ".bak2")
with open(path, "r", encoding="utf-8") as f:
    lines = f.read().split("\n")
start = None
for i, l in enumerate(lines):
    if "BUDGET AUJOURD" in l and "RESTE CE MOIS" in l:
        start = i + 1
        break
if start is None:
    print("ERREUR: BUDGET AUJOURD HUI introuvable"); exit(1)
end = None
for i in range(start, min(start + 150, len(lines))):
    if "titre(" in lines[i]:
        end = i; break
if end is None:
    print("ERREUR: titre() introuvable"); exit(1)
with open(r"C:\Users\BoulePiou\cockpit-raphael\bloc_v2.txt", "r", encoding="utf-8") as f:
    new = f.read().split("\n")
result = lines[:start] + [""] + new + [""] + lines[end:]
with open(path, "w", encoding="utf-8") as f:
    f.write("\n".join(result))
print(f"OK ! Lignes {start+1}-{end} remplacees par {len(new)} lignes.")
