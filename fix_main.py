p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'a',encoding='utf-8')
f.write('''

def main():
    init_db()
    profil=get_profil(); cap=get_capital()
    if not profil or not cap:
        st.error("Erreur base de donnees."); return
    age=age_actuel(profil); C=capital_total(cap)
    with st.sidebar:
        st.markdown("## Cockpit Raphael")
        st.markdown(f"**Age :** {age:.1f} ans")
        st.markdown(f"**Capital :** {C:,.0f} EUR")
        st.markdown(f"**Rail :** {profil['rail_mensuel']:,.0f} EUR/mois")
        st.markdown(f"**MDPH :** {profil['taux_mdph']}%")
        al=calculer_alertes(profil,cap)
        nr=sum(1 for n,_ in al if n=='rouge')
        no=sum(1 for n,_ in al if n=='orange')
        if nr: st.markdown(f"**{nr} alerte(s) rouge(s)**")
        elif no: st.markdown(f"{no} alertes(s) orange")
        else: st.markdown("Aucune alerte")
        st.markdown("---")
        page=st.radio("Navigation",[
            "Tableau de bord",
            "Moteur ARVA",
            "Suivi AV x 3 contrats",
            "Scenarios simulateurs",
            "Fiscal & CAF",
            "Declaration impots",
            "LMNP & IRL",
            "Jalons & Actions",
            "AAH / CAF / PCH",
            "Inflation",
            "Succession",
            "Mode Senior",
            "Bilan d exportation",
            "BoursoBank",
            "Crypto",
            "Annexe - Reference",
            "Saisie capital",
        ])
        st.markdown("---")
        st.caption("v4.2 - Mars 2026")
    {
        "Tableau de bord":        lambda: page_dashboard(profil,cap),
        "Moteur ARVA":           lambda: page_arva(profil,cap),
        "Suivi AV x 3 contrats": lambda: page_suivi_av(profil,cap),
        "Scenarios simulateurs": lambda: page_simulateur(profil,cap),
        "Fiscal & CAF":          lambda: page_fiscal(profil,cap),
        "Declaration impots":    lambda: page_impots(profil,cap),
        "LMNP & IRL":            lambda: page_lmnp(profil,cap),
        "Jalons & Actions":       lambda: page_jalons(profil,cap),
        "AAH / CAF / PCH":       lambda: page_caf_pch(profil,cap),
        "Inflation":              lambda: page_inflation(profil,cap),
        "Succession":             lambda: page_succession(profil,cap),
        "Mode Senior":            lambda: page_senior(profil,cap),
        "Bilan d exportation":    lambda: page_export(profil,cap),
        "BoursoBank":             lambda: page_boursobank(profil,cap),
        "Crypto":                  lambda: page_crypto(profil,cap),
        "Annexe - Reference":      lambda: page_annexe(profil,cap),
        "Saisie capital":        lambda: page_saisie(profil,cap),
    }[page]()

if __name__=="__main__":
    main()
''')
f.close()
print('main() restaure OK')
