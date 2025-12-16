import streamlit as st
from datetime import datetime
import random

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

if "game" not in st.session_state:
    st.session_state.game = None

if st.button("🧘 Je fais une pause"):
    st.session_state.pause = True
    st.session_state.game = random.choice(["number", "rps", "math"])

# ===============================
#           JEUX
# ===============================

if st.session_state.pause:

    # -------- Jeu 1 : Deviner le nombre --------
    if st.session_state.game == "number":
        st.subheader("🎯 Devine le nombre")

        if "secret" not in st.session_state:
            st.session_state.secret = random.randint(1, 10)

        guess = st.number_input(
            "Choisis un nombre entre 1 et 10",
            1, 10, step=1
        )

        if st.button("Valider"):
            if guess == st.session_state.secret:
                st.success("🎉 Bravo !")
                st.session_state.secret = random.randint(1, 10)
            else:
                st.error("❌ Raté, réessaie 😉")

    # -------- Jeu 2 : Pierre Feuille Ciseaux --------
    elif st.session_state.game == "rps":
        st.subheader("✊✋✌ Pierre – Feuille – Ciseaux")

        choices = ["Pierre", "Feuille", "Ciseaux"]
        player = st.radio("Ton choix :", choices)

        if st.button("Jouer"):
            computer = random.choice(choices)
            st.write(f"🤖 L'ordinateur a choisi **{computer}**")

            if player == computer:
                st.info("🤝 Égalité")
            elif (
                (player == "Pierre" and computer == "Ciseaux") or
                (player == "Feuille" and computer == "Pierre") or
                (player == "Ciseaux" and computer == "Feuille")
            ):
                st.success("🎉 Tu gagnes !")
            else:
                st.error("❌ Tu perds !")

    # -------- Jeu 3 : Calcul rapide --------
    elif st.session_state.game == "math":
        st.subheader("🧠 Calcul rapide")

        if "a" not in st.session_state:
            st.session_state.a = random.randint(1, 10)
            st.session_state.b = random.randint(1, 10)

        answer = st.number_input(
            f"Combien font {st.session_state.a} + {st.session_state.b} ?",
            step=1
        )

        if st.button("Valider"):
            if answer == st.session_state.a + st.session_state.b:
                st.success("✅ Bonne réponse !")
                st.session_state.a = random.randint(1, 10)
                st.session_state.b = random.randint(1, 10)
            else:
                st.error("❌ Mauvaise réponse")








