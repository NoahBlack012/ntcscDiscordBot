import discord
from discord.ext import commands
from random import randint


inspirations = "Nothing is impossible, the word itself says “I’m possible”! -- Audrey Hepburn qqq I’ve learned that people will forget what you said, people will forget what you did, but people will never forget how you made them feel. -- Maya Angelou qqq Whether you think you can or you think you can’t, you’re right. -- Henry Ford qqq Perfection is not attainable, but if we chase perfection we can catch excellence. -- Vince Lombardi qqq Life is 10 percent what happens to me and 90 percent of how I react to it. -- Charles Swindoll qqq If you look at what you have in life, you’ll always have more. If you look at what you don’t have in life, you’ll never have enough. -- Oprah Winfrey qqq None of us is as smart as all of us. -- Ken Blanchard qqq I can’t change the direction of the wind, but I can adjust my sails to always reach my destination. -- Jimmy Dean qqq Believe you can and you’re halfway there. -- Theodore Roosevelt qqq To handle yourself, use your head; to handle others, use your heart. -- Eleanor Roosevelt qqq Too many of us are not living our dreams because we are living our fears. -- Les Brown qqq Alone, we can do so little; together we can do so much. -- Helen Keller qqq Whatever the mind of man can conceive and believe, it can achieve. -- Napoleon Hill qqq Twenty years from now you will be more disappointed by the things that you didn’t do than by the ones you did do, so throw off the bowlines, sail away from safe harbor, catch the trade winds in your sails. Explore, Dream, Discover. -- Mark Twain qqq I’ve missed more than 9000 shots in my career. I’ve lost almost 300 games. 26 times I’ve been trusted to take the game-winning shot and missed. I’ve failed over and over and over again in my life. And that is why I succeed. -- Michael Jordan qqq Strive not to be a success, but rather to be of value. -- Albert Einstein qqq I am not a product of my circumstances. I am a product of my decisions. -- Stephen Covey When everything seems to be going against you, remember that the airplane takes off against the wind, not with it. --Henry Ford"
inspirations = inspirations.split("qqq")

def random_inspiration():
    index = randint(0, len(inspirations)-1)
    return inspirations[index]  

class inspirational_quote(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def inspiration(self, ctx):
        val = random_inspiration()
        await ctx.send(val)


def setup(client):
    client.add_cog(inspirational_quote(client))