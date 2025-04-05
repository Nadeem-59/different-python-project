import streamlit as st
import numpy as np
import random

# Define emojis
MINE = "💣"
FLAG = "🚩"
HIDDEN = "⬜"
NUMBERS = ["", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣"]

# Game settings
GRID_SIZE = 8
MINES_COUNT = 10

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRT_EA-S4PxD4PACkgm-9FoEN6h9f-hVJyvKQ&s");
        background-size: cover;
        background-position: center;
    }       
    .stButton > button {
        background-color: purple;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 10px 20px;
    }
    .stButton > button:hover {
        background-color: sky blue;
    }
    .word-display {
        font-size: 2.5rem;
        letter-spacing: 0.5rem;
        font-family: monospace;
    }
    .game-title {
        color: #2c3e50;
        text-align: center;
        font-size: 3rem;
        margin-bottom: 2rem;
    }
    .category {
        color: purple;
        font-weight: bold;
    }
    .score {
        font-size: 1.2rem;
        color: #2980b9;
    }
    </style>
    """, unsafe_allow_html=True)


# Initialize session state
if 'grid' not in st.session_state:
    st.session_state.grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
    st.session_state.revealed = np.full((GRID_SIZE, GRID_SIZE), False)
    st.session_state.flags = np.full((GRID_SIZE, GRID_SIZE), False)
    st.session_state.game_over = False
    st.session_state.won = False
    
    # Place mines randomly
    mine_positions = random.sample(range(GRID_SIZE * GRID_SIZE), MINES_COUNT)
    for pos in mine_positions:
        row, col = divmod(pos, GRID_SIZE)
        st.session_state.grid[row, col] = -1  # -1 represents a mine
    
    # Calculate numbers around mines
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if st.session_state.grid[row, col] == -1:
                continue
            count = sum(
                (0 <= row + dr < GRID_SIZE and 0 <= col + dc < GRID_SIZE and st.session_state.grid[row + dr, col + dc] == -1)
                for dr in [-1, 0, 1] for dc in [-1, 0, 1]
            )
            st.session_state.grid[row, col] = count

# Reveal function
def reveal(row, col):
    if st.session_state.revealed[row, col] or st.session_state.flags[row, col]:
        return
    
    st.session_state.revealed[row, col] = True
    
    if st.session_state.grid[row, col] == -1:
        st.session_state.game_over = True
        return
    
    if st.session_state.grid[row, col] == 0:
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if 0 <= row + dr < GRID_SIZE and 0 <= col + dc < GRID_SIZE:
                    reveal(row + dr, col + dc)

# Check win condition
def check_win():
    if np.sum((st.session_state.grid != -1) & ~st.session_state.revealed) == 0:
        st.session_state.won = True

# UI layout
st.title("Minesweeper with Emojis")

if st.session_state.game_over:
    st.error("Game Over! You hit a mine! 💣")
    st.session_state.revealed[:, :] = True  # Reveal all cells
elif st.session_state.won:
    st.success("Congratulations! You won! 🎉")

for row in range(GRID_SIZE):
    cols = st.columns(GRID_SIZE)
    for col in range(GRID_SIZE):
        if st.session_state.revealed[row, col]:
            if st.session_state.grid[row, col] == -1:
                cols[col].button(MINE, key=f"{row}-{col}", disabled=True)
            else:
                cols[col].button(NUMBERS[st.session_state.grid[row, col]], key=f"{row}-{col}", disabled=True)
        elif st.session_state.flags[row, col]:
            if cols[col].button(FLAG, key=f"{row}-{col}"):
                st.session_state.flags[row, col] = False
        else:
            if cols[col].button(HIDDEN, key=f"{row}-{col}"):
                reveal(row, col)
                check_win()

# Restart button
if st.button("Restart Game"):
    st.session_state.clear()
    st.rerun()



    #Minesweeper ek puzzle game hai jisme aapko mines (bombs) ko avoid karna hota hai aur safe cells ko reveal karna hota hai.
    #  Streamlit ka use karke hum Python me ek interactive Minesweeper bana rahe hain, jo emojis use karta hai. 
    # Chalo, step by step samajhte hain:
#📌 Game Ka Basic Concept
#Ek Grid Hoti Hai (Jaise 8x8 cells ka ek board).Kuch cells ke neeche bombs (💣) chhupi hoti hain.

#Baaki cells ya toh khali hoti hain ya ek number dikhati hain.Ye number bataata hai ki kitni mines uske aas paas hain.

#Jaise agar kisi cell pe "2️⃣" likha hai, iska matlab uske 8 neighbors me 2 mines hain.

#Aapka Goal → Sab safe cells reveal karna bina kisi mine pe click kiye!

#Agar aap kisi mine pe click kar dete hain, toh game over!

#Agar aap sab safe cells reveal kar dete hain, toh aap jeet jate hain! 🎉

#🏗 Code Kaise Kaam Karta Hai?
#1️⃣ Game Board Create Hota Hai
#Hum 8x8 ka ek grid (numpy array) banate hain.

#Random mines daali jaati hain (10 bombs).

#Jo cells mines nahi hain, unke aas paas kitni mines hain wo count hota hai.

#2️⃣ User Ka Interaction
#Streamlit buttons ka use karke har cell dikhayi jaati hai.Left-click se cell reveal hoti hai.Right-click ya flag button se 🚩 flag lagaya jata hai.

#Agar koi zero waali cell click hoti hai, toh uske aas paas wali safe cells automatically reveal hoti hain.

#3️⃣ Game Over ya JeetAgar mine (💣) pe click hua → Game Over!Agar saare safe cells reveal ho gaye → Jeet gaye! 🎉

