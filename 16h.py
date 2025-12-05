import streamlit as st
from datetime import datetime

st.title("Vérification de l'heure")

now = datetime.now()
hour = now.hour
weekday = now.weekday()   # lundi = 0 ... dimanche = 6

# --- Partie 1 : Vérifier 16h ---
if hour >= 15:
    st.write("🕓 C'est déjà 16 heures !")
else:
    st.write("⏳ Ce n'est pas encore 16 heures.")

st.write("---")

# --- Partie 2 : Vérifier si c'est vendredi ---
if weekday == 4:  # 4 = vendredi
    st.write("🎉 C'est vendredi !")
    
    # Sous-condition : vérifier midi
    if hour >= 12:
        st.write("🍽️ C'est déjà midi !")
    else:
        st.write("⏳ Ce n'est pas encore midi.")




