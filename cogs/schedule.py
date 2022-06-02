import discord
from discord.ext import commands
import datetime


#the present date
present = datetime.date.today()
#the first day of school
first_day = datetime.date(2022, 2, 3)
#assign the first day to a value
day = 1


#list of dates that are weekdays that we do not have school
no_school = [datetime.date(2022, 2, 18), datetime.date(2022, 2, 21), datetime.date(2022, 3, 14), datetime.date(2022, 3, 15), datetime.date(2022, 3, 16), datetime.date(2022, 3, 17), datetime.date(2022, 3, 18), datetime.date(2022, 4, 15), datetime.date(2022, 4, 18), datetime.date(2022, 5, 23), datetime.date(2022, 6, 3), datetime.date(2022, 6, 30)]

odd_day1 = [datetime.date(2022, 4, 18), datetime.date(2022, 4, 19), datetime.date(2022, 5, 10)]
odd_day2 = [datetime.date(2022, 4, 27), datetime.date(2022, 4, 28), datetime.date(2022, 5, 12), datetime.date(2022, 6, 27), datetime.date(2022, 6, 28)]

#time delta that will increase the day by 1
next_day = datetime.timedelta(days = 1)

#assign variables that will give the result in ctx.send command
weekend = "Today is a weekend"
give_day = "Today is a day "
no_school_today = "There is no school today"


class Schedule(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def schedule(self, ctx):

        #function that checks all of the days that are weekdays where there is no school
        def no_school_days():
        
            #check through all of no school dates
            for i in range (11):

                #if today is a day during the week where there is no school
                if no_school[i] == present:

                    return True

            return False


        #function that checks that if the date that is being checked is a day were there is no school    
        def no_school_days2():
            global first_day

            #check through all of the no school days
            for i in range(11):

                #validify if the date that is being checked is during a day where there is no school so the program can skip over it when counting "school days"
                if no_school[i] == first_day:

                    return True
            
            return False
            

        #function that checks if the date being checked is a day where there is a day 1, 2 days in a row
        def odd_day1_check():
            global first_day

            for i in range(3):

                #validify if the date that is being checked is where there is a second day 1 so the program can skip over it when counting "school days"
                if odd_day1[i] == first_day:

                    return True

            return False


        #function that checks if the date being checked is a day where there is a day 2, 2 days in a row
        def odd_day2_check():
            global first_day

            for i in range(5):

                #validify if the date that is being checked is where there is a second day 2 so the program can skip over it when counting "school days"
                if odd_day2[i] == first_day:

                    return True

            return False


        #function that checks if school is today
        def is_school_today():

            global give_result
            global first_day
            global day

            """
            the first day of school is a day 1 so this function will check if the first day of school is the present. if this is not true
            1 day will be added to the first day and the day will switch from 1 to 2 (if it is not a weekend and there is school). This is so
            that the function can assign each school day a 1 or a 2 until we get to the present and will print what day it is.
            """

            #check through each day in the second semester
            for i in range (149):

                if present == first_day:

                    #if today is saturday
                    if present.isoweekday() == 6:
                        #the result will tell the user it is a weekend
                        give_result = weekend
                        return False

                    if present.isoweekday() == 7:

                        give_result = weekend
                        return False


                    #if today is a school day
                    else:
                        give_result = "Today is a day " + str(day)
                        return True
                





                #if we have not reached the present
                else:

                    #if the date that is being checked is a day where there is no school
                    if no_school_days2() == True:

                        #go to the next day
                        first_day += next_day

                    #if the date that is being checked is a saturday
                    elif first_day.isoweekday() == 6:

                        #go to the next day
                        first_day += next_day

                    #if the day that is being checked is a sunday
                    elif first_day.isoweekday() == 7:

                        #go to the next day
                        first_day += next_day

                    elif odd_day1_check() == True:  

                        first_day += next_day    

                    elif odd_day2_check() == True:

                        first_day += next_day

                    #if the date being checked is a school day
                    else:

                        #go to the next day
                        first_day = first_day + next_day

                        #change the school day
                        day += 1
                        if day == 3:
                            day = 1

            return True 
            
        #if today is not a holiday
        if no_school_days() == False:

            #if there is no school
            if is_school_today() == False:
                
                give_result = weekend
            else:
                give_result = give_day + str(day)
        else:
            give_result = no_school_today

        await ctx.send(give_result)

def setup(client):
    client.add_cog(Schedule(client))
