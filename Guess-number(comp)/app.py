import streamlit as st
import time

# Configure the Streamlit page
st.set_page_config(
    page_title="Guess the Number Game",
    page_icon="🎮",
    layout="centered",
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://files.oaiusercontent.com/file-WPCUjmcztYoADn6RapnMQy?se=2025-03-24T11%3A57%3A45Z&sp=r&sv=2024-08-04&sr=b&rscc=max-age%3D604800%2C%20immutable%2C%20private&rscd=attachment%3B%20filename%3Dd3f9827d-cab8-4dfb-9bae-d950bb4084c5.webp&sig=Z8X%2Bf%2BCRGbug9HxRQmXQcu813u8e1icSos/AcWs7NVA%3D");
        background-size: cover;
        background-position: center;
    }
    .title {
        font-size: 2.8rem;
        color: crimson;
        text-align: center;
        animation: fadeIn 1.5s;
    }
    .feedback {
        font-size: 1.4rem;
        color: darkred;
        text-align: center;
        animation: slideIn 1s;
    }
    .attempts {
        font-size: 1.1rem;
        color: maroon;
        text-align: center;
        animation: fadeIn 2s;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @keyframes slideIn {
        from { transform: translateY(-20px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and instructions
st.markdown('<h1 class="title">Guess the Number Game 🎮</h1>', unsafe_allow_html=True)
st.write("Think of a number between 1 and 70, and I'll guess it!")

# Initialize session state variables
game_state = st.session_state
if "low" not in game_state:
    game_state.low = 1
if "high" not in game_state:
    game_state.high = 100
if "attempts" not in game_state:
    game_state.attempts = 0
if "guess" not in game_state:
    game_state.guess = None
if "game_over" not in game_state:
    game_state.game_over = False

# Function to generate a new guess
def generate_guess():
    game_state.guess = (game_state.low + game_state.high) // 2
    game_state.attempts += 1

# Function to restart the game
def restart_game():
    game_state.low, game_state.high = 1, 100
    game_state.attempts, game_state.guess = 0, None
    game_state.game_over = False

# Generate the first guess if none exists
if game_state.guess is None:
    generate_guess()

# Display the current guess
if not game_state.game_over:
    st.markdown(f'<p class="feedback">Is your number <strong>{game_state.guess}</strong>?</p>', unsafe_allow_html=True)
    
    # User response buttons
    left, center, right = st.columns(3)
    with left:
        if st.button("Higher ⬆️"):
            game_state.low = game_state.guess + 1
            generate_guess()
    with center:
        if st.button("Lower ⬇️"):
            game_state.high = game_state.guess - 1
            generate_guess()
    with right:
        if st.button("Correct 🎉"):
            game_state.game_over = True
            st.balloons()

# Display success message when game ends
if game_state.game_over:
    st.markdown(f'<p class="feedback">🎉 Hooray! I guessed it in <strong>{game_state.attempts}</strong> attempts!</p>', unsafe_allow_html=True)
    if st.button("Play Again 🔄"):
        restart_game()

# Show attempts count
st.markdown(f'<p class="attempts">Attempts: {game_state.attempts}</p>', unsafe_allow_html=True)
