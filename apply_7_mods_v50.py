#!/usr/bin/env python3
"""
Applique les 7 modifications identifiées sur v49 pour créer v50
"""

def apply_7_mods():
    input_file = r'C:\Users\BoulePiou\cockpit-raphael\app_cockpit_v49.py'
    output_file = r'C:\Users\BoulePiou\cockpit-raphael\app_cockpit_v50.py'
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("Application des 7 modifications...")
    
    # 1. Navigation plus grosse dans sidebar
    content = content.replace(
        'st.markdown("## 🧭 Navigation")\n        page = st.radio(\n            "Choisir une page",',
        'st.markdown("## 🧭 Navigation")\n        st.markdown("---")\n        page = st.radio(\n            "",'
    )
    
    # 2. ARVA renommé
    content = content.replace('"ARVA"', '"ARVA (Rente Vie Autonome)"')
    
    # 3. Onglets simulateur renommés
    content = content.replace('"Simulation"', '"📊 Simulation complète"')
    content = content.replace('"Rachat unique"', '"💰 Rachat ponctuel"')
    content = content.replace('"Rachats programmés"', '"📅 Rachats réguliers"')
    
    # 4. Stratégies non retenues dans expander
    old = 'st.subheader("📊 Stratégies non retenues")'
    new = 'with st.expander("📊 Stratégies non retenues", expanded=False):'
    content = content.replace(old, new)
    
    # 5. Résultat ARVA en tableau HTML
    old_code = 'st.code(result, language="text")'
    new_html = '''st.markdown(f"""
                <div style='background-color: #f0f2f6; padding: 20px; border-radius: 10px;'>
                    <pre style='font-family: monospace; white-space: pre;'>{result}</pre>
                </div>
                """, unsafe_allow_html=True)'''
    content = content.replace(old_code, new_html)
    
    # 6. Sensibilité formatage
    content = content.replace(
        'st.write(f"Montant optimal: {montant_opt:,.0f} €")',
        'st.metric("Montant optimal", f"{montant_opt:,.0f} €")'
    )
    
    # 7. Ajustement cash manuel (après synchro Finary)
    search_finary = '''                st.success(f"✅ Synchronisation réussie! {updated} comptes mis à jour")'''
    replace_finary = '''                st.success(f"✅ Synchronisation réussie! {updated} comptes mis à jour")
                
                # Ajustement manuel du cash
                with st.expander("⚙️ Ajustement manuel du solde", expanded=False):
                    st.info("Pour corriger le décalage temporel de Finary")
                    cash_adjustment = st.number_input(
                        "Ajuster le cash BoursoBank",
                        value=0.0,
                        step=100.0,
                        help="Positif pour ajouter, négatif pour retrancher"
                    )
                    if cash_adjustment != 0:
                        # Mettre à jour le cash dans finance_data
                        st.session_state.finance_data['cash'] += cash_adjustment
                        st.success(f"Cash ajusté de {cash_adjustment:+.0f}€")'''
    
    content = content.replace(search_finary, replace_finary)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Créé: {output_file}")
    print(f"   Taille: {len(content)} bytes")
    return output_file

if __name__ == "__main__":
    apply_7_mods()
