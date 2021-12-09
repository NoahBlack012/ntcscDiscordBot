import discord
from discord.ext import commands

class Calender(commands.Cog):
    def __init__(self, client):
        self.client = client

    ## Add commands here ##


    ########################

def setup(client):
    client.add_cog(Calender(client))
#eeeeeeeeeee