# 🎮 Emoji Multiplayer Game

A fun multiplayer game built with Streamlit where players can create or join game rooms and play an emoji-based game together.

## Features

- Create or join game rooms
- Real-time multiplayer gameplay
- Emoji-based guessing game
- Score tracking
- Simple and intuitive interface

## Setup Instructions

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Set up Firebase:
   - Create a Firebase project at https://console.firebase.google.com/
   - Enable Firestore Database
   - Generate a service account key and download the JSON file
   - Rename the downloaded file to `firebase-credentials.json` and place it in the project root

3. Run the application:
```bash
streamlit run app.py
```

## How to Play

1. Enter your name
2. Either create a new game room or join an existing one using the room ID
3. Wait for other players to join
4. The room creator can start the game
5. Players take turns guessing what the emoji represents
6. Scores are updated in real-time

## Requirements

- Python 3.7+
- Streamlit
- Firebase Admin SDK
- Internet connection

## Note

Make sure to keep your Firebase credentials secure and never commit them to version control. 