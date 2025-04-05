import streamlit as st
import random

# Set page configuration
st.set_page_config(
    page_title="Rock, Paper, Scissors Game",
    page_icon="✂️",
    layout="centered",
)

# Add custom CSS for background image and styling
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIclQXktECPiaGXn-ws2aVRbRwycs6X1JfZQ&s");
        background-size: cover;
        background-position: center;
    }
    .title {
        font-size: 3rem;
        color: white; /* White title text */
        text-align: center;
        animation: fadeIn 2s;
    }
    .result {
        font-size: 2rem;
        color: #00008B; /* Dark blue for result text */
        text-align: center;
        animation: slideIn 1s;
    }
    .choice {
        font-size: 1.5rem;
        color: #00008B; /* Dark blue for choice text */
        text-align: center;
    }
    .stButton button {
        color: white; /* Button text color */
        background-color: #00008B; /* Dark blue button background */
        border-radius: 5px;
        border: 1px solid #00008B;
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

# Title
st.markdown('<h1 class="title">Rock, Paper, Scissors Game 🎮</h1>', unsafe_allow_html=True)

# Initialize session state variables
if "user_choice" not in st.session_state:
    st.session_state.user_choice = None
if "computer_choice" not in st.session_state:
    st.session_state.computer_choice = None
if "result" not in st.session_state:
    st.session_state.result = None

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie! 🤝"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        return "You win! 🎉"
    else:
        return "Computer wins! 🤖"

# User choice buttons
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🪨 Rock"):
        st.session_state.user_choice = "Rock"
with col2:
    if st.button("📄 Paper"):
        st.session_state.user_choice = "Paper"
with col3:
    if st.button("✂️ Scissors"):
        st.session_state.user_choice = "Scissors"

# Computer choice and result
if st.session_state.user_choice:
    st.session_state.computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    st.session_state.result = determine_winner(st.session_state.user_choice, st.session_state.computer_choice)

    # Display choices and result
    st.markdown(f'<p class="choice">Your choice: {st.session_state.user_choice}</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="choice">Computer\'s choice: {st.session_state.computer_choice}</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="result">{st.session_state.result}</p>', unsafe_allow_html=True)

    # Celebration animation if the user wins
    if st.session_state.result == "You win! 🎉":
        st.balloons()

# Reset button
if st.session_state.user_choice:
    if st.button("Play Again 🔄"):
        st.session_state.user_choice = None
        st.session_state.computer_choice = None
        st.session_state.result = None
        st.experimental_rerun()