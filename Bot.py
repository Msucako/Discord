import discord
from discord.ext import commands

import config



intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık') 

#İŞLEMLER
@bot.command()
async def bölme(ctx, s1=5 , s2=10):
    await ctx.send(s1 / s2)

@bot.command()
async def çarpma(ctx, s1=5 , s2=10):
    await ctx.send(s1 * s2)

@bot.command()
async def toplama(ctx, s1=5 , s2=10):
    await ctx.send(s1 + s2)

@bot.command()
async def çıkartma(ctx, s1=5 , s2=10):
    await ctx.send(s1 - s2)  




bot.run(config.token)
