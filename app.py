"""
COCKPIT PATRIMONIAL — RAPHAËL
Sprint 1+2 : Dashboard corrigé + Suivi AV + Impôts + Surplus automatique
"""

import streamlit as st
import sqlite3
import db_wrapper
import math
from datetime import date, datetime
from pathlib import Path

st.set_page_config(

    page_title="Cockpit Patrimonial — Raphaël",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


if "sidebar_state" not in st.session_state:
    st.session_state.sidebar_state = "expanded"

if st.session_state.sidebar_state == "collapsed":
    st.markdown("""<style>
        section[data-testid="stSidebar"] { display: none !important; }
        div[data-testid="stMainBlockContainer"] > div:first-child div[data-testid="stButton"] button {
            position: fixed !important;
            top: 0.8rem !important;
            left: 1rem !important;
            width: 2.5rem !important;
            height: 2.5rem !important;
            background-color: #1a0a12 !important;
            border: 1px solid #FFD060 !important;
            color: #FFD060 !important;
            padding: 0 !important;
            z-index: 999999 !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            border-radius: 0.5rem !important;
            font-size: 1.2rem !important;
        }
        div[data-testid="stMainBlockContainer"] > div:first-child div[data-testid="stButton"] button:hover {
            background-color: #2A0A12 !important;
            box-shadow: 0 0 8px rgba(255,208,96,0.4) !important;
        }
    </style>""", unsafe_allow_html=True)
    if st.button("\u276F"):
        st.session_state.sidebar_state = "expanded"
        st.rerun()
else:
    st.markdown("""<style>
        section[data-testid="stSidebar"] {
            display: block !important;
            visibility: visible !important;
            transform: translateX(0) !important;
            width: 300px !important;
            min-width: 300px !important;
        }
    </style>""", unsafe_allow_html=True)

    with st.sidebar:
        if st.button("\u276E", key="close_sb"):
            st.session_state.sidebar_state = "collapsed"
            st.rerun()
        st.markdown("""<style>
            div[data-testid="stSidebar"] button[kind="secondary"] {
                background: #1a0a12 !important;
                color: #FFD060 !important;
                border: 2px solid #FFD060 !important;
                border-radius: 8px !important;
                font-weight: bold !important;
            }
        </style>""", unsafe_allow_html=True)
        if st.button("FERMER LE MENU", key="close_sb", use_container_width=True):
            st.session_state.sidebar_open = False
            st.rerun()
        st.markdown("## Cockpit Raphael")
        st.markdown(f"**Age :** {age:.1f} ans")
        st.markdown('<div style="background:#0A2010;border:1px solid #1A6B4B;border-radius:6px;padding:8px 12px;margin:4px 0;text-align:center;"><span style="color:#4DFF99;font-size:11px;font-weight:700;letter-spacing:1px;">PLAN OPERATIONNEL</span><br><span style="color:#BBA888;font-size:10px;">Garanti jusqu&#39;a 92 ans</span></div>', unsafe_allow_html=True)
        st.markdown(f"**Capital :** {C:,.0f} EUR")
        st.markdown(f"**Rail :** {profil['rail_mensuel']:,.0f} EUR/mois")
        mdph80 = profil.get('mdph_80plus', 0)
        st.markdown(f"**MDPH :** {profil['taux_mdph']}%")
        if mdph80:
            st.markdown('<div style="background:#0A2010;border:1px solid #4DFF99;border-radius:6px;padding:6px 10px;text-align:center;"><span style="color:#4DFF99;font-size:10px;font-weight:700;">AAH A VIE</span></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div style="background:#2A1800;border:1px solid #D4A017;border-radius:6px;padding:6px 10px;text-align:center;"><span style="color:#FFD060;font-size:10px;font-weight:700;">AAH STOP 64 ANS</span></div>', unsafe_allow_html=True)
        al=calculer_alertes(profil,cap)
        nr=sum(1 for n,_ in al if n=='rouge')
        no=sum(1 for n,_ in al if n=='orange')
        if nr: st.markdown(f"**{nr} alerte(s) rouge(s)**")
        elif no: st.markdown(f"{no} alertes(s) orange")
        else: st.markdown("Aucune alerte")
        st.markdown("---")
        page=st.radio("Navigation",[
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
        ])
        st.markdown("---")
        st.caption("v4.3 - Mars 2026")
    {
        "Tableau de bord":        lambda: page_dashboard(profil,cap),
        "Moteur ARVA (Rente)":           lambda: page_arva(profil,cap),
        "Suivi AV x 3 contrats": lambda: page_suivi_av(profil,cap),
        "Scenarios simulateurs": lambda: page_simulateur(profil,cap),
        "Fiscal & CAF":          lambda: page_fiscal(profil,cap),
        "Declaration impots":    lambda: page_impots(profil,cap),
        "LMNP (Location Meublee) & IRL":            lambda: page_lmnp(profil,cap),
        "Jalons & Actions":       lambda: page_jalons(profil,cap),
        "AAH / CAF / PCH (Allocations)":       lambda: page_caf_pch(profil,cap),
        "Inflation":              lambda: page_inflation(profil,cap),
        "Succession":             lambda: page_succession(profil,cap),
        "Mode Senior":            lambda: page_senior(profil,cap),
        "Bilan d exportation":    lambda: page_export(profil,cap),
        "BoursoBank":             lambda: page_boursobank(profil,cap),
        "Crypto":                  lambda: page_crypto(profil,cap),
        "Annexe - Reference":      lambda: page_annexe(profil,cap),
        "Parametres":              lambda: page_parametres(profil,cap),
        "Saisie capital":          lambda: page_saisie(profil,cap),
    }[page]()

if __name__=="__main__":
    main()
