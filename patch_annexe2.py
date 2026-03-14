p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Trouver et remplacer la page annexe existante
old_start = "def page_annexe(profil, cap):"
old_end = "def main():"

idx1 = t.find(old_start)
idx2 = t.find(old_end)

if idx1 > 0 and idx2 > idx1:
    before = t[:idx1]
    after = t[idx2:]

    new_annexe = '''def page_annexe(profil, cap):
    titre("ANNEXE COMPLETE - REFERENCE DU PLAN PATRIMONIAL")
    st.markdown('<div style="color:#D0C0A8;font-size:13px;margin-bottom:20px;">Document de reference exhaustif. Chaque chiffre, chaque date, chaque decision. Mis a jour : mars 2026.</div>', unsafe_allow_html=True)

    titre("1. IDENTITE ET SITUATION")
    st.markdown("""
| | Detail |
|---|---|
| **Nom** | Raphael Boussy |
| **Date de naissance** | 26 aout 1975 |
| **Age actuel** | 50,5 ans |
| **Situation** | Celibataire, sans enfant |
| **Handicap** | MDPH taux 75% (objectif >= 80%) |
| **Heritiere** | Anne-Lyse Boussy (soeur) |
| **Domicile** | Meylan, Isere (38) |
| **Banque** | BoursoBank |
| **Horizon du plan** | 50 ans -> 92 ans (42 ans, 504 mois) |
""")

    titre("2. CAPITAL INITIAL DETAILLE - 393 192 EUR")
    st.markdown("""
| Poche | Montant | Taux net | Interet annuel | Ordre pioche |
|---|---|---|---|---|
| Compte courant | 500 EUR | 0,00% | 0 EUR | 1er |
| Livret A | 22 950 EUR | 2,40% | 551 EUR | 2e |
| LDDS | 12 000 EUR | 2,40% | 288 EUR | 3e |
| AV1 (ouverte 2016) | 109 500 EUR | 3,50% | 3 833 EUR | 4e |
| AV2 (ouverte 2026) | 109 500 EUR | 3,50% | 3 833 EUR | 5e |
| AV3 (ouverte 2010) | 128 742 EUR | 3,50% | 4 506 EUR | 6e |
| LEP | 10 000 EUR | 3,50% | 350 EUR | 7e (dernier) |
| **TOTAL** | **393 192 EUR** | **3,398%** | **13 360 EUR/an** | |

**Rendement pondere reel** : 3,398% (cible >= 3,365%)

**Buffer livrets** : 22 950 + 12 000 = 34 950 EUR (cible max 16 560 EUR)
Surplus a reinjecter : 34 950 - 16 560 = **18 390 EUR -> AV1**
""")

    titre("3. ASSURANCES-VIE - DETAIL PAR CONTRAT")
    st.markdown("""
**AV1 - Abattement disponible**
| | |
|---|---|
| Ouverture | 01/01/2016 (10,2 ans) |
| Valeur rachat | 109 500 EUR |
| Versements cumules | 95 000 EUR |
| PV latentes | 14 500 EUR (13,2%) |
| Rendement | 3,50%/an |
| Abattement 8 ans | OUI - 4 600 EUR |
| Rachat max sans IR | 34 738 EUR |

**AV2 - Ouvert 2026**
| | |
|---|---|
| Ouverture | 01/01/2026 (0,2 ans) |
| Valeur rachat | 109 500 EUR |
| Versements cumules | 500 EUR |
| PV latentes | 109 000 EUR (99,5%) |
| Rendement | 3,50%/an |
| Abattement 8 ans | NON - disponible 01/01/2034 |
| Rachat max sans IR | Attendre 2034 |

**AV3 - Reserve strategique**
| | |
|---|---|
| Ouverture | 01/01/2010 (16,2 ans) |
| Valeur rachat | 128 742 EUR |
| Versements cumules | 110 000 EUR |
| PV latentes | 18 742 EUR (14,6%) |
| Rendement | 3,50%/an |
| Abattement 8 ans | OUI - 4 600 EUR |
| Rachat max sans IR | 31 598 EUR |

**TOTAUX 3 CONTRATS**
| | |
|---|---|
| Total AV | 347 742 EUR (88,4% du capital) |
| PV latentes totales | 142 242 EUR |
| Rachat max sans IR | 66 336 EUR/an |
| Abattement succession | 3 x 152 500 = 457 500 EUR |
""")

    titre("4. REVENUS MENSUELS PAR PHASE")
    st.markdown("""
**PHASE 1 : 50 -> 64 ans (168 mois)**
| Source | Montant | Note |
|---|---|---|
| AAH | +1 033 EUR/mois | Non imposable |
| Loyer LMNP net | +448 EUR/mois | T3 Meylan |
| Pioche Livret A | +1 279 EUR/mois | Puis AV quand livrets epuises |
| **TOTAL** | **2 760 EUR/mois** | = **33 120 EUR/an** |

Pioche totale Phase 1 : 1 279 x 168 = **214 872 EUR** en capital

**TRANSITION 64 ANS (aout 2039)**
| Evenement | Impact |
|---|---|
| AAH sarrete | -1 033 EUR/mois |
| Loyer sarrete (vente T3) | -448 EUR/mois |
| Vente T3 Meylan + garage | +252 510 EUR en capital |
| Capital avant vente | ~361 000 EUR |
| Capital apres vente | ~613 000 EUR (rebond) |

**PHASE 2 : 64 -> 75 ans (132 mois)**
| Source | Montant | Note |
|---|---|---|
| Pioche capital seule | +2 760 EUR/mois | 100% depuis AV |
| **TOTAL** | **2 760 EUR/mois** | = **33 120 EUR/an** |

Pioche totale Phase 2 : 2 760 x 132 = **364 320 EUR** en capital

**PHASE 3 : 75 -> 92 ans (204 mois)**
| Source | Montant | Note |
|---|---|---|
| RVD (rente viagere) | +450 EUR/mois | Garantie a vie |
| Pioche capital | +2 310 EUR/mois | Reduite grace a RVD |
| **TOTAL** | **2 760 EUR/mois** | = **33 120 EUR/an** |

Pioche totale Phase 3 : 2 310 x 204 = **471 240 EUR** en capital
""")

    titre("5. TRAJECTOIRE DU CAPITAL - DETAIL PAR AGE")
    st.markdown("""
| Age | Annee | Capital | Evenement |
|---|---|---|---|
| 50 | 2025 | 393 192 EUR | Depart du plan |
| 51 | 2026 | ~385 000 EUR | Travaux parents -75k + MaPrime +11,4k |
| 52 | 2027 | ~382 000 EUR | Croisiere |
| 55 | 2030 | ~381 000 EUR | Bilan mi-parcours |
| 58 | 2033 | ~375 000 EUR | Abattement AV2 disponible |
| 60 | 2035 | ~372 000 EUR | DEADLINE MDPH |
| 62 | 2037 | ~367 000 EUR | Estimation vente T3 |
| 64 avant | 2039 | ~361 000 EUR | Fin Phase 1 |
| 64 apres | 2039 | ~613 000 EUR | Vente T3 (+252 510 EUR) |
| 65 | 2040 | ~593 000 EUR | Phase 2 croisiere |
| 70 | 2045 | ~534 000 EUR | |
| 73 | 2048 | ~490 000 EUR | Dernier moment RVD |
| 75 | 2050 | ~453 000 EUR | Activation RVD +450 EUR/mois |
| 80 | 2055 | ~358 000 EUR | Bilan dependance |
| 85 | 2060 | ~245 000 EUR | Bilan succession |
| 90 | 2065 | ~111 000 EUR | |
| 92 | 2067 | ~50 000 EUR | OBJECTIF ATTEINT |
""")

    titre("6. IMMOBILIER - T3 MEYLAN + GARAGE")
    st.markdown("""
| | Detail |
|---|---|
| Adresse | Meylan (38) |
| Acquisition | 2010 |
| Valeur acquisition | 165 000 EUR |
| Part terrain | 30 000 EUR (non amortissable) |
| Valeur mobilier | 8 000 EUR |
| Loyer brut | 680 EUR/mois (8 160 EUR/an) |
| Loyer net (apres charges) | 448 EUR/mois |
| Charges annuelles | 2 000 EUR |
| Rendement brut | 2,62% (sur valeur totale) |
| Valeur estimee 2026 | ~205 000 EUR |
| Valeur estimee 2039 (64 ans) | ~252 510 EUR (+1,5%/an) |
| Revalorisation IRL | +2,6%/an (dernier trimestre) |
| **Vente prevue** | **64 ans (2039)** |

**LMNP - Amortissements**
| Type | Annuel | Reste |
|---|---|---|
| Immeuble (30 ans) | 4 500 EUR/an | ~13,8 ans (fin ~2038) |
| Mobilier (7 ans) | 1 143 EUR/an | Epuise |
| **Total amort** | **4 500 EUR/an** | |

**Resultat BIC** : 8 160 - 2 000 - 4 500 = **1 660 EUR** (attention si positif)
""")

    titre("7. TRAVAUX PARENTS - 75 000 EUR")
    st.markdown("""
| Poste | Montant |
|---|---|
| Extension maison | ~60 000 EUR |
| Panneaux solaires | ~15 000 EUR |
| **Total brut** | **75 000 EUR** |
| MaPrimeRenov (40% panneaux) | -6 000 EUR |
| TVA reduite 5,5% isolation | -5 400 EUR |
| **Aides estimees** | **~11 400 EUR** |
| **Cout reel net** | **~63 600 EUR** |

Financement : pris sur le capital initial
Impact sur capital : 393 192 - 63 600 = **329 592 EUR** (temporaire, avant reinvestissement)
""")

    titre("8. FISCALITE - DETAIL COMPLET")
    st.markdown("""
**Impot sur le revenu : 0 EUR/an A VIE**
- AAH non imposable
- LMNP : resultat BIC = ~0 EUR (amortissements)
- PV AV sous abattement 4 600 EUR : pas d'IR
- TMI = 0%

**Prelevements sociaux : 17,2% sur PV AV**
- Sur 4 600 EUR de PV cristallisees/an = ~791 EUR/an max
- Inevitable mais faible

**Case 2OP** : TOUJOURS cocher (option bareme > PFU quand TMI = 0%)

**Tax-Gain Harvesting annuel**
| Annee | Contrat | PV cristallisees | IR | PS 17,2% | Total |
|---|---|---|---|---|---|
| 2027 | AV1 | 4 600 EUR | 0 EUR | 0 EUR (sous abattement) | 0 EUR |
| 2028 | AV1 | 4 600 EUR | 0 EUR | 0 EUR | 0 EUR |
| ... | AV1 | 4 600 EUR | 0 EUR | 0 EUR | 0 EUR |
| 2034+ | AV1+AV2 | 9 200 EUR | 0 EUR | 0 EUR | 0 EUR |

**CAF et AAH**
- Seuil ressources CAF Isere : ~12 396 EUR/an (A CONFIRMER)
- Revenus declares : AAH 12 396 EUR/an + PV rachats
- Marge : tres serree -> verifier AVANT chaque rachat
- Livrets exoneres de la base CAF
- Capital AV non declare tant que pas rachete
""")

    titre("9. SUCCESSION ANNE-LYSE - SIMULATION")
    st.markdown("""
**Si deces a 75 ans (capital ~453 000 EUR)**
| Actif | Montant | Regime |
|---|---|---|
| AV1 | ~120 000 EUR | Hors succession (abattement 152 500 EUR) |
| AV2 | ~130 000 EUR | Hors succession (abattement 152 500 EUR) |
| AV3 | ~150 000 EUR | Hors succession (abattement 152 500 EUR) |
| Total AV | ~400 000 EUR | **0 EUR de droits** (< 457 500 EUR) |
| CC + Livrets + LEP | ~53 000 EUR | Succession classique |
| Abattement frere/soeur | -15 932 EUR | |
| Base taxable | ~37 000 EUR | |
| Droits 35% (tranche 1) | ~8 551 EUR | Tranche < 24 430 EUR |
| Droits 45% (tranche 2) | ~5 657 EUR | Tranche > 24 430 EUR |
| **Total droits** | **~14 208 EUR** | |

**Donation nue-propriete T3 Meylan**
| | |
|---|---|
| Valeur pleine propriete | 205 000 EUR |
| NP a 50 ans (50%) | 102 500 EUR |
| Abattement parent->enfant | -100 000 EUR |
| Base taxable | 2 500 EUR |
| Droits | ~125 EUR |
| Frais notaire | ~1 200 EUR |
| **Economie succession** | **30 000 - 50 000 EUR** |
""")

    titre("10. MDPH / AAH / PCH - SCENARIOS")
    st.markdown("""
| Scenario | AAH fin | PCH | C92 | Gain vs base |
|---|---|---|---|---|
| Base : MDPH 75% | 64 ans | 0 EUR | 174 021 EUR | - |
| MDPH >= 80% | 67 ans | 0 EUR | +95 000 EUR | +95k |
| MDPH >= 80% + PCH 300 EUR | 67 ans | 300 EUR/mois | +225 000 EUR | +225k |
| MDPH >= 80% + PCH 500 EUR | 67 ans | 500 EUR/mois | +282 000 EUR | +282k |
| MDPH >= 80% + PCH 800 EUR | 67 ans | 800 EUR/mois | +380 000 EUR | +380k |

**Le MDPH est le levier n1 du plan** : +282 000 EUR pour un dossier medical.
""")

    titre("11. RVD - RENTE VIAGERE DIFFEREE")
    st.markdown("""
| | Detail |
|---|---|
| Montant investi | 50 000 EUR |
| Age souscription | Avant 64 ans |
| Age activation | 75 ans |
| Rente garantie | ~450 EUR/mois a vie |
| Taux implicite | ~5,5%/an |
| Impact Phase 3 | Pioche reduite de 2 760 a 2 310 EUR/mois |
| Assureurs possibles | Spirica, Suravenir, AG2R |
| **Statut** | **A souscrire** |
""")

    titre("12. STRESS TESTS")
    st.markdown("""
| Scenario | Impact C92 | Verdict |
|---|---|---|
| Rendement 2,5%/an | -57 000 EUR (ruine) | CRITIQUE - minimum 3,0% |
| Rendement 2,8%/an | ~0 EUR | Limite |
| Rendement 3,0%/an | +40 000 EUR | Acceptable |
| Rendement 3,5%/an (base) | +174 000 EUR | Confortable |
| EHPAD 2 500 EUR/mois a 80 ans | -180 000 EUR | Tenable avec APA |
| EHPAD net APA (GIR2) = 1 300 EUR | -95 000 EUR | OK |
| Seq. Returns 2% sur 3 ans a 64 | -63 000 EUR | Risque Phase 2 |
| Buffer > 16 560 EUR | -15 000 EUR | Buffer OBLIGATOIRE |
| RVD pas souscrite | -100 000 EUR | RVD INDISPENSABLE |
""")

    titre("13. TOUTES LES DECISIONS ACTEES")
    st.markdown("""
| # | Decision | Date | Valide par |
|---|---|---|---|
| 1 | Rail constant 2 760 EUR/mois | 09/03/2026 | Claude + Perplexity + Gemini + DeepSeek |
| 2 | Vente T3 a 64 ans | 09/03/2026 | 4 IA |
| 3 | Pas d'ASPA | 09/03/2026 | 4 IA |
| 4 | Option bareme (2OP) chaque annee | 09/03/2026 | 4 IA |
| 5 | LEP en dernier | 09/03/2026 | Perplexity |
| 6 | Buffer max 16 560 EUR | 09/03/2026 | Perplexity |
| 7 | Cible 50 000 EUR a 92 ans | 09/03/2026 | 4 IA |
| 8 | Travaux 75 000 EUR | 09/03/2026 | Raphael |
| 9 | Profil fonds euros pur (pas d'actions) | 09/03/2026 | Raphael |
| 10 | Pionex liste noire AMF | 10/03/2026 | Claude (AMF) |
| 11 | Age transition 64 ans | 09/03/2026 | Perplexity (reforme 2023) |
| 12 | Capital 393 192 EUR (post travaux) | 09/03/2026 | 4 IA |
""")

    titre("14. COMPTES ET PLATEFORMES")
    st.markdown("""
| Compte | Statut | Action |
|---|---|---|
| BoursoBank (CC) | Actif | Connexion Tink en cours |
| Livret A | Actif | Plafond atteint |
| LDDS | Actif | |
| LEP | Actif | |
| AV1 (assureur ?) | Actif | A renseigner |
| AV2 Linxea Spirit 2 | A OUVRIR | 500 EUR cette semaine |
| AV3 (assureur ?) | Actif | A renseigner |
| AV Carrefour Horizons | A CLOTURER | 1,70% net - obsolete |
| eToro | Actif | Trading - a integrer |
| Kraken/Bitvavo | A OUVRIR | Crypto AMF agreee |
| Pionex | INTERDIT | Liste noire AMF |
""")

    titre("15. FRAIS PREVUS")
    st.markdown("""
| Frais | Montant | Quand |
|---|---|---|
| Ouverture AV2 | 500 EUR (versement initial) | Mars 2026 |
| Notaire (testament+mandat+donation) | ~1 300 EUR | Avant juin 2026 |
| Travaux parents | 75 000 EUR brut / 63 600 EUR net | 2026 |
| Expert-comptable LMNP | ~500 EUR/an | Chaque annee |
| PS sur rachats AV | ~791 EUR/an max | Chaque janvier |
| Frais gestion AV | ~0,5-0,75%/an (inclus dans rendement) | Continu |
| RVD souscription | 50 000 EUR | Avant 64 ans |
| Frais vente T3 notaire | ~8 000 EUR (3%) | 2039 |
| Droits succession estimés | ~14 208 EUR | Au deces |
""")


'''

    t = before + new_annexe + after

f = open(p, 'w', encoding='utf-8')
f.write(t)
f.close()
print('Annexe complete OK')
