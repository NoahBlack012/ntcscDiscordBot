import discord
from discord.ext import commands

class Menu(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def menu(self, ctx):
        await ctx.send("__Command Menu__ \nShow late start schedule: **.latestart** \nShow the next late start: **.nextlatestart** \nTells you what day it is: **.schedule** \nPlay the NTCI trivia: **.trivia_instructions** \nFind your guidance counselor: **.guidance [insert last name]** \nPlay the school anthem: **.anthem** \nRecieve an inspirational quote: **.inspiration** \nPlay an NT version of Wordle: **.play_northle**")

def setup(client):
    client.add_cog(Menu(client))