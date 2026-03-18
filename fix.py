lines = open('app.py', 'r', encoding='utf-8').readlines()
out, i = [], 0
while i < len(lines):
    if "_vals = ''" in lines[i]:
        while i < len(lines):
            if 'st.markdown' in lines[i] and '_vals' in lines[i]:
                i += 1; break
            i += 1
        continue
    if "pvals = ''" in lines[i]:
        while i < len(lines):
            if 'st.markdown' in lines[i] and 'pvals' in lines[i]:
                i += 1; break
            i += 1
        continue
    out.append(lines[i])
    i += 1
open('app.py', 'w', encoding='utf-8').writelines(out)
print(f'OK: {len(lines)-len(out)} lignes supprimees')
