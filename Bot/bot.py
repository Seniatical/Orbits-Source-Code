import discord
from discord.ext import commands
import traceback
import datetime
import os
import AUTO, INVITE
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

def GETCHANNEL(guild, category):
    channel = 777947981324353590
    return channel

class Orbit(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(
            command_prefix=PREFIX,case_insensitive=True,
            allowed_mentions=allowed_mentions,intents=intents,
            help_command=None,description=desc,owner_ids=owners,
        )
        for file in os.listdir('./cogs'):
            if file == "__pycache__":
                return
            else:
                try:
                    self.load_extension('cogs.{}'.format(file[:-3]))
                except Exception as error:
                    error_traceback = traceback.format_exception(etype=type(error), value=error, tb=error.__traceback__)
                    print(error_traceback + '\n\n')
        self.TRACKER = INVITE.TRACKER(self)
        self.launch_time = datetime.datetime.utcnow()
        self.AUTOMOD = False

        @self.command(aliases=['ut'])
        @commands.cooldown(1, 10, commands.BucketType.user) # you forgot to add commands. before BucketType :D
        async def uptime(ctx): 
            delta_uptime = datetime.datetime.utcnow() - bot.launch_time
            hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
            minutes, seconds = divmod(remainder, 60) 
            days, hours = divmod(hours, 24)
            embed = discord.Embed(title = "Uptime:",description = f"Days: {days}\nHours: {hours}\nMins: {minutes}", color = discord.Colour.red())
            await ctx.send(embed = embed)
        
    async def on_connect(self):
        print('{} has connected to discords endpoint.'.format(self.user))
        
    '''
    INVITE TRACKING SECTION
    DONT MODIFY
    '''
    async def on_ready(self):
        await self.TRACKER.ALL_INVITES() 
        print('All cogs have been loaded!')
    async def on_guild_join(self, guild):
        await self.TRACKER.CREATE_GUILD_INVITES(guild)
    async def on_guild_remove(self, guild):
        await self.TRACKER.REMOVE_INVITES(guild)
    async def on_invite_create(self, invite):
        await self.TRACKER.UPDATE_INVITE(invite)
        """^You forgot an S TRACKER.UPDATE_INVITE(S)?"""
        
    async def on_invite_delete(self, invite):
        await self.TRACKER.REMOVE_INVITES(invite)
    async def on_member_join(self, member):
        x = await self.TRACKER.GET_INVITER(member)
        channel = GETCHANNEL(member.guild, 'on_join')
        await self.get_channel(channel).send('> **{}** has been invited by **{}**'.format(member, x))
        
if __name__ == '__main__':
    bot = Orbit()
    bot.load_extension("jishaku")
    bot.run(secret['discord']['token'])
