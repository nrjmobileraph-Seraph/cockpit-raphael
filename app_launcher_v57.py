import os
import runpy

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CANDIDATES = [
    "app_cockpit_v57_dashboard_fixed.py",
    "app_cockpit_v56_dashboard_real.py",
    "app_cockpit_v55_dashboard_schema.py",
    "app_cockpit_v54_tests.py",
    "app_cockpit_v53_dashboard.py",
    "app_cockpit_v51.py",
    "app_cockpit_v50.py",
    "app_v50_final.py",
    "app_backup_definitive.py",
]

target = None
for name in CANDIDATES:
    path = os.path.join(BASE_DIR, name)
    if os.path.exists(path):
        target = path
        break

if target is None:
    raise FileNotFoundError(
        "Aucune version cockpit exploitable trouvée. Cherché : " + ", ".join(CANDIDATES)
    )

runpy.run_path(target, run_name="__main__")
