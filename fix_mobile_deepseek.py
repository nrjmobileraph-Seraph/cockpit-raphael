p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# 1. Supprimer l'ancien CSS mobile qui marchait pas
old_mobile = '''@media (max-width: 768px) {
        [data-testid="stSidebar"] {display: none !important;}
        [data-testid="collapsedControl"] {display: none !important;}
        .main .block-container {padding: 0.5rem !important; max-width: 100% !important;}
    }'''
t = t.replace(old_mobile, '')

# 2. Supprimer l'ancien menu mobile
old_menu = '''    # Menu mobile (visible seulement sur petit ecran)
    st.markdown("""<style>
        @media (min-width: 769px) { .mobile-menu { display: none !important; } }
        @media (max-width: 768px) { .mobile-menu { display: block !important; } }
    </style>""", unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="mobile-menu">', unsafe_allow_html=True)
        page_mobile = st.selectbox("Navigation", [
            "Tableau de bord","Moteur ARVA (Rente)","Suivi AV x 3 contrats",
            "Scenarios simulateurs","Fiscal & CAF","Declaration impots",
            "LMNP (Location Meublee) & IRL","Jalons & Actions",
            "AAH / CAF / PCH (Allocations)","Inflation","Succession",
            "Mode Senior","Bilan d exportation","BoursoBank","Crypto",
            "Annexe - Reference","Parametres","Saisie capital"],
            key="mobile_nav")
        st.markdown('</div>', unsafe_allow_html=True)'''
t = t.replace(old_menu, '')

# Aussi supprimer page = page if
t = t.replace('    page = page if "page" in dir() and page else page_mobile\n', '')

# 3. Trouver le with st.sidebar et ajouter le nouveau systeme avant
old_with = '    with st.sidebar:'
new_system = '''    # === NAVIGATION MOBILE + DESKTOP ===
    pages_list = [
        "Tableau de bord","Moteur ARVA (Rente)","Suivi AV x 3 contrats",
        "Scenarios simulateurs","Fiscal & CAF","Declaration impots",
        "LMNP (Location Meublee) & IRL","Jalons & Actions",
        "AAH / CAF / PCH (Allocations)","Inflation","Succession",
        "Mode Senior","Bilan d exportation","BoursoBank","Crypto",
        "Annexe - Reference","Parametres","Saisie capital"]
    if "page" not in st.session_state:
        st.session_state.page = "Tableau de bord"

    # JS pour cacher sidebar sur mobile
    st.markdown("""
    <script>
    function toggleSidebar() {
        var sb = document.querySelector('[data-testid="stSidebar"]');
        var ctrl = document.querySelector('[data-testid="collapsedControl"]');
        if (!sb) return;
        if (window.innerWidth < 768) {
            sb.style.display = 'none';
            if (ctrl) ctrl.style.display = 'none';
        } else {
            sb.style.display = '';
            if (ctrl) ctrl.style.display = '';
        }
    }
    window.addEventListener('resize', toggleSidebar);
    window.addEventListener('load', toggleSidebar);
    new MutationObserver(toggleSidebar).observe(document.body, {childList:true, subtree:true});
    </script>
    <style>
    @media (max-width: 768px) {
        [data-testid="stSidebar"] {display: none !important;}
        [data-testid="collapsedControl"] {display: none !important;}
    }
    @media (min-width: 769px) {
        .mobile-only {display: none !important;}
    }
    </style>
    """, unsafe_allow_html=True)

    # Menu mobile en haut
    st.markdown('<div class="mobile-only">', unsafe_allow_html=True)
    page_mobile = st.selectbox("Navigation", pages_list,
        index=pages_list.index(st.session_state.page), key="mob_nav")
    st.session_state.page = page_mobile
    st.markdown('</div>', unsafe_allow_html=True)

    with st.sidebar:'''

t = t.replace(old_with, new_system, 1)

# 4. Synchroniser le sidebar radio avec session_state
old_radio = '        page=st.radio("Navigation",['
new_radio = '        page=st.radio("Navigation", pages_list, index=pages_list.index(st.session_state.page), key="desk_nav")\n        st.session_state.page = page\n        # ancien radio remplace\n        if False and st.radio("x",['

# Trop risque, on fait plus simple : juste remplacer la ligne radio
# On garde le radio tel quel et on synchronise apres
old_radio_block = '''        page=st.radio("Navigation",[
            "Tableau de bord",
            "Moteur ARVA (Rente)",
            "Suivi AV x 3 contrats",
            "Scenarios simulateurs",
            "Fiscal & CAF",
            "Declaration impots",
            "LMNP (Location Meublee) & IRL",
            "Jalons & Actions",
            "AAH / CAF / PCH (Allocations)",
            "Inflation",
            "Succession",
            "Mode Senior",
            "Bilan d exportation",
            "BoursoBank",
            "Crypto",
            "Annexe - Reference",
            "Parametres","Saisie capital",
        ])'''

new_radio_block = '''        page=st.radio("Navigation", pages_list,
            index=pages_list.index(st.session_state.page), key="desk_nav")
        st.session_state.page = page'''

t = t.replace(old_radio_block, new_radio_block)

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print('Systeme mobile DeepSeek installe')

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
