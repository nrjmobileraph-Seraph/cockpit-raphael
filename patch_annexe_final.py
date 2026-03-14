p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Trouver et remplacer la section succession Jean-Luc
old_succ = 'titre("SUCCESSION JEAN-LUC BOUSSY")'
idx = t.find(old_succ)
if idx > 0:
    end = t.find("titre(", idx + 100)
    if end > idx:
        new_section = '''titre("VENTE SCI DU PONT DE LA BALME")
    st.markdown('<div style="background:#140810;border-radius:10px;padding:20px;margin-bottom:16px;color:#F0E6D8;font-size:14px;line-height:1.8;"><b style="color:#FFD060;">Prix de vente signe</b> : 433 000 EUR<br>Commission agence (6%) : -26 000 EUR<br><b>Net vendeur : 407 000 EUR</b><br><br>Prix acquisition 2003 : 129 782 EUR<br>+ 7,5% frais : +9 734 EUR<br>+ 15% travaux : +19 467 EUR<br>= Prix corrige : 158 983 EUR<br><br>Plus-value brute : 433 000 - 158 983 = <b>274 017 EUR</b><br><br><b style="color:#4DFF99;">IR 19% = 0 EUR</b> (exonere apres 22 ans de detention)<br>Abattement PS : 28% -> 72% soumis aux PS<br>PS 17,2% sur 72% de 274 017 = <b style="color:#FF7777;">33 944 EUR</b></div>', unsafe_allow_html=True)
    st.markdown('<div style="background:#140810;border-radius:10px;padding:20px;margin-bottom:16px;color:#F0E6D8;font-size:14px;line-height:1.8;"><b style="color:#FFD060;">Frais et sorties</b><br>Remboursement pret : -70 000 EUR<br>Penalite remboursement anticipe (3%) : -2 100 EUR<br>Mainlevee hypotheque : -800 EUR<br>Dissolution SCI (greffe+notaire+annonces) : -3 209 EUR<br>Diagnostics + CSI : -910 EUR<br>Droit de partage (1,10% du boni) : -3 245 EUR<br>Prelevements sociaux : -33 944 EUR<br><br><b>Tresorerie nette SCI : 291 792 EUR</b><br><br>Raphael 85% = 247 024 EUR<br>+ Don du pere 15% = 43 769 EUR (exonere, abattement 100k parent-enfant, renouvele 2024)<br><br><b style="color:#4DFF99;">NET FINAL SCI RAPHAEL : 291 800 EUR</b></div>', unsafe_allow_html=True)

    titre("SUCCESSION JEAN-LUC BOUSSY")
    st.markdown('<div style="background:#140810;border-radius:10px;padding:20px;margin-bottom:16px;color:#F0E6D8;font-size:14px;line-height:1.8;"><b style="color:#FFD060;">Patrimoine du defunt</b><br>Maison : 200 000 EUR<br>Appartement neuf (solde restant 17 000 EUR) : 290 000 EUR<br>Liquidites bancaires : 30 000 EUR<br>Voiture : 2 000 EUR<br>Assurance-vie (primes avant 70 ans) : 69 000 EUR<br><b>Total brut : 591 000 EUR</b><br><br><b style="color:#FFD060;">Dettes deduites</b><br>Solde appartement neuf (VEFA) : -17 000 EUR<br>Cuisine en cours : -7 000 EUR<br>Frais fonctionnement deces : -5 000 EUR<br><b>Actif net global : 562 000 EUR</b><br><b>Actif net successoral (hors AV) : 493 000 EUR</b><br><b>Part par heritier : 246 500 EUR</b></div>', unsafe_allow_html=True)
    st.markdown('<div style="background:#140810;border-radius:10px;padding:20px;margin-bottom:16px;color:#F0E6D8;font-size:14px;line-height:1.8;"><b style="color:#FFD060;">Impots par heritier</b><br>Part brute : 246 500 EUR<br>- Abattement neveu (art. 779 V CGI) : -7 967 EUR<br>- Abattement handicap (art. 779 II CGI) : -159 325 EUR<br>= Part taxable : 79 208 EUR<br>x Taux 55% (oncle-neveu) : <b style="color:#FF7777;">-43 564 EUR</b><br>= Net apres impots : 202 936 EUR<br><br>+ Assurance-vie (34 500 EUR, art. 990 I, 0 EUR impot) : +34 500 EUR<br><b>Sous-total : 237 436 EUR</b></div>', unsafe_allow_html=True)
    st.markdown('<div style="background:#140810;border-radius:10px;padding:20px;margin-bottom:16px;color:#F0E6D8;font-size:14px;line-height:1.8;"><b style="color:#FFD060;">Frais par heritier</b><br>Notaire (~2% actif successoral) : -4 930 EUR<br>Agence immo (maison 4% + appart 5%) : -11 250 EUR<br>Diagnostics : -400 EUR<br>Charges courantes 6 mois : -1 440 EUR<br>Debarras maison : -2 000 EUR<br><b>Total frais : -20 020 EUR</b><br><br>237 436 - 20 020 = <b style="color:#4DFF99;">NET FINAL SUCCESSION RAPHAEL : 217 400 EUR</b></div>', unsafe_allow_html=True)

    titre("CAPITAL TOTAL RAPHAEL")
    st.markdown('<div style="background:#140810;border-radius:10px;padding:20px;margin-bottom:16px;color:#F0E6D8;font-size:14px;line-height:1.8;"><b style="color:#FFD060;">Entrees</b><br>SCI net : 291 800 EUR<br>Succession net : 217 400 EUR<br><b>Total entrees : 509 200 EUR</b><br><br><b style="color:#FFD060;">Depenses</b><br>Travaux renovation T3 Meylan : -33 000 EUR<br>Donation usufruit (frais notaire) : -1 200 EUR<br><b>Total depenses : -34 200 EUR</b><br><br><b style="color:#4DFF99;font-size:18px;">CAPITAL NET DISPONIBLE : 475 000 EUR</b><br><br>+ Appartement Meylan renove : 183 000 EUR<br>+ Garage Meylan : 22 000 EUR<br><b style="color:#FFD060;font-size:16px;">PATRIMOINE TOTAL : 680 000 EUR</b></div>', unsafe_allow_html=True)

    '''
        t = t[:idx] + new_section + t[end:]

f = open(p, 'w', encoding='utf-8')
f.write(t)
f.close()
print('Annexe SCI + Succession mise a jour OK')
