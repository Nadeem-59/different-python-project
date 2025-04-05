import streamlit as st

# Set page configuration
st.set_page_config(page_title="🚀 Quick Python Website", page_icon="🌍", layout="wide")

# Custom styling
st.markdown("""
    <style>
        body {
            background-color: #f5f5f5;
            color: #333;
            font-family: 'Arial', sans-serif;
        }
        .main {
            background: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
            margin: 20px auto;
            max-width: 900px;
        }
        h1, h2, h3 {
            color: #6a1b9a;
            text-align: center;
        }
        .stButton>button {
            background: #6a1b9a;
            color: white;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 10px;
            border: none;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background: #4a148c;
            transform: scale(1.05);
        }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.markdown("<h1>🌟 Build a Python Website in 15 Minutes! ⏳</h1>", unsafe_allow_html=True)
st.write("🚀 Welcome to this quick guide on creating a Python-powered web app using Streamlit!")

# Sidebar
with st.sidebar:
    st.markdown("<h2>🔧 Features</h2>", unsafe_allow_html=True)
    st.write("✔️ Easy-to-use interface")
    st.write("✔️ No HTML/CSS needed")
    st.write("✔️ Fast deployment")
    st.write("✔️ Interactive UI with Streamlit")

# Main section
st.markdown("<h2>🛠️ Let's Get Started!</h2>", unsafe_allow_html=True)
st.write("Follow these simple steps to build your own web app!")

st.markdown("**Step 1:** Install Streamlit 📦")
st.code("pip install streamlit", language="bash")

st.markdown("**Step 2:** Create a Python file and write your first app 📝")
st.code("""
import streamlit as st

st.title("Hello, Streamlit! 🚀")
st.write("This is your first web app with Python!")
""", language="python")

st.markdown("**Step 3:** Run your app 🚀")
st.code("streamlit run your_script.py", language="bash")

st.markdown("**Step 4:** Add more interactivity 🖱️")
st.code("""
name = st.text_input("Enter your name: ✍️")
st.write(f"Hello, {name}! 👋")
""", language="python")

st.markdown("**Step 5:** Deploy your app 🌍")
st.write("Use Streamlit Sharing or platforms like Heroku, AWS, or Google Cloud to share your app!")

# Footer
st.markdown("""
    <div style='text-align: center; margin-top: 30px;'>
        🚀 Happy Coding! 🎉 | Made by MUSTABSHIRA KHALID
    </div>
""", unsafe_allow_html=True)
