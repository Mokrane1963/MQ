# -*- coding: utf-8 -*-
"""
Created on Sat Sep 20 14:34:04 2025

@author: mokrane
"""

import streamlit as st
import numpy as np

# Données typiques
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

st.title("Prédiction du rapport Rs/R0 pour différents gaz")

# Choix du gaz
gaz = st.selectbox("Choisissez un gaz :", list(data.keys()))

# Entrée de la concentration
concentration_input = st.number_input(
    "Entrez la concentration (ppm) :", 
    min_value=1, 
    step=1
)

# Récupération des données correspondantes
concs = np.array(data[gaz]["concentrations"])
responses = np.array(data[gaz]["responses"])

# Vérification et interpolation
if concentration_input > 0:
    if concentration_input < concs.min() or concentration_input > concs.max():
        st.warning(f"La concentration entrée est en dehors de la plage ({concs.min()} - {concs.max()} ppm).")
    else:
        predicted_response = np.interp(concentration_input, concs, responses)
        st.success(f"Pour {gaz}, à {concentration_input} ppm, Rs/R0 ≈ **{predicted_response:.3f}**")

# Affichage du tableau de données
st.subheader("Données expérimentales")
st.write("Concentrations (ppm) :", concs.tolist())
st.write("Réponses (Rs/R0) :", responses.tolist())
