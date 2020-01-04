import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import datetime
from datetime import datetime

class joins:
    def __init__(self, client):
        self.client = client
        
    async def on_member_join(self, member):
        embed = discord.Embed(description=f"Before chatting, please **read the server rules**, found in <#513244827106672651>. You can also find other information regarding this server in that channel. If you have any unanswered questions, you may DM <@507432299403542539> or ask one of the server <@&557645389344276491>.", color=discord.Colour.red(), timestamp=datetime.now())
        embed.set_footer(text=f"{member}", icon_url=member.avatar_url)
        embed.set_thumbnail(url=member.avatar_url)
        channel = discord.utils.get(member.server.channels, name="general")
        sendwelcome = await self.client.send_message(channel, f"Welcome to the server {member.mention}!", embed=embed)
        emoji = get(self.client.get_all_emojis(), name='wave_hand')
        await self.client.add_reaction(sendwelcome, emoji=emoji)
        role = discord.utils.get(member.server.roles, id="511739438418886728")
        await self.client.add_roles(member, role)
        await asyncio.sleep(180)
        await self.client.delete_message(sendwelcome)
        
def setup(client):
    client.add_cog(joins(client))
