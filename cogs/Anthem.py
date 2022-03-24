import discord
from discord.ext import commands

class NTCI_anthem(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def anthem(self, ctx):
        await ctx.send("https://www.youtube.com/watch?v=pUOvFpABxYk")

def setup(client):
    client.add_cog(NTCI_anthem(client))