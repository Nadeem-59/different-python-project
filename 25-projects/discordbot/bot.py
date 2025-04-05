import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Store emoji reactions
emoji_data = {}

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    # Load saved emoji data if exists
    try:
        with open('emoji_data.json', 'r') as f:
            global emoji_data
            emoji_data = json.load(f)
    except FileNotFoundError:
        emoji_data = {}

@bot.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return
    
    message_id = str(reaction.message.id)
    if message_id not in emoji_data:
        emoji_data[message_id] = []
    
    emoji_info = {
        'emoji': str(reaction.emoji),
        'user': user.name,
        'timestamp': str(reaction.message.created_at)
    }
    
    emoji_data[message_id].append(emoji_info)
    
    # Save to file
    with open('emoji_data.json', 'w') as f:
        json.dump(emoji_data, f)

@bot.command(name='emojis')
async def show_emojis(ctx):
    """Show all emoji reactions for the current message"""
    message_id = str(ctx.message.id)
    if message_id in emoji_data:
        response = "Emoji reactions for this message:\n"
        for emoji in emoji_data[message_id]:
            response += f"{emoji['emoji']} by {emoji['user']} at {emoji['timestamp']}\n"
        await ctx.send(response)
    else:
        await ctx.send("No emoji reactions for this message yet!")

# Run the bot
bot.run(os.getenv('DISCORD_TOKEN')) 