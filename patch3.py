p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Trouver et remplacer dans la navigation
if 'BoursoBank' not in t.split('Navigation')[1].split('])')[0] if 'Navigation' in t else '':
    t = t.replace('Saisie capital",\n        ])', 'Saisie capital",\n            "BoursoBank",\n            "Crypto",\n        ])')
    t = t.replace('page_saisie(profil,cap),\n    }[page]()', 'page_saisie(profil,cap),\n        "BoursoBank":             lambda: page_boursobank(profil,cap),\n        "Crypto":                  lambda: page_crypto(profil,cap),\n    }[page]()')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print('Lambdas:', t.count('lambda:'))
print('BoursoBank dans nav:', 'BoursoBank' in t.split('radio')[1] if 'radio' in t else False)
