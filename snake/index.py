import streamlit as st
import time
import random

# Streamlit page config
st.set_page_config(page_title="Snake Game 🐍", layout="wide")

# Title and description
st.title("Snake Game 🐍")
st.markdown("Enjoy a fun Snake game with emojis! 🕹️")

# Initialize session state variables
if "snake" not in st.session_state:
    st.session_state.snake = [[5, 5]]  # Snake starting position
    st.session_state.food = [random.randint(0, 9), random.randint(0, 9)]  # Random food position
    st.session_state.direction = "RIGHT"  # Initial direction
    st.session_state.running = False
    st.session_state.last_update = time.time()

grid_size = 10
snake_emoji = "🟩"
food_emoji = "🍎"
empty_emoji = "⬜"

def draw_game():
    """Draw the game grid with snake and food."""
    grid = [[empty_emoji for _ in range(grid_size)] for _ in range(grid_size)]
    
    # Place food
    grid[st.session_state.food[0]][st.session_state.food[1]] = food_emoji
    
    # Place snake
    for segment in st.session_state.snake:
        grid[segment[0]][segment[1]] = snake_emoji
    
    # Display grid
    st.write("\n".join("".join(row) for row in grid))

def update_game():
    """Move the snake and check for collisions."""
    head = st.session_state.snake[-1][:]  # Copy head position
    
    # Move head in the current direction
    if st.session_state.direction == "UP":
        head[0] -= 1
    elif st.session_state.direction == "DOWN":
        head[0] += 1
    elif st.session_state.direction == "LEFT":
        head[1] -= 1
    elif st.session_state.direction == "RIGHT":
        head[1] += 1
    
    # Check for wall collision
    if head[0] < 0 or head[0] >= grid_size or head[1] < 0 or head[1] >= grid_size:
        st.session_state.running = False
        st.error("Game Over! You hit the wall! ❌")
        return
    
    # Check for self-collision
    if head in st.session_state.snake:
        st.session_state.running = False
        st.error("Game Over! You hit yourself! ❌")
        return
    
    # Add new head to snake
    st.session_state.snake.append(head)
    
    # Check for food
    if head == st.session_state.food:
        st.session_state.food = [random.randint(0, 9), random.randint(0, 9)]  # New food position
    else:
        st.session_state.snake.pop(0)  # Remove tail if no food eaten

draw_game()

# Control buttons
col1, col2, col3, col4 = st.columns(4)
if col1.button("⬅️ Left"):
    st.session_state.direction = "LEFT"
if col2.button("⬆️ Up"):
    st.session_state.direction = "UP"
if col3.button("⬇️ Down"):
    st.session_state.direction = "DOWN"
if col4.button("➡️ Right"):
    st.session_state.direction = "RIGHT"

if st.button("Start Game 🎮"):
    st.session_state.running = True

if st.button("Stop Game ⏹️"):
    st.session_state.running = False

# Automatic Game Loop
if st.session_state.running:
    if time.time() - st.session_state.last_update > 0.5:
        update_game()
        st.session_state.last_update = time.time()
        st.rerun()  # Fixed: replaced st.experimental_rerun() with st.rerun()
