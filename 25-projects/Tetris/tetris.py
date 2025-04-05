import streamlit as st
import random

# Grid settings (even smaller)
ROWS, COLS = 10, 5

# Shapes and colors (shorter shapes)
SHAPES = [
    [[[1, 1, 1]]],
    [[[1, 1], [1, 1]]],
    [[[0, 1, 0], [1, 1, 1]]],
    [[[1, 0], [1, 1], [1, 0]]],
    [[[0, 1], [1, 1], [0, 1]]]
]

COLORS = ["cyan", "orange", "blue", "yellow", "green"]

EMOJI_MAP = {
    "cyan": "🟦",
    "orange": "🟧",
    "blue": "🔵",
    "yellow": "🟨",
    "green": "🟩",
    "purple": "🟪",
    "red": "🟥",
    "black": "⬛"
}

def create_grid(locked):
    grid = [["black" for _ in range(COLS)] for _ in range(ROWS)]
    for (x, y), color in locked.items():
        if 0 <= y < ROWS and 0 <= x < COLS:
            grid[y][x] = color
    return grid

class Piece:
    def __init__(self, x, y, shape, color):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        self.rotation = 0

def rotate_shape(shape, rotation):
    shape = shape[0]  # Extract inner shape list
    for _ in range(rotation % 4):
        shape = [list(row) for row in zip(*shape[::-1])]
    return shape

def convert_shape_format(piece):
    positions = []
    rotated_shape = rotate_shape(piece.shape, piece.rotation)
    for i, line in enumerate(rotated_shape):
        for j, column in enumerate(line):
            if column == 1:
                positions.append((piece.x + j, piece.y + i))
    return positions

def valid_space(piece, grid):
    accepted = [(j, i) for i in range(ROWS) for j in range(COLS) if grid[i][j] == "black"]
    formatted = convert_shape_format(piece)
    for pos in formatted:
        if pos not in accepted and pos[1] >= 0:
            return False
    return True

def clear_rows(grid, locked):
    cleared = 0
    for i in range(ROWS-1, -1, -1):
        if "black" not in grid[i]:
            cleared += 1
            for j in range(COLS):
                del locked[(j, i)]
    if cleared > 0:
        new_locked = {}
        for (x, y), color in locked.items():
            shift = sum(1 for i in range(y + 1, y + 1 + cleared) if all((j, i) not in locked for j in range(COLS)))
            new_locked[(x, y + shift)] = color
        return new_locked, cleared
    return locked, 0

def get_shape():
    shape = random.choice(SHAPES)
    color = random.choice(COLORS)
    return Piece(2, 0, shape, color)

# --- Streamlit UI ---
st.set_page_config(page_title="Tetris", layout="centered")
st.title("🎮 Tetris in Streamlit")

def init_game():
    if "locked" not in st.session_state:
        st.session_state.locked = {}
        st.session_state.current = get_shape()
        st.session_state.next = get_shape()
        st.session_state.grid = create_grid(st.session_state.locked)
        st.session_state.score = 0

init_game()

piece = st.session_state.current
locked = st.session_state.locked

def move(dx, dy):
    piece.x += dx
    piece.y += dy
    if not valid_space(piece, st.session_state.grid):
        piece.x -= dx
        piece.y -= dy

def rotate():
    piece.rotation += 1
    if not valid_space(piece, st.session_state.grid):
        piece.rotation -= 1

def drop():
    piece.y += 1
    if not valid_space(piece, st.session_state.grid):
        piece.y -= 1
        for pos in convert_shape_format(piece):
            locked[pos] = piece.color
        st.session_state.current = st.session_state.next
        st.session_state.next = get_shape()
        st.session_state.locked, cleared = clear_rows(st.session_state.grid, locked)
        st.session_state.score += cleared * 10

    st.session_state.grid = create_grid(st.session_state.locked)

def draw_grid():
    grid = create_grid(locked)
    for (x, y) in convert_shape_format(piece):
        if 0 <= y < ROWS and 0 <= x < COLS:
            grid[y][x] = piece.color
    st.session_state.grid = grid
    for row in grid:
        st.write("".join([EMOJI_MAP[color] for color in row]))

draw_grid()

col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("⬅️ Left"):
        move(-1, 0)
with col2:
    if st.button("🔁 Rotate"):
        rotate()
with col3:
    if st.button("➡️ Right"):
        move(1, 0)
with col4:
    if st.button("⬇️ Down"):
        drop()

st.subheader(f"Score: {st.session_state.score}")

if st.button("🔄 Restart Game"):
    st.session_state.clear()
    st.experimental_rerun()

# Check for loss
for x, y in locked:
    if y < 1:
        st.error("Game Over! 🎮")
        st.session_state.clear()



 # Custom CSS
st.markdown("""
    <style>
    .stApp {
        background-image: url("data:image/jpeg;base64,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");
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
       
