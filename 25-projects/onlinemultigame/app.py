import streamlit as st
import random
import time

# Game emojis
EMOJIS = ["🎮", "🎲", "🎯", "🎨", "🎭", "🎪", "🎫", "🎬", "🎤", "🎧", "🎼", "🎹", "🎷", "🎺", "🎸", "🎻"]

# Initialize session state
if 'game_data' not in st.session_state:
    st.session_state.game_data = {
        'players': [],
        'scores': {},
        'current_round': 1,
        'status': 'waiting',
        'current_emoji': None,
        'guesses': {}
    }

if 'player_name' not in st.session_state:
    st.session_state.player_name = ""

if 'room_id' not in st.session_state:
    st.session_state.room_id = ""

def create_game_room():
    room_id = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))
    st.session_state.room_id = room_id
    st.session_state.game_data = {
        'players': [st.session_state.player_name],
        'scores': {st.session_state.player_name: 0},
        'current_round': 1,
        'status': 'waiting',
        'current_emoji': None,
        'guesses': {st.session_state.player_name: None}
    }
    return room_id

def join_game_room(room_id, player_name):
    if room_id == st.session_state.room_id:
        if player_name not in st.session_state.game_data['players']:
            st.session_state.game_data['players'].append(player_name)
            st.session_state.game_data['scores'][player_name] = 0
            st.session_state.game_data['guesses'][player_name] = None
        return True
    return False

def main():
    st.title("🎮 Emoji Multiplayer Game 🎮")
    
    # Player name input
    player_name = st.text_input("Enter your name:", value=st.session_state.player_name)
    if player_name:
        st.session_state.player_name = player_name
    
    # Game room options
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Create New Game Room"):
            if not player_name:
                st.error("Please enter your name first!")
            else:
                room_id = create_game_room()
                st.success(f"Game room created! Room ID: {room_id}")
                st.info("Share this room ID with your friends to play together!")
    
    with col2:
        room_id_input = st.text_input("Enter Room ID to join:")
        if st.button("Join Game Room") and room_id_input:
            if not player_name:
                st.error("Please enter your name first!")
            else:
                if join_game_room(room_id_input, player_name):
                    st.success("Successfully joined the game room!")
                else:
                    st.error("Invalid room ID!")
    
    # Game interface
    if st.session_state.room_id:
        st.subheader(f"Game Room: {st.session_state.room_id}")
        
        # Display players
        st.write("Players in room:")
        for player in st.session_state.game_data['players']:
            st.write(f"👤 {player} - Score: {st.session_state.game_data['scores'].get(player, 0)}")
        
        # Start game button (only for room creator)
        if (st.session_state.game_data['status'] == 'waiting' and 
            st.session_state.game_data['players'] and 
            st.session_state.game_data['players'][0] == player_name):
            if st.button("Start Game"):
                st.session_state.game_data['status'] = 'playing'
                st.session_state.game_data['current_emoji'] = random.choice(EMOJIS)
                st.experimental_rerun()
        
        # Game interface
        if st.session_state.game_data['status'] == 'playing':
            st.subheader(f"Round {st.session_state.game_data['current_round']}")
            
            # Display current emoji
            st.write(f"Current Emoji: {st.session_state.game_data['current_emoji']}")
            
            # Show waiting message if player has already guessed
            if st.session_state.game_data['guesses'].get(player_name) is not None:
                st.info("Waiting for other players to guess...")
            else:
                # Player input
                player_guess = st.text_input("What do you think this emoji represents?")
                
                if st.button("Submit Guess"):
                    if player_guess:
                        st.session_state.game_data['guesses'][player_name] = player_guess
                        st.success("Guess submitted!")
                        
                        # Check if all players have guessed
                        if all(guess is not None for guess in st.session_state.game_data['guesses'].values()):
                            # Award points
                            for player in st.session_state.game_data['players']:
                                st.session_state.game_data['scores'][player] = st.session_state.game_data['scores'].get(player, 0) + 1
                            
                            # Reset for next round
                            st.session_state.game_data['current_round'] += 1
                            st.session_state.game_data['current_emoji'] = random.choice(EMOJIS)
                            st.session_state.game_data['guesses'] = {player: None for player in st.session_state.game_data['players']}
                            st.experimental_rerun()
                    else:
                        st.error("Please enter your guess!")

if __name__ == "__main__":
    main() 