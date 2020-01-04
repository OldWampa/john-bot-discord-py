import discord
from discord.ext import commands

# This file sends command errors to a private channel in discord.

class errors:
    def __init__(self, client):
        self.client = client
        
    async def on_command_error(self, error, ctx):
        place = ctx.message.server
        if isinstance(error, commands.CommandNotFound):
            return
        if isinstance(error, commands.UserInputError):
            return
        dude = ctx.message.author
        command = ctx.message.content
        channel = self.client.get_channel('541802042809647170')
        await self.client.send_message(channel, f"<:priority2:542154064218292226> __**{place}**__ \n**{dude}**: `{command}` \n\n```{error}```")
        
def setup(client):
    client.add_cog(errors(client))
