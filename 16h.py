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



def sudoku_game():
    st.subheader("🧩 Sudoku (simple)")

    grid = [
        [5, 3, "", "", 7, "", "", "", ""],
        [6, "", "", 1, 9, 5, "", "", ""],
        ["", 9, 8, "", "", "", "", 6, ""],
        [8, "", "", "", 6, "", "", "", 3],
        [4, "", "", 8, "", 3, "", "", 1],
        [7, "", "", "", 2, "", "", "", 6],
        ["", 6, "", "", "", "", 2, 8, ""],
        ["", "", "", 4, 1, 9, "", "", 5],
        ["", "", "", "", 8, "", "", 7, 9],
    ]

    for i in range(9):
        cols = st.columns(9)
        for j in range(9):
            with cols[j]:
                if grid[i][j] == "":
                    st.text_input("", key=f"{i}-{j}", max_chars=1)
                else:
                    st.markdown(f"**{grid[i][j]}**")

import streamlit.components.v1 as components

def worm_game():
    st.subheader("🐍 Worm")

    components.html(
        """
        <canvas id="game" width="400" height="400"></canvas>
        <script>
        const canvas = document.getElementById("game");
        const ctx = canvas.getContext("2d");

        let snake = [{x:200,y:200}];
        let dir = {x:20,y:0};
        let food = {x:100,y:100};

        document.addEventListener("keydown", e => {
            if (e.key === "ArrowUp") dir={x:0,y:-20};
            if (e.key === "ArrowDown") dir={x:0,y:20};
            if (e.key === "ArrowLeft") dir={x:-20,y:0};
            if (e.key === "ArrowRight") dir={x:20,y:0};
        });

        function game(){
            ctx.clearRect(0,0,400,400);
            let head = {x: snake[0].x + dir.x, y: snake[0].y + dir.y};
            snake.unshift(head);

            if (head.x === food.x && head.y === food.y){
                food = {
                    x: Math.floor(Math.random()*20)*20,
                    y: Math.floor(Math.random()*20)*20
                };
            } else {
                snake.pop();
            }

            ctx.fillStyle="green";
            snake.forEach(s => ctx.fillRect(s.x,s.y,20,20));

            ctx.fillStyle="red";
            ctx.fillRect(food.x,food.y,20,20);
        }

        setInterval(game,150);
        </script>
        """,
        height=450
    )


def space_invaders():
    st.subheader("🚀 Space Invaders")

    components.html(
        """
        <canvas id="game" width="400" height="400"></canvas>
        <script>
        const c = document.getElementById("game");
        const ctx = c.getContext("2d");

        let ship = {x:180,y:350};
        let bullet = null;
        let alien = {x:180,y:50};

        document.addEventListener("keydown", e=>{
            if(e.key==="ArrowLeft") ship.x-=20;
            if(e.key==="ArrowRight") ship.x+=20;
            if(e.key===" ") bullet={x:ship.x+10,y:ship.y};
        });

        function game(){
            ctx.clearRect(0,0,400,400);

            ctx.fillStyle="blue";
            ctx.fillRect(ship.x,ship.y,40,20);

            ctx.fillStyle="green";
            ctx.fillRect(alien.x,alien.y,40,20);

            if(bullet){
                bullet.y-=10;
                ctx.fillStyle="red";
                ctx.fillRect(bullet.x,bullet.y,5,10);

                if(bullet.y < alien.y+20){
                    alien.x = Math.random()*360;
                    bullet = null;
                }
            }
        }

        setInterval(game,50);
        </script>
        """,
        height=450
    )


if st.session_state.pause:
    if st.session_state.game == "sudoku_game":
        sudoku_game()
    elif st.session_state.game == "worm_game":
        worm_game()
    elif st.session_state.game == "space_invaders":
        space_invaders()









