# -*- coding: utf-8 -*-
"""
Created on Sat Sep 20 14:52:16 2025

@author: mokrane
"""

import streamlit as st
import numpy as np

# Données typiques pour MQ135 (CO2 et NH3)
data = {
    "CO₂ (Dioxyde de carbone)": {
        "concentrations": [10, 50, 100, 200, 500, 1000],
        "responses": [6.5, 4.0, 3.0, 2.0, 1.3, 0.8]
    },
    "NH₃ (Ammoniac)": {
        "concentrations": [10, 50, 100, 200, 500, 1000],
        "responses": [3.8, 2.5, 2.0, 1.4, 0.9, 0.6]
    }
}

st.title("Prédiction du rapport Rs/R0 avec le capteur MQ135")

# Choix du gaz
gaz = st.selectbox("Choisissez un gaz :", list(data.keys()))

# Entrée de la concentration
concentration_input = st.number_input(
    "Entrez la concentration (ppm) :",
    min_value=1,
    step=1
)

# Récupération des données
concs = np.array(data[gaz]["concentrations"])
responses = np.array(data[gaz]["responses"])

# Vérification + interpolation
if concentration_input > 0:
    if concentration_input < concs.min() or concentration_input > concs.max():
        st.warning(f"La concentration entrée est en dehors de la plage ({concs.min()} - {concs.max()} ppm).")
    else:
        predicted_response = np.interp(concentration_input, concs, responses)
        st.success(f"Pour {gaz}, à {concentration_input} ppm, Rs/R0 ≈ **{predicted_response:.3f}**")

# Affichage des données utilisées
st.subheader("Données expérimentales")
st.write("Concentrations (ppm) :", concs.tolist())
st.write("Réponses (Rs/R0) :", responses.tolist())
