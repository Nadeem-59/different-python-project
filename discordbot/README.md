# Discord Emoji Tracker Bot with Streamlit Interface

This project consists of a Discord bot that tracks emoji reactions and a Streamlit interface to visualize them.

## Features
- Tracks emoji reactions on Discord messages
- Stores reaction data with user information and timestamps
- Beautiful Streamlit interface to view reaction statistics
- Real-time updates of emoji reactions

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the project root and add your Discord bot token:
```
DISCORD_TOKEN=your_discord_bot_token_here
```

3. Run the Discord bot:
```bash
python bot.py
```

4. In a separate terminal, run the Streamlit interface:
```bash
streamlit run app.py
```

## Usage

### Discord Bot Commands
- `!emojis` - Shows all emoji reactions for the current message

### Streamlit Interface
- View total emoji reactions and messages with reactions
- See detailed information about each reaction
- Refresh data in real-time using the refresh button

## Requirements
- Python 3.8+
- discord.py
- streamlit
- python-dotenv
- pandas 