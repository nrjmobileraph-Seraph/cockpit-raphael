src = open(r'C:\Users\BoulePiou\cockpit-raphael\app.py', encoding='utf-8').read()

# Ajouter padding-top au contenu sidebar pour dégager le bouton
src = src.replace(
    'section[data-testid="stSidebar"]{{display:block!important;visibility:visible!important;transform:translateX(0)!important;}}',
    'section[data-testid="stSidebar"]{{display:block!important;visibility:visible!important;transform:translateX(0)!important;}} section[data-testid="stSidebarUserContent"]{{padding-top:4rem!important;}}'
)

open(r'C:\Users\BoulePiou\cockpit-raphael\app.py', 'w', encoding='utf-8').write(src)
print("OK")
