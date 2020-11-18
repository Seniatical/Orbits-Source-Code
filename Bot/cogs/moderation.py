import discord
from discord.ext import commands


class TEST(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member = None, *, reason: str = None):
        if user == None:
            return True
        if user == ctx.author:
            return True

        if reason == None:
            reason = "Not Valid"
        else:
            reason = reason

        embed = discord.Embed(
            title="Kick",
            description=f"{user.mention} has been kicked from {ctx.guild} by {ctx.author} with the reason of: \"{reason}\""
        )
        embed.set_footer(text="Command done by: <@338999581474029578>")
        await user.kick(reason=reason)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member = None, *, reason: str = None):
        if user == None:
            return True
        if user == ctx.author:
            return True

        if reason == None:
            reason = "Not Valid"
        else:
            reason = reason

        embed = discord.Embed(
            title="Kick",
            description=f"{user.mention} has been kicked from {ctx.guild} by {ctx.author} with the reason of: \"{reason}\""
        )
        embed.set_footer(text="Command done by: <@338999581474029578>")
        await user.ban(reason=reason)


def setup(bot):
    bot.add_cog(TEST(bot))
