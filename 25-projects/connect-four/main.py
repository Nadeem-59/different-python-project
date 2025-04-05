import streamlit as st
import numpy as np

# Streamlit page config
st.set_page_config(page_title="Connect Four 🎲", layout="wide")

# Title and description
st.title("Connect Four 🎲")
st.markdown("Drop your pieces and try to connect four in a row! 🔴🟡")


# Custom CSS
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ3t3X7encNt9NvK8a0lXYVeEOWYqUpDtxXHw&s");
        background-size: cover;
        background-position: center;
    }       
    .stButton > button {
        background-color:purple;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 10px 20px;
    }
    .stButton > button:hover {
        background-color:green;
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


# Initialize game variables
ROWS, COLS = 6, 7
if "board" not in st.session_state:
    st.session_state.board = np.zeros((ROWS, COLS), dtype=int)
    st.session_state.current_player = 1  # Player 1 starts (🔴)
    st.session_state.game_over = False

# Emojis for board representation
empty_emoji = "⚪"
player_emojis = {1: "🔴", 2: "🟡"}

def drop_piece(col):
    """Drop a piece into the selected column."""
    if st.session_state.game_over:
        return
    
    for row in range(ROWS - 1, -1, -1):  # Start from bottom row
        if st.session_state.board[row, col] == 0:
            st.session_state.board[row, col] = st.session_state.current_player
            if check_winner(row, col, st.session_state.current_player):
                st.session_state.game_over = True
                st.success(f"Player {st.session_state.current_player} ({player_emojis[st.session_state.current_player]}) wins! 🎉")
            else:
                st.session_state.current_player = 3 - st.session_state.current_player  # Switch player
            break

def check_winner(row, col, player):
    """Check if the last move wins the game."""
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # Vertical, Horizontal, Diagonal
    for dr, dc in directions:
        count = 1
        for d in [-1, 1]:
            r, c = row + dr * d, col + dc * d
            while 0 <= r < ROWS and 0 <= c < COLS and st.session_state.board[r, c] == player:
                count += 1
                r += dr * d
                c += dc * d
                if count >= 4:
                    return True
    return False

def draw_board():
    """Render the Connect Four board in Streamlit."""
    board_display = "\n".join("".join(player_emojis.get(cell, empty_emoji) for cell in row) for row in st.session_state.board)
    st.text(board_display)

draw_board()

# Column selection buttons
cols = st.columns(COLS)
for i, col in enumerate(cols):
    if col.button(f"⬇️ Column {i+1}"):
        drop_piece(i)
        st.rerun()

if st.button("Restart 🔄"):
    st.session_state.board = np.zeros((ROWS, COLS), dtype=int)
    st.session_state.current_player = 1
    st.session_state.game_over = False
    st.rerun()
