import discord
from discord.ext import commands
import datetime

#variable for the today's date
present = datetime.date.today()

#list of all the late start dates
late_start = [datetime.date(2021,9,29), datetime.date(2021,10,20), datetime.date(2021,10,27), datetime.date(2021,11,5), datetime.date(2021,11,17), datetime.date(2021,11,24), datetime.date(2021,12,8), datetime.date(2021,12,14), datetime.date(2022,1,12), datetime.date(2022,1,19), datetime.date(2022,1,26), datetime.date(2022,2,16), datetime.date(2022,2,23), datetime.date(2022,3,23), datetime.date(2022,3,30), datetime.date(2022,4,20), datetime.date(2022,4,27), datetime.date(2022,5,18), datetime.date(2022,5,25)]

class Calender(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def nextlatestart(self, ctx):

        #check through each late start on the list
        for i in range(19):

            #if the late start has not already happened
            if(late_start[i] > present):

                #convert the date to written form
                written_date = late_start[i].strftime("%B %d, %Y")

                #print the informaion
                await ctx.send("The next late start is " + written_date)

                #stop the loop from repeating
                break
        else:
            # If no late starts are found in the future (Loop does not break)
            await ctx.send("There are currently no late starts in the future")

    @commands.command()
    async def latestart(self, ctx):

        list_of_dates = ""

        #add each late start date
        for i in range(19):
            
            #convert dates to written form
            written_date = late_start[i].strftime("%B %d, %Y")

            #add each late start date to a string
            list_of_dates = list_of_dates + written_date + "\n"

        #print the string of late start dates
        await ctx.send("__Late Start Dates for the 2021-2022 School Year__\n" + list_of_dates)

def setup(client):
    client.add_cog(Calender(client))