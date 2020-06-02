import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='$')
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)
while True:
    bot.run('NzE3MDAwNzczMzI1NTUzNzI3.XtZSRA.QW8WDmWBMJUMH5latt5yr3VIaNI')