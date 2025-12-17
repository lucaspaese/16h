import streamlit as st
from datetime import datetime
import random
import time

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

st.write("---")

# ===============================
#        PAUSE + MINI-JEU
# ===============================

if "pause" not in st.session_state:
    st.session_state.pause = False

if st.button("🧘 Je fais une pause"):
    st.session_state.pause = True

if "snake" not in st.session_state:
    st.session_state.snake = [(5, 5), (5, 4), (5, 3)]
    st.session_state.direction = "RIGHT"
    st.session_state.food = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
    st.session_state.game_over = False

grid_size = 20
st.title("🐍 Snake Game")


# Controls
col1, col2, col3 = st.columns(3)
with col2:
    if st.button("⬆️"):
        st.session_state.direction = "UP"
col4, col5, col6 = st.columns(3)
with col4:
    if st.button("⬅️"):
        st.session_state.direction = "LEFT"
with col6:
    if st.button("➡️"):
        st.session_state.direction = "RIGHT"
col7, col8, col9 = st.columns(3)
with col8:
    if st.button("⬇️"):
        st.session_state.direction = "DOWN"


# Move snake
if not st.session_state.game_over:
    head_x, head_y = st.session_state.snake[0]


    if st.session_state.direction == "UP":
        head_x -= 1
    elif st.session_state.direction == "DOWN":
        head_x += 1
    elif st.session_state.direction == "LEFT":
        head_y -= 1
    elif st.session_state.direction == "RIGHT":
        head_y += 1


    new_head = (head_x, head_y)
    
    
    # Collision
    if (head_x < 0 or head_x >= grid_size or head_y < 0 or head_y >= grid_size or new_head in st.session_state.snake):
        st.session_state.game_over = True
    else:
        st.session_state.snake.insert(0, new_head)


    if new_head == st.session_state.food:
        st.session_state.food = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
    else:
        st.session_state.snake.pop()


# Draw grid
grid = [["⬜" for _ in range(grid_size)] for _ in range(grid_size)]
for x, y in st.session_state.snake:
    grid[x][y] = "🟩"
fx, fy = st.session_state.food
grid[fx][fy] = "🍎"


st.markdown("<br>".join(["".join(row) for row in grid]), unsafe_allow_html=True)


if st.session_state.game_over:
    st.error("💀 Game Over")
if st.button("Restart"):
    for k in ["snake", "direction", "food", "game_over"]:
        del st.session_state[k]
    st.experimental_rerun()


# Auto refresh
time.sleep(0.3)
st.experimental_rerun()



