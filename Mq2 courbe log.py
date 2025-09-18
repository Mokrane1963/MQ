# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 11:11:40 2025

@author: mokrane
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Données d'exemple
x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 2.5, 1.11, 0.625, 0.4])

# Transformation logarithmique
X = np.log(x).reshape(-1, 1)  # X = ln(x)
Y = np.log(y)                 # Y = ln(y)

# Ajuster un modèle linéaire
model = LinearRegression()
model.fit(X, Y)

# Extraire les paramètres
A = model.coef_[0]  # Coefficient angulaire (A = -b)
B = model.intercept_  # Ordonnée à l'origine (B = ln(a))

# Retrouver les paramètres originaux
b = -A
a = np.exp(B)

print(f"Paramètre a : {a:.4f}")
print(f"Paramètre b : {b:.4f}")

# Prédictions
y_pred = np.exp(model.predict(X))  # Revenir à l'échelle originale

# Tracer les données et la courbe ajustée
plt.scatter(x, y, color='blue', label='Données réelles')
plt.plot(x, y_pred, color='red', label='Courbe ajustée')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Ajustement de y = a * x^(-b)')
plt.legend()
plt.show()