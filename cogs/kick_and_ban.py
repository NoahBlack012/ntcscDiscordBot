
import discord
from discord.ext import commands
import re



class bad(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('just a reminder to that there is no anti-ntci propaganda in this server {0.mention}.'.format(member))
    """
    @commands.command()
    async def kick(self, ctx: commands.context, discord.Member, *, reason = None):
        await member.kick(reason = reason)
    """
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message): 
        
        censors = ["fuck nt", "nt is trash", "ntci is trash", "fuck ntci"]
        if message.content == "i hate nt" or message.content == "i hate ntci":
            channel = message.channel
            await channel.send("Shut Up \n Do not disrespect NTCI")
            #await kick(self, message.content)
        elif re.match("(?i)[i]\s(hate|dislike)\s(nt|ntci)", message.content) or re.match("(?i)(nt|ntci)\sis\s(shit|trash|awful)", message.content):
            channel = message.channel
            await channel.send("Shut Up \n Do not disrespect NTCI") 
        else:
            for censor in censors:
                #text = re.findall(censor, message.content)
                if message.content == censor:
                    channel = message.channel
                    await channel.send("Shut Up \n Do not disrespect NTCI") 
                    break


def setup(client):
    client.add_cog(bad(client))
    