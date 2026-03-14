p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Ajouter la page Annexe avant def main()
annexe_page = '''
def page_annexe(profil, cap):
    titre("ANNEXE - REFERENCE COMPLETE DU PLAN")
    st.info("Toutes les decisions, calculs et reflexions du projet patrimonial. Mis a jour au fil des sessions.")

    titre("1. PARAMETRES DEFINITIFS (valides par 4 IA)")
    st.markdown("""
| Parametre | Valeur | Statut |
|---|---|---|
| Capital initial | 393 192 EUR | Fige |
| Rail mensuel | 2 760 EUR/mois constant | Fige |
| AAH | 1 033 EUR/mois | Perdue a 64 ans (base) |
| Loyer LMNP net | 448 EUR/mois | Jusqu'a vente 64 ans |
| Rendement | 3,5%/an effectif | Fige |
| Cible C92 | 50 000 EUR | Fige |
| Age transition | 64 ans (reforme 2023, ne 1975) | Fige |
| Vente immo | A partir de 64 ans | Fige |
| Heritiere | Anne-Lyse Boussy | Fige |
""")

    titre("2. REPARTITION DU CAPITAL")
    st.markdown("""
| Poche | Montant | Taux | Role | Ordre pioche |
|---|---|---|---|---|
| CC | 500 EUR | 0% | Vie quotidienne | 1er |
| Livret A | 22 950 EUR | 2,4% | Buffer 6 mois | 2e |
| LDDS | 12 000 EUR | 2,4% | Buffer complementaire | 3e |
| AV1 | 109 500 EUR | 3,5% | Abattement disponible (>8 ans) | 4e |
| AV2 | 109 500 EUR | 3,5% | Abattement en 2034 | 5e |
| AV3 | 128 742 EUR | 3,5% | Reserve strategique | 6e |
| LEP | 10 000 EUR | 3,5% | DERNIER - meilleur taux | 7e |
""")

    titre("3. PHASES DU PLAN")
    st.markdown("""
**Phase 1 (50-64 ans)** : AAH 1 033 + Loyer 448 + Pioche 1 279 = 2 760 EUR/mois

**Transition 64 ans** : AAH sarrete + Vente T3 (+252 510 EUR) + Loyer sarrete

**Phase 2 (64-75 ans)** : Pioche capital seule = 2 760 EUR/mois

**Phase 3 (75-92 ans)** : RVD 450 + Pioche 2 310 = 2 760 EUR/mois
""")

    titre("4. TRAJECTOIRE DU CAPITAL")
    st.markdown("""
| Age | Capital | Evenement |
|---|---|---|
| 50 ans | 393 192 EUR | Depart du plan |
| 56 ans | ~381 000 EUR | Croisiere Phase 1 |
| 62 ans | ~367 000 EUR | Estimation vente immo |
| 64 ans avant vente | ~361 000 EUR | Fin AAH + fin loyer |
| 64 ans apres vente | ~613 000 EUR | Rebond (+252 510 EUR) |
| 70 ans | ~534 000 EUR | Phase 2 croisiere |
| 75 ans | ~453 000 EUR | Activation RVD |
| 80 ans | ~358 000 EUR | Bilan dependance |
| 85 ans | ~245 000 EUR | Bilan succession |
| 90 ans | ~111 000 EUR | Derniere ligne droite |
| 92 ans | ~50 000 EUR | Objectif atteint |
""")

    titre("5. FISCALITE")
    st.markdown("""
- **IR = 0 EUR toute la vie** (AAH non imposable + LMNP amortissements = 0)
- **Case 2OP a cocher** chaque annee (option bareme > PFU)
- **Tax-Gain Harvesting** : cristalliser 4 600 EUR de PV AV/an a 0% IR
- **Apres 2034** : 2 contrats AV > 8 ans = 9 200 EUR/an de PV exonerees
- **PS 17,2%** sur PV AV : inevitable mais faible si sous abattement
- **CAF** : seules les PV comptent, pas le capital rembourse
- **Seuil CAF Isere** : ~12 396 EUR/an (a confirmer)
""")

    titre("6. LMNP - T3 MEYLAN")
    st.markdown("""
- Acquisition : 2010 | Valeur : 165 000 EUR | Terrain : 30 000 EUR
- Amortissement immeuble : 30 ans (4 500 EUR/an) | Reste ~13,8 ans
- Amortissement mobilier : 7 ans (epuise)
- Loyer brut : 680 EUR/mois | Charges : 2 000 EUR/an
- Resultat BIC : ~1 660 EUR (attention si positif = impact AAH)
- Revalorisation IRL : +2,6%/an (a mettre a jour chaque trimestre)
""")

    titre("7. SUCCESSION - ANNE-LYSE")
    st.markdown("""
- **AV hors succession** : 3 contrats x 152 500 EUR abattement = 457 500 EUR
- Si total AV < 457 500 EUR : **0 EUR de droits** sur les AV
- **Hors AV** : abattement frere/soeur 15 932 EUR, droits 35-45%
- **Donation NP T3 Meylan** : economie 30-50k EUR sur succession
- **Mandat de protection future** : Anne-Lyse gestionnaire si incapacite
- **Testament** : a rediger chez notaire
""")

    titre("8. MDPH / AAH / PCH")
    st.markdown("""
- **Taux actuel** : 75% | **Cible** : >= 80% (maintien AAH a vie)
- **AAH** : 1 033 EUR/mois | Non imposable
- **PCH si >=80%** : cumulable avec AAH | Jusqu'a 1 700 EUR/mois
- **Gain PCH 500 EUR/mois** : +282 000 EUR sur C92
- **Deadline** : dossier depose AVANT 60 ans (irreversible)
- **AAH sarrete a 64 ans** si taux 50-79%
- **AAH maintenue jusqu'a 67 ans** si taux >= 80%
""")

    titre("9. TECHNIQUES FINANCIERES UTILISEES")
    st.markdown("""
| Technique | Statut | Impact |
|---|---|---|
| ARVA (recalcul annuel) | Active | Pilote automatique pioche |
| Guyton-Klinger adapte | Active | Alerte si rendement < 2,8% |
| Tax-Gain Harvesting | Active | 0 EUR IR sur 4 600 EUR PV/an |
| RVD (Rente Viagere Differee) | A souscrire | +450 EUR/mois a 75 ans |
| Cascade decaissement | Active | CC > LA > LDDS > AV1 > AV2 > AV3 > LEP |
| Sequence of Returns Risk | Documente | Stress test Phase 2 |
| MaPrimeRenov | A demander | ~11 400 EUR aides |
| PCH | En cours MDPH | +282 000 EUR si obtenu |
""")

    titre("10. COMPTES A OUVRIR / CLOTURER")
    st.markdown("""
| Action | Quand | Montant | Statut |
|---|---|---|---|
| AV2 Linxea Spirit 2 | Cette semaine | 500 EUR | A faire |
| Cloturer AV Carrefour Horizons | < 6 mois | Reinjecter en AV2 | A faire |
| Kraken ou Bitvavo (crypto) | Quand tu veux | 0 EUR | A faire |
| RVD 50 000 EUR | Avant 64 ans | 50 000 EUR | A planifier |
| eToro | Deja ouvert | A integrer | En cours |
""")

    titre("11. DECISIONS ACTEES")
    st.markdown("""
1. Rail constant 2 760 EUR/mois de 50 a 92 ans - **ACTE**
2. Vente T3 Meylan a 64 ans - **ACTE**
3. Pas d'ASPA (recupérable sur succession) - **ACTE**
4. Option bareme (case 2OP) chaque annee - **ACTE**
5. LEP en dernier dans la cascade - **ACTE**
6. Buffer livrets max 16 560 EUR - **ACTE**
7. Cible 50 000 EUR a 92 ans - **ACTE**
8. Travaux parents 75 000 EUR - **ACTE**
9. Pas de bourse / profil fonds euros pur - **ACTE**
10. Pionex liste noire AMF - ne plus utiliser - **ACTE**
""")

    titre("12. ALERTES A SURVEILLER")
    st.markdown("""
- Rendement AV < 2,8% : contacter assureur
- SWR Phase 3 > 9% : souscrire RVD immediatement
- Buffer livrets > 16 560 EUR : reinjecter surplus en AV1
- CC < 1 000 EUR : renflouer depuis Livret A
- Resultat LMNP positif : impact potentiel AAH
- Seuil CAF depasse : BLOQUER le rachat AV
""")


'''

t = t.replace('def main():', annexe_page + 'def main():')

# Ajouter dans navigation
t = t.replace('"Crypto",', '"Crypto",\n            "Annexe - Reference",')

# Ajouter dans dispatch
t = t.replace('"Crypto":                  lambda: page_crypto(profil,cap),', '"Crypto":                  lambda: page_crypto(profil,cap),\n        "Annexe - Reference":      lambda: page_annexe(profil,cap),')

f = open(p, 'w', encoding='utf-8')
f.write(t)
f.close()
print('Lambdas:', t.count('lambda:'))
print('Annexe OK')
