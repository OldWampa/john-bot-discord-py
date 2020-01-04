import discord
from discord.ext import commands
from discord.utils import get
import random
import time

# Most of these commands have been updated recently.

class general:
    def __init__(self, client):
        self.client = client
        
    @commands.command(pass_context=True)
    async def server(self, ctx):
        server = ctx.message.server
        created = server.created_at.strftime("%A, %B %d, %Y @ %H:%M.%S %p")
        online = 0
        offline = 0
        idle = 0
        dnd = 0
        bots = 0
        humans = 0
        for member in server.members:
            if str(member.status) == 'online':
                online += 1
            if str(member.status) == 'offline':
                offline += 1
            if str(member.status) == 'idle':
                idle += 1
            if str(member.status) == 'dnd':
                dnd += 1
            if str(member.bot) == 'True':
                bots += 1
            if str(member.bot) == 'False':
                humans += 1
        roles = server.role_hierarchy
        xrole = f"**{len(server.roles)} Roles** - "
        for role in roles:
            xrole += role.mention + ", "
        if 'VANITY_URL' in server.features:
            partner = "<:tick1Green:529809815514513408>**PARTNERED**"
        else:
            partner = "<:tick3Red:529809815480827914>**PARTNERED**"
        if str(server.region) == "brazil":
            loc = "\U0001f1e7\U0001f1f7**BRAZIL**"
        if str(server.region) == "us-west":
            loc = "\U0001f1fa\U0001f1f8**US WEST**"
        if str(server.region) == "japan":
            loc = "\U0001f1ef\U0001f1f5**JAPAN**"
        if str(server.region) == "singapore":
            loc = "\U0001f1f8\U0001f1ec**SINGAPORE**"
        if str(server.region) == "eu-central":
            loc = "\U0001f1ea\U0001f1fa**CENTRAL EUROPE**"
        if str(server.region) == "hongkong":
            loc = "\U0001f1ed\U0001f1f0**HONG KONG**"
        if str(server.region) == "us-south":
            loc = "\U0001f1fa\U0001f1f8**US SOUTH**"
        if str(server.region) == "southafrica":
            loc = "\U0001f1ff\U0001f1e6**SOUTH AFRICA**"
        if str(server.region) == "us-central":
            loc = "\U0001f1fa\U0001f1f8**US CENTRAL**"
        if str(server.region) == "us-east":
            loc = "\U0001f1fa\U0001f1f8**US EAST**"
        if str(server.region) == "sydney":
            loc = "\U0001f1e6\U0001f1fa**SYDNEY**"
        if str(server.region) == "eu-west":
            loc = "\U0001f1ea\U0001f1fa**WESTERN EUROPE**"
        if str(server.region) == "russia":
            loc = "\U0001f1f7\U0001f1fa**RUSSIA**"
        wump = ["<:new_discord1:534180127051874304>", "<:new_discord2:534180128238862346>"]
        nd = random.choice(wump)
        embed = discord.Embed(color=discord.Colour(0x00c4ff))
        embed.set_thumbnail(url=server.icon_url)
        embed.add_field(name=f'{server.name}', value=f"<:owner:534166150863388673>**{server.owner}** \n{loc} \n{partner}", inline=False)
        embed.add_field(name=f'Members', value=f"<:status_online:529809816495849492>**ONLINE** - {online} \n<:status_idle:529809816462426113>**IDLE** - {idle} \n<:status_dnd:529809816600838154>**DND** - {dnd} \n<:status_offline:529809816328077315>**OFFLINE** - {offline} \n<:bot:534147741530718208>**BOTS** - {bots} \n<:new_member:534180127022776330>**HUMANS** - {humans} \n<:discord_logo:534182147200909320>**TOTAL** - {server.member_count}", inline=False)
        embed.add_field(name="Roles", value=f"{xrole}  ".replace(",  ", ""), inline=False)
        embed.add_field(name='Other Stats', value=f'<:discord_logo:534182147200909320>**Server ID**: \n`{server.id}` \n{nd}**Created**:\n`{created}`', inline=False)
        embed.set_footer(text=server.name, icon_url=server.icon_url)
        await self.client.say(embed=embed)
    
    @commands.command(pass_context=True)
    async def user(self, ctx, member:discord.Member=None):
        nm = "<:new_member:534180127022776330>"
        wump = ["<:new_discord1:534180127051874304>", "<:new_discord2:534180128238862346>"]
        nd = random.choice(wump)
        dl = "<:discord_logo:534182147200909320>"
        if member is None:
            member = ctx.message.author
        created = member.created_at.strftime("%A, %B %d, %Y @ %H:%M.%S %p")
        joined = member.joined_at.strftime("%A, %B %d, %Y @ %H:%M.%S %p")
        if ".gif" in member.avatar_url:
            nitro = "<:nitro:534145690457079808> **DISCORD NITRO**\n"
        else:
            nitro = ""
        if member is ctx.message.server.owner:
            owner = "<:owner:534166150863388673> **SERVER OWNER**\n"
        else:
            owner = ""
        if member.bot is True:
            bot = "<:bot:534147741530718208> **BOT**\n"
        else:
            bot = ""
        q = sorted(ctx.message.server.members, key=lambda member: member.joined_at).index(member)+1
        if str(q).endswith('11'):
            af ="th"
        elif str(q).endswith('12'):
            af ="th"
        elif str(q).endswith('13'):
            af ="th"
        elif str(q).endswith('14'):
            af = "th"
        elif str(q).endswith('1'):
            af ="st"
        elif str(q).endswith('2'):
            af ="nd"
        elif str(q).endswith('3'):
            af ="rd"
        else:
            af = "th"
        roles = member.roles
        result = f"**{len(member.roles)} Roles** - "
        for role in roles:
            result += role.mention + ", "
        embed = discord.Embed(color=member.color)
        embed.add_field(name=f'{member}', value=f"{owner}{nitro}{bot}{member.status} - {member.game}".replace("online", f"<:status_online:529809816495849492> **ONLINE**").replace("offline", f"<:status_offline:529809816328077315> **OFFLINE**").replace("idle", f"<:status_idle:529809816462426113> **IDLE**").replace("dnd", f"<:status_dnd:529809816600838154> **DND**").replace(" - None", ""), inline=False)
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name='Roles', value=f"{result}  \n**Top Role** - {member.top_role.mention} \n**Permissions Value** - {member.server_permissions.value}".replace(",  ", ""), inline=False)
        embed.add_field(name='Other Stats', value=f'{dl}**User ID**: \n`{member.id}` \n{nm}**Join Queue**: \n`{q}{af} member to join this server` \n{nm}**Joined**: \n`{joined}` \n{nd}**Created**: \n`{created}`', inline=False)
        embed.set_footer(text=member, icon_url=member.avatar_url)
        await self.client.say(embed=embed)
    
    @commands.command(pass_context=True)
    async def avatar(self, ctx, member:discord.Member=None):
        if member is None:
            member = ctx.message.author
        embed = discord.Embed(title=f"{member.name}'s avatar", url=member.avatar_url, color=member.color)
        embed.set_image(url=member.avatar_url)
        await self.client.say(embed=embed)
    
    @commands.command(pass_context=True)
    async def ping(self, ctx):
        channel = ctx.message.channel
        t1 = time.perf_counter()
        await self.client.send_typing(channel)
        t2 = time.perf_counter()
        ping = discord.Embed(title="Pong!", description='It took {}ms.'.format(round((t2-t1)*1000)), color=discord.Colour(0x00c4ff))
        await self.client.say(embed=ping)
    
        
def setup(client):
    client.add_cog(general(client))
