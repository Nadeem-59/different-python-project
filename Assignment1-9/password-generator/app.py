import streamlit as st
import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        return "⚠️ Please select at least one option!"
    
    return "".join(random.choice(characters) for _ in range(length))

# Streamlit UI
st.set_page_config(page_title="Password Generator", page_icon="🔐")
st.title("🔐 Password Generator 🔑")

st.write("Select options to generate a secure password.")

use_letters = st.checkbox("Include Letters", value=True)
use_numbers = st.checkbox("Include Numbers", value=True)
use_symbols = st.checkbox("Include Symbols", value=True)
password_length = st.slider("Password Length", min_value=4, max_value=20, value=8)

generated_password = ""
if st.button("Generate Password"):
    generated_password = generate_password(password_length, use_letters, use_numbers, use_symbols)
    
st.text_area("Generated Password", generated_password, height=70)
