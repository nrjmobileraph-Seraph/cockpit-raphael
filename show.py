with open('C:/Users/BoulePiou/cockpit-raphael/app.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i in range(395, 405):
    print(f'{i+1}: {repr(lines[i][:80])}')
