# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 22:45:00 2024

@author: mokrane
"""
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Définition des données pour chaque gaz
data ={
"gpl": {
         "concentrations": np.array([200.23, 297.36, 400.92, 499.43, 595.4]),  # en ppm
         "responses": np.array([1.59816, 1.33874, 1.18140, 1.05348, 0.98964])   # Rs/R0
      },
"fumé": {
        "concentrations": np.array([200.23, 297.36, 400.92, 499.43, 595.4]),  # en ppm
        "responses": np.array([3.38386, 2.89427, 2.60789, 2.37446, 2.20745])   # Rs/R0
      },
"co": {      
          "concentrations": np.array([200.23, 297.36, 400.92, 499.43, 595.4]),  # en ppm
          "responses": np.array([5.187, 4.57755, 4.21148, 3.91526, 3.71651])     # Rs/R0
      },
"methane": { 
            "concentrations": np.array([100, 150, 200, 250, 300]),               # en ppm
            "responses": np.array([1.23456, 1.12345, 1.05023, 1.01234, 0.98765])  # Rs/R0
      },
"ethanol": {
         "concentrations": np.array([50, 100, 150, 200, 250]),                # en ppm
         "responses": np.array([2.34567, 2.12345, 2.05678, 2.02345, 1.98765])  # Rs/R0
           },

"ammoniac": {     
           "concentrations": np.array([20, 40, 60, 80, 100]),                   # en ppm
           "responses": np.array([6.54321, 5.43210, 4.56789, 3.43210, 2.98765])  # Rs/R0
            },
"acetylene": {
           "concentrations": np.array([10, 50, 100, 150, 200]),                 # en ppm 
           "responses": np.array([1.78901, 1.56789, 1.34567, 1.23456, 1.12345])  # Rs/R0
             },

"butane": {
            "concentrations": np.array([50, 100, 150, 200, 300]),                # en ppm
            "responses": np.array([2.56789, 2.34567, 2.12345, 2.01234, 1.98765])  # Rs/R0
          },
   
"cetones": {
        "concentrations": np.array([10, 50, 100, 200, 300]),                 # en ppm
        "responses": np.array([4.56789, 4.34567, 4.12345, 3.98765, 3.76543])  # Rs/R0
    
           },

"so2": { 
      "concentrations": np.array([20, 50, 100, 200, 400]),                 # en ppm
      "responses": np.array([3.56789, 3.23456, 3.01234, 2.87654, 2.56789])  # Rs/R0
       }
     
      } 

# Menu interactif pour choisir un gaz
print("Choisissez un gaz parmi les options suivantes :")
for index, gaz in enumerate(data.keys(), start=1):
    print(f"{index}. {gaz.capitalize()}")


choix = input("Entrez votre choix : ").strip().lower()

if choix in data:
    gaz_detecté = data[choix]
    concentrations = gaz_detecté["concentrations"]
    responses = gaz_detecté["responses"]
    
    print(f"Gaz sélectionné : {choix.upper()}")
    print("Concentrations (ppm) :", concentrations)
    print("Réponses (Rs/R0) :", responses)
else:
    print("Erreur : choix non valide.")


#++++++++++++++++++++++++++++++++++
# Ajustement du modèle log-log pour déterminer les paramètres a et b
log_x = np.log10(concentrations)
log_y = np.log10(responses)
coeffs = np.polyfit(log_x, log_y, 1)  # Ajustement linéaire dans l'espace log-log
b = coeffs[0]
log_a = coeffs[1]
a = 10**log_a

# Fonction de prédiction
def predict_response(concentration):
    return a * concentration**b

# Évaluation du modèle
predicted_responses = predict_response(concentrations)
mse = mean_squared_error(responses, predicted_responses)
r2 = r2_score(responses, predicted_responses)

# Visualisation des données et du modèle
plt.figure(figsize=(8, 6))
plt.scatter(concentrations, responses, color="red", label=choix)
plt.plot(concentrations, predicted_responses, color="blue", label="Modèle ajusté")
plt.xscale('log')
plt.yscale('log')
plt.xlabel("Concentration (ppm, échelle logarithmique)", fontsize=12)
plt.ylabel("Rs/R0 (échelle logarithmique)", fontsize=12)
plt.title("Modèle ajusté pour le capteur MQ2", fontsize=14)
equation_text = f"y = {a:.4f} * x^{b:.8f}"
plt.text(0.1, 0.25, equation_text, transform=plt.gca().transAxes, 
     fontsize=12, verticalalignment='top', bbox=dict(boxstyle="round,pad=0.3",
         edgecolor="blue", facecolor="lightgrey"))
R_text = f"R^2 = {r2:.4f}"
plt.text(0.2, 0.3,R_text , transform=plt.gca().transAxes ,
     fontsize=12, verticalalignment='top', bbox=dict(boxstyle="round,pad=0.3",
         edgecolor="blue", facecolor="lightgrey"))
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.legend(fontsize=12)
plt.tight_layout()
plt.show()
print(f"\nModèle ajusté : y = {a:.4f} * x^{b:.8f}")
print(f"Erreur quadratique moyenne (MSE) : {mse:.8f}")
print(f"Coefficient de détermination (R²) : {r2:.8f}")





# Interaction avec l'utilisateur
while True:
    user_input = input("Entrez une concentration en ppm (ou 'q' pour quitter) : ")
    if user_input.lower() == 'q':
        print("Programme terminé.")
        break
    try:
        concentration = float(user_input)
        if concentration <= 0:
            print("Veuillez entrer une valeur positive.")
            continue
        predicted_response = predict_response(concentration)
        print(f"Pour une concentration de {concentration:.2f} ppm, la réponse prédit est Rs/R0 = {predicted_response:.4f}")
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        



      
    


        
        
        