p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Trouver le debut de page_dashboard
idx = t.find('def page_dashboard(profil, cap):')
# Trouver la fonction suivante
next_def = t.find('\ndef ', idx+10)

old_dashboard = t[idx:next_def]

new_dashboard = '''def page_dashboard(profil, cap):
    from datetime import date, datetime
    import calendar
    today = date.today()
    age = age_actuel(profil)
    C = capital_total(cap)

    # Planning chronologique avec solde cumule
    planning = [
        ('2026-03-12', 'Situation actuelle', 0, 'info'),
        ('2026-04-15', 'Reception AV Jean-Luc', 34500, 'entree'),
        ('2026-04-25', 'Donation usufruit MEYLAN', -3349, 'sortie'),
        ('2026-06-10', 'Virement net SCI', 296100, 'entree'),
        ('2026-06-30', 'Acompte travaux 30%', -9900, 'sortie'),
        ('2026-07-05', 'Virement net succession', 182900, 'entree'),
        ('2026-08-01', 'Recuperation appart + garage', 0, 'info'),
        ('2026-11-15', 'Solde artisans 70%', -23100, 'sortie'),
        ('2026-12-01', 'Mobilier LMNP', -15000, 'sortie'),
        ('2026-12-31', 'Charges courantes avant location', -1075, 'sortie'),
        ('2027-01-15', 'Premier bail mobilite - LMNP operationnel', 0, 'info'),
    ]

    # Calculer solde cumule a la date du jour
    solde = 0
    passe = []
    avenir = []
    for d, label, flux, typ in planning:
        dt = date.fromisoformat(d)
        solde_avant = solde
        if flux != 0:
            solde += flux
        if dt <= today:
            passe.append((d, label, flux, typ, solde))
        else:
            avenir.append((d, label, flux, typ, solde))

    # Phase detection
    phase_0 = today < date(2027, 1, 15)

    if phase_0:
        # === DASHBOARD PHASE 0 : CONSTRUCTION ===
        titre("COCKPIT PATRIMONIAL - PHASE CONSTRUCTION")

        # AAH reelle (625 en 2026-2027, pas 1033)
        aah_reelle = 625
        versement_parents = 325
        loyers_actuels = 0  # pas encore de loyers LMNP
        reste_vivre = aah_reelle - versement_parents + loyers_actuels

        # Determiner sous-phase
        if today < date(2026, 4, 15):
            sous_phase = "Preparation"
            sous_phase_icon = "📋"
        elif today < date(2026, 6, 10):
            sous_phase = "AV recue - Donation usufruit"
            sous_phase_icon = "📝"
        elif today < date(2026, 7, 5):
            sous_phase = "SCI encaissee"
            sous_phase_icon = "💰"
        elif today < date(2026, 8, 1):
            sous_phase = "Succession encaissee"
            sous_phase_icon = "💰"
        elif today < date(2026, 11, 15):
            sous_phase = "Travaux en cours"
            sous_phase_icon = "🔨"
        elif today < date(2027, 1, 15):
            sous_phase = "Ameublement et mise en location"
            sous_phase_icon = "🏠"
        else:
            sous_phase = "LMNP operationnel"
            sous_phase_icon = "✅"

        # Ligne 1 : Sous-phase + solde
        st.markdown(f"""<div style="background:linear-gradient(145deg, #1A0D12 0%, #150A10 100%);border:2px solid #C4922A;border-radius:12px;padding:20px;text-align:center;margin-bottom:16px;">
            <div style="color:#BBA888;font-size:12px;text-transform:uppercase;letter-spacing:2px;">{sous_phase_icon} PHASE ACTUELLE</div>
            <div style="color:#FFD060;font-size:28px;font-weight:900;margin:8px 0;">{sous_phase}</div>
            <div style="color:#DDCCBB;font-size:14px;">{age:.1f} ans · {today.strftime('%d/%m/%Y')}</div>
        </div>""", unsafe_allow_html=True)

        # Ligne 2 : 3 KPI
        k1, k2, k3 = st.columns(3)
        with k1:
            st.markdown(f"""<div style="background:#1A0D12;border:2px solid #1A6B4B;border-radius:12px;padding:16px;text-align:center;">
                <div style="color:#BBA888;font-size:11px;text-transform:uppercase;">SOLDE CUMULE</div>
                <div style="color:#4DFF99;font-size:36px;font-weight:900;">{solde:,.0f} EUR</div>
                <div style="color:#DDCCBB;font-size:12px;">Capital en construction</div>
            </div>""", unsafe_allow_html=True)
        with k2:
            st.markdown(f"""<div style="background:#1A0D12;border:2px solid #D4A017;border-radius:12px;padding:16px;text-align:center;">
                <div style="color:#BBA888;font-size:11px;text-transform:uppercase;">AAH REELLE 2026</div>
                <div style="color:#FFD060;font-size:36px;font-weight:900;">{aah_reelle} EUR</div>
                <div style="color:#DDCCBB;font-size:12px;">Base revenus 2024 (SCI active)</div>
            </div>""", unsafe_allow_html=True)
        with k3:
            st.markdown(f"""<div style="background:#1A0D12;border:2px solid #8B0000;border-radius:12px;padding:16px;text-align:center;">
                <div style="color:#BBA888;font-size:11px;text-transform:uppercase;">RESTE POUR VIVRE</div>
                <div style="color:#FF7777;font-size:36px;font-weight:900;">{reste_vivre} EUR</div>
                <div style="color:#DDCCBB;font-size:12px;">AAH {aah_reelle} - parents {versement_parents}</div>
            </div>""", unsafe_allow_html=True)

        # Objectif final
        st.markdown(f"""<div style="background:#0A0A0A;border:1px solid #333;border-radius:8px;padding:12px;margin:16px 0;text-align:center;">
            <span style="color:#BBA888;font-size:12px;">OBJECTIF JANVIER 2027 :</span>
            <span style="color:#4DFF99;font-size:14px;font-weight:700;"> Capital 461 000 EUR · Loyers 320 EUR/mois · AAH protegee</span>
        </div>""", unsafe_allow_html=True)

        # Prochaines actions
        titre("📋 PROCHAINES ACTIONS")
        if avenir:
            for d, label, flux, typ, sol in avenir[:6]:
                dt = date.fromisoformat(d)
                jours = (dt - today).days
                if flux > 0:
                    flux_txt = f'<span style="color:#4DFF99;font-weight:700;">+{flux:,.0f} EUR</span>'
                elif flux < 0:
                    flux_txt = f'<span style="color:#FF7777;font-weight:700;">{flux:,.0f} EUR</span>'
                else:
                    flux_txt = '<span style="color:#BBA888;">—</span>'
                badge_col = "#4DFF99" if typ=="entree" else ("#FF7777" if typ=="sortie" else "#FFD060")
                st.markdown(f"""<div style="background:#140810;border-left:3px solid {badge_col};border-radius:0 8px 8px 0;padding:10px 16px;margin:4px 0;display:flex;justify-content:space-between;align-items:center;">
                    <div>
                        <span style="color:#F0E6D8;font-size:14px;font-weight:600;">{label}</span><br>
                        <span style="color:#BBA888;font-size:11px;">Dans {jours} jours · {dt.strftime('%d/%m/%Y')}</span>
                    </div>
                    <div style="text-align:right;">
                        {flux_txt}<br>
                        <span style="color:#BBA888;font-size:11px;">Solde apres : {sol:,.0f} EUR</span>
                    </div>
                </div>""", unsafe_allow_html=True)
        else:
            st.markdown('<div style="color:#4DFF99;font-size:16px;text-align:center;padding:20px;">✅ Toutes les etapes sont terminees !</div>', unsafe_allow_html=True)

        # Actions deja faites
        if passe:
            titre("✅ DEJA FAIT")
            for d, label, flux, typ, sol in passe:
                flux_txt = f"+{flux:,.0f}" if flux>0 else (f"{flux:,.0f}" if flux<0 else "—")
                st.markdown(f'<div style="color:#666;font-size:12px;padding:4px 16px;">✓ {d} · {label} · {flux_txt} EUR</div>', unsafe_allow_html=True)

        # Tresorerie previsionnelle
        titre("📈 TRESORERIE PREVISIONNELLE")
        all_events = passe + avenir
        chart_data = []
        for d, label, flux, typ, sol in all_events:
            if flux != 0:
                chart_data.append({"date": d, "solde": sol})
        if chart_data:
            import pandas as pd
            df = pd.DataFrame(chart_data)
            st.line_chart(df.set_index("date")["solde"], use_container_width=True)

        # Budget mensuel reel
        titre("💶 BUDGET MENSUEL REEL")
        b1, b2 = st.columns(2)
        with b1:
            st.markdown(f"""<div style="background:#140810;border-radius:8px;padding:16px;">
                <div style="color:#BBA888;font-size:11px;text-transform:uppercase;">REVENUS</div>
                <div style="color:#F0E6D8;font-size:13px;margin-top:8px;">AAH : +{aah_reelle} EUR</div>
                <div style="color:#F0E6D8;font-size:13px;">Loyers LMNP : +0 EUR (pas encore)</div>
                <div style="color:#4DFF99;font-size:16px;font-weight:700;margin-top:8px;">Total : +{aah_reelle} EUR</div>
            </div>""", unsafe_allow_html=True)
        with b2:
            st.markdown(f"""<div style="background:#140810;border-radius:8px;padding:16px;">
                <div style="color:#BBA888;font-size:11px;text-transform:uppercase;">DEPENSES</div>
                <div style="color:#F0E6D8;font-size:13px;margin-top:8px;">Versement parents : -{versement_parents} EUR</div>
                <div style="color:#F0E6D8;font-size:13px;">Depenses perso : ~-200 EUR</div>
                <div style="color:#FF7777;font-size:16px;font-weight:700;margin-top:8px;">Reste : ~{reste_vivre - 200} EUR</div>
            </div>""", unsafe_allow_html=True)

        # Countdown
        objectif = date(2027, 1, 15)
        jours_restants = (objectif - today).days
        st.markdown(f"""<div style="background:linear-gradient(145deg, #0A0505 0%, #1A0A12 100%);border:1px solid #C4922A;border-radius:12px;padding:20px;text-align:center;margin-top:16px;">
            <div style="color:#BBA888;font-size:12px;text-transform:uppercase;">COMPTE A REBOURS</div>
            <div style="color:#FFD060;font-size:48px;font-weight:900;">{jours_restants} jours</div>
            <div style="color:#DDCCBB;font-size:14px;">avant LMNP operationnel (15 janvier 2027)</div>
        </div>""", unsafe_allow_html=True)

    else:
        # === DASHBOARD PHASE OPERATIONNELLE (janvier 2027+) ===
        mois = mois_restants(profil)
        W = arva(C, mois, profil['rendement_annuel'])
        traj = trajectoire_theorique(profil, age)
        rp = rendement_pondere(cap)
        ph_num, ph_label = phase(age)
        pioche, src = pioche_ce_mois(profil, cap)
        rail = profil['rail_mensuel']
        ecart_traj = (C-traj)/traj*100 if traj>0 else 0
        ecart_arva = W - rail
        cc_val = cap['cc']
        aah_m = profil['aah_mensuel']
        pch_m = profil.get('pch_mensuel', 0)
        loyer_m = profil['loyer_net']
        rvd_m = profil.get('rvd_mensuel', 0) if ph_num == 3 else 0
        entrees_auto = aah_m + pch_m + loyer_m + rvd_m
        manque = rail - entrees_auto

        import calendar
        jours_dans_mois = calendar.monthrange(today.year, today.month)[1]
        jours_restants = jours_dans_mois - today.day + 1
        budget_jour = int(rail / jours_dans_mois)
        mois_noms = ["Janvier","Fevrier","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Decembre"]
        mois_nom = mois_noms[today.month-1]

        bd1, bd2 = st.columns(2)
        with bd1:
            st.markdown(f\\'<div style="background:linear-gradient(145deg, #1A0D12 0%, #150A10 100%);border:2px solid #C4922A;border-radius:12px;padding:20px;text-align:center;"><div style="color:#BBA888;font-size:12px;text-transform:uppercase;letter-spacing:1px;">BUDGET DU JOUR</div><div style="color:#4DFF99;font-size:42px;font-weight:900;margin:8px 0;">{budget_jour} EUR</div><div style="color:#DDCCBB;font-size:13px;">{jours_restants} jours restants</div></div>\\', unsafe_allow_html=True)
        with bd2:
            st.markdown(f\\'<div style="background:linear-gradient(145deg, #1A0D12 0%, #150A10 100%);border:2px solid #D4A017;border-radius:12px;padding:20px;text-align:center;"><div style="color:#BBA888;font-size:12px;text-transform:uppercase;letter-spacing:1px;">BUDGET DU MOIS</div><div style="color:#FFD060;font-size:42px;font-weight:900;margin:8px 0;">{rail:,.0f} EUR</div><div style="color:#DDCCBB;font-size:13px;">{mois_nom} {today.year}</div></div>\\', unsafe_allow_html=True)

        cc_border = "#CC3333" if cc_val < 1000 else ("#D4A017" if cc_val < manque*2 else "#1A6B4B")
        st.markdown(f\\'<div style="background:linear-gradient(145deg, #1A0D12 0%, #150A10 100%);border:2px solid {cc_border};border-radius:12px;padding:20px;text-align:center;margin-top:10px;"><div style="color:#BBA888;font-size:12px;text-transform:uppercase;letter-spacing:1px;">COMPTE COURANT</div><div style="color:#4DFF99;font-size:42px;font-weight:900;margin:8px 0;">{cc_val:,.0f} EUR</div><div style="color:#FFD060;font-size:14px;font-weight:600;">Alimente ce mois-ci de {manque:,.0f} EUR</div></div>\\', unsafe_allow_html=True)

        titre("5 INDICATEURS CLES")
        k1,k2,k3,k4,k5 = st.columns(5)
        cc2 = "vert" if ecart_traj>=0 else ("orange" if ecart_traj>-10 else "rouge")
        coul = "vert" if abs(ecart_arva)<100 else ("orange" if ecart_arva>-300 else "rouge")
        with k1: kpi("Capital total",f"{C:,.0f} EUR",f"Traj. : {traj:,.0f} EUR ({ecart_traj:+.1f}%)",cc2)
        with k2: kpi("Rail mensuel",f"{rail:,.0f} EUR/mois",f"ARVA recommande : {W:,.0f} EUR",coul)
        with k3: kpi("Rendement pondere",f"{rp*100:.2f} %","Sur l ensemble des poches","bleu")
        with k4: kpi("Loyer net",f"{loyer_m:,.0f} EUR/mois","LMNP reel - base 0 EUR","bleu")
        with k5: kpi("Phase",f"{ph_num}",ph_label,"bleu")

'''

t = t[:idx] + new_dashboard + t[next_def:]

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print('Dashboard Phase 0 installe OK')
