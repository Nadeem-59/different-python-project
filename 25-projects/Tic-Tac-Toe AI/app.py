import streamlit as st
import numpy as np

# Emojis for display
PLAYER_X = "🎯"
PLAYER_O = "🔵"
EMPTY = "⬜"

def check_winner(board):
    for row in board:
        if all(cell == row[0] and cell != EMPTY for cell in row):
            return row[0]
    for col in range(3):
        if all(board[row][col] == board[0][col] and board[row][col] != EMPTY for row in range(3)):
            return board[0][col]
    if all(board[i][i] == board[0][0] and board[i][i] != EMPTY for i in range(3)) or \
       all(board[i][2 - i] == board[0][2] and board[i][2 - i] != EMPTY for i in range(3)):
        return board[1][1]
    return None

def is_draw(board):
    return all(cell != EMPTY for row in board for cell in row)

def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == PLAYER_X:
        return -1
    elif winner == PLAYER_O:
        return 1
    elif is_draw(board):
        return 0
    
    if is_maximizing:
        best_score = -np.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    score = minimax(board, False)
                    board[i][j] = EMPTY
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = np.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    score = minimax(board, True)
                    board[i][j] = EMPTY
                    best_score = min(score, best_score)
        return best_score

def ai_move(board):
    best_score = -np.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_O
                score = minimax(board, False)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    if best_move:
        board[best_move[0]][best_move[1]] = PLAYER_O
button_style = """
    <style>
    .stApp {
        background-image: url("data:image/jpeg;base64,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");
        background-size: cover;
        background-position: center;
    }
        div.stButton > button {
            background-color:red;
            color: white;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
            transition: 0.3s;
        }
        div.stButton > button:hover {
            background-color:yellow;
        }
    </style>
"""
st.markdown(button_style, unsafe_allow_html=True)



# Streamlit UI
st.title("🎮 Tic-Tac-Toe AI 🎮")
st.write("Play against AI (🔵 starts first)")

if "board" not in st.session_state:
    st.session_state.board = [[EMPTY] * 3 for _ in range(3)]
    st.session_state.turn = PLAYER_X

board = st.session_state.board
turn = st.session_state.turn

cols = st.columns(3)
for i in range(3):
    for j in range(3):
        if cols[j].button(board[i][j], key=f"{i}{j}") and board[i][j] == EMPTY and turn == PLAYER_X:
            board[i][j] = PLAYER_X
            if not check_winner(board) and not is_draw(board):
                ai_move(board)
            st.session_state.turn = PLAYER_X if turn == PLAYER_O else PLAYER_O

winner = check_winner(board)
if winner:
    st.success(f"Winner: {winner} 🎉")
elif is_draw(board):
    st.warning("It's a Draw! 🤝")

if st.button("Restart Game"):
    st.session_state.board = [[EMPTY] * 3 for _ in range(3)]
    st.session_state.turn = PLAYER_X
    st.rerun()
