from discord.ext import commands
import string
from profanity_filter import ProfanityFilter
pf = ProfanityFilter()

## Run pip install spacy && python -m spacy download en
## This is to prevent any errors

alpha = (list(string.ascii_lowercase)) 

def profantiy(message):
    message = message.lower()
    x = pf.censor(message)
    if x != message:
        return True
    return False
    
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
    elif 
except Exception as error:
    return await message.channel.send(error)
"""
