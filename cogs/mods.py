import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import datetime
from datetime import datetime

# This code is pretty old. Probably could use an update / some more organization.

class mods:
    def __init__(self, client):
        self.client = client
        
    @commands.has_permissions(view_audit_logs=True)
    @commands.command(pass_context=True)
    async def infractions(self, ctx, member:discord.Member=None):
        if member is None:
            member = ctx.message.author
        modlog = client.get_channel("515672869666029568")
        puns = 0
        msgs = []
        async for x in self.client.logs_from(modlog):
            msgs.append(x)
        for message in msgs:
            if str(member.id) in message.content:
                puns += 1
        embed = discord.Embed(description=f"**{puns}** Infractions")
        embed.set_author(name=member, icon_url=member.avatar_url)
        await self.client.say(embed=embed)

    @commands.has_permissions(view_audit_logs=True)
    @commands.command(pass_context=True)
    async def warn(self, ctx, member:discord.Member=None, *, reason=None):
        if member is None:
            await self.client.say('**Please specify a member!**')
            return
        if member.server_permissions.view_audit_logs:
            await self.client.say('**You cannot warn a moderator!**')
            return
        if reason is None:
            reason = "Unspecified"
        user = member
        modlog = discord.utils.get(ctx.message.server.channels, name="moderation-log")
        embed = discord.Embed(colour=discord.Colour(0xd3d3d3), timestamp=datetime.now())
        embed.set_author(name="Warn", icon_url="https://cdn.discordapp.com/attachments/362056767284445187/508026169971572743/628px-Attention_Sign.svg.png")
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="User", value=f"{user.mention} ({user})")
        embed.add_field(name="Moderator", value=f"{ctx.message.author.mention} ({ctx.message.author})")
        embed.add_field(name="Reason", value=f"{reason}")
        await self.client.send_message(modlog, f"`+1 Infraction for {user}:` {user.id}", embed=embed)
        embed2 = discord.Embed(colour=discord.Colour(0xd3d3d3))
        embed2.set_author(name="Warning", icon_url="https://cdn.discordapp.com/attachments/362056767284445187/508026169971572743/628px-Attention_Sign.svg.png")
        await self.client.say(f'{user.mention}, you have been **warned** by {ctx.message.author.mention} for "**{reason}**"', embed=embed2)

    @commands.has_permissions(mute_members=True)
    @commands.command(pass_context=True)
    async def mute(self, ctx, member:discord.Member=None, *, reason=None):
        if member is None:
            await self.client.say('**Please specify a member!**')
            return
        if member.server_permissions.view_audit_logs:
            await self.client.say('**You cannot mute/unmute a moderator!**')
            return
        if reason is None:
            reason = "Unspecified"
        user = member
        modlog = discord.utils.get(ctx.message.server.channels, name="moderation-log")
        embed = discord.Embed(colour=discord.Colour(0xffff00), timestamp=datetime.now())
        embed.set_author(name="Mute", icon_url="https://img.icons8.com/metro/1600/mute.png")
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="User", value=f"{user.mention} ({user})")
        embed.add_field(name="Moderator", value=f"{ctx.message.author.mention} ({ctx.message.author})")
        embed.add_field(name="Reason", value=f"{reason}")
        await self.client.send_message(modlog, f"`+1 Infraction for {user}:` {user.id}", embed=embed)
        embed2 = discord.Embed(colour=discord.Colour(0xffff00))
        embed2.set_author(name="Mute", icon_url="https://img.icons8.com/metro/1600/mute.png")
        await self.client.say(f'{user.mention}, you have been **muted** by {ctx.message.author.mention} for "**{reason}**"', embed=embed2)
        mute = discord.utils.get(member.server.roles, name="Muted")
        await self.client.add_roles(user, mute)

    @commands.has_permissions(mute_members=True)
    @commands.command(pass_context=True)
    async def unmute(self, ctx, member:discord.Member=None, *, reason=None):
        if member is None:
            await self.client.say('**Please specify a member!**')
            return
        if member.server_permissions.view_audit_logs:
            await self.client.say('**You cannot mute/unmute a moderator!**')
            return
        if reason is None:
            reason = "Unspecified"
        user = member
        modlog = discord.utils.get(ctx.message.server.channels, name="moderation-log")
        embed = discord.Embed(colour=discord.Colour(0x00ff00), timestamp=datetime.now())
        embed.set_author(name="Unmute", icon_url="https://www.cityphones.com.au/wp-content/uploads/2017/06/volume_mute-key-repair-200x200.png")
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="User", value=f"{user.mention} ({user})")
        embed.add_field(name="Moderator", value=f"{ctx.message.author.mention} ({ctx.message.author})")
        embed.add_field(name="Reason", value=f"{reason}")
        await self.client.send_message(modlog, embed=embed)
        embed2 = discord.Embed(colour=discord.Colour(0x00ff00))
        embed2.set_author(name="Unmute", icon_url="https://www.cityphones.com.au/wp-content/uploads/2017/06/volume_mute-key-repair-200x200.png")
        await self.client.say(f'{user.mention}, you have been **unmuted** by {ctx.message.author.mention} for "**{reason}**"', embed=embed2)
        unmute = discord.utils.get(member.server.roles, name="Muted")
        await self.client.remove_roles(user, unmute)

    @commands.has_permissions(kick_members=True)
    @commands.command(pass_context=True)
    async def kick(self, ctx, member:discord.Member=None, *, reason=None):
        if member is None:
            await self.client.say('**Please specify a member!**')
            return
        if member.server_permissions.view_audit_logs:
            await self.client.say('**You cannot kick a moderator!**')
            return
        if reason is None:
            reason = "Unspecified"
        user = member
        modlog = discord.utils.get(ctx.message.server.channels, name="moderation-log")
        embed = discord.Embed(colour=discord.Colour(0xffa500), timestamp=datetime.now())
        embed.set_author(name="Kick", icon_url="https://static.thenounproject.com/png/380644-200.png")
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="User", value=f"{user.mention} ({user})")
        embed.add_field(name="Moderator", value=f"{ctx.message.author.mention} ({ctx.message.author})")
        embed.add_field(name="Reason", value=f"{reason}")
        await self.client.send_message(modlog, f"`+1 Infraction for {user}:` {user.id}", embed=embed)
        embed2 = discord.Embed(colour=discord.Colour(0xffa500))
        embed2.set_author(name="Kick", icon_url="https://static.thenounproject.com/png/380644-200.png")
        await self.client.say(f'**{user}** has been **kicked** by {ctx.message.author.mention} for "**{reason}**"', embed=embed2)
        await self.client.kick(user)

    @commands.has_permissions(ban_members=True)
    @commands.command(pass_context=True)
    async def ban(self, ctx, member:discord.Member=None, *, reason=None):
        if member is None:
            await self.client.say('**Please specify a member!**')
            return
        if member.server_permissions.view_audit_logs:
            await self.client.say('**You cannot ban a moderator!**')
            return
        if reason is None:
            reason = "Unspecified"
        user = member
        modlog = discord.utils.get(ctx.message.server.channels, name="moderation-log")
        embed = discord.Embed(colour=discord.Colour(0xff0000), timestamp=datetime.now())
        embed.set_author(name="Ban", icon_url="https://i.imgur.com/tq43DIX.jpg")
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="User", value=f"{user.mention} ({user})")
        embed.add_field(name="Moderator", value=f"{ctx.message.author.mention} ({ctx.message.author})")
        embed.add_field(name="Reason", value=f"{reason}")
        await self.client.send_message(modlog, f"`+1 Infraction for {user}:` {user.id}", embed=embed)
        embed2 = discord.Embed(colour=discord.Colour(0xff0000))
        embed2.set_author(name="Ban", icon_url="https://i.imgur.com/tq43DIX.jpg")
        embed2.set_image(url="https://i.imgur.com/O3DHIA5.gif")
        await self.client.say(f'**{user}** has been **BANNED** by {ctx.message.author.mention} for "**{reason}**"', embed=embed2)
        await self.client.ban(user)

    @commands.has_permissions(manage_messages=True)
    @commands.command(pass_context=True)
    async def clear(self, ctx, amount=10):
        channel = ctx.message.channel
        messages = []
        async for message in self.client.logs_from(channel, limit=int(amount) + 1):
            messages.append(message)
        await self.client.delete_messages(messages)
        dmsg = await self.client.say('Messages deleted.')
        await asyncio.sleep(5)
        await self.client.delete_message(dmsg)

    @commands.has_permissions(manage_channels=True)
    @commands.command(pass_context=True)
    async def lock(self, ctx):
        server = ctx.message.server
        author = ctx.message.author
        channel = ctx.message.channel
        role = server.default_role
        overwrite = channel.overwrites_for(role)
        overwrite.send_messages = False
        overwrite.add_reactions = False
        await self.client.edit_channel_permissions(channel, role, overwrite)
        embed = discord.Embed(title="Channel Locked!", description=f"Chat was locked by **{author}**!", color=0xff0000)
        await self.client.say(embed=embed)
        await self.client.delete_message(ctx.message)

    @commands.has_permissions(manage_channels=True)
    @commands.command(pass_context=True)
    async def unlock(self, ctx):
        server = ctx.message.server
        author = ctx.message.author
        channel = ctx.message.channel
        role = server.default_role
        overwrite = channel.overwrites_for(role)
        overwrite.send_messages = True
        overwrite.add_reactions = True
        await self.client.edit_channel_permissions(channel, role, overwrite)
        embed=discord.Embed(title="Channel Unlocked!", description=f"Chat was unlocked by **{author}**!", color=0x00ff00)
        await self.client.say(embed=embed)
        await self.client.delete_message(ctx.message)
    
        
def setup(client):
    client.add_cog(mods(client))
