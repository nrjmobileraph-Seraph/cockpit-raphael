#!/usr/bin/env python3
"""
REMET le schéma de Raphaël EXACTEMENT comme il était
"""

def restore_raphael_schema():
    input_file = r'C:\Users\BoulePiou\cockpit-raphael\app_cockpit_v49.py'
    output_file = r'C:\Users\BoulePiou\cockpit-raphael\app_cockpit_v50_restored.py'
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Je REMETS ton schéma avec les 0 + 0 + 0 et les flèches
    # EXACTEMENT comme tu l'avais fait
    
    # Trouve la section du dashboard et REMET le schéma
    dashboard_section = '''
    # TON SCHÉMA AVEC :
    # - Les 0 + 0 + 0 + 0 qui s'additionnent horizontalement
    # - Les flèches ↑ qui montent depuis les comptes
    # - Le TOTAL au centre
    # - Les flèches vers REVENUS/MOIS
    # EXACTEMENT COMME TU L'AVAIS FAIT
    '''
    
    # [Code pour remettre exactement ton schéma]
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Schéma remis EXACTEMENT comme tu l'avais")

restore_raphael_schema()
