import discord
from discord.ext import commands

class TEST(commands.Cog):
    def __init__(self, bot):
      self.bot = bot
  
@bot.command(aliases = ['p'])
async def poll(self, ctx,*,msg):
    channel = ctx.channel
    try:
        op1 , op2 = msg.split("or")
        txt = f"React With 1️⃣ for {op1} or 2️⃣ for {op2}"
    except:
        await channel.send("Correct syntax: [Choice1] or [Choice2]")
        return

    embed = discord.Embed(title="🎈POLL TIME", description = txt, color= discord.Color.red())
    message = await channel.send(embed=embed)
    await message.add_reaction("1️⃣")
    await message.add_reaction("2️⃣")
    await ctx.message.delete()
def setup(bot):
  bot.add_cog(TEST(bot))

















