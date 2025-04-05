import streamlit as st
import numpy as np

# Emojis for X and O
X_EMOJI = "❌"
O_EMOJI = "⭕"
EMPTY = "➖"

# Initialize game state
if "board" not in st.session_state:
    st.session_state.board = np.full((3, 3), EMPTY)
    st.session_state.current_player = X_EMOJI
    st.session_state.winner = None

# Function to check winner
def check_winner():
    board = st.session_state.board
    for i in range(3):
        if all(board[i, :] == board[i, 0]) and board[i, 0] != EMPTY:
            return board[i, 0]
        if all(board[:, i] == board[0, i]) and board[0, i] != EMPTY:
            return board[0, i]
    if all(board.diagonal() == board[0, 0]) and board[0, 0] != EMPTY:
        return board[0, 0]
    if all(np.fliplr(board).diagonal() == board[0, 2]) and board[0, 2] != EMPTY:
        return board[0, 2]
    if EMPTY not in board:
        return "Draw"
    return None

# Game Title
st.title("🎮 Tic-Tac-Toe with Emojis 😍")

# Display Board
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        with cols[j]:
            if st.button(st.session_state.board[i, j], key=f"{i}{j}"):
                if st.session_state.board[i, j] == EMPTY and not st.session_state.winner:
                    st.session_state.board[i, j] = st.session_state.current_player
                    st.session_state.current_player = O_EMOJI if st.session_state.current_player == X_EMOJI else X_EMOJI
                    st.session_state.winner = check_winner()

# Show Winner
if st.session_state.winner:
    if st.session_state.winner == "Draw":
        st.success("🤝 It's a Draw!")
    else:
        st.success(f"🏆 {st.session_state.winner} Wins!")

# Reset Button
if st.button("🔄 Restart Game"):
    st.session_state.board = np.full((3, 3), EMPTY)
    st.session_state.current_player = X_EMOJI
    st.session_state.winner = None
