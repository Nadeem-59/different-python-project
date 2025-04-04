import streamlit as st
import json
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Discord Emoji Tracker", page_icon="😀")

st.title("Discord Emoji Tracker 😀")

# Function to load emoji data
def load_emoji_data():
    try:
        with open('emoji_data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Load the data
emoji_data = load_emoji_data()

# Display statistics
st.header("📊 Statistics")
total_reactions = sum(len(reactions) for reactions in emoji_data.values())
st.metric("Total Emoji Reactions", total_reactions)
st.metric("Total Messages with Reactions", len(emoji_data))

# Display emoji reactions
st.header("😀 Recent Emoji Reactions")

if emoji_data:
    # Create a list of all reactions
    all_reactions = []
    for message_id, reactions in emoji_data.items():
        for reaction in reactions:
            all_reactions.append({
                'Message ID': message_id,
                'Emoji': reaction['emoji'],
                'User': reaction['user'],
                'Timestamp': reaction['timestamp']
            })
    
    # Convert to DataFrame
    df = pd.DataFrame(all_reactions)
    
    # Sort by timestamp
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df = df.sort_values('Timestamp', ascending=False)
    
    # Display the data
    st.dataframe(df)
else:
    st.info("No emoji reactions recorded yet!")

# Add auto-refresh
if st.button("🔄 Refresh Data"):
    st.rerun() 