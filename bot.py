import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix=".")

# Prints Bot is ready when bot is online
@client.event
async def on_ready():
    print ("Bot is ready")

# Load cogs
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

# Add your token in the string below
client.run("YOUR_TOKEN_HERE")
