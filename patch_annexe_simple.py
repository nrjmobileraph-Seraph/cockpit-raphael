p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Trouver le debut de l'annexe
old_start = 'def page_annexe(profil, cap):'
idx = t.find(old_start)
idx_end = t.find('def main():')

if idx > 0 and idx_end > idx:
    before = t[:idx]
    after = t[idx_end:]
    
    simple_annexe = '''def page_annexe(profil, cap):
    titre("ANNEXE - TOUT COMPRENDRE EN 5 MINUTES")

    titre("Comment ca marche ?")
    st.markdown('<div style="background:#140810;border-radius:10px;padding:20px;margin-bottom:16px;color:#F0E6D8;font-size:14px;line-height:1.8;">Tu as <b style="color:#4DFF99;">393 192 EUR</b> de cote. Chaque mois tu recois <b style="color:#4DFF99;">2 760 EUR</b> pour vivre. Ca vient de 3 sources : ton AAH (1 033 EUR), ton loyer du T3 Meylan (448 EUR), et le reste tu le pioches dans ton epargne (1 279 EUR). Ce rythme est calcule pour durer jusqu\\'a tes 92 ans avec 50 000 EUR de matelas a la fin.</div>', unsafe_allow_html=True)

    titre("D ou vient l argent ?")
    st.markdown('<div style="background:#140810;border-radius:10px;padding:20px;margin-bottom:16px;color:#F0E6D8;font-size:14px;line-height:1.8;"><b style="color:#FFD060;">Aujourd hui (50-64 ans)</b><br>AAH : 1 033 EUR/mois (le handicap)<br>Loyer : 448 EUR/mois (ton locataire a Meylan)<br>Pioche : 1 279 EUR/mois (depuis le Livret A puis les AV)<br>Total : 2 760 EUR/mois<br><br><b style="color:#FFD060;">A 64 ans il se passe un truc important</b><br>L AAH s arrete. Le loyer aussi parce que tu vends l appart. Mais la vente rapporte 252 510 EUR qui reviennent dans ton capital. Du coup ton capital remonte d un coup a 613 000 EUR et c est lui qui finance tout la suite.<br><br><b style="color:#FFD060;">A 75 ans</b><br>Une rente viagere (RVD) demarre : 450 EUR/mois garanti a vie. Ca reduit ce que tu pioches dans le capital. Le plan tient jusqu a 92 ans.</div>', unsafe_allow_html=True)

    titre("Ou est range l argent ?")
    st.markdown('<div style="background:#140810;border-radius:10px;padding:20px;margin-bottom:16px;color:#F0E6D8;font-size:14px;line-height:1.8;">Ton argent est reparti dans 7 poches. On pioche dans cet ordre :<br><br><b>1.</b> Compte courant (500 EUR) - pour payer au quotidien<br><b>2.</b> Livret A (22 950 EUR) - la reserve qu on tape en premier<br><b>3.</b> LDDS (12 000 EUR) - reserve complementaire<br><b>4.</b> AV1 (109 500 EUR) - assurance-vie, abattement fiscal disponible<br><b>5.</b> AV2 (109 500 EUR) - assurance-vie, abattement en 2034<br><b>6.</b> AV3 (128 742 EUR) - reserve strategique<br><b>7.</b> LEP (10 000 EUR) - on y touche en DERNIER car meilleur taux<br><br>Le capital travaille a 3,5% par an. Ca genere environ 13 000 EUR d interets par an qui compensent en grande partie ce qu on pioche.</div>', unsafe_allow_html=True)

    titre("Les grosses depenses prevues")
    st.markdown('<div style="background:#140810;border-radius:10px;padding:20px;margin-bottom:16px;color:#F0E6D8;font-size:14px;line-height:1.8;"><b style="color:#FF7777;">Travaux parents : 75 000 EUR</b><br>Extension maison + panneaux solaires. Aides MaPrimeRenov attendues : 11 400 EUR. Cout reel : 63 600 EUR.<br><br><b style="color:#FF7777;">Notaire : 1 300 EUR</b><br>Testament + mandat de protection + donation nue-propriete. 3 actes en 1 RDV.<br><br><b style="color:#FF7777;">RVD : 50 000 EUR</b><br>Rente viagere differee. Tu paies maintenant, tu recois 450 EUR/mois a partir de 75 ans. A vie.<br><br><b style="color:#FF7777;">Expert-comptable : 500 EUR/an</b><br>Pour la declaration LMNP tant que tu as l appart.</div>', unsafe_allow_html=True)

    titre("Les impots ?")
    st.markdown('<div style="background:#140810;border-radius:10px;padding:20px;margin-bottom:16px;color:#F0E6D8;font-size:14px;line-height:1.8;"><b style="color:#4DFF99;">Tu paies 0 EUR d impots.</b> Toute ta vie.<br><br>L AAH n est pas imposable. Le LMNP est couvert par les amortissements. Les rachats sur les assurances-vie restent sous l abattement de 4 600 EUR par an.<br><br>Chaque 1er janvier tu cristallises 4 600 EUR de plus-values sur tes AV. C est gratuit (0 EUR d impot). Ca s appelle le Tax-Gain Harvesting.<br><br>La seule chose qu on paie : les prelevements sociaux (17,2%) sur les plus-values AV si elles depassent l abattement. En pratique c est moins de 800 EUR par an.</div>', unsafe_allow_html=True)

    titre("Anne-Lyse - qu est-ce qu elle recoit ?")
    st.markdown('<div style="background:#140810;border-radius:10px;padding:20px;margin-bottom:16px;color:#F0E6D8;font-size:14px;line-height:1.8;">Tes 3 assurances-vie sont hors succession. Chacune a un abattement de 152 500 EUR. Total : 457 500 EUR d abattement. Tant que le total AV reste en dessous, Anne-Lyse recoit tout sans payer de droits.<br><br>Pour le reste (CC + livrets), il y a un abattement frere/soeur de 15 932 EUR puis des droits a 35-45%.<br><br><b style="color:#FFD060;">Concretement :</b><br>Si tu decedes a 75 ans avec 453 000 EUR : Anne-Lyse recoit environ 440 000 EUR net.<br>Si tu decedes a 92 ans avec 50 000 EUR : Anne-Lyse recoit environ 49 200 EUR net (quasi 0 droits).<br><br>La donation nue-propriete du T3 Meylan (a faire chez le notaire) permet d economiser 30 000 a 50 000 EUR de droits supplementaires.</div>', unsafe_allow_html=True)

    titre("Le MDPH - pourquoi c est le plus important")
    st.markdown('<div style="background:#140810;border-radius:10px;padding:20px;margin-bottom:16px;color:#F0E6D8;font-size:14px;line-height:1.8;">Ton taux MDPH est a 75%. Si tu arrives a 80% ou plus, deux choses changent :<br><br><b>1.</b> L AAH est maintenue jusqu a 67 ans au lieu de 64 ans (+3 ans de revenus)<br><b>2.</b> Tu deviens eligible a la PCH (Prestation Compensation Handicap) en plus de l AAH<br><br><b style="color:#4DFF99;">Impact chiffre :</b><br>Avec une PCH de 500 EUR/mois, ton capital a 92 ans passe de 50 000 EUR a 282 000 EUR de plus. C est le levier le plus puissant de tout le plan.<br><br><b style="color:#FF7777;">Attention :</b> le dossier doit etre depose AVANT 60 ans. Apres c est trop tard, irreversible. Tu as 9,5 ans pour le faire.</div>', unsafe_allow_html=True)

    titre("Ce qu il faut faire maintenant")
    st.markdown('<div style="background:#140810;border-radius:10px;padding:20px;margin-bottom:16px;color:#F0E6D8;font-size:14px;line-height:1.8;"><b style="color:#CC3333;">URGENT (cette semaine)</b><br>- Ouvrir AV2 chez Linxea (500 EUR) pour lancer l horloge des 8 ans<br>- Prendre RDV medecin pour le dossier MDPH<br><br><b style="color:#D4A017;">IMPORTANT (3 mois)</b><br>- Deposer dossier MDPH complet<br>- RDV notaire : testament + mandat + donation NP<br><br><b style="color:#C4922A;">A PLANIFIER (6 mois)</b><br>- Cloturer AV Carrefour Horizons (1,70% c est trop bas)<br>- Reduire les livrets a 16 560 EUR, mettre le surplus en AV1<br>- Lancer travaux parents + demande MaPrimeRenov</div>', unsafe_allow_html=True)

    titre("Comment le cockpit gere tout ca automatiquement")
    st.markdown('<div style="background:#140810;border-radius:10px;padding:20px;margin-bottom:16px;color:#F0E6D8;font-size:14px;line-height:1.8;">Le cockpit a un moteur qui s appelle ARVA. Chaque 1er janvier il regarde combien il reste de capital, combien de mois il reste jusqu a 92 ans, et il calcule la pioche optimale pour le mois.<br><br>Si le capital a bien travaille dans l annee, l ARVA te dit que tu peux piocher un peu plus. Si le rendement a ete mauvais, il te dit de reduire. C est le pilote automatique.<br><br>Les alertes (orange et rouge) se declenchent automatiquement si quelque chose deraille : rendement trop bas, buffer trop gros, CC trop bas, seuil CAF depasse.<br><br>Toi tu n as rien a calculer. Tu ouvres le cockpit, tu regardes le budget du jour et du mois, et tu vis ta vie.</div>', unsafe_allow_html=True)

    st.markdown("---")
    titre("TABLEAUX DETAILLES")
    st.info("Les sections ci-dessous reprennent les memes informations en format tableau pour reference precise.")

'''

    t = before + simple_annexe + after

f = open(p, 'w', encoding='utf-8')
f.write(t)
f.close()
print('Annexe simple OK')
