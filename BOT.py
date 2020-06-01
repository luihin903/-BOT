import discord
from discord.ext import commands
bot=commands.Bot(command_prefix='[')
@bot.event
async def on_ready():
    print('Bot is online')
bot.run('NzE3MDAwNzczMzI1NTUzNzI3.XtT9Xg.iYitMQJNU1dXCBpAmowpHnr5Ek4')