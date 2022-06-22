from discord.ext import commands
import discord
import datetime
import random

from sqlalchemy.orm import sessionmaker
from sqlalchemy import select 

try:
    from database import db, Northle_Table, engine, User
    # Create a new session
    Session = sessionmaker(bind=engine)
    session = Session()
except NameError:
    # If database URI cannot be accessed
    print ("You must set up database URI to use the northle.py file")

async def get_guess(channel, client):
    def check_response(message):
        return message.channel == channel

    guess = ""
    while len(guess) != 5:
        message = await client.wait_for("message", check=check_response)
        guess = message.content.lower()
        if len(guess) != 5:
            await channel.send("You must enter a five letter word")
    return guess

# Generate respone to user guess
def generate_response(guess, word):
    # Create dictionary to store counts of letters in word
    word_map = {}
    for i in word:
        if i not in word_map:
            word_map[i] = 1
        else:
            word_map[i] += 1
    # Initally make reponse array of asterisks of length 5
    response = ["*" for i in range(5)]
    for n, i in enumerate(word):
        # If a letter in the word is equal to the letter in the guess at the same position
        if i == guess[n]:
            # Set the response at that position to a green sqaure
            response[n] = "🟩"
            # Subtract one from the letter in word_map since it has been used in the response
            word_map[i] -= 1
    # If there are no asterisks in the response array, the guess was correct
    correct = not ("*" in response)
    for n, i in enumerate(word):
        if correct:
            break
        if i != guess[n]:
            # If the letter in the guess is in the word and the word_map for that letter has a value abive zero
            if guess[n] in word and word_map[guess[n]] > 0:
                # Put a yellow square in the response
                response[n] = "🟨"
                # Subtract one from the letter in word_map since it has been used in the response
                word_map[i] -= 1
            else:
                # If the letter in the guess is not in the word, put a black square in the response
                response[n] = "⬛"
    # Return the response and the correct boolean
    return "".join(response), correct

def split_words(words):
    out = []
    current = ""
    print (words)
    for letter in words:
        if letter == " ":
            continue
        if letter != ",":
            current += letter
        else:
            out.append(current)
            current = ""
    return out

def get_current_word(user_id):
    # Get current date
    date = datetime.datetime.now()
    str_date = date.strftime("%d/%m/%Y")

    northle_data = session.execute(select(Northle_Table)).scalar()
    if northle_data.date == str_date:
        str_users = northle_data.users
        users = split_words(str_users)
        if user_id in [int(i) for i in users]:
            return "", 0, True
        else:
            str_users += f"{user_id},"
            northle_data.users = str_users # Add user to list of users who have played today
            session.add(northle_data) # Add data to session
            session.commit() # Commit to database
        northle_data.users += f"{user_id},"
        session.add(northle_data) # Add data to session
        session.commit() # Commit to database
        return northle_data.word, northle_data.number, False
    else:
        # Update info to current day
        next_words = northle_data.next_words
        words = split_words(next_words)
        try:
            new_word = words.pop(0)
        except IndexError:
            # If words list is enpty
            next_words = "class,study,norse,davis,small,music,halls,ginos,field,phone,yonge,doors,walls,chair,jones,desks,paper,notes,books,email,lunch,clubs,arson,floor,teach,erase,write,grade,board,bored,chalk,sport,table,drama,tests,latin"
            words = split_words(next_words)
            new_word = words.pop(0)

        next_words = ",".join(words) + ","

        # Update database info
        northle_data.word = new_word
        northle_data.number += 1
        northle_data.date = str_date
        northle_data.users = f"{user_id},"
        northle_data.next_words = next_words

        session.add(northle_data) # Add data to session
        session.commit() # Commit to database
        return new_word, northle_data.number, False


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
        user_id = member.id
        # Get word from database
        word, count, played = get_current_word(user_id)
        #played = False

        if played:
            # User has already played today
            await ctx.reply("You have already played Northle today. Wait until tomorrow to play again")
        else:
            dm_channel = await member.create_dm() # Create DM channel with user who entered command
            await dm_channel.send("Try to guess the five letter word!") # DM to user
            await ctx.reply("Check your messages to play Northle!") # Reply to user in original channel

        # Set initial attributes of the game
        gameover = False
        guesses = 0
        all_responses = []
        while not gameover and not played:
            guesses += 1
            if guesses > 6:
                message = f"Northle #{count} X/6. The word is {word}"
                break

            guess = await get_guess(dm_channel, self.client)
            print (guess)
            response, gameover = generate_response(guess, word)
            if gameover:
                message = f"Northle #{count} {guesses}/6"
            await dm_channel.send(response)
            all_responses.append(response)
        # Send game end message and all responses to the user
        if not played:
            # Update user stats
            user = session.execute(select(User).filter_by(userid=str(user_id))).scalar()
            if user is None:
                new_user = User(userid=str(user_id))
                new_user.northle_plays += 1
                if guesses <= 6:
                    new_user.total_northle_guesses += guesses
                    new_user.northle_wins += 1

                session.add(new_user) # Add data to session
                session.commit() # Commit to database
            else:
                user.northle_plays += 1
                if guesses <= 6:
                    user.total_northle_guesses += guesses
                    user.northle_wins += 1

                session.add(user) # Add data to session
                session.commit() # Commit to database
            # Send messages back to user
            await dm_channel.send(message)
            await dm_channel.send("\n".join(all_responses))

    """
    User sends: .northle_leadboard
    Bot sends: List of users with top winning percentages, Lowest guess average
    """
    # @commands.command()
    # async def northle_leadboard(self, ctx):
    #     await ctx.send("Bot Test")
    # WIP

    """
    User sends: .northle_stats
    Bot sends: User's game stats (Winning percentage, guess average, current streak)
    """
    @commands.command()
    async def northle_stats(self, ctx):
        user_id = ctx.message.author.id
        username = ctx.message.author.name
        user = session.execute(select(User).filter_by(userid=str(user_id))).scalar()
        win_rate = str(user.northle_wins/user.northle_plays*100)[:4]
        guess_average = str(user.total_northle_guesses/user.northle_wins)[:3]
        message = discord.Embed(
            title =  f"{username}'s Northle Stats",
            description = f"Win rate: {win_rate}%\nGuess Average: {guess_average}"
        )
        await ctx.send(embed=message)

def setup(client):
    client.add_cog(Northle(client))