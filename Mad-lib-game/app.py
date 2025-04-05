import streamlit as st

# Function to add background image
def add_bg_from_url(url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{url}");
            background-attachment: fixed;
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def generate_story(name, place, animal, food, action, adjective, profession, object):
    story = f"""
    🌞 On a bright and adventurous morning, {name}, a {adjective} {profession}, set off on a journey to {place}. ✨
    As they wandered through the mystical land, they stumbled upon a {animal} 🦜 happily munching on {food} 🍎.
    Curious and excited, {name} picked up a {object} 🏮 and decided to {action} 🎭 with it.
    Suddenly, a magical portal 🌌 opened, pulling them into a whirlwind of laughter 😂 and surprises! 🎊
    It was truly an unforgettable experience! 🌟
    """
    return story

# Streamlit App
st.title("🎉 Mad Libs - Create a Funny Story! 📝")

# Add Background Image
background_url = "https://getwallpapers.com/wallpaper/full/8/b/c/136088.jpg"
add_bg_from_url(background_url)

# User Inputs (Pre-filled values)
with st.form(key="madlibs_form"):
    name = st.text_input("Enter a name:", value="Maha")
    place = st.text_input("Enter a place:", value="Enchanted Forest")
    animal = st.text_input("Enter an animal:", value="Talking Parrot")
    food = st.text_input("Enter a food item:", value="Golden Apple")
    action = st.text_input("Enter an action (e.g., dance, sing):", value="spun around")
    adjective = st.text_input("Enter an adjective:", value="brave")
    profession = st.text_input("Enter a profession:", value="Treasure Hunter")
    object = st.text_input("Enter an object:", value="Glowing Lantern")
    submit = st.form_submit_button("✨ Generate Story ✨")

if submit:
    if name and place and animal and food and action and adjective and profession and object:
        story = generate_story(name, place, animal, food, action, adjective, profession, object)
        st.subheader("📖 Your Magical Story:")
        st.markdown(story)
    else:
        st.error("🚨 Please fill in all fields! 🛑")
