import praw
import discord
import random
from discord.ext import commands
import json

secret = json.load(open('../Bot/configs/secret.json')) # getting API key and acc details from json file


r = praw.Reddit(client_id = secret['reddit']['client_id'], 
                client_secret = secret['reddit']['client_secret'], 
                username = secret['reddit']['username'], 
                password = secret['reddit']['password'],
                user_agent = secret['reddit']['user_agent'])
"""PRAW stuff"""

class memes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    
    @commands.command(description="Dankest of them memes")
    async def meme(self, ctx):
        subreddit = r.subreddit("dankmemes").hot() #sorting r/dankmemes from hot
        post = random.randint(1, 100)
        for x in range (0, post):
            submission = next(x for x in subreddit if not x.stickied)

                
        name = submission.title
        url = submission.url
        colour = discord.Colour.dark_theme()
            
        embed = discord.Embed(title = name, colour=colour)
        embed.set_footer(text="Original post by u/"+submission.author.name)
        embed.set_image(url = url)
        await ctx.send(embed=embed)
        

def setup(bot):
    bot.add_cog(memes(bot))

