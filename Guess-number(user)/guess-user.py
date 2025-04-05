import streamlit as st
import random

# Set page configuration
st.set_page_config(
    page_title="Guess the Number Game (User)",
    page_icon="🎮",
    layout="centered",
)

# Add custom CSS for background image and red text
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("data:image/jpeg;base64,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");
        background-size: cover;
        background-position: center;
    }
    .title {
        font-size: 3rem;
        color: red; /* Red text */
        text-align: center;
        animation: fadeIn 2s;
    }
    .feedback {
        font-size: 1.5rem;
        color: red; /* Red text */
        text-align: center;
        animation: slideIn 1s;
    }
    .attempts {
        font-size: 1.2rem;
        color: red; /* Red text */
        text-align: center;
        animation: fadeIn 2s;
    }
    .input-label {
        font-size: 1.2rem;
        color: red; /* Red text */
        text-align: center;
    }
    .stNumberInput label {
        color: red; /* Red text for number input label */
    }
    .stButton button {
        color: red; /* Button text color */
        background-color: white; /* Button background color */
        border-radius: 5px;
        border: 1px solid red;
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
st.markdown('<p class="input-label">I\'ve picked a number between 1 and 100. Can you guess it?</p>', unsafe_allow_html=True)

# Initialize session state variables
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)  # Random number between 1 and 100
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "guess" not in st.session_state:
    st.session_state.guess = None
if "game_over" not in st.session_state:
    st.session_state.game_over = False

# Function to reset the game
def reset_game():
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.guess = None
    st.session_state.game_over = False

# User input for guessing the number
guess = st.number_input("Enter your guess (1-100):", min_value=1, max_value=100, step=1)

# Check the guess
if st.button("Submit Guess"):
    st.session_state.attempts += 1
    if guess < st.session_state.number:
        st.markdown('<p class="feedback">Too low! Try a higher number. ⬆️</p>', unsafe_allow_html=True)
    elif guess > st.session_state.number:
        st.markdown('<p class="feedback">Too high! Try a lower number. ⬇️</p>', unsafe_allow_html=True)
    else:
        st.session_state.game_over = True
        st.balloons()  # Celebration animation
        st.markdown(f'<p class="feedback">🎉 Congratulations! You guessed the number in {st.session_state.attempts} attempts!</p>', unsafe_allow_html=True)

# Display the number of attempts
st.markdown(f'<p class="attempts">Attempts: {st.session_state.attempts}</p>', unsafe_allow_html=True)

# Reset button
if st.session_state.game_over:
    if st.button("Play Again 🔄"):
        reset_game()
