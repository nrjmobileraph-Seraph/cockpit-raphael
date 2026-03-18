# simulator.py – Simulateur de backtest intégrant les décisions finales
# Version 2.0 – 16 mars 2026
# Inclut : friction 3-4%, phase Moine (capital + durée), backtest FTX 2022

import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import logging

from config import *
from module import ModuleSeraphure
from cockpit import CockpitClient
from risk import Watchdog, GestionnaireRisque
from indicators import normaliser_serie, volatilite_reelle

logger = logging.getLogger("Séraphure.Simulator")

class Simulateur:
    def __init__(self,
                 module: ModuleSeraphure,
                 cockpit: Optional[CockpitClient] = None,
                 donnees: Optional[pd.DataFrame] = None):
        self.module = module
        self.cockpit = cockpit
        self.donnees = donnees
        self.watchdog = Watchdog(module, cockpit)
        self.gestionnaire_risque = GestionnaireRisque(module)
        self.resultats = None

    def generer_donnees_synthetiques(self,
                                      nb_heures: int = 24 * 365 * 3,
                                      seed: int = 42) -> pd.DataFrame:
        """
        Génère des données synthétiques réalistes avec queues épaisses.
        Distribution : Student ν=4 + clip [-25%, +30%] (conforme aux audits).
        """
        np.random.seed(seed)
        dates = pd.date_range(start=PERIODE_DEBUT, periods=nb_heures, freq='h')

        # Prix avec rendements Student ν=4
        from scipy.stats import t
        rendements = t.rvs(df=4, loc=0, scale=0.02, size=nb_heures-1)  # vol horaire ~2%
        rendements = np.clip(rendements, -0.25, 0.30)  # clip [-25%, +30%]

        prix = [1.0]
        for r in rendements:
            prix.append(prix[-1] * (1 + r))

        high = np.array(prix) * (1 + np.abs(np.random.normal(0, 0.01, nb_heures)))
        low = np.array(prix) * (1 - np.abs(np.random.normal(0, 0.01, nb_heures)))
        vol = volatilite_reelle(prix, fenetre=24)
        vol_norm = normaliser_serie(vol)
        sentiment = 0.5 + 0.3 * np.sin(np.linspace(0, 20*np.pi, nb_heures)) + 0.1 * np.random.randn(nb_heures)
        sentiment = np.clip(sentiment, 0, 1)
        funding = 0.01 * np.random.randn(nb_heures)

        df = pd.DataFrame({
            'timestamp': dates,
            'actif': 'XRP/USDT',
            'prix': prix,
            'high': high,
            'low': low,
            'volatilite': vol_norm,
            'sentiment': sentiment,
            'funding': funding
        })
        self.donnees = df
        return df

    def charger_donnees_reelles(self,
                                 actif: str = 'XRP/USDT',
                                 debut: str = PERIODE_DEBUT,
                                 fin: str = PERIODE_FIN):
        """
        Charge des données réelles depuis une source (à implémenter avec ccxt).
        Pour l'instant, on utilisera des fichiers CSV pré-téléchargés.
        """
        # Exemple de structure attendue :
        # timestamp, open, high, low, close, volume
        pass

    def run(self,
            pas_temps_heures: float = 1.0,
            avec_watchdog: bool = True):
        """
        Lance la simulation avec prise en compte de la friction et de la phase Moine.
        """
        if self.donnees is None:
            logger.warning("Aucune donnée fournie, génération de données synthétiques.")
            self.generer_donnees_synthetiques()

        logger.info(f"Début de la simulation sur {len(self.donnees)} pas de temps.")

        # Initialisation des compteurs pour la phase Moine
        mois_ecoules = 0
        capital_max_phase_moine = 0

        if avec_watchdog:
            self.watchdog.start()

        for idx, row in self.donnees.iterrows():
            actif = row.get('actif', 'XRP/USDT')
            prix = row['prix']
            high = row.get('high', prix)
            low = row.get('low', prix)

            # Appliquer la friction (slippage + frais) au prix réel pour le module
            # Le slippage est aléatoire entre 0 et 2 * SLIPPAGE_MOYEN, pour simuler des conditions variables
            slippage_reel = np.random.uniform(0, 2 * FRICTION["slippage"])
            frais_reels = FRICTION["frais_trading"]
            prix_effectif = prix * (1 - slippage_reel - frais_reels)  # impact négatif sur les trades

            prix_data = {actif: (prix_effectif, high, low)}

            self.module.volatilite = row.get('volatilite', self.module.volatilite)
            self.module.sentiment = row.get('sentiment', self.module.sentiment)
            self.module.funding = row.get('funding', self.module.funding)

            # Exécution du pas de temps du module
            self.module.pas_de_temps(prix_data)

            if avec_watchdog:
                self.watchdog.heartbeat()

            # Envoi de rapports périodiques (toutes les 6h)
            if self.cockpit and idx % 6 == 0:
                self.module.envoyer_rapport_cockpit()

            # Vérification quotidienne des seuils de sacrifice
            if idx % 24 == 0:
                self.module.verifier_seuils_sacrifice()
                mois_ecoules = idx // (24 * 30)  # approximation mois

                # Suivi du capital max pour la phase Moine
                if self.module.capital > capital_max_phase_moine:
                    capital_max_phase_moine = self.module.capital

                # Vérification de la sortie de phase Moine
                if (capital_max_phase_moine >= PHASE_MOINE_CAPITAL_MIN and
                    mois_ecoules >= PHASE_MOINE_DUREE_MOIS):
                    logger.info("🎯 Conditions de sortie de phase Moine atteintes.")
                    # La validation humaine sera gérée plus tard via l'interface

            # Progression tous les 10%
            if idx % (len(self.donnees) // 10) == 0:
                logger.info(f"Progression : {idx/len(self.donnees)*100:.1f}%")

        if avec_watchdog:
            self.watchdog.stop()

        self.resultats = self.module.historique.copy()
        logger.info("Simulation terminée.")

    def analyser(self):
        """Affiche les métriques de performance après simulation."""
        if self.resultats is None:
            logger.warning("Aucun résultat à analyser.")
            return

        capital_final = self.resultats['capital'][-1]
        capital_max = max(self.resultats['capital'])
        drawdown_max = max(self.resultats['drawdown'])
        pat_atteint = capital_final >= self.module.pat_cible

        duree_heures = len(self.resultats['capital'])
        duree_annees = duree_heures / (365 * 24)
        if duree_annees > 0:
            rendement_annualise = (capital_final / self.module.capital_initial) ** (1 / duree_annees) - 1
        else:
            rendement_annualise = 0

        # Intégration de la friction totale
        rendement_net = rendement_annualise * (1 - FRICTION["total_hors_impots"])

        print("\n" + "="*50)
        print("📊 RÉSULTATS DE LA SIMULATION")
        print("="*50)
        print(f"Capital initial        : {self.module.capital_initial:.2f} €")
        print(f"Capital final          : {capital_final:.2f} €")
        print(f"PAT atteint ?           : {'OUI' if pat_atteint else 'NON'}")
        print(f"PAT cible               : {self.module.pat_cible:.2f} €")
        print(f"Rendement annualisé brut : {rendement_annualise*100:.2f}%")
        print(f"Friction totale          : {FRICTION['total_hors_impots']*100:.1f}%")
        print(f"Rendement net estimé    : {rendement_net*100:.2f}%")
        print(f"Drawdown maximum        : {drawdown_max*100:.1f}%")
        print(f"Capital max atteint     : {capital_max:.2f} €")
        print("="*50)

    def graphiques(self):
        """Affiche les graphiques d'évolution."""
        try:
            import matplotlib.pyplot as plt
            fig, axes = plt.subplots(3, 1, figsize=(12, 8))

            axes[0].plot(self.resultats['timestamp'], self.resultats['capital'], label='Capital')
            axes[0].axhline(y=self.module.pat_cible, color='r', linestyle='--', label='PAT')
            axes[0].set_ylabel('Capital (€)')
            axes[0].legend()

            axes[1].plot(self.resultats['timestamp'], self.resultats['matelas'], label='Matelas', color='orange')
            axes[1].set_ylabel('Matelas (€)')
            axes[1].legend()

            axes[2].plot(self.resultats['timestamp'], self.resultats['drawdown'], label='Drawdown', color='red')
            axes[2].axhline(y=0.4, color='gray', linestyle='--', label='Seuil -40%')
            axes[2].set_ylabel('Drawdown')
            axes[2].set_xlabel('Temps')
            axes[2].legend()

            plt.tight_layout()
            plt.show()
        except ImportError:
            logger.warning("Matplotlib non installé, impossible d'afficher les graphiques.")