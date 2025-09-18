# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 09:19:45 2024

@author: mokrane
-----------------------------------------------------------------------
​Données typiques pour la réponse du capteur MQ2 au monoxyde de carbone
(CO), basées sur les courbes trouvées dans la fiche technique officielle
------------------------------------------------------------------------
--------------------------------------------------
 Gaz	      Concentration (ppm)          Rs/R0  
  GPL          100                          0.45  
               1000                         0.15  
  ------------------------------------------------             
               
  Methane      100                          0.75
               1000                         0.30
  ------------------------------------------------             
  Hydrogeme    100                          0.60
               1000                         0.20
  -------------------------------------------------
"""
import numpy as np
import matplotlib.pyplot as plt

# Modélisation des réponses Rs/R0 en fonction des concentrations (ppm)
def response_gpl(concentration):
    return 0.45 * (concentration / 100)**-0.1  # Approximation logarithmique pour le GPL

def response_methane(concentration):
    return 0.75 * (concentration / 100)**-0.12  # Approximation logarithmique pour le méthane

def response_hydrogen(concentration):
    return 0.6 * (concentration / 100)**-0.11  # Approximation logarithmique pour l'hydrogène

# Génération de données aléatoires pour les concentrations
np.random.seed(42)  # Reproductibilité
random_concentrations = np.random.uniform(100, 10000, 50)  # Concentrations aléatoires entre 100 et 10000 ppm
print("random_concentrations",random_concentrations)
# Calcul des réponses du capteur pour chaque gaz
gpl_responses = response_gpl(random_concentrations)
methane_responses = response_methane(random_concentrations)
hydrogen_responses = response_hydrogen(random_concentrations)

# Tracé des courbes de réaction
plt.figure(figsize=(10, 6))
plt.xscale('log')
plt.yscale('log')

plt.scatter(random_concentrations, gpl_responses, label='GPL', color='blue', alpha=0.7, marker='o')
plt.scatter(random_concentrations, methane_responses, label='Méthane (CH4)', color='green', alpha=0.7, marker='s')
plt.scatter(random_concentrations, hydrogen_responses, label='Hydrogène (H2)', color='red', alpha=0.7, marker='^')

# Configuration du graphique
plt.title("Réponse simulée du capteur MQ2 pour des concentrations aléatoires", fontsize=14)
plt.xlabel("Concentration (ppm, échelle logarithmique)", fontsize=12)
plt.ylabel("Ratio Rs/R0 (échelle logarithmique)", fontsize=12)
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.legend(fontsize=12)
plt.tight_layout()

# Affichage
plt.show()

