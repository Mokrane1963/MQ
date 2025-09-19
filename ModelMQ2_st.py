# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 22:18:30 2025

@author: mokrane
"""

import numpy as np
import streamlit as st



# =======================
# Définition des données
# =======================
data = {
    "gpl": {
        "concentrations": np.array([200.23, 297.36, 400.92, 499.43, 595.4]),  # en ppm
        "responses": np.array([1.59816, 1.33874, 1.18140, 1.05348, 0.98964])   # Rs/R0
    },
    "fumé": {
        "concentrations": np.array([200.23, 297.36, 400.92, 499.43, 595.4]),  
        "responses": np.array([3.38386, 2.89427, 2.60789, 2.37446, 2.20745])   
    },
    "co": {
        "concentrations": np.array([200.23, 297.36, 400.92, 499.43, 595.4]),
        "responses": np.array([5.187, 4.57755, 4.21148, 3.91526, 3.71651])     
    },
    "methane": {
        "concentrations": np.array([100, 150, 200, 250, 300]),
        "responses": np.array([1.23456, 1.12345, 1.05023, 1.01234, 0.98765])
    },
    "ethanol": {
        "concentrations": np.array([50, 100, 150, 200, 250]),
        "responses": np.array([2.34567, 2.12345, 2.05678, 2.02345, 1.98765])
    },
    "ammoniac": {
        "concentrations": np.array([20, 40, 60, 80, 100]),
        "responses": np.array([6.54321, 5.43210, 4.56789, 3.43210, 2.98765])
    },
    "acetylene": {
        "concentrations": np.array([10, 50, 100, 150, 200]),
        "responses": np.array([1.78901, 1.56789, 1.34567, 1.23456, 1.12345])
    },
    "butane": {
        "concentrations": np.array([50, 100, 150, 200, 300]),
        "responses": np.array([2.56789, 2.34567, 2.12345, 2.01234, 1.98765])
    },
    "cetones": {
        "concentrations": np.array([10, 50, 100, 200, 300]),
        "responses": np.array([4.56789, 4.34567, 4.12345, 3.98765, 3.76543])
    },
    "so2": {
        "concentrations": np.array([20, 50, 100, 200, 400]),
        "responses": np.array([3.56789, 3.23456, 3.01234, 2.87654, 2.56789])
    }
}

# =======================
# Interface Streamlit
# =======================
st.title("Modélisation des gaz avec le capteur MQ2")
st.subtitle("Hachemi mokrane")
# Choix du gaz
choix = st.selectbox("Sélectionnez un gaz :", list(data.keys()))

# Récupération des données
gaz_detecte = data[choix]
concentrations = gaz_detecte["concentrations"]
responses = gaz_detecte["responses"]

st.write(f"### Gaz sélectionné : **{choix.upper()}**")
st.write("**Concentrations (ppm) :**", concentrations)
st.write("**Réponses (Rs/R0) :**", responses)

# =======================
# Ajustement du modèle
# =======================
log_x = np.log10(concentrations)
log_y = np.log10(responses)
coeffs = np.polyfit(log_x, log_y, 1)
b = coeffs[0]
log_a = coeffs[1]
a = 10**log_a

# Fonction de prédiction
def predict_response(concentration):
    return a * concentration**b

# Évaluation du modèle
predicted_responses = predict_response(concentrations)




equation_text = f"y = {a:.4f} * x^{b:.8f}"





# =======================
# Affichage des métriques
# =======================
st.write(f"**Modèle ajusté :** y = {a:.4f} * x^{b:.8f}")


# =======================
# Prédiction utilisateur
# =======================
st.subheader("Prédire une nouvelle valeur")

new_concentration = st.number_input("Entrez une concentration en ppm :", min_value=0.0, value=100.0)

if new_concentration > 0:
    predicted_value = predict_response(new_concentration)
    st.success(f"Pour une concentration de {new_concentration:.2f} ppm, la réponse prédite est Rs/R0 = {predicted_value:.4f}")
