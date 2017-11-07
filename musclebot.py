import discord
from discord.ext import commands
import random
import asyncio
import tokens

description = '''Test bot for various features.'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(tokens.TOKEN)
