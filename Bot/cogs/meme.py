import discord
from discord.ext import commands
import praw

client = commands.Bot(command_prefix = "?")

reddit = praw.Reddit(client_id = "",
                    client_secret = "",
                    username = "",
                    password = "",
                    user_agent = "")
                    
@client.command()
async def meme(ctx):
    subreddit = reddit.subreddit("memes","")
    all_subs = []
    top = subreddit.top(limit = 50)

    for submission in top:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url

    em = discord.Embed(title = name)

    em.set_image(url = url)

    await ctx.send(embed= em)
    
    
    @client.command(aliases = ["user","info"])
@commands.has_permissions(kick_members=True)
async def whois(ctx, member : discord.Member):
    embed = discord.Embed(title = member.name , description = member.mention , color = discord.Color.green())
    embed.add_field(name = "ID" , value = member.id , inline = True )
    embed.set_thumbnail(url = member.avatar_url)
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested By {ctx.author.name}")
    await ctx.send(embed=embed)
