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
            await ctx.send("Invalid usage, please specify a proper duration.")
            return
        elif seconds => 31536000:
            await ctx.send("Invalid usage, maximum duration is 365 days.")
            return
        else:
            await ctx.send(f"Alright, I will remind you about `{reminder}` in `{counter}`.")
            await asyncio.sleep(seconds)
            await ctx.send(f"**Reminder** {user.mention}: {reminder}")
            return

def setup(bot):
    bot.add_cog(Reminder(bot))
