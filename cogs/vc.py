import discord
from discord.ext import commands

# Old code but it is simple and serves it's purpose.

class vc:
    def __init__(self, client):
        self.client = client
        
    async def on_voice_state_update(self, before, after):
        role = discord.utils.get(after.server.roles, id="538983972202348554")
        if not before.voice.voice_channel and after.voice.voice_channel:
            await self.client.add_roles(after, role)
        elif before.voice.voice_channel and not after.voice.voice_channel:
            await self.client.remove_roles(after, role)
        
def setup(client):
    client.add_cog(vc(client))
