forbidden = ('fuck', 'cock', 'dick', 'fcuk')

message_event = """
try:
    if message.content.lower() in forbidden:
        await message.delete()
        return await message.channel.send('{} that is a forbidden word!'.format(message.author.mention))
    elif 'discord.gg/' in message.content and message.author.permissions_in(message.channel).manage_messages == False:
        await message.delete()
        return await ctx.send('{} You cannot send invite links in the server!'.format(message.author.mention))
    elif 'https://www.' in message.content and message.author.permissions_in(message.channel).manage_messages == False:
        await message.delete()
        return await ctx.send('{} You cannot send website links in the server!'.format(message.author.mention))
except Exception as error:
    return await message.channel.send(error)
"""
