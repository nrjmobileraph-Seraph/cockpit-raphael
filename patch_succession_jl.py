p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Ajouter la section succession Jean-Luc dans l'annexe, avant le dernier '''
insert = '    st.info("Les sections ci-dessous reprennent les memes informations en format tableau pour reference precise.")'

succession_jl = '''    titre("SUCCESSION JEAN-LUC BOUSSY")
    st.markdown('<div style="color:#D0C0A8;font-size:13px;margin-bottom:10px;">Document etabli le 3 mars 2026. Heritiers : Raphael et Anne-Lyse. Neveu et niece - Abattement handicap applique.</div>', unsafe_allow_html=True)

    st.markdown("""
**Partie 1 - Patrimoine du defunt**

| Element | Montant |
|---|---|
| Maison | 200 000 EUR |
| Appartement (neuf, solde restant -17 000 EUR) | 290 000 EUR |
| Liquidites bancaires | 30 000 EUR |
| Voiture | 2 000 EUR |
| Assurance-vie (hors succession) | 69 000 EUR |
| **TOTAL PATRIMOINE** | **591 000 EUR** |

**Partie 2 - Dettes deduites de la succession**

| Poste | Montant |
|---|---|
| Solde restant achat appartement neuf | -17 000 EUR |
| Cuisine en cours d installation | -7 000 EUR |
| Frais de fonctionnement lies au deces | -5 000 EUR |
| Obseques (corps donne a la science) | 0 EUR |
| **ACTIF NET SUCCESSORAL** | **493 000 EUR** |
| **Part par heritier (÷ 2)** | **246 500 EUR** |

**Partie 3 - Calcul des impots (par heritier)**

| Etape | Montant |
|---|---|
| Part brute | 246 500 EUR |
| - Abattement neveu/niece | -7 967 EUR |
| - Abattement handicap (art. 779 II CGI) | -159 325 EUR |
| = Part taxable | 79 208 EUR |
| x Taux 55% (oncle -> neveu/niece) | -43 564 EUR |
| = Net apres impots | 202 936 EUR |
| + Assurance-vie (avant 70 ans, net) | +34 500 EUR |
| **= SOUS-TOTAL PAR HERITIER** | **237 436 EUR** |

**Partie 4 - Detail complet de tous les frais**

| Poste de frais | Total | Par heritier |
|---|---|---|
| **FRAIS DE NOTAIRE** | | |
| Acte de notoriete | 81 EUR | |
| Declaration de succession | 3 370 EUR | |
| Attestation propriete maison | 2 493 EUR | |
| Attestation propriete appartement | 3 391 EUR | |
| Partage amiable | 7 583 EUR | |
| TVA 20% | 3 384 EUR | |
| Contribution securite immobiliere | 490 EUR | |
| Debours (copies, extraits, etats) | 800 EUR | |
| Sous-total notaire | 21 592 EUR | **10 796 EUR** |
| **AGENCE IMMOBILIERE** | | |
| Maison (4%) | 8 000 EUR | |
| Appartement (5%) | 14 500 EUR | |
| Sous-total agence | 22 500 EUR | **11 250 EUR** |
| **DIAGNOSTICS IMMOBILIERS** | | |
| Maison (DPE, amiante, plomb) | 450 EUR | |
| Appartement | 350 EUR | |
| Sous-total diagnostics | 800 EUR | **400 EUR** |
| **CHARGES COURANTES (~6 mois)** | | |
| Taxe fonciere (2 biens) | 1 350 EUR | |
| Charges copropriete appartement | 900 EUR | |
| Assurance habitation (2 biens) | 330 EUR | |
| Eau / electricite / entretien | 300 EUR | |
| Sous-total charges courantes | 2 880 EUR | **1 440 EUR** |
| **DEBARRAS MAISON** | 4 000 EUR | **2 000 EUR** |
| | | |
| **TOTAL DE TOUS LES FRAIS** | **51 772 EUR** | **25 886 EUR** |

**Resultat final - Net de tout**

| | Montant |
|---|---|
| Sous-total par heritier | 237 436 EUR |
| - Total frais par heritier | -25 886 EUR |
| **NET FINAL RAPHAEL** | **211 550 EUR** |
| **NET FINAL ANNE-LYSE** | **211 550 EUR** |
| **TOTAL RECU PAR LES 2 HERITIERS** | **423 099 EUR** |
""")
    st.warning("L abattement handicap (159 325 EUR) necessite un certificat medical et/ou decision CDAPH attestant l incapacite de travailler. Chiffres estimatifs - seul le notaire fera le decompte definitif.")

    '''

t = t.replace(insert, succession_jl + insert)

f = open(p, 'w', encoding='utf-8')
f.write(t)
f.close()
print('Succession Jean-Luc integree OK')
