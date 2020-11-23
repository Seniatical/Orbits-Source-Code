import discord
from discord.ext import commands
from datetime import datetime
import asyncio

class Reminder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['remind','remindme'])
    async def reminder(self, ctx, time, *, reminder):
        user = ctx.message.author
        embed = discord.Embed(color=0x55a7f7)
        seconds = 0
        if time.lower().endswith("d" or "D"):
            seconds += int(time[:-1]) * 60 * 60 * 24
            counter = f"{seconds // 60 // 60 // 24} days"
            if time.lower().endswith("h" or "H"):
                seconds += int(time[:-1]) * 60 * 60
                counter = f"{seconds // 60 // 60} hours"
            elif time.lower().endswith("m" or "M"):
                seconds += int(time[:-1]) * 60
                counter = f"{seconds // 60} minutes"
            elif time.lower().endswith("s" or "S"):
                seconds += int(time[:-1])
                if seconds == 1:
                    counter = f"{seconds} second"
                else:
                    counter = f"{seconds} seconds"
            if seconds == 0:
                embed.add_field(name='Invalid Usage',value='Please specify a proper duration')
            elif seconds > 31536000:
                embed.add_field(name='Invalid Usage', value='Maximum duration is 365 days.')
            else:
                await ctx.send(f"Alright, I will remind you about `{reminder}` in `{counter}`.")
                await asyncio.sleep(seconds)
                await ctx.send(f"**Reminder** {user.mention}: {reminder}")
                return
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Reminder(bot))