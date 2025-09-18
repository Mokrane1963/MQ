# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 19:35:10 2024

@author: mokrane


-----------------------------------------------------------------------
  ​Données typiques pour la réponse du capteur MQ135 au Co2 et NH3 
  basées sur les courbes trouvées dans la fiche technique officielle
------------------------------------------------------------------------
Concentration de CO (ppm     Rs/R0     Concentration de NH(3 (ppm)   Rs/R0 
     10                       6.5                                    3.8
     50                       4.0                                    2.5
     100                      3.0                                    2.0
     200                      2.0                                    1.4
     500                      1.3                                    0.9
     1000                     0,8                                    0.6
    -----------------------------------------------------------------------
      ​Données typiques pour la réponse du capteur MQ135 au Co2 
      basées sur les courbes trouvées dans la fiche technique officielle
    ------------------------------------------------------------------------
  
"""

import numpy as np
import matplotlib.pyplot as plt 
# Modélisation de la réponse Rs/R0 pour les gaz mesurés par le MQ135
def réponse_co2(concentration):
    return 0.6 * ( concentration / 100)**-0.2 # Approximation pour CO2 
def réponse_nh3(concentration) :
    return 0.8 * (concentration / 100)**-0.15 # Approximation pour NH3 
 # Génération de données aléatoires pour les concentrations np.random.seed(42) # Reproductibilité 
random_concentrations = np.random.uniform(100, 10000, 50) # Concentrations aléatoires entre 100 et 10000 ppm
 # Calcul des réponses du capteur pour chaque gaz
co2_réponses = réponse_co2(random_concentrations)
nh3_responses = réponse_nh3(random_concentrations) # Tracé des courbes de réaction 
plt.figure(figsize=(10, 6))
plt.xscale('log')
plt.yscale('log') 
plt.scatter(random_concentrations, co2_réponses, label='Dioxyde de carbone (CO2)', color='green', alpha=0.7, marker='x')
plt.scatter(random_concentrations, nh3_responses, label='Ammoniaque (NH3)', color='orange', alpha=0.7, marker='o') # Configuration du graphique
plt.title("Réponse simulée du capteur MQ135 pour des concentrations aléatoires", fontsize=14)
plt.xlabel("Concentration (ppm, échelle logarithmique)", fontsize=12) 
plt.ylabel("Ratio Rs/R0 (échelle logarithmique)", fontsize=12) 
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.legend(fontsize=12) 
plt.tight_layout()
 # Affichage 
plt.show()