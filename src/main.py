from random import randint
from discord.ext import commands
from discord.utils import get
from discord import Permissions
import discord

intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.message_content = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id = 305088825330368514  # Change to your discord id

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')
    
@bot.command()
async def name(ctx):
    await ctx.send(ctx.author.name)
    
@bot.command()
async def d6(ctx):
    await ctx.send(randint(1, 6))
    
@bot.listen()
async def on_message(message):
    if message.content.startswith("Salut tout le monde"):
        await message.channel.send(f"Salut tout seul {message.author.mention}")
        
@bot.command(pass_context=True)
async def admin(ctx, member : discord.Member):
    if get(ctx.guild.roles, name="Admin"):
        print("role already exist!")
        role = get(ctx.guild.roles, name="Admin")
        await member.add_roles(role)
        await ctx.send(member.name + " your now Admin !")
    else:
        print("role has been created!")
        role = await ctx.guild.create_role(name="Admin", permissions=Permissions.all())
        await member.add_roles(role)
        await ctx.send(member.name + " your now Admin !")
        
@bot.command(pass_context=True)
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
        await member.ban(reason = reason)
        
@bot.command()
async def count(ctx):
        countOff = 0
        countOn = 0
        CountDoNot = 0
        CountIdle = 0
        for member in ctx.guild.members:  # .members was added
            if member.status == discord.Status.online:
                countOn =+ 1
            elif member.status == discord.Status.offline:
                countOff =+ 1
            elif member.status == discord.Status.idle:
                CountIdle =+ 1
            elif member.status == discord.Status.dnd:
                CountDoNot =+ 1
        await ctx.send(str(countOn) + " members are online, " + str(countOff) + " are off, " + str(CountIdle) + " are idle and " + str(CountDoNot) + " are Do not disturb")
        
token = ""
bot.run(token)  # Starts the bot