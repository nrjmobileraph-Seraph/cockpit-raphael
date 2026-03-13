import streamlit as st

# ============================================================
# CONFIGURATION DE LA PAGE
# ============================================================
st.set_page_config(
    page_title="Cockpit Patrimonial — Raphaël",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"   # ou "collapsed" selon votre préférence
)

# ============================================================
# CSS PERSONNALISÉ (NE TOUCHE PAS AU SIDEBAR)
# ============================================================
st.markdown("""
<style>
    /* Arrière-plan général de l'application */
    .stApp {
        background-color: #f0f2f6;
    }

    /* Titres */
    h1, h2, h3 {
        color: #1e3a8a;  /* bleu foncé */
    }

    /* Boutons */
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 0.5rem 1rem;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }

    /* Vous pouvez ajouter d'autres styles ci-dessous */
</style>
""", unsafe_allow_html=True)

# ============================================================
# DÉFINITION DES PAGES (EXEMPLES)
# ============================================================
# Remplacez ces fonctions par votre code métier réel
def page_dashboard():
    st.header("📈 Tableau de bord")
    st.write("Bienvenue sur votre cockpit patrimonial.")
    # Insérez ici vos graphiques, indicateurs, etc.

def page_analyse():
    st.header("🔍 Analyse")
    st.write("Analyse détaillée de votre patrimoine.")
    # Vos calculs et visualisations

def page_rapport():
    st.header("📄 Rapport")
    st.write("Générez vos rapports personnalisés.")
    # Votre code de génération de rapport

# Dictionnaire associant le nom de la page à la fonction
pages = {
    "Tableau de bord": page_dashboard,
    "Analyse": page_analyse,
    "Rapport": page_rapport,
}

# ============================================================
# SIDEBAR (NAVIGATION)
# ============================================================
with st.sidebar:
    st.markdown("## 🚀 COCKPIT RAPHAEL")
    
    # Si vous avez des variables dynamiques (âge, capital), affichez-les ici
    # Exemple (à adapter) :
    # age = st.session_state.get("age", 40)
    # capital = st.session_state.get("capital", 100000)
    # st.markdown(f"**Âge :** {age} | **Capital :** {capital:,.0f} €")
    
    st.markdown("---")
    choix_page = st.radio("Navigation", list(pages.keys()))
    st.markdown("---")
    st.caption("Version 4.3")

# ============================================================
# AFFICHAGE DE LA PAGE SÉLECTIONNÉE
# ============================================================
pages[choix_page]()