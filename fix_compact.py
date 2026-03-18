import shutil
shutil.copy2("app.py", "app.py.bak3")
with open("app.py", "r", encoding="utf-8") as f:
    content = f.read()
old1 = 'flex:1;min-width:100px;max-width:160px;background:#0A1E12;border:1px solid #1A6B4B;border-radius:8px;padding:8px 6px;text-align:center;'
new1 = 'flex:1 1 calc(16% - 8px);min-width:85px;max-width:120px;background:#0A1E12;border:1px solid #1A6B4B;border-radius:8px;padding:6px 4px;text-align:center;'
content = content.replace(old1, new1)
old2 = 'font-size:9px;text-transform:uppercase;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">{_n}</div><div style="color:#4DFF99;font-size:18px;font-weight:900;margin-top:4px;">{_v:,.0f} EUR'
new2 = 'font-size:8px;text-transform:uppercase;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">{_n}</div><div style="color:#4DFF99;font-size:14px;font-weight:900;margin-top:2px;">{_v:,.0f}'
content = content.replace(old2, new2)
old3 = 'border:1px solid #1A6B4B;border-radius:10px;padding:10px;display:flex;gap:6px'
new3 = 'border:1px solid #1A6B4B;border-radius:10px;padding:8px;display:flex;gap:5px'
content = content.replace(old3, new3)
with open("app.py", "w", encoding="utf-8") as f:
    f.write(content)
print("OK - Revenus compactes comme les poches capital")
