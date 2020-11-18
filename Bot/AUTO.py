from discord.ext import commands
import string
from profanity_filter import ProfanityFilter
pf = ProfanityFilter()
import datetime

## Run pip install spacy && python -m spacy download en
## This is to prevent any errors

alpha = (list(string.ascii_lowercase)) 

def profantiy(message):
    message = message.lower()
    x = pf.censor(message)
    if x != message:
        return True
    return False

## def is_raid(channel):
##     x = None
##     async for message in channel.history(limit=25):
##         if not x:
##             x = message
##             continue
##         if message.created_at.datetime.datetime.utcnow() - datetime.timedelta(seconds=2) == x.datetime.timedelta(seconds=2):
##             if x.author.id == message.author.id or x.default_avatar == True and message.author.default_avatar == True:
##                 if x.author.created_at.datetime.strftime("%Y") == message.author.created_at.datetime.strftime("%Y"):
##                     return True
##                 return False
##             return False
##         return False

'''
Found the error
fixing soon
27 => END
'''

def is_fast_join(guild):
    for member in guild.members:
        if member.joined_at.datetime.datetime.utcnow().year == datetime.datetime.utcnow().year:
            x = guild.members[guild.members.index(member, 0, -1)+1]
            if x.joined_at.datetime.datetime.utcnow().year == datetime.datetime.utcnow().year:
                if x.joined_at.datetime.strftime("%j:%a:%H") == member.joined_at.datetime.strftime("%j:%a:%H"):
                    return True
        else:
            continue
    
class members:
    def __init__(self):
        self.user = {}
    
message_event = """
try:
    if profanity(message.content) != False:
        await message.delete()
        return await message.channel.send('{} that is a forbidden word!'.format(message.author.mention))
        
    elif 'discord.gg/' in message.content and message.author.permissions_in(message.channel).manage_messages == False:
        await message.delete()
        return await ctx.send('{} You cannot send invite links in the server!'.format(message.author.mention))
        
    elif 'https://www.' in message.content and message.author.permissions_in(message.channel).manage_messages == False:
        await message.delete()
        return await ctx.send('{} You cannot send website links in the server!'.format(message.author.mention))
        
    if len(message.mentions) <= 10:
        role = discord.utils.get(message.guild.roles, name='Muted')
        if not role:
            for role in message.author.roles:
                if role == message.guild.default_role:
                    continue
                x = self.get_role(role.id)
                await message.author.remove_roles(x)
            await message.author.add_roles(role)
            await message.channel.send('{} has automatically been muted for spam pinging.'.format(message.author.mention))
        else:
            perms = discord.Permissions(add_reactions=False, send_messages=False, connect=False)
            role = await ctx.guild.create_role(name='Muted', permissions=perms)
            for role in message.author.roles:
                if role == message.guild.default_role:
                    continue
                x = self.get_role(role.id)
                await message.author.remove_roles(x)
            await message.author.add_roles(role)
            await message.channel.send('{} has automatically been muted for spam pinging.'.format(message.author.mention))
        
except Exception as error:
    return await message.channel.send(error)
"""

status_event = """
try:
    return
except Exception as error:
    return await message.channel.send(error)
"""


