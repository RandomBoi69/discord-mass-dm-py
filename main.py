import discord
from discord.ext import commands

token = "" #set your token here
prefix = "-" #change your prefix if you want

client = discord.client
intents = discord.Intents(messages=True, members=True)
client = commands.Bot(command_prefix=prefix, description="Mass Dm Bot", self_bot="True", intents=intents) #change self bot to false if you aren't using self bot

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def start(ctx, *, args):
  for user in ctx.guild.members:
    try:
      await user.send(args)
    except:
      continue
  await ctx.send("successfully send your message to members!")

client.run(token, bot=False) # change to false if you aren't use self bot
