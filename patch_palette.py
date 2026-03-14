p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Marron -> rouge profond / cuivre partout
t = t.replace('#1A1015', '#140810')
t = t.replace('#3A1520', '#2A0A12')
t = t.replace('#8B6914', '#C4922A')
t = t.replace('#FFD699', '#FFD4A0')
t = t.replace('rgba(139,105,20,', 'rgba(196,146,42,')

# Hover plus visible: halo dore plus fort
t = t.replace('box-shadow: 0 6px 20px rgba(196,146,42,0.3)', 'box-shadow: 0 8px 25px rgba(196,146,42,0.5)')
t = t.replace('box-shadow: 0 4px 15px rgba(196,146,42,0.4)', 'box-shadow: 0 6px 20px rgba(196,146,42,0.6)')
t = t.replace('transform: translateY(-3px)', 'transform: translateY(-4px) scale(1.01)')
t = t.replace('transform: scale(1.03)', 'transform: scale(1.05)')

# Menu hover: flash dore visible
t = t.replace('background: rgba(196,146,42,0.15)', 'background: rgba(196,146,42,0.25)')
t = t.replace('background: rgba(204,51,51,0.2)', 'background: rgba(196,146,42,0.3)')

# Sidebar text: creme dore plus lumineux
t = t.replace('#CCBBAA', '#E8D5B5')

f = open(p, 'w', encoding='utf-8')
f.write(t)
f.close()
print('Palette complete OK')
