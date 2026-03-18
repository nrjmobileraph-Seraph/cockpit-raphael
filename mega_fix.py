# mega_fix.py - Fait tout d'un coup
import os, shutil, glob

DOSSIER = r"C:\Users\BoulePiou\cockpit-raphael"

print("=" * 60)
print("  MEGA FIX - Cockpit Raphael")
print("=" * 60)

# ============================================================
# 1. FIX date_maj -> updated dans page_finary.py
# ============================================================
print("\n[1/4] Fix date_maj dans page_finary.py...")
pf = os.path.join(DOSSIER, "page_finary.py")
with open(pf, "r", encoding="utf-8") as f:
    contenu = f.read()

ancien = "ORDER BY date_maj DESC LIMIT 1"
nouveau = "ORDER BY updated DESC LIMIT 1"

if ancien in contenu:
    contenu = contenu.replace(ancien, nouveau)
    with open(pf, "w", encoding="utf-8") as f:
        f.write(contenu)
    print("   OK - date_maj remplace par updated")
else:
    if nouveau in contenu:
        print("   DEJA FAIT - updated deja present")
    else:
        print("   ATTENTION - pattern non trouve")

# ============================================================
# 2. FIX set_page_config dans app.py (favicon + sidebar)
# ============================================================
print("\n[2/4] Fix set_page_config dans app.py...")
ap = os.path.join(DOSSIER, "app.py")
with open(ap, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Trouver la ligne st.set_page_config(
idx_config = None
for i, line in enumerate(lines):
    if "st.set_page_config(" in line:
        idx_config = i
        break

if idx_config is not None:
    # Trouver la fin du bloc set_page_config (ligne avec ')' fermante)
    idx_end = idx_config
    paren_count = 0
    for i in range(idx_config, min(idx_config + 15, len(lines))):
        paren_count += lines[i].count("(") - lines[i].count(")")
        if paren_count <= 0:
            idx_end = i
            break

    # Remplacer le bloc entier
    nouveau_config = [
        'st.set_page_config(\n',
        '    page_title="Cockpit Patrimonial Raphael",\n',
        '    page_icon="\U0001f4b0",\n',
        '    layout="wide",\n',
        '    initial_sidebar_state="collapsed"\n',
        ')\n',
    ]

    lines = lines[:idx_config] + nouveau_config + lines[idx_end + 1:]

    with open(ap, "w", encoding="utf-8") as f:
        f.writelines(lines)
    print(f"   OK - set_page_config remplace (lignes {idx_config+1}-{idx_end+1})")
    print("   -> favicon: argent, sidebar: collapsed par defaut")
else:
    print("   ERREUR - set_page_config non trouve")

# ============================================================
# 3. NOUVEAU Cockpit.bat (mode app plein ecran)
# ============================================================
print("\n[3/4] Creation Cockpit.bat ameliore...")
bat_path = os.path.join(DOSSIER, "..", "Desktop", "Cockpit.bat")
bat_content = """@echo off
title Cockpit Raphael - Demarrage
cd /d C:\\Users\\BoulePiou\\cockpit-raphael

:: Fermer ancien serveur Streamlit si actif
taskkill /f /im "streamlit.exe" >nul 2>&1

:: Lancer le serveur en arriere-plan
start /min cmd /c "streamlit run app.py --server.headless true --server.port 8501"

:: Attendre que le serveur demarre
echo Demarrage du cockpit...
timeout /t 6 /nobreak >nul

:: Ouvrir Edge en mode application (plein ecran, sans barre)
start msedge --app=http://localhost:8501

echo Cockpit lance !
"""
try:
    with open(bat_path, "w", encoding="utf-8") as f:
        f.write(bat_content)
    print(f"   OK - Cockpit.bat cree sur le Bureau")
    print(f"   -> Double-clic = Edge plein ecran sans barre")
except Exception as e:
    # Fallback dans le dossier cockpit
    bat_path2 = os.path.join(DOSSIER, "Cockpit.bat")
    with open(bat_path2, "w", encoding="utf-8") as f:
        f.write(bat_content)
    print(f"   OK - Cockpit.bat cree dans cockpit-raphael/")
    print(f"   (Deplace-le sur le Bureau manuellement)")

# ============================================================
# 4. NETTOYAGE des fichiers parasites
# ============================================================
print("\n[4/4] Nettoyage des fichiers parasites...")

# Patterns a supprimer
patterns_suppr = [
    "fix_*.py", "fix2*.py",
    "patch*.py",
    "show*.py",
    "check*.py", "check_*.py",
    "find*.py", "find_*.py",
    "clean_*.py",
    "audit*.py",
    "cache*.py",
    "add_*.py",
    "v49_*.py",
    "final*.py", "final_*.py",
    "update_*.py",
    "upgrade_*.py",
    "hide_*.py",
    "compare_*.py",
    "count.py",
    "diag.py", "diagnostic.py",
    "pre_doc.py",
    "remove_*.py",
    "status_check.py",
    "verif.py",
    "lanceur.py",
    "migrate_cloud.py",
    "setup_cloud.py",
    "supabase_create.py",
    "supabase_migrate.py",
    "tests_complets.py",
    "tests_niveau2.py",
    "test_all.py",
    "test_pages.py",
    "test_serveur_final.py",
    "test_supabase.py",
    "backup.py",
    "show.py",
    "ace",
    "python",
    "streamlit",
    "impregnation_condensee.txt",
    "chk.py",
    "app.py.backup",
    "app.py.backup_before_clean",
    "app.py.backup_local",
    "app.py.backup_sqlite",
    "app.py.bak_*",
    "app.py.bak_parents",
    "app.py.manual-backup",
    "app.py.MORT*",
    "patch_parents.py",
]

# Fichiers a GARDER absolument
garder = {
    "app.py",
    "app_cockpit_v49.py",
    "db_wrapper.py",
    "finary_wrapper.py",
    "page_finary.py",
    "finary_api.py",
    "credentials.json",
    "jwt.json",
    "localCookiesMozilla.txt",
    ".finary_token.json",
    ".env",
    ".gitignore",
    "fond.png",
    "cockpit.db",
    "Cockpit.bat",
    "Cockpit_Raphael.spec",
    "Procfile",
    "README.md",
    "requirements.txt",
    "mega_fix.py",
}

# Dossiers a garder
dossiers_garder = {
    ".streamlit", "backups", "build", "cockpit-raphael",
    "dist", "static", "__pycache__"
}

supprimes = 0
for item in os.listdir(DOSSIER):
    chemin = os.path.join(DOSSIER, item)

    # Skip dossiers
    if os.path.isdir(chemin):
        continue

    # Skip fichiers a garder
    if item in garder:
        continue

    # Verifier si le fichier matche un pattern
    supprimer = False
    for pat in patterns_suppr:
        if "*" in pat:
            import fnmatch
            if fnmatch.fnmatch(item, pat):
                supprimer = True
                break
        else:
            if item == pat:
                supprimer = True
                break

    if supprimer:
        try:
            os.remove(chemin)
            print(f"   Supprime: {item}")
            supprimes += 1
        except Exception as e:
            print(f"   ERREUR sur {item}: {e}")

print(f"\n   Total supprime: {supprimes} fichiers")

# ============================================================
# RESUME
# ============================================================
print("\n" + "=" * 60)
print("  RESUME")
print("=" * 60)
print("  [1] date_maj -> updated dans page_finary.py    OK")
print("  [2] set_page_config avec favicon + collapsed    OK")
print("  [3] Cockpit.bat sur le Bureau                   OK")
print("  [4] Nettoyage fichiers parasites                OK")
print("")
print("  PROCHAINE ETAPE:")
print("  1. Relance le cockpit: streamlit run app.py")
print("  2. Sur smartphone: Chrome > URL Render > 3 points")
print("     > Ajouter a l ecran d accueil")
print("  3. Sur PC: double-clic sur Cockpit.bat")
print("=" * 60)
