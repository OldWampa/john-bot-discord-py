import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import datetime
from datetime import datetime
import random

# This is my development file where I test out code before I release it.

class dev:
    def __init__(self, client):
        self.client = client
        
    @commands.command(pass_context=True)
    async def test_role_hierarchy(self, ctx):
        roles = ctx.message.server.role_hierarchy
        xrole = f"**{len(ctx.message.server.roles)} Roles** - "
        for role in roles:
            xrole += role.mention + ", "
        embed = discord.Embed(description=f"{xrole}  ".replace(",  ", ""))
        await self.client.say(embed=embed)
    
    @commands.command(pass_context=True)
    async def evalm(self, ctx):
        message = ctx.message
        await asyncio.sleep(1)
        await self.client.say(f"type - {message.type}\n attachments - {message.attachments}\n embeds - {message.embeds}")
        
    @commands.command(pass_context=True)
    async def rollr(self, ctx, message, channel:discord.Channel):
        m = await self.client.get_message(channel, message)
        r = m.reactions
        for reaction in m.reactions:
            if reaction.emoji == "❄️":
                list = await self.client.get_reaction_users(reaction)
                winner = random.choice(list)
                await self.client.say(winner.mention)
        
    @commands.command(pass_context=True)
    async def rollwinner(self, ctx, message, emoji, channel:discord.Channel=None):
        if channel is None:
            channel = ctx.message.channel
        m = await self.client.get_message(channel, message)
        for reaction in m.reactions:
            if reaction.emoji == emoji:
                list = await self.client.get_reaction_users(reaction)
                winner = random.choice(list)
                await self.client.say(f"The winner is {winner.mention}! Congratulations!")
        
def setup(client):
    client.add_cog(dev(client))
