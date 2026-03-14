import shutil, os
from datetime import date

src = 'C:/Users/BoulePiou/cockpit-raphael/cockpit.db'
backup_dir = 'C:/Users/BoulePiou/cockpit-raphael/backups'
os.makedirs(backup_dir, exist_ok=True)

backup_name = f'cockpit_backup_{date.today()}.db'
backup_path = os.path.join(backup_dir, backup_name)
shutil.copy2(src, backup_path)

# Garder les 10 derniers backups
backups = sorted(os.listdir(backup_dir))
while len(backups) > 10:
    os.remove(os.path.join(backup_dir, backups.pop(0)))

print(f'Backup cree : {backup_path}')
print(f'Backups existants : {len(os.listdir(backup_dir))}')
