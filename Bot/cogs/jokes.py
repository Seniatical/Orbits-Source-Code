import discord
from discord.ext import commands
import requests


class jokes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def joke(self, ctx, arg=None):
        if arg is None:
            r = requests.get(
                "https://sv443.net/jokeapi/v2/joke/Miscellaneous?blacklistFlags=nsfw,religious,political,racist,sexist&type=twopart")
            joke = r.json()
            embed = discord.Embed(
                colour=discord.Color.orange(),
                title=joke['setup']
            )
            embed.add_field(name="_ _", value=joke['delivery'])
            await ctx.send(embed=embed)
        else:
            try:
                arg = arg.capitalize()  # making the first letter capital so it fits the link
                r = requests.get(
                    f"https://sv443.net/jokeapi/v2/joke/{arg}?blacklistFlags=nsfw,religious,political,racist,sexist&type=twopart")
                """
                using arg here so we don't need to 
                copy paste the same code for every type of joke
                """
                if r.status_code == 200:
                    jokes = r.json()
                    embed = discord.Embed(
                        colour=discord.Color.magenta(),
                        title=jokes['setup']
                    )
                    embed.add_field(name="_ _", value=jokes['delivery'])
                    await ctx.send(embed=embed)
            except KeyError:
                await ctx.send("Something went wrong while fetching your joke :/ try again!")


def setup(bot):
    bot.add_cog(jokes(bot))
