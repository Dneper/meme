import discord
from discord.ext import commands
import os, random

bot = commands.Bot(command_prefix='$', intents=discord.Intents.default() )

@bot.event
async def on_ready():
    print('Я работаю')

#@bot.command()
#async def mem(ctx):
    #with open('images/fact.jpg', 'rb') as f:
        #picture = discord.File(f)
    #await ctx.send(file=picture)

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def animal(ctx):
    img_names = random.choice(os.listdir('animals'))
    with open(f'animals/{img_names}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run('MTE1OTg3OTg3NzExODQwMjU3Mg.GLA1FE.PaSJmq7rkd9BuLqbSMzUX7ubYeU-wP57BEos1Q')