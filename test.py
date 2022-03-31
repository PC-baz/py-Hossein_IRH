# import discord
import discord
from discord.ext import commands
from datetime import datetime, time, timedelta
from discord_slash import SlashCommand, SlashContext
from playsound import *
# ____________________________#

# bot Token
Token = 'OTU3OTg5NDUxNTU5MjE1MjE0.YkGzMw.OGy7IeH10PchA3-6H3A5c7cFn54'
# ____________________________#

# client Prefix
intents = discord.Intents.all()
client = commands.Bot(command_prefix='%', help_command=None, intents=intents)
slash = SlashCommand(client, sync_commands=True)
# ____________________________#


@client.command()
async def party(ctx):
    party = "<:devil:958057329012658297>" #assigning the emoji
    await ctx.send(party) #sending the emoji

#info command
@client.command()
async def info(ctx):
    info = discord.Embed(title="info command", colour=0xE59866)
    info.add_field(name="members:", value=ctx.guild.member_count, inline=False)
    info.add_field(name="server name:", value=ctx.guild.name, inline=False)
    info.add_field(name="channels:", value=ctx.guild.get_all_channels)
    info.add_field(name='Created At', value=ctx.guild.created_at.__format__('%A, %d. %B %Y at %H:%M:%S'), inline=False)
    info.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.reply(embed=info)

@slash.slash(name="info", description="info command📄")
async def info(ctx):
    info = discord.Embed(title="info command", colour=0xE59866)
    info.add_field(name="members:", value=ctx.guild.member_count, inline=False)
    info.add_field(name="server name:", value=ctx.guild.name, inline=False)
    info.add_field(name='Created At', value=ctx.guild.created_at.__format__('%A, %d. %B %Y at %H:%M:%S'), inline=False)
    info.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.send(embed=info)
# ____________________________#

#client login     

@client.event
async def on_ready():
    print("bot is online")  

#import keep_alive
#keep_alive.keep_alive()
# ____________________________#
client.run(Token)
