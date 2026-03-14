p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

idx = t.find('def page_annexe(profil, cap):')
next_def = t.find(chr(10)+'def ', idx+10)

new_annexe = '''def page_annexe(profil, cap):
    st.subheader("ANNEXE - REFERENCE COMPLETE v3")
    st.caption("Document de reference valide par Claude + Perplexity - 12 mars 2026")

    st.subheader("1. COMMENT CA MARCHE ?")
    st.write("""Le cockpit gere ton patrimoine sur 42 ans (2026-2067). Il suit le capital, les revenus (AAH, loyers), les charges, et calcule chaque mois combien piocher. En Phase 0 (maintenant), il suit la construction du capital. En Phase 3 (janvier 2027+), il pilote la rente.""")

    st.subheader("2. D OU VIENT L ARGENT ?")
    st.write("**SCI du Pont de la Balme**")
    st.write("Prix vente signe : 433 000 EUR | Commission agent 6% : -26 000 EUR | Net vendeur : 407 000 EUR")
    st.write("PV brute : 246 717 EUR | IR 19% : 0 EUR (exonere > 22 ans) | PS 17,2% sur 72% : -30 553 EUR")
    st.write("Remboursement pret + IRA 3% : -72 100 EUR | Mainlevee : -800 EUR | Dissolution SCI : -3 209 EUR")
    st.write("Diagnostics + CSI : -910 EUR | Droit de partage 1,10% : -3 294 EUR")
    st.write("**Tresorerie nette SCI : 296 134 EUR | NET RAPHAEL : 296 100 EUR**")
    st.divider()
    st.write("**Succession Jean-Luc Boussy**")
    st.write("Actif brut : 591 000 EUR (maison 200k + appart 290k + liquidites 30k + voiture 2k + AV 69k)")
    st.write("Dettes : -29 000 EUR (VEFA 17k + cuisine 7k + frais deces 5k)")
    st.write("Actif net hors AV : 493 000 EUR | Part heritier (div 2) : 246 500 EUR")
    st.write("Abattement neveu : -7 967 EUR | Abattement handicap : -159 325 EUR | Base taxable : 79 208 EUR")
    st.write("Droits 55% : -43 564 EUR | Net apres droits : 202 936 EUR")
    st.write("AV Jean-Luc (art 990 I, 0 EUR impot) : +34 500 EUR")
    st.write("Frais (notaire + agences + diag + charges + debarras) : -20 020 EUR")
    st.write("**NET SUCCESSION RAPHAEL : 217 400 EUR**")
    st.write("Flux : AV +34 500 EUR en avril | Virement notaire +182 900 EUR en juillet")
    st.error("CONFIRMER abattement handicap co-heritiere Anne-Lyse aupres du notaire. Sans abattement : ses droits = 131 193 EUR.")
    st.divider()
    st.write("**Prix planchers vente (frais caches integres)**")
    st.write("Maison La Ravoire : **207 000 EUR minimum** (200k + 7k frais caches)")
    st.write("Appart Bassens : **290 000 EUR minimum** (marge neuf couvre les frais)")

    st.subheader("3. MEYLAN - LMNP")
    st.write("**Donation usufruit :** mere 81 ans, usufruit 20% = 33 200 EUR | Droits : 0 EUR | Frais notaire : 3 349 EUR")
    st.write("**Investissement :** donation 3 349 + travaux 33 000 + mobilier 15 000 = **51 349 EUR**")
    st.write("**Valeur apres travaux :** appart 199 000 + garage 20 000 = **219 000 EUR**")
    st.write("**Recettes :** loyer 800 CC x 9,7 mois + garage 110 x 9,7 = **8 827 EUR/an**")
    st.write("**Charges :** agence 794 + copro 280 + TF 950 + PNO 190 + entretien 1 990 + CFE 300 + comptable 400 + elec 80 = **4 984 EUR/an**")
    st.write("**Net en poche : 3 843 EUR/an = 320 EUR/mois**")
    st.write("**Amortissements :** batiment 5 644/an + travaux 3 300/an + mobilier 2 143/an = **11 087 EUR/an**")
    st.success("Base imposable = 0 EUR jusqu en 2051 (amortissements > resultat)")

    st.subheader("4. CAPITAL TOTAL")
    st.write("SCI nette : +296 100 | AV Jean-Luc : +34 500 | Succession nette : +182 900 = **+513 500 EUR**")
    st.write("Donation usufruit : -3 349 | Travaux : -33 000 | Mobilier : -15 000 | Charges : -1 075 = **-52 424 EUR**")
    st.write("**CAPITAL NET : 461 000 EUR | PATRIMOINE TOTAL : 680 000 EUR**")
    st.divider()
    st.write("**Repartition capital :**")
    st.write("CC : 500 | Livret A : 22 950 | LDDS : 12 000 | LEP : 10 000 | AV1 : 130 000 | AV2 : 130 000 | AV3 : 155 550")

    st.subheader("5. ALLOCATIONS")
    st.write("**AAH (51-64 ans) :** 1 033 EUR/mois si LMNP reel (RFR = 0). Protegee par amortissements.")
    st.write("**AAH reelle 2026 :** 625 EUR/mois (base revenus 2024 SCI active)")
    st.write("**Transition :** 2026-2027 : 625 EUR | 2028 : ~900 EUR | 2029+ : 1 033 EUR")
    st.write("**ASPA (64+ ans) :** prend 3% valeur venale de TOUS les biens. Amortissements LMNP = aucun effet.")
    st.write("**Seuil ASPA :** capital < 198 433 EUR (~80 ans)")
    st.write("**Si MDPH >= 80% :** AAH a vie, pas de bascule ASPA, plan renforce")

    st.subheader("6. VERSEMENT PARENTS")
    st.write("325 EUR/mois : nourriture 250 + electricite 50 + eau 5 + TEOM 20")
    st.write("Art. 205 Code civil - obligation alimentaire - non imposable pour les parents")

    st.subheader("7. ACTIONS PRIORITAIRES")
    st.error("1. Confirmer abattement handicap Anne-Lyse - notaire")
    st.error("2. Demander dates baux appart + garage aux parents")
    st.error("3. Appel notaire donation usufruit MEYLAN - 1er avril")
    st.warning("4. Envoi conge LRAR locataire appart - des signature donation")
    st.warning("5. Contacter artisans + devis - mai")
    st.warning("6. Declaration LMNP P0i + CFE + comptable - mai")
    st.warning("7. Selection agence bail mobilite - mai")

    st.subheader("8. COCKPIT - COMMENT IL GERE")
    st.write("**Phase 0 (mars 2026 - janvier 2027) :** suit la construction du capital, les flux, le planning")
    st.write("**Phase 3 (janvier 2027+) :** pilote la rente, calcule la pioche mensuelle, les alertes, la trajectoire")
    st.write("**Jalons :** chaque flux a une saisie, un ecart, une confirmation 1 mois et 6 mois")
    st.write("**AAH :** saisie annuelle, recalcul automatique du budget")
    st.write("**MDPH :** si >= 80%, bascule automatique AAH a vie")
    st.write("**Version : v4.3 - 12 mars 2026**")

'''

t = t[:idx] + new_annexe + t[next_def:]

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print('Annexe v3 installee')

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
