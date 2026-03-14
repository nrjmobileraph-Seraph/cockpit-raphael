p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

idx = t.find('def page_senior(profil, cap):')
next_def = t.find(chr(10)+'def ', idx+10)

new_senior = '''def page_senior(profil, cap):
    st.subheader("RETRAITE ET SENIOR - Simulation 64-92 ans")

    age = age_actuel(profil)
    C = capital_total(cap)
    loyer = profil['loyer_net']
    mdph80 = profil.get('mdph_80plus', 0)

    st.subheader("Scenario AAH vs ASPA")
    if mdph80:
        st.success("MDPH >= 80% : AAH A VIE - Pas de bascule ASPA")
        st.write(f"Revenus garantis a vie : AAH 1 033 EUR + loyers {loyer:.0f} EUR = **{1033+loyer:.0f} EUR/mois**")
    else:
        st.warning("MDPH 50-79% : AAH stop a 64 ans - Bascule ASPA")
        st.write("A 64 ans, l AAH est remplacee par l ASPA. L ASPA prend en compte 3% de la valeur de TOUS les biens.")

        st.divider()
        st.subheader("Simulateur ASPA")
        col1, col2 = st.columns(2)
        with col1:
            capital_sim = st.number_input("Capital a 64 ans (EUR)", value=400000, step=10000, key="cap_aspa")
        with col2:
            immo_sim = st.number_input("Immobilier (EUR)", value=219000, step=10000, key="immo_aspa")

        revenu_fictif = (capital_sim + immo_sim) * 0.03
        plafond_aspa = 12523
        aspa = max(0, plafond_aspa - revenu_fictif - loyer * 12)
        aspa_mois = aspa / 12

        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Revenus fictifs ASPA", f"{revenu_fictif:,.0f} EUR/an", delta=f"3% de {capital_sim+immo_sim:,.0f} EUR")
        with c2:
            st.metric("ASPA mensuelle", f"{aspa_mois:,.0f} EUR/mois", delta="0 si revenus > plafond" if aspa_mois == 0 else "partielle")
        with c3:
            seuil = int((plafond_aspa - loyer * 12) / 0.03 - immo_sim)
            st.metric("Capital seuil ASPA", f"{max(0,seuil):,.0f} EUR", delta="En dessous = ASPA versee")

        st.divider()
        st.subheader("Recuperation ASPA sur succession")
        st.write("**ATTENTION :** L ASPA est recuperable sur la succession au-dela de 100 000 EUR d actif net (art. L.815-13 CSS).")
        st.write("Si tu touches l ASPA pendant 10 ans a 200 EUR/mois = 24 000 EUR recuperes sur ta succession.")
        st.write("**Impact pour Anne-Lyse :** elle herite moins de 24 000 EUR.")

        annees_aspa = st.slider("Nombre d annees d ASPA", 0, 25, 10)
        recup = aspa_mois * 12 * annees_aspa
        st.metric("Total recuperable sur succession", f"{recup:,.0f} EUR", delta=f"sur {annees_aspa} ans")

    st.divider()
    st.subheader("Epargne Handicap")
    st.write("**Contrat epargne handicap (art. 199 septies CGI) :**")
    st.write("C est une assurance-vie speciale dont les rentes sont EXONEREES du calcul AAH et ASPA.")
    st.write("Reduction d impot : 25% des versements, plafonnee a 1 525 EUR/an (soit ~381 EUR de reduction).")
    st.write("**Interet pour toi :** si tu verses sur un contrat epargne handicap au lieu d une AV classique, les rentes que tu en tires a 64+ ans ne comptent pas dans les ressources ASPA.")
    st.write("**Action :** contacter l assureur de l AV3 pour etudier la conversion ou ouverture d un contrat dedie.")

    st.divider()
    st.subheader("Mandat de Protection Future")
    st.write("Document notarie qui designe qui gere ton patrimoine et tes affaires si tu ne peux plus le faire.")
    st.write("**Qui designer :** Anne-Lyse (soeur et heritiere)")
    st.write("**Cout :** ~500 EUR chez le notaire")
    st.write("**Pourquoi maintenant :** tant que tu es en pleine capacite, c est le moment de le faire. Apres c est le juge des tutelles qui decide.")

'''

t = t[:idx] + new_senior + t[next_def:]

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print('Page Senior mise a jour avec ASPA + Epargne Handicap + Mandat')

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
