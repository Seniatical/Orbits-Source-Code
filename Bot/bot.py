import discord
from discord.ext import commands
import traceback
import datetime

desc = """Orbit. The one bot to replace many!"""
owners = [475357293949485076, 338999581474029578, 464694683231191042, 482179909633048597, 523580106548183048, 564881596990357533, 724982934154510407]
allowed_mentions = discord.AllowedMentions(everyone=False, roles=False, users=True)
intents = discord.Intents.all()

class Orbit(command.AutoShardedBot):
    def __init__(self):
        super().__init__(
            command_prefix=PREFIX,case_insensitive=True,
            allowed_mentions=allowed_mentions,intents=intents,
            help_command=None,description=desc,owner_ids=owners,
        )
        for file in os.listdir('./cogs'):
            try:
                self.load_extention('cogs.{}'.format(file[:-3]))
            except Exception as error:
                error_traceback = traceback.format_exception(etype=type(error), value=error, tb=error.__traceback__)
                print(error_traceback + '\n\n')
                
        self.launch_time = datetime.datetime.utcnow()
        
    async def on_connect(self):
        print('{} has connected to discords endpoint.'.format(self.user))
        
    async def on_ready(self):
        print('All cogs have been loaded!')
        
if __name__ == '__main__':
    bot = Oribit()
    bot.run('')
