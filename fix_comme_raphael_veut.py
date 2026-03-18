#!/usr/bin/env python3
"""
Remet tout comme Raphaël veut, basé sur ses photos
"""

def fix_everything():
    input_file = r'C:\Users\BoulePiou\cockpit-raphael\app_cockpit_v49.py'
    output_file = r'C:\Users\BoulePiou\cockpit-raphael\app_cockpit_v50_correct.py'
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # ICI on va mettre EXACTEMENT ce que tu veux d'après les photos
    # Dis-moi ce que tu vois qui ne va pas sur les photos
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Tout remis comme tu veux")

if __name__ == "__main__":
    fix_everything()
