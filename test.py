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


#say command
@client.command()
async def say(ctx, message, channel, type=None):
    sended = client.get_channel(int(channel))
    if type == None:
        say = discord.Embed(colour=0xE59866)
        say.add_field(name="message sended!", value="‌")
        await sended.send(message)
        await ctx.reply(embed=say)
    else:
        if type == "Embed" or type == "Text":
            if type == "Embed":
                say = discord.Embed(colour=0xE59866)
                say.add_field(name="message sended!", value="‌")
                Embed = discord.Embed(colour=0xE59866)
                Embed.add_field(name="‌", value=message)
                await sended.send(embed=Embed)
                await ctx.reply(embed=say)
            if type == "Text":
                say = discord.Embed(colour=0xE59866)
                say.add_field(name="message sended!", value="‌")
                await sended.send(message)
                await ctx.reply(embed=say)
        else:
            say = discord.Embed(colour=0xE59866)
            say.add_field(name="Error from Type is not Embed or Text!", value="‌")
            await ctx.reply(embed=say)

@slash.slash(name="say", description="send a message to a channel💬")               
async def say(ctx, message, channel, type=None):
    sended = client.get_channel(int(channel))
    if type == None:
        say = discord.Embed(colour=0xE59866)
        say.add_field(name="message sended!", value="‌")
        await sended.send(message)
        await ctx.reply(embed=say)
    else:
        if type == "Embed" or type == "Text":
            if type == "Embed":
                say = discord.Embed(colour=0xE59866)
                say.add_field(name="message sended!", value="‌")
                Embed = discord.Embed(colour=0xE59866)
                Embed.add_field(name="‌", value=message)
                await sended.send(embed=Embed)
                await ctx.reply(embed=say)
            if type == "Text":
                say = discord.Embed(colour=0xE59866)
                say.add_field(name="message sended!", value="‌")
                await sended.send(message)
                await ctx.reply(embed=say)
        else:
            say = discord.Embed(colour=0xE59866)
            say.add_field(name="Error from Type is not Embed or Text!", value="‌")
            await ctx.reply(embed=say)

# ____________________________#

#client login     

@client.event
async def on_ready():
    print("bot is online")  

#import keep_alive
#keep_alive.keep_alive()
# ____________________________#
client.run(Token)