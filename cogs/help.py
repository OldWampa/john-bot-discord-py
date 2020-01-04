import discord
from discord.ext import commands

# This file is only really updated when a new command is released.

class help:
    def __init__(self, client):
        self.client = client
        
    @commands.command(pass_context=True)
    async def help(self, ctx):
        help = discord.Embed(color=discord.Colour(0x00c4ff))
        help.set_thumbnail(url='https://cdn.discordapp.com/attachments/516376650230005760/566112917540438022/bluequestion.png')
        help.set_author(name='Commands', icon_url='https://cdn.discordapp.com/attachments/512454926300086282/516138030143373343/johnbot.png')
        help.add_field(name="<:john_happy:509194295182360576> General", value="`help` - Displays this list of commands \n`server` - Displays some statistics on the server \n`user` - Statistics about a specefied user \n`avatar` - Get an avatar of a user \n`ping` - Bot reaction speed \n`suggest` - Send a suggestion to the suggestions channel", inline=False)
        help.add_field(name="<:john_pencil:533431235981344798> Fun & Misc", value="`roll` - Roles dice in NdN \n`8ball` - Ask the magic 8 ball a question \n`flip` - Flips a coin... or a user \n`protip` - Extremely useful life pro tips \n`cat` - Random cat pictures \n`dog` - Random dog pictures \n`amplify` - Repeats your message with funny amplified text \n`clapify` - Clapifies your text \n`split` - Splits your text with the emoji or word given \n`rps` - Play rock paper scissors with the bot", inline=False)
        await self.client.say(embed=help)
    
    @commands.has_permissions(view_audit_logs=True)
    @commands.command(pass_context=True)
    async def modhelp(self, ctx):
        help = discord.Embed(color=discord.Colour(0x7289da))
        help.set_thumbnail(url='https://cdn.discordapp.com/attachments/516376650230005760/566112917540438022/bluequestion.png')
        help.set_author(name='Mod Commands', icon_url='https://cdn.discordapp.com/attachments/512454926300086282/516138030143373343/johnbot.png')
        help.add_field(name="Moderation", value="`infractions` - Check the infractions of a user \n`warn` - Warns a user \n`mute` - Mutes a user \n`unmute` - Unmutes a user \n`kick` - Kicks a user \n`ban` - Bans a user \n`clear` - Clears messages in a channel \n`lock` - Locks a channel \n`unlock` - Unlocks a channel", inline=False)
        help.add_field(name="Suggestions", value="`accept` - Approves a suggestion \n`reject` - Denies a suggestion \n`ignore` - Ignores a suggestion", inline=False)
        help.add_field(name="Support", value="`message` - Message a user", inline=False)
        help.add_field(name="Bot Configuration", value="`load` - Loads a cog \n`unload` - Unloads a cog", inline=False)
        await self.client.say(embed=help)
    
        
def setup(client):
    client.add_cog(help(client))
