# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 21:24:30 2024

@author: mokrane
"""

import matplotlib.pyplot as plt


# Données typiques (Concentration en ppm et Rs/R0 pour chaque gaz)
data = {
    "CO (Monoxyde de carbone)": {
        "concentrations": [10, 50, 100, 500, 1000],
        "responses": [1.5, 1.0, 0.6, 0.2, 0.1]
    },
    "GPL (Gaz de pétrole liquéfié)": {
        "concentrations": [200, 400, 800, 1600, 3200],
        "responses": [2.5, 1.5, 1.0, 0.6, 0.3]
    },
    "CH₄ (Méthane)": {
        "concentrations": [200, 400, 800, 1600, 3200],
        "responses": [2.2, 1.4, 0.9, 0.5, 0.25]
    }
}

# Initialisation du graphique
plt.figure(figsize=(10, 7))

# Parcours des gaz et tracé des courbes
for gas, gas_data in data.items():
    concentrations = gas_data["concentrations"]
    responses = gas_data["responses"]
    plt.plot(
        concentrations, responses, marker='o', linestyle='-', label=gas
    )

# Configuration du graphique
plt.xscale('log')
plt.yscale('log')
plt.title("Réponse du capteur MQ9 à différents gaz", fontsize=14)
plt.xlabel("Concentration (ppm, échelle logarithmique)", fontsize=12)
plt.ylabel("Ratio Rs/R0 (échelle logarithmique)", fontsize=12)
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.legend(fontsize=12)
plt.tight_layout()

# Affichage du graphique
plt.show()

