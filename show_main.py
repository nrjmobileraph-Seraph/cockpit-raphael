p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
lines=f.readlines()
f.close()

# Trouver def main()
for i in range(len(lines)):
    if 'def main():' in lines[i]:
        print(f'main() ligne {i+1}')
        for j in range(i, min(i+15, len(lines))):
            print(f'  {j+1}: {lines[j].rstrip()[:100]}')
        break
