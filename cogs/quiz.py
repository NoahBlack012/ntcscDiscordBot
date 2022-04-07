from tempfile import TemporaryFile
import discord
#import requests
import json
import asyncio
from discord.ext import commands
import re
from random import randint

questions = ["When was NT founded?", "", "q3"]
answers = {
    "Which of the following celebs went to NT? \na) Ryan Gostling \nb) Rachel McAdams \nc) Keanu Reeves \nd) Michael Bublé" : "c",
    "When was NTCI founded? \na) 1910 \nb) 1912\nc) 1915\nd) 1917" : "b",
    "When did the first Maytime melodies take place? \na) May 1947 \nb) May 1940 \nc) May 1952 \nd) February 1952" : "a",
    "How much money did NT raise in their first Charity Week that took place in 1986? \na) $1000 \nb) $1500 \nc) $2000 \nd) $3000" : "a",
    "When did NT switch to a new building? \na) 2008 \nb) 2009 \nc) 2010 \nd) 2011" : "c",
    "What was Graffiti originally known as? \na) The NTCI Post \nb) Graffiti \nc) The NT Star \nd) The Roehampton Edition" : "d",
    "Which of the following teachers are married to another teacher at NT? \na) Miron \nb) Zohar \nc) Seepersad \nd) Kinoshita" : "d"
}

questions = list(answers.keys())
#print(questions)

scores = {

}

def get_question():
    index = randint(0, len(questions)-1)
    return questions[index], answers[questions[index]]  

class trivia(commands.Cog):
    def __init__(self, client):
        self.client = client
    
        

    @commands.Cog.listener()
    async def on_message(self, message):
        
        if message.content.startswith('!start_trivia'):
            print(str(message.author)[:-5])
            curr_questions = []
            curr_answers = []
            count = 0
            while count < 3:
                qs, answer = get_question()
                if qs in curr_questions:
                    continue
                else:
                    curr_questions.append(qs)
                    curr_answers.append(answer)
                    count += 1
                    await message.channel.send(qs)

            if str(message.author)[:-5] not in scores.keys():
                scores[str(message.author)[:-5]] = 0
            
            curr_score = 0
            def check(m):
                return m.author == message.author 

            try:
                guess = await self.client.wait_for('message', check=check, timeout=30.0)
            except asyncio.TimeoutError:
                return await message.channel.send('Sorry, you took too long')
            user_answers = guess.content
            #print(user_answers)
            user_answers = str(user_answers).split()
            #print(user_answers)
            i = 0
            while i < len(user_answers):
                #print(user_answers[i])
                try:
                    if user_answers[i] == answers[curr_questions[i]]:
                        await message.channel.send('Correct!')
                        curr_score += 1
                        
                        #val = "here is your current score:" + str(scores[str(message.author)[:-5]])
                        
                    else:
                        await message.channel.send('Wrong!')
                except:
                    await message.channel.send("error")
                i += 1
            val = "Your final score: " + str(curr_score) + "/3"
            await message.channel.send(val)
            if scores[str(message.author)[:-5]] < curr_score:
                scores[str(message.author)[:-5]] = curr_score
    @commands.command()
    async def my_trivia_score(self, ctx):
        #print(str(ctx.author)[:-5])
        #print(scores[str(ctx.author)[:-5]])
        try:
            val = scores[str(ctx.author)[:-5]]
            if val >= 3:
                val = "your highest quiz score is: " + str(val) + ". You are a patriot to NT."
                await ctx.send(val)
            else:
                val = "your highest quiz score is: " + str(val) + ". You could do better :("
                await ctx.send(val)
        except TypeError:
            await ctx.send("No quiz record found :(")
            #await ctx.send(scores[str(ctx.author)[:-5]])
    @commands.command()
    async def trivia_instructions(self, ctx):
        await ctx.send("This NT trivia will have 3 question multiple choice questions that you have to answer in 30 seconds. Use the command: '!start_trivia' to start the trivia. Once it is started, the questions will be printed. Type your answers out in a single line with the letter of the option and a space between each answer. Submit by pressing enter. Once you've submitted the bot will type out your score. \n Use the command: 'my_trivia_score' to see your highest trivia score. ")


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
    client.add_cog(trivia(client))
    