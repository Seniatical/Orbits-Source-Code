import discord
from discord.ext import commands


class TEST(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kick(self, ctx, user: discord.Member = None, *, reason: str = None):
        if user == None:
            return True
        if user == ctx.author:
            return True

        if not reason == None:
            reason = reason
        else:
            reason = "Not Valid"

        embed = discord.Embed(
            title="Kick",
            description=f"{user.mention} has been kicked from {ctx.guild} by {ctx.author} with the reason of: \"{reason}\""
        )
        embed.set_footer(text="Command done by: <@>")
        await user.kick(reason=reason)


def setup(bot):
    bot.add_cog(TEST(bot))
