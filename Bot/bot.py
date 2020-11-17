import discord
from discord.ext import commands
import traceback
import datetime
import os
import AUTO
import json
from pathlib import Path

cwd = Path(__file__).parents[0]
cwd = str(cwd)

desc = """Orbit. The one bot to replace many!"""
owners = [475357293949485076, 338999581474029578, 464694683231191042, 482179909633048597, 523580106548183048, 564881596990357533, 724982934154510407]
allowed_mentions = discord.AllowedMentions(everyone=False, roles=False, users=True)
intents = discord.Intents.all()
PREFIX = '?'
secret = json.load(open(cwd+'/configs/secret.json'))

class Orbit(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(
            command_prefix=PREFIX,case_insensitive=True,
            allowed_mentions=allowed_mentions,intents=intents,
            help_command=None,description=desc,owner_ids=owners,
        )
        for file in os.listdir('./cogs'):
            if filename.endswith('.py'):
                try:
                    self.load_extension('cogs.{}'.format(file[:-3]))
                except Exception as error:
                    error_traceback = traceback.format_exception(etype=type(error), value=error, tb=error.__traceback__)
                    print(error_traceback + '\n\n')

        @self.command(aliases=['ut'])
        @commands.cooldown(1, 10, BucketType.user)
        async def uptime(ctx):
            delta_uptime = datetime.datetime.utcnow() - bot.launch_time
            hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
            minutes, seconds = divmod(remainder, 60)
            days, hours = divmod(hours, 24)
            embed = discord.Embed(title = "Uptime:",description = f"Days: {days}\nHours: {hours}\nMins: {minutes}", color = discord.Colour.red())
            await ctx.send(embed = embed)
                
        self.launch_time = datetime.datetime.utcnow()
        self.AUTOMOD = False
        
    async def on_connect(self):
        print('{} has connected to discords endpoint.'.format(self.user))
        
    async def on_ready(self):
        print('All cogs have been loaded!')
        
    # async def on_message(self, message):
    #     if self.AUTOMOD != True:
    #         exec(AUTO.message_event)
    #         return
        
if __name__ == '__main__':
    bot = Orbit()
    bot.run(secret['token'])
