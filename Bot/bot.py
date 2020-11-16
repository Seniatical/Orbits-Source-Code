import discord
from discord.ext import commands

class Orbit(command.AutoShardedBot):
    def __init__(self):
        allowed_mentions = discord.AllowedMentions(everyone=False, roles=False, users=True)
        intents = discord.Intents.all()
        super().__init__(
            command_prefix=PREFIX,
            case_insensitive=True,
            allowed_mentions=allowed_mentions,
            intents=intents,
            description='Orbit. The one bot to replace many!',
            help_command=None,
            owner_ids=[475357293949485076, 338999581474029578, 464694683231191042, 482179909633048597, 523580106548183048, 564881596990357533, 724982934154510407],
        )
        
if __name__ == '__main__':
    bot = Oribit()
    bot.run('')
