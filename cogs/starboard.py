import discord
from discord.ext import commands
from discord.utils import get
import time
import asyncio

# This code has been updated and organized very recently.

class starboard:
    def __init__(self, client):
        self.client = client
        
    async def on_reaction_add(self, reaction, user):
        starboard = discord.utils.get(reaction.message.server.channels, name="starboard")
        if reaction.emoji != "\U00002b50":
            return
        if reaction.message.author.bot:
            return
        if user == reaction.message.author and reaction.emoji == "\U00002b50":
            await self.client.remove_reaction(reaction.message, reaction.emoji, reaction.message.author)
            return
        if reaction.emoji == "\U00002b50":
            getstars = await self.client.get_reaction_users(reaction)
            if str(len(getstars)) == "3":
                embed = discord.Embed(description=f"{reaction.message.content} \n\n➜[Jump to message](https://discordapp.com/channels/{reaction.message.server.id}/{reaction.message.channel.id}/{reaction.message.id})", color=discord.Colour.gold(), timestamp=reaction.message.timestamp)
                embed.set_author(name=f"{reaction.message.author}", icon_url=reaction.message.author.avatar_url)
                if reaction.message.attachments:
                    attachments = reaction.message.attachments[0]["url"]
                    embed.set_image(url=attachments)
                await self.client.send_message(starboard, f"{reaction.emoji} {reaction.message.channel.mention} ID: {reaction.message.id}", embed=embed)
                
    async def on_reaction_remove(self, reaction, user):
        starboard = discord.utils.get(reaction.message.server.channels, name="starboard")
        if reaction.emoji != "\U00002b50":
            return
        if reaction.message.author.bot:
            return
        if reaction.emoji == "\U00002b50":
            getstars = await self.client.get_reaction_users(reaction)
            if str(len(getstars)) == "2":
                msgs = []
                async for x in self.client.logs_from(starboard):
                    msgs.append(x)
                for message in msgs:
                    if str(reaction.message.id) in message.content:
                        await self.client.delete_message(message)
        
def setup(client):
    client.add_cog(starboard(client))
