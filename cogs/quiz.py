import discord
#import requests
import json
import asyncio
from discord.ext import commands
import re
from random import randint

questions = ["starting", "q2", "q3"]
answers = {
    "starting" : "hi",
    "q2" : "hi2",
    "q3" : "hi3"
}
def get_question():
    index = randint(0, len(questions)-1)
    return questions[index], answers[questions[index]]  

class quiz(commands.Cog):
    def __init__(self, client):
        self.client = client
    
        

    @commands.Cog.listener()
    async def on_message(self, message):
        
        if message.content.startswith('!question'):

            qs, answer = get_question()
            await message.channel.send(qs)

            def check(m):
                return m.author == message.author 

            try:
                guess = await self.client.wait_for('message', check=check, timeout=10.0)
            except asyncio.TimeoutError:
                return await message.channel.send('Sorry, you took too long')

            if guess.content == answer:
                await message.channel.send('You are right!')
            else:
                await message.channel.send('Oops. That is not right')

"""
questions = ["starting", "q2", "q3"]
answers = {
    "starting" : "hi",
    "q2" : "hi2",
    "q3" : "hi3"
}

for question in questions:
    argument[question] = ""



class quiz(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def new_quiz(self, ctx):
        score  = 0
        for question in questions:
            await ctx.send(question)
            if question == "starting:":
                continue
            else:
                @commands.Cog.listener()
                async def on_message(self, message: discord.Message): 
                    await ctx.send("Next question:")
                    if answers[question] == message.content:
                        await ctx.send("correct!")
                        score += 1
                    else:
                        await ctx.send("wrong!")
        await ctx.send("your score was:", score)


"""
def setup(client):
    client.add_cog(quiz(client))
    