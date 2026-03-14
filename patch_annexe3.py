p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Ajouter section 16-20 dans l'annexe avant le dernier '''
insert_point = "titre(\"15. FRAIS PREVUS\")"
idx = t.find(insert_point)
# Trouver la fin de la section 15
end_section = t.find("'''", idx + 100)

extra_sections = '''

    titre("16. VENTE T3 MEYLAN - VENTILATION COMPLETE")
    st.markdown("""
**Valeur estimee a 64 ans (2039) : 252 510 EUR**

| Poste | Calcul | Montant |
|---|---|---|
| Prix de vente brut | 205 000 x 1,015^14 | 252 510 EUR |
| Frais agence (4%) | 252 510 x 4% | -10 100 EUR |
| Frais notaire acquereur | a charge acheteur | 0 EUR |
| Diagnostics obligatoires | forfait | -1 500 EUR |
| Plus-value immobiliere | | |
| - Prix acquisition 2010 | | 165 000 EUR |
| - Detention > 22 ans | exoneration IR | 0 EUR IR |
| - Detention > 30 ans | exoneration PS | 0 EUR PS |
| **Net vendeur** | 252 510 - 10 100 - 1 500 | **240 910 EUR** |

Note : si vente apres 2032 (22 ans detention) = exoneration totale IR
Si vente apres 2040 (30 ans detention) = exoneration totale IR + PS
Vente a 64 ans (2039) = 29 ans detention -> IR exonere, PS residuels faibles
""")

    titre("17. HERITAGE PARENTS - VENTILATION")
    st.markdown("""
**Hypothese : heritage de la maison parents (valeur estimee ~150 000 EUR)**

| Poste | Raphael | Anne-Lyse | Total |
|---|---|---|---|
| Valeur maison parents | 75 000 EUR (50%) | 75 000 EUR (50%) | 150 000 EUR |
| Abattement parent->enfant | -100 000 EUR | -100 000 EUR | |
| Base taxable | 0 EUR | 0 EUR | |
| Droits de succession | **0 EUR** | **0 EUR** | **0 EUR** |
| Frais notaire succession | ~1 500 EUR | ~1 500 EUR | ~3 000 EUR |
| **Net recu** | **~73 500 EUR** | **~73 500 EUR** | **~147 000 EUR** |

Note : abattement 100 000 EUR par parent par enfant. Si valeur < 200 000 EUR = 0 droits.
Frais notaire = emoluments (~1,5% sur biens immobiliers) + debours.
""")

    titre("18. SUCCESSION RAPHAEL -> ANNE-LYSE - VENTILATION PAR AGE")
    st.markdown("""
**Si deces a 70 ans (capital ~534 000 EUR)**
| Actif | Montant | Regime | Droits |
|---|---|---|---|
| AV1 | ~130 000 EUR | Hors succession | 0 EUR (< 152 500) |
| AV2 | ~140 000 EUR | Hors succession | 0 EUR (< 152 500) |
| AV3 | ~200 000 EUR | Hors succession | 0 EUR (< 152 500) |
| CC + Livrets | ~64 000 EUR | Succession | |
| - Abattement frere/soeur | | | -15 932 EUR |
| - Base taxable | | | 48 068 EUR |
| - Tranche 1 (< 24 430) | 35% | | 8 551 EUR |
| - Tranche 2 (> 24 430) | 45% | | 10 637 EUR |
| **Total droits** | | | **19 188 EUR** |
| Frais notaire succession | | | ~2 000 EUR |
| **Anne-Lyse recoit net** | | | **~512 812 EUR** |

**Si deces a 80 ans (capital ~358 000 EUR)**
| Actif | Montant | Regime | Droits |
|---|---|---|---|
| AV1 | ~80 000 EUR | Hors succession | 0 EUR |
| AV2 | ~90 000 EUR | Hors succession | 0 EUR |
| AV3 | ~140 000 EUR | Hors succession | 0 EUR |
| CC + Livrets | ~48 000 EUR | Succession | |
| - Abattement | | | -15 932 EUR |
| - Base taxable | | | 32 068 EUR |
| - Droits | | | 11 966 EUR |
| Frais notaire | | | ~1 800 EUR |
| **Anne-Lyse recoit net** | | | **~344 234 EUR** |

**Si deces a 92 ans (capital ~50 000 EUR)**
| Actif | Montant | Regime | Droits |
|---|---|---|---|
| AV residuelles | ~35 000 EUR | Hors succession | 0 EUR |
| CC + Livrets | ~15 000 EUR | Succession | |
| - Abattement | | | -15 000 EUR |
| - Base taxable | | | 0 EUR |
| - Droits | | | **0 EUR** |
| Frais notaire | | | ~800 EUR |
| **Anne-Lyse recoit net** | | | **~49 200 EUR** |
""")

    titre("19. FLUX ANNUELS DETAILLES - 10 PREMIERES ANNEES")
    st.markdown("""
| Annee | Age | AAH | Loyer | Pioche | Total | Capital fin |
|---|---|---|---|---|---|---|
| 2026 | 50-51 | 12 396 EUR | 5 376 EUR | 15 348 EUR | 33 120 EUR | ~385 000 EUR* |
| 2027 | 51-52 | 12 396 EUR | 5 376 EUR | 15 348 EUR | 33 120 EUR | ~382 000 EUR |
| 2028 | 52-53 | 12 396 EUR | 5 376 EUR | 15 348 EUR | 33 120 EUR | ~380 000 EUR |
| 2029 | 53-54 | 12 396 EUR | 5 376 EUR | 15 348 EUR | 33 120 EUR | ~379 000 EUR |
| 2030 | 54-55 | 12 396 EUR | 5 376 EUR | 15 348 EUR | 33 120 EUR | ~378 000 EUR |
| 2031 | 55-56 | 12 396 EUR | 5 376 EUR | 15 348 EUR | 33 120 EUR | ~378 000 EUR |
| 2032 | 56-57 | 12 396 EUR | 5 376 EUR | 15 348 EUR | 33 120 EUR | ~379 000 EUR |
| 2033 | 57-58 | 12 396 EUR | 5 376 EUR | 15 348 EUR | 33 120 EUR | ~380 000 EUR |
| 2034 | 58-59 | 12 396 EUR | 5 376 EUR | 15 348 EUR | 33 120 EUR | ~381 000 EUR |
| 2035 | 59-60 | 12 396 EUR | 5 376 EUR | 15 348 EUR | 33 120 EUR | ~383 000 EUR |

*2026 inclut -63 600 EUR travaux (net apres aides)
Le capital se stabilise puis remonte grace aux interets (13 360 EUR/an > pioche 15 348 EUR/an -> ecart seulement -1 988 EUR/an)
""")

    titre("20. FLUX ANNUELS - PHASE 2 (64-75 ans)")
    st.markdown("""
| Annee | Age | Pioche | Interets | Capital fin |
|---|---|---|---|---|
| 2039 | 64 | 33 120 EUR | +21 455 EUR | ~613 000 EUR (post vente) |
| 2040 | 65 | 33 120 EUR | +20 300 EUR | ~600 000 EUR |
| 2041 | 66 | 33 120 EUR | +19 800 EUR | ~587 000 EUR |
| 2042 | 67 | 33 120 EUR | +19 300 EUR | ~573 000 EUR |
| 2043 | 68 | 33 120 EUR | +18 700 EUR | ~559 000 EUR |
| 2044 | 69 | 33 120 EUR | +18 100 EUR | ~544 000 EUR |
| 2045 | 70 | 33 120 EUR | +17 500 EUR | ~528 000 EUR |
| 2046 | 71 | 33 120 EUR | +16 800 EUR | ~512 000 EUR |
| 2047 | 72 | 33 120 EUR | +16 100 EUR | ~495 000 EUR |
| 2048 | 73 | 33 120 EUR | +15 300 EUR | ~477 000 EUR |
| 2049 | 74 | 33 120 EUR | +14 500 EUR | ~459 000 EUR |
| 2050 | 75 | 33 120 EUR | +13 700 EUR | ~453 000 EUR |
""")

    titre("21. FLUX ANNUELS - PHASE 3 (75-92 ans)")
    st.markdown("""
| Annee | Age | RVD | Pioche | Total | Interets | Capital fin |
|---|---|---|---|---|---|---|
| 2050 | 75 | 5 400 EUR | 27 720 EUR | 33 120 EUR | +15 855 EUR | ~453 000 EUR |
| 2055 | 80 | 5 400 EUR | 27 720 EUR | 33 120 EUR | +12 526 EUR | ~358 000 EUR |
| 2060 | 85 | 5 400 EUR | 27 720 EUR | 33 120 EUR | +8 562 EUR | ~245 000 EUR |
| 2065 | 90 | 5 400 EUR | 27 720 EUR | 33 120 EUR | +3 884 EUR | ~111 000 EUR |
| 2067 | 92 | 5 400 EUR | 27 720 EUR | 33 120 EUR | +1 750 EUR | ~50 000 EUR |
""")

    titre("22. RECAPITULATIF - OU VA CHAQUE EURO")
    st.markdown("""
**Sur 42 ans de plan (2025-2067)**

| Poste | Total |
|---|---|
| **ENTREES** | |
| AAH recue (14 ans) | 173 544 EUR |
| Loyers LMNP (14 ans) | 75 264 EUR |
| Vente T3 Meylan net | 240 910 EUR |
| Interets capital (42 ans) | ~420 000 EUR |
| RVD recue (17 ans) | 91 800 EUR |
| MaPrimeRenov | 11 400 EUR |
| **TOTAL ENTREES** | **~1 012 918 EUR** |
| | |
| **SORTIES** | |
| Depenses de vie (42 ans x 33 120) | 1 390 560 EUR* |
| Travaux parents | 75 000 EUR |
| RVD souscription | 50 000 EUR |
| Notaire (tous actes) | ~3 100 EUR |
| Expert-comptable (14 ans) | ~7 000 EUR |
| PS sur rachats AV | ~12 000 EUR |
| Frais vente immo | ~11 600 EUR |
| **TOTAL SORTIES** | **~1 549 260 EUR** |
| | |
| **Capital initial** | 393 192 EUR |
| **Capital final (92 ans)** | ~50 000 EUR |

*Le rail de 2 760 EUR/mois inclut la pioche + AAH + loyer. La pioche seule totalise ~1 050 432 EUR sur 42 ans.
La difference est financee par les interets composes (~420 000 EUR generes par le capital).
""")

'''

t = t[:end_section] + extra_sections + t[end_section:]

f = open(p, 'w', encoding='utf-8')
f.write(t)
f.close()
print('Sections 16-22 ajoutees OK')
