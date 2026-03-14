p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()
# Supprimer tout le bloc mobile menu + JS
old = '''    # === NAVIGATION MOBILE + DESKTOP ===
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
new = '''    pages_list = [
        "Tableau de bord","Moteur ARVA (Rente)","Suivi AV x 3 contrats",
        "Scenarios simulateurs","Fiscal & CAF","Declaration impots",
        "LMNP (Location Meublee) & IRL","Jalons & Actions",
        "AAH / CAF / PCH (Allocations)","Inflation","Succession",
        "Mode Senior","Bilan d exportation","BoursoBank","Crypto",
        "Annexe - Reference","Parametres","Saisie capital"]
    with st.sidebar:'''
t = t.replace(old, new)
# Remettre le radio simple
old_radio = '''        page=st.radio("Navigation", pages_list,
            index=pages_list.index(st.session_state.page), key="desk_nav")
        st.session_state.page = page'''
new_radio = '''        page=st.radio("Navigation", pages_list)'''
t = t.replace(old_radio, new_radio)
f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print('Nettoyage mobile - sidebar natif')
import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
