import re
import os

FILE_PATH = r"C:/Users/BoulePiou/cockpit-raphael/app.py"
BACKUP_PATH = FILE_PATH + ".backup_before_clean"

SUSPECT_SELECTORS = [
    r'stSidebar',
    r'collapsedControl',
    r'sidebar',
    r'@media.*?\(\s*max-width\s*:\s*\d+px\s*\)',
    r'display\s*:\s*(?:none|block|flex|grid)\s*!important',
    r'width\s*:\s*\d+px\s*!important',
    r'min-width\s*:\s*\d+px\s*!important',
    r'transform\s*:\s*none\s*!important',
    r'opacity\s*:\s*1\s*!important',
]

def contains_suspect_css(text):
    for pattern in SUSPECT_SELECTORS:
        if re.search(pattern, text, re.IGNORECASE):
            return True
    return False

def find_st_markdown_blocks(lines):
    blocks = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if 'st.markdown(' in line:
            start = i
            j = i
            open_paren = line.count('(') - line.count(')')
            while j < len(lines) and open_paren > 0:
                j += 1
                if j >= len(lines):
                    break
                open_paren += lines[j].count('(') - lines[j].count(')')
            end = j if j < len(lines) else i
            blocks.append((start, end))
            i = end + 1
        else:
            i += 1
    return blocks

def is_block_css_suspect(lines, start, end):
    block_text = ''.join(lines[start:end+1])
    if '{' not in block_text or '}' not in block_text:
        return False
    return contains_suspect_css(block_text)

def main():
    if not os.path.exists(FILE_PATH):
        print(f"❌ Fichier introuvable : {FILE_PATH}")
        return

    with open(FILE_PATH, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    print(f"📄 Fichier chargé : {len(lines)} lignes.")
    blocks = find_st_markdown_blocks(lines)
    print(f"🔍 {len(blocks)} bloc(s) st.markdown trouvé(s).")

    suspect_blocks = []
    for (start, end) in blocks:
        if is_block_css_suspect(lines, start, end):
            suspect_blocks.append((start, end))
            print(f"\n⚠️  Bloc suspect (lignes {start+1} à {end+1}) :")
            for i in range(start, min(start+3, end+1)):
                print(f"  L{i+1}: {lines[i].rstrip()}")
            if end - start > 3:
                print("  ...")
            print("-" * 50)

    if not suspect_blocks:
        print("✅ Aucun bloc CSS suspect trouvé.")
        return

    print(f"\n🗑️  {len(suspect_blocks)} bloc(s) vont être supprimés.")
    confirm = input("Confirmer la suppression ? (oui/non) : ").strip().lower()
    if confirm not in ['oui', 'o', 'yes', 'y']:
        print("Annulation.")
        return

    os.rename(FILE_PATH, BACKUP_PATH)
    print(f"💾 Sauvegarde créée : {BACKUP_PATH}")

    new_lines = []
    last_idx = 0
    for (start, end) in sorted(suspect_blocks):
        new_lines.extend(lines[last_idx:start])
        last_idx = end + 1
    new_lines.extend(lines[last_idx:])

    with open(FILE_PATH, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

    print(f"✅ Nettoyage terminé. {len(suspect_blocks)} bloc(s) supprimé(s).")

if __name__ == "__main__":
    main()
