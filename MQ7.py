# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 19:01:36 2024

@author: mokrane

-----------------------------------------------------------------------
​Données typiques pour la réponse du capteur MQ7 au monoxyde de carbone
(CO), basées sur les courbes trouvées dans la fiche technique officielle
------------------------------------------------------------------------
Concentration de CO (ppm)    Rs/R0
    50                        3.6
    100	                      2.5
    200	                      1.8
    400	                      1.2
    800	                      0.85
    1600	                  0.6
    3200	                  0.4
"""
import numpy as np
import matplotlib.pyplot as plt

# Modélisation de la réponse Rs/R0 pour le monoxyde de carbone (CO) avec le capteur MQ7
def response_co(concentration):
    return 0.85 * (concentration / 100)**-0.2  # Approximation logarithmique pour le CO

# Génération de données aléatoires pour les concentrations
np.random.seed(42)  # Reproductibilité
random_concentrations = np.random.uniform(100, 10000, 50)  # Concentrations aléatoires entre 100 et 10000 ppm
print("Random_concetration",random_concentrations)
# Calcul des réponses du capteur pour le monoxyde de carbone
co_responses = response_co(random_concentrations)
test=float(input("donnez une valeur"))
rep=0.85 * (test / 100)**-0.2 
print("la concentration ",rep)
# Tracé des courbes de réaction
plt.figure(figsize=(10, 6))
plt.xscale('log')
plt.yscale('log')

plt.scatter(random_concentrations, co_responses, label='Monoxyde de carbone (CO)', color='purple', alpha=0.7, marker='o')

# Configuration du graphique
plt.title("Réponse simulée du capteur MQ7 pour des concentrations aléatoires de CO", fontsize=14)
plt.xlabel("Concentration (ppm, échelle logarithmique)", fontsize=12)
plt.ylabel("Ratio Rs/R0 (échelle logarithmique)", fontsize=12)
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.legend(fontsize=12)
plt.tight_layout()
# Affichage
plt.show()
