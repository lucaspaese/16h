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
    if hour >= 11:
        st.write("🍽️ C'est déjà midi !")
    else:
        st.write("⏳ Ce n'est pas encore midi.")

if "pause" not in st.session_state:
    st.session_state.pause = False

if st.button("🧘 Je fais une pause"):
    st.session_state.pause = True

if st.session_state.pause:
    st.subheader("🎮 Mini-jeu : devine le nombre")

    if "number_to_guess" not in st.session_state:
        st.session_state.number_to_guess = random.randint(1, 10)

    guess = st.number_input(
        "Devine un nombre entre 1 et 10",
        min_value=1,
        max_value=10,
        step=1
    )

    if st.button("Valider"):
        if guess == st.session_state.number_to_guess:
            st.success("🎉 Bravo ! Tu as gagné 🎉")
            st.session_state.number_to_guess = random.randint(1, 10)
        else:
            st.error("❌ Raté… essaie encore 😉")






