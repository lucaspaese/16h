import streamlit as st
from datetime import datetime

st.title("Vérification 16 heures")

# Récupérer l'heure actuelle
now = datetime.now()
current_hour = now.hour

if current_hour >= 16:
    st.write("🕓 C'est déjà 16 heures")
else:
    st.write("⏳ Ce n'est pas encore 16 heures")
