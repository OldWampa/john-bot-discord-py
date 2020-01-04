import discord
from discord.ext import commands
import random
import asyncio
import time
import datetime
from datetime import datetime
from discord.utils import get
import aiohttp
import os
import re
from os import path
import traceback
import logging
import json

prefix = ["j!", "J!"]

client = commands.Bot(command_prefix=prefix)
client.launch_time = datetime.now()
client.remove_command('help')

extensions = ["cogs.help",
             "cogs.general",
             "cogs.suggest",
             "cogs.mods",
             "cogs.fun",
             "cogs.starboard",
             "cogs.support",
             "cogs.errors",
             "cogs.joins",
             "cogs.vc",
             "cogs.chat"]

@client.event
async def on_message(message):
    if message.author.bot:
        return
    else:
        await client.process_commands(message)

@commands.has_permissions(administrator=True)
@client.command()
async def load(extension):
    try:
        client.load_extension(extension)
        await client.say(f'{extension} loaded.')
    except Exception as error:
        await client.say(f'{extension} cannot be loaded. ```{error}```')

@commands.has_permissions(administrator=True)
@client.command()
async def unload(extension):
    try:
        client.unload_extension(extension)
        await client.say(f'{extension} unloaded.')
    except Exception as error:
        await client.say(f'{extension} cannot be unloaded. ```{error}```')

if __name__ == "__main__":
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print(f'{extension} cannot be loaded. {error}')
    client.run('NTA3NDMyMjk5NDAzNTQyNTM5.DzuCFg.J6jZaXibF-Xw8D5Dx76ZOD4uddE')
