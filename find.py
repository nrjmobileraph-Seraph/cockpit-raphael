with open('C:/Users/BoulePiou/cockpit-raphael/app.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines, 1):
    if 'sqlite3' in line or 'BoulePiou' in line:
        print(f'{i}: {line.rstrip()[:100]}')
