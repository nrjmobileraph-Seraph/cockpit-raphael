# config.py – Tous les paramètres figés du projet Séraphure
# Version finale – 16 mars 2026
# Intègre les décisions de Raphaël sur Q2, Q3, Q4, Q5, Q6, Q7, Q8

import os
from dotenv import load_dotenv

load_dotenv()

# ------------------------------------------------------------
# COCKPIT
# ------------------------------------------------------------
CAPITAL_COCKPIT_INITIAL = 454_000
PASSIF_LATENT = 87_000
CAPITAL_COCKPIT_NET = CAPITAL_COCKPIT_INITIAL - PASSIF_LATENT
RENDEMENT_ANNUEL_COCKPIT = 0.035          # 3.5% net
REVENUS_FIXES_MENSUELS = 620
INFLATION_ANNUELLE = 0.02

# ------------------------------------------------------------
# MODULE SÉRAPHURE
# ------------------------------------------------------------
CAPITAL_MODULE_INITIAL = 35_000
OBJECTIF_REVENU_NET_MENSUEL = 5_000        # cible après PAT
TAUX_IMPOSITION = 0.30
FRACTION_REINVESTISSEMENT = 0.20           # β : part des gains réinvestis après PAT
RENDEMENT_MENSUEL_CIBLE = 0.04              # 4% (scénario réaliste)

COEFF_RISQUE_INITIAL = 1.0
COEFF_RISQUE_BETA = 1.0                      # βγ (à ajuster si besoin)
MATELAS_OBJECTIF_PROPORTION = 0.6            # α : 60% du capital exposé

SEUIL_TRANCHAGE = 0.10                        # -10%
SEUIL_RACHAT_DRAWDOWN = 0.40                  # -40%
SEUIL_RACHAT_PEUR = 0.80                       # indice peur > 80%
LATENCE_RACHAT_HEURES = 48                     # 48h (à réviser ?)
SEUIL_REBOND_REPRISE = 0.10                     # +10%

# ------------------------------------------------------------
# PARAMÈTRES DU GRID TRADING
# ------------------------------------------------------------
FRAIS_TRADING = 0.001                           # 0.1% par transaction
SLIPPAGE_MOYEN = 0.02                           # 2% (décision Q7)
NOMBRE_GRILLES = 50
FOURCHETTE_GRILLE = 0.20
VOLUME_MIN_TRADE = 10

# ------------------------------------------------------------
# INDICE DE PEUR COMPOSITE
# ------------------------------------------------------------
POIDS_VOLATILITE = 0.4
POIDS_SENTIMENT = 0.3
POIDS_FUNDING = 0.3

# ------------------------------------------------------------
# SEUILS DE SACRIFICE (CONTRAT À FROID)
# ------------------------------------------------------------
SEUIL_MATELAS_ALERTE_1 = 0.60
SEUIL_MATELAS_ALERTE_2 = 0.40
SEUIL_MATELAS_ALERTE_3 = 0.25
DUREE_ALERTE_1_JOURS = 15
DUREE_ALERTE_2_JOURS = 30

# ------------------------------------------------------------
# PHASE MOINE (Q8)
# ------------------------------------------------------------
PHASE_MOINE_CAPITAL_MIN = 100_000                # capital minimum pour sortir
PHASE_MOINE_DUREE_MOIS = 24                      # durée minimum
PHASE_MOINE_VALIDATION_HUMAINE = True            # validation manuelle requise

# ------------------------------------------------------------
# CASINO DU CASINO (Q3)
# ------------------------------------------------------------
CASINO_SOURCE = "house_money"                    # uniquement les profits
CASINO_SPOT_RATIO = 0.70                          # 70% en spot pur
CASINO_LEVIER_RATIO = 0.30                        # 30% avec levier
CASINO_LEVIER_MAX = 3                              # levier maximum ×3
CASINO_STOP_LOSS = 0.02                            # stop-loss à -2% sur positions à levier

# ------------------------------------------------------------
# MATELAS – RÉPARTITION MULTI‑PLATEFORME (Q2)
# ------------------------------------------------------------
MATELAS_REPARTITION = [
    {"exchange": "Pionex", "stablecoin": "USDT", "proportion": 0.50},
    {"exchange": "Kraken", "stablecoin": "USDC", "proportion": 0.50},
]

# ------------------------------------------------------------
# FROTTEMENTS / COÛTS (hors impôts) – Q7
# ------------------------------------------------------------
FRICTION = {
    "slippage": 0.02,          # 2%
    "frais_trading": 0.01,      # 1%
    "infrastructure": 0.005,    # 0.5% (VPS, API, etc.)
    "total_hors_impots": 0.035  # 3.5%
}

# ------------------------------------------------------------
# CANAUX D'ALERTES (Q5)
# ------------------------------------------------------------
ALERTES = {
    "email": True,
    "telegram": True,
    "whatsapp": False,          # à activer plus tard si besoin
    "discord": False            # à activer plus tard si besoin
}

# ------------------------------------------------------------
# SOURCES DE DONNÉES (APIs)
# ------------------------------------------------------------
COINGLASS_API_KEY = os.getenv("COINGLASS_API_KEY", "")
GLASSNODE_API_KEY = os.getenv("GLASSNODE_API_KEY", "")
PIONEX_API_KEY = os.getenv("PIONEX_API_KEY", "")
PIONEX_API_SECRET = os.getenv("PIONEX_API_SECRET", "")
KRAKEN_API_KEY = os.getenv("KRAKEN_API_KEY", "")
KRAKEN_API_SECRET = os.getenv("KRAKEN_API_SECRET", "")
COCKPIT_API_URL = os.getenv("COCKPIT_API_URL", "http://localhost:8000")
COCKPIT_API_KEY = os.getenv("COCKPIT_API_KEY", "")

# ------------------------------------------------------------
# SIMULATION
# ------------------------------------------------------------
PERIODE_DEBUT = "2020-01-01"
PERIODE_FIN = "2026-03-16"
NOM_SIMULATIONS_MONTE_CARLO = 1000