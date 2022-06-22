import discord
from discord.ext import commands

class Guidance(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def guidance(self, ctx):
        def check_response(message):
            return message.channel == ctx.channel
        await ctx.send("Enter your last name")
        name = await self.client.wait_for("message", check=check_response)
        name = name.content.lower()
        letter = name[0]

        DB=("abcdABCD")
        HA=("efghijzEFGHIJZ")
        SH=("lmLM")
        HE=("knopqKNOPQ")
        TA=("rstuvwxyRSTUVWXY")

        line1=("You can reach them at this email: ")
        line2=("Use this link to book an appointment: ")

        out = ""
        if letter in DB:
            out += "Your guidance counsellor is Ms.De Braux\n"
            out += line1 + "michelle.debraux@tdsb.on.ca\n"
            out += line2 + "https://calendly.com/msdebraux/guidance-appointment%22"
        elif letter in HA:
            out += "Your guidance counsellor is Ms.Hayden\n"
            out += line1 + "jenny.hayden@tdsb.on.ca\n"
            out += line2 + "https://calendly.com/ms-hayden/guidance-appointment%22"
        elif letter in SH:
            out += "Your guidance counsellor is Ms.Schwartz\n"
            out += line1 + "jennifer.schwartz@tdsb.on.ca\n"
            out += line2 + "https://calendly.com/jennifer-schwartz-1/guidance-appointment%22"
        elif letter in HE:
            out += "Your guidance counsellor is Ms.Heron\n"
            out += line1 + "amanda.heron@tdsb.on.ca\n"
            out += line2 + "https://calendly.com/amanda-heron/guidance-appointment%22"
        elif letter in TA:
            out += "Your guidance counsellor is Mr.Taylor\n"
            out += line1+ "john.taylor@tdsb.on.ca\n"
            out += line2 + "https://calendly.com/john-taylor-17/guidance-appointment%22"
        else:
            out += "invalid name"
        await ctx.send(out)

def setup(client):
    client.add_cog(Guidance(client))


