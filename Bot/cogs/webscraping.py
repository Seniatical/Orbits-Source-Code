import praw
import discord
import random
from discord.ext import commands
from discord.ext.commands import BucketType
import json


secret = json.load(open('../Bot/configs/secret.json')) # getting API key and acc details from json file


r = praw.Reddit(client_id = secret['reddit']['client_id'], 
                client_secret = secret['reddit']['client_secret'], 
                username = secret['reddit']['username'], 
                password = secret['reddit']['password'],
                user_agent = secret['reddit']['user_agent'])
"""PRAW stuff"""

class Webscraping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        


    @commands.command(aliases=["red", "r"], desc="Surf subreddits")
    @commands.cooldown(1,5,commands.BucketType.user)
    async def reddit(self, ctx, sub=None):
        if sub == None:
            return await ctx.send('Give a subreddit name!,\n `eg: ?reddit wholesome`')
        subreddit = r.subreddit(sub).hot()
        post = random.randint(1, 100)
        for x in range(0, post):
            submission = next(x for x in subreddit if not x.stickied)

        if (submission.over_18) == True:
            if ctx.channel.is_nsfw() is False: 
                await ctx.send("This post is NSFW, I can't send it.. Try it in an NSFW marked channel")
            elif ctx.channel.is_nsfw() is True:
                embed = discord.Embed(
                    title = submission.title,
                    colour = discord.Colour.gold(),
                )
                embed.set_image(url=submission.url)
                embed.set_footer(text="Original post by u/"+submission.author.name+" in r/"+sub)
                await ctx.send(embed = embed)
                
        else:
            embed = discord.Embed(
                title = submission.title,
                colour = discord.Colour.gold(),
            )
            embed.set_image(url=submission.url)
            embed.set_footer(text="Original post by u/"+submission.author.name+" in r/"+sub)
            await ctx.send(embed = embed)
            
def setup(bot):
    bot.add_cog(Webscraping(bot))
