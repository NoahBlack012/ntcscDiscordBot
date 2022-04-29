# Idea: User enters command to play northle -> Bot starts DM chain to play if user has not played yet, If user has played already - Bot ssays the user has already played
# Other commands - Get leaderboard, get user stats
# All commands .play_northle .northle_leadboard .northle_stats
from discord.ext import commands
import random

async def get_guess(channel, client):
    channel.send("Enter a five letter word")
    def check_response(message):
        return message.channel == channel

    guess = ""
    while len(guess) != 5:
        message = await client.wait_for("message", check=check_response)
        guess = message.content.lower()
        if len(guess) != 5:
            channel.send("You must enter a five letter word")
    return guess


def generate_response(guess, word):
    word_map = {}
    for i in word:
        if i not in word_map:
            word_map[i] = 1
        else:
            word_map[i] += 1

    response = ["*" for i in range(5)]
    for n, i in enumerate(word):
        if i == guess[n]:
            response[n] = "🟩"
            word_map[i] -= 1
    correct = not ("*" in response)
    for n, i in enumerate(word):
        if correct:
            break
        if i != guess[n]:
            if guess[n] in word and word_map[guess[n]] > 0:
                response[n] = "🟨"
                word_map[i] -= 1
            else:
                response[n] = "⬛"
    return "".join(response), correct

class Northle(commands.Cog):
    def __init__(self, client):
        self.client = client

    """
    User sends: .play_northle
    Bot sends: Direct message to user to start game
    """
    @commands.command()
    async def play_northle(self, ctx):
        member = ctx.message.author
        dm_channel = await member.create_dm() # Create DM channel with user who entered command
        await dm_channel.send("Try to guess the five letter word!") # DM to user
        await ctx.reply("Check your messages to play Northle!") # Reply to user in original channel

        # Get word from database
        words = ["hello", "world", "north"] 
        word = random.choice(words)

        # Set initial attributes of the game
        gameover = False
        guesses = 0
        all_responses = []
        while not gameover:
            guesses += 1
            if guesses > 6:
                message = f"Sorry, better luck next time. The word is {word}"
                break

            guess = await get_guess(dm_channel, self.client)
            response, gameover = generate_response(guess, word)
            if gameover:
                message = "Congratulations, you got the word correct!"
            await dm_channel.send(response)
            all_responses.append(response)
        await dm_channel.send(message)
        await dm_channel.send("\n".join(all_responses))

    """
    User sends: .northle_leadboard
    Bot sends: List of users with top winning percentages, Lowest guess average
    """
    @commands.command()
    async def northle_leadboard(self, ctx):
        await ctx.send("Bot Test")

    """
    User sends: .northle_stats
    Bot sends: User's game stats (Winning percentage, guess average, current streak)
    """
    @commands.command()
    async def northle_stats(self, ctx):
        await ctx.send("Bot Test")


def setup(client):
    client.add_cog(Northle(client))