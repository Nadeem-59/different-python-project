import streamlit as st
import time

# Streamlit page config
st.set_page_config(page_title="Pong Game 🏓", layout="wide")

# Title and description
st.title("Pong Game 🏓")
st.markdown("Enjoy a simple Pong game simulation with emojis!")

# Initialize session state variables
if "ball_pos" not in st.session_state:
    st.session_state.ball_pos = [5, 5]
    st.session_state.ball_direction = [1, 1]
    st.session_state.paddle_left_pos = 4
    st.session_state.paddle_right_pos = 4
    st.session_state.running = False

ball = "🏐"
paddle_left = "🟥"
paddle_right = "🟦"
grid_size = 10

def draw_game():
    """Draw the game grid with paddles and ball."""
    grid = [["⬜" for _ in range(grid_size)] for _ in range(grid_size)]
    
    # Place paddles
    grid[st.session_state.paddle_left_pos][0] = paddle_left
    grid[st.session_state.paddle_right_pos][-1] = paddle_right
    
    # Place ball
    grid[st.session_state.ball_pos[0]][st.session_state.ball_pos[1]] = ball
    
    # Display grid
    st.write("\n".join("".join(row) for row in grid))

def update_game():
    """Update ball position and check for collisions."""
    st.session_state.ball_pos[0] += st.session_state.ball_direction[0]
    st.session_state.ball_pos[1] += st.session_state.ball_direction[1]
    
    # Bounce off walls
    if st.session_state.ball_pos[0] == 0 or st.session_state.ball_pos[0] == grid_size - 1:
        st.session_state.ball_direction[0] *= -1
    if st.session_state.ball_pos[1] == 0 or st.session_state.ball_pos[1] == grid_size - 1:
        st.session_state.ball_direction[1] *= -1

draw_game()

if st.button("Start Game 🎮"):
    st.session_state.running = True
    while st.session_state.running:
        time.sleep(0.5)
        update_game()
        st.rerun()

if st.button("Stop Game ⏹️"):
    st.session_state.running = False
