import discord
from discord.ext import commands
import string
import string
import random

def gen_key():
    alpha, num = list(string.ascii_lowercase), list(string.digits)
    mapper = []
    for i in range(10):
        x = ('y', 'n')
        if random.choice(x) == 'y':
            if random.choice(x) == 'y':
                mapper.append(random.choice(alpha).upper())
            else:
                mapper.append(random.choice(alpha))
        else:
            mapper.append(str(random.choice(num)))
            
    return ''.join(map(str, mapper))


class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.poll_keys = {}

    @commands.command()
    async def poll(self, ctx,  question=None, *options: str):
        if question == None:
            embed = discord.Embed(title="Follow the syntax below", description='For numbered polls:\n?poll <"Question"> <option1> <option2> upto 10 options\n\nFor yes or no polls:\n?poll <"Question"> <yes> <no>', colour=discord.Color.red())
            embed.set_footer(text="without the <>")
            await ctx.send(embed=embed)
        if len(options) == 0:
            await ctx.send("You need 2 options to make a poll")
        if len(options) <= 1:
            await ctx.send('You need more than one option to make a poll!')
            return
        if len(options) > 10:
            await ctx.send('You cannot make a poll for more than 10 things!')
            return

        if len(options) == 2 and options[0].lower() == 'yes' and options[1].lower() == 'no':
            reactions = ['✅', '❌']
        elif len(options) == 2 and options[1].lower() == 'yes' and options[0].lower() == 'no':
            reactions = ['❌', '✅']
        else:
            reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']

        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
        embed = discord.Embed(title=question, description=''.join(description), colour=0xffff00)
        react_message = await ctx.send(embed=embed)
        for reaction in reactions[:len(options)]:
            await react_message.add_reaction(reaction)
        pollkey = gen_key()
        embed.set_footer(text='Poll ID: {}'.format(pollkey))
        self.poll_keys[pollkey] = react_message.id
        await react_message.edit(embed=embed)
        


    @commands.command()
    async def tally(self, ctx, poll : str=None):
        if id == None:
            return await ctx.send("Please Enter poll ID")
        poll_message = await ctx.channel.fetch_message(self.poll_keys[poll])
        if not poll_message:
            return await ctx.send('Please enter the correct id!')
        embed = poll_message.embeds[0]
        unformatted_options = [x.strip() for x in embed.description.split('\n')]
        print(f'unformatted{unformatted_options}')
        opt_dict = {x[:2]: x[3:] for x in unformatted_options} if unformatted_options[0][0] == '1' \
            else {x[:1]: x[2:] for x in unformatted_options}
        # check if we're using numbers for the poll, or x/checkmark, parse accordingly
        voters = [self.bot.user.id]  # add the bot's ID to the list of voters to exclude it's votes

        tally = {x: 0 for x in opt_dict.keys()}
        for reactions in poll_message.reactions:
            if reactions.emoji in opt_dict.keys():
                reactors = await reactions.users().flatten()
                for reactor in reactors:
                    if reactor.id not in voters:
                        tally[reactions.emoji] += 1
                        voters.append(reactor.id)
                        
        res = '\n'.join(['{}: {}'.format(opt_dict[key], tally[key]) for key in tally.keys()])
        await ctx.send(embed=discord.Embed(title=f'Results of the poll for **{embed.title}**:', colour=discord.Colour.red(), description=res))
        await poll_message.clear_reactions()

def setup(bot):
    bot.add_cog(Poll(bot))