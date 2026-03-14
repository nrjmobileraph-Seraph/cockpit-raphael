import re
p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
lines=f.readlines()
f.close()

fixed=0
mots = ["aujourd'hui","d'achat","d'un","d'une","l'ensemble","n'est",
        "l'indice","l'INSEE","qu'il","qu'on","qu'une","qu'en",
        "l'AAH","l'ASPA","l'APA","l'appart","l'appartement",
        "l'abattement","l'agent","l'assurance","l'immobilier",
        "l'impot","l'inflation","l'investissement","l'usufruit",
        "l'ancien","l'annexe","l'application","l'allocation",
        "d'epargne","d'euros","d'impot","d'imposition","d'activite",
        "d'acquisition","d'amortissement","d'entretien","d'exploitation",
        "c'est","s'applique","s'arrete","s'il","j'ai",
        "jusqu'a","jusqu'au","jusqu'en"]

for i in range(len(lines)):
    if "st.markdown(f'" in lines[i]:
        for mot in mots:
            if mot in lines[i]:
                lines[i]=lines[i].replace(mot, mot.replace("'","&#39;"))
                fixed+=1

f=open(p,'w',encoding='utf-8')
f.writelines(lines)
f.close()
print(f'Apostrophes corrigees: {fixed}')

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    # Trouver le mot problematique
    err=str(e)
    print(f'Encore une erreur: {err[:200]}')
    # Afficher la ligne problematique
    if 'line' in err:
        import re
        m=re.search(r'line (\d+)',err)
        if m:
            ln=int(m.group(1))-1
            print(f'Ligne {ln+1}: {lines[ln][:150]}')
