#!/usr/bin/env python3
"""
Ajoute des flèches visuelles sur le dashboard pour montrer le flux des revenus
"""

import sys
import os

def add_arrows_to_dashboard():
    # Lire le fichier v49
    input_file = r'C:\Users\BoulePiou\cockpit-raphael\app_cockpit_v49.py'
    output_file = r'C:\Users\BoulePiou\cockpit-raphael\app_cockpit_v51_arrows.py'
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Trouver et modifier la section du dashboard des revenus
    old_revenus_section = """            # Revenus passifs
            col1, col2 = st.columns(2)
            with col1:
                st.metric("AAH", f"{st.session_state.finance_data['revenus']['AAH']:,.0f} €/mois")
            with col2:
                st.metric("Loyers nets LMNP", f"{st.session_state.finance_data['revenus']['loyers_nets']:,.0f} €/mois")
            
            # Total revenus passifs
            total_passif = st.session_state.finance_data['revenus']['AAH'] + st.session_state.finance_data['revenus']['loyers_nets']
            st.metric("**Total revenus passifs**", f"{total_passif:,.0f} €/mois")"""
    
    new_revenus_section = """            # Revenus passifs avec flèches
            col1, col2 = st.columns(2)
            with col1:
                st.metric("AAH", f"{st.session_state.finance_data['revenus']['AAH']:,.0f} €/mois")
                st.markdown("<div style='text-align: center; font-size: 20px; color: #4CAF50;'>↘</div>", unsafe_allow_html=True)
            with col2:
                st.metric("Loyers nets LMNP", f"{st.session_state.finance_data['revenus']['loyers_nets']:,.0f} €/mois")
                st.markdown("<div style='text-align: center; font-size: 20px; color: #4CAF50;'>↙</div>", unsafe_allow_html=True)
            
            # Total revenus passifs avec flèche montante
            total_passif = st.session_state.finance_data['revenus']['AAH'] + st.session_state.finance_data['revenus']['loyers_nets']
            st.metric("**Total revenus passifs**", f"{total_passif:,.0f} €/mois")
            st.markdown("<div style='text-align: center; font-size: 30px; color: #2196F3; font-weight: bold;'>⬆</div>", unsafe_allow_html=True)"""
    
    content = content.replace(old_revenus_section, new_revenus_section)
    
    # Modifier aussi la section du revenu total du mois pour ajouter des flèches convergentes
    old_revenu_mois = """        # Revenu mensuel total
        revenu_mois = (
            st.session_state.finance_data['revenus']['AAH'] +
            st.session_state.finance_data['revenus']['loyers_nets'] +
            st.session_state.finance_data['revenus'].get('activite_pro', 0)
        )
        st.metric(
            "**REVENU DU MOIS**",
            f"{revenu_mois:,.0f} €",
            delta=f"{revenu_mois - st.session_state.finance_data['budget']['budget_mensuel']:+,.0f} €"
        )"""
    
    new_revenu_mois = """        # Revenu mensuel total avec flèches convergentes
        st.markdown("<div style='text-align: center; margin: -10px 0;'>", unsafe_allow_html=True)
        st.markdown('''
        <div style="display: flex; justify-content: center; align-items: center; margin: 10px 0;">
            <span style="font-size: 20px; color: #4CAF50;">↗</span>
            <span style="margin: 0 20px; font-size: 14px; color: #666;">Revenus passifs</span>
            <span style="font-size: 20px; color: #FF9800;">↖</span>
            <span style="margin-left: 20px; font-size: 14px; color: #666;">Revenus pro</span>
        </div>
        ''', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        revenu_mois = (
            st.session_state.finance_data['revenus']['AAH'] +
            st.session_state.finance_data['revenus']['loyers_nets'] +
            st.session_state.finance_data['revenus'].get('activite_pro', 0)
        )
        st.metric(
            "**REVENU DU MOIS**",
            f"{revenu_mois:,.0f} €",
            delta=f"{revenu_mois - st.session_state.finance_data['budget']['budget_mensuel']:+,.0f} €"
        )
        
        # Grande flèche vers le budget
        st.markdown('''
        <div style="text-align: center; margin: 20px 0;">
            <div style="font-size: 40px; color: #2196F3; font-weight: bold;">⬇</div>
            <div style="font-size: 12px; color: #666; margin-top: -10px;">alimente le budget</div>
        </div>
        ''', unsafe_allow_html=True)"""
    
    content = content.replace(old_revenu_mois, new_revenu_mois)
    
    # Ajouter aussi des flèches pour les revenus pro s'ils existent
    old_revenus_pro = """            # Revenus professionnels si applicable
            if st.session_state.finance_data['revenus'].get('activite_pro', 0) > 0:
                st.metric(
                    "Revenus professionnels",
                    f"{st.session_state.finance_data['revenus']['activite_pro']:,.0f} €/mois"
                )"""
    
    new_revenus_pro = """            # Revenus professionnels si applicable avec flèche
            if st.session_state.finance_data['revenus'].get('activite_pro', 0) > 0:
                st.metric(
                    "Revenus professionnels",
                    f"{st.session_state.finance_data['revenus']['activite_pro']:,.0f} €/mois"
                )
                st.markdown("<div style='text-align: center; font-size: 25px; color: #FF9800; font-weight: bold;'>⬆</div>", unsafe_allow_html=True)"""
    
    content = content.replace(old_revenus_pro, new_revenus_pro)
    
    # Écrire le fichier modifié
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Fichier créé : {output_file}")
    print("\n🎯 Flèches ajoutées :")
    print("  • AAH et Loyers → convergent vers Total revenus passifs")
    print("  • Total revenus passifs ⬆ monte vers Revenu du mois")
    print("  • Revenus pro ⬆ monte aussi vers Revenu du mois")
    print("  • Revenu du mois ⬇ grande flèche vers le budget")
    print("\n👊 Pour tester : streamlit run app_cockpit_v51_arrows.py")

if __name__ == "__main__":
    add_arrows_to_dashboard()
