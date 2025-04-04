import streamlit as st
import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        text = '\n\n'.join([para.get_text() for para in paragraphs])
        return text
    except requests.exceptions.RequestException as e:
        return f"❌ Error: {e}"

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTMN1nOwWNISnKg-atykOgSP0jQGEBO1oS6aQ&s");
        background-size: cover;
        background-position: center;
    }       
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 10px 20px;
    }
    .stButton > button:hover {
        background-color: #45a049;
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

# Streamlit UI
st.title("🕷️ Web Scraper App 🕸️")
st.write("🔍 Enter a URL to scrape text content:")

url = st.text_input("🌍 Website URL", "https://en.wikipedia.org/wiki/Web_scraping")
if st.button("🚀 Scrape"):
    with st.spinner("⏳ Scraping..."):
        scraped_data = scrape_website(url)
        st.text_area("📜 Scraped Content", scraped_data, height=400)
