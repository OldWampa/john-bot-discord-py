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

client = commands.Bot(command_prefix='j!')
client.launch_time = datetime.utcnow()
client.remove_command('help')

@client.event
async def on_ready():
	print('JohnBot#6361 is online and connected to discord.')



#Welcome

@client.listen()
async def on_member_join(member):
        embed = discord.Embed(title=f"Welcome to John's Community!", description=f"{member.mention} ({member.name}#{member.discriminator})", color=discord.Colour.red(), timestamp=datetime.now())
        embed.add_field(name=f"Where do I start?",value="Read <#513244827106672651> at the top for some basic server information and guidlines. To unsubscribe to in-server [YouTube](https://youtube.com/c/johnimationstudios) and [Twitter](https://twitter.com/TheJRSWorld) announcements, then go to <#509186234283982848> and type `j!unsubscribe <feed type>`. Type `j!help` for a list of commands.", inline=False)
        embed.set_footer(text=f"{member.name}#{member.discriminator}", icon_url=member.avatar_url)
        embed.set_thumbnail(url=member.avatar_url)
        channel = discord.utils.get(member.server.channels, name="general")
        sendwelcome = await client.send_message(channel, embed=embed)
        emoji = get(client.get_all_emojis(), name='wave_hand')
        await client.add_reaction(sendwelcome, emoji=emoji)
        role1 = discord.utils.get(member.server.roles, name="YouTube Feed")
        role2 = discord.utils.get(member.server.roles, name="Twitter Feed")
        await client.add_roles(member, role1, role2)
        await asyncio.sleep(60)
        await client.delete_message(sendwelcome)


#VC

@client.event
async def on_voice_state_update(before, after):
        role = discord.utils.get(after.server.roles, id="538983972202348554")
        if not before.voice.voice_channel and after.voice.voice_channel:
                await client.add_roles(after, role)
        elif before.voice.voice_channel and not after.voice.voice_channel:
                await client.remove_roles(after, role)


#Informational

@client.command()
async def help():
	help = discord.Embed(color=discord.Colour.gold())
	help.set_thumbnail(url='https://housing.umn.edu/sites/housing.umn.edu/files/help.png')
	help.set_author(name='Commands', icon_url='https://cdn.discordapp.com/attachments/512454926300086282/516138030143373343/johnbot.png')
	
	help.add_field(name="Informational Commands", value="`j!help` - Displays this list of commands \n`j!serverinfo` - Displays some statistics on the server \n`j!userinfo` - Statistics about a specefied user \n`j!avatar` - Get an avatar of a user \n`j!uptime` - Statistics on the bots uptime \n`j!ping` - Bot reaction speed", inline=False)
	help.add_field(name="Moderation Commands", value="`j!infractions` - View the infractions of a user \n`j!punish` - Automattically punishes a user based off of their current infractions \n`j!warn` - Warns the specified member \n`j!tempmute` - Temporarily mutes the specified member \n`j!mute` - Mutes the specified member \n`j!unmute` - Unmutes the specified member \n`j!kick` - Kicks the specified member \n`j!ban` - Bans the specified member \n`j!clear` - Purges the specified number of messages in a channel \n`j!lock` - Locks the current channel \n`j!unlock` - Unlocks the current channel", inline=False)
	help.add_field(name="Fun Commands", value="`j!roll` - Roles dice in NdN \n`j!8ball` - Ask the magic 8 ball a question \n`j!coinflip` - Flips a coin heads or tails \n`j!protip` - Extremely useful life pro tips \n`j!cat` - Random cat pictures \n`j!dog` - Random dog pictures \n`j!umbo` - **BETA** Makes an emoji JUMBO size \n`j!amplify` - Repeats your message with funny amplified text \n`j!clapify` - Clapifies your text\n`j!split` - Splits your text with the emoji or word given \n`j!quote` - Quotes a message \n`j!snipe` - Snipes the last deleted message \n`j!rps` - Play rock paper scissors with the bot", inline=False)
	help.add_field(name="Other Commands", value="`j!subscribe` - Subscribes you to the specified feed \n`j!unsubscribe` - Unsubscibes you to the specified feed \n`j!suggest` - Send a suggestion to the suggestions channel \n`j!accept` - Marks a suggestion in the suggestions channel as accepted \n`j!reject` - Marks a suggestion in the suggestions channel as reject \n`j!ignore` - Marks a suggestion in the suggestions channel as ignored \n`j!poll` - Start a poll! (mods only)", inline=False)
	
	await client.say(embed=help)



@client.command(pass_context=True, name='serverinfo', aliases=['si', 'server'])
async def server_info(ctx):
    server = ctx.message.server
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
    
    roles = server.roles
    xrole = f"**{len(server.roles)} Roles** - "
    for role in roles:
    	xrole += role.mention + ", "
    
    if str(server.features) == '[]':
    	partner = "<:tick3Red:529809815480827914>**PARTNERED**"
    else:
    	partner = "<:tick1Green:529809815514513408>**PARTNERED**"
    
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
    embed = discord.Embed(color=discord.Colour.blue())
    embed.set_thumbnail(url=server.icon_url)
    embed.add_field(name=f'{server.name}', value=f"<:owner:534166150863388673>**{server.owner}** \n{loc} \n{partner}", inline=False)
    embed.add_field(name=f'Members', value=f"<:status_online:529809816495849492>**ONLINE** - {online} \n<:status_idle:529809816462426113>**IDLE** - {idle} \n<:status_dnd:529809816600838154>**DND** - {dnd} \n<:status_offline:529809816328077315>**OFFLINE** - {offline} \n<:bot:534147741530718208>**BOTS** - {bots} \n<:new_member:534180127022776330>**HUMANS** - {humans} \n<:discord_logo:534182147200909320>**TOTAL** - {server.member_count}", inline=False)
    embed.add_field(name="Roles", value=f"{xrole}  ".replace(",  ", ""), inline=False)
    embed.add_field(name='Other Stats', value=f'<:discord_logo:534182147200909320>**Server ID**: \n`{server.id}` \n{nd}**Created**: \n`{server.created_at.strftime("%A, %B %d, %Y @ %H:%M.%S %p")}`', inline=False)
    embed.set_footer(text=server.name, icon_url=server.icon_url)

    await client.say(embed=embed)

@client.command(pass_context=True, name='userinfo', aliases=['ui', 'user'])
async def user_info(ctx, member:discord.Member=None):
        nm = "<:new_member:534180127022776330>"
        wump = ["<:new_discord1:534180127051874304>", "<:new_discord2:534180128238862346>"]
        nd = random.choice(wump)
        dl = "<:discord_logo:534182147200909320>"
        if member is None:
                member = ctx.message.author
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
        embed.add_field(name='Other Stats', value=f'{dl}**User ID**: \n`{member.id}` \n{nm}**Join Queue**: \n`{q}{af} member to join this server` \n{nm}**Joined**: \n`{member.joined_at.strftime("%A, %B %d, %Y @ %H:%M.%S %p")}` \n{nd}**Created**: \n`{member.created_at.strftime("%A, %B %d, %Y @ %H:%M.%S %p")}`', inline=False)
        embed.set_footer(text=member, icon_url=member.avatar_url)
        await client.say(embed=embed)

@client.command(pass_context=True)
async def avatar(ctx, member:discord.Member=None):
	if member is None:
		user = ctx.message.author
		embed = discord.Embed(title=f"{user.name}'s avatar", url=user.avatar_url, color=user.color)
		embed.set_image(url=user.avatar_url)
		await client.say(embed=embed)
	else:
		embed = discord.Embed(title=f"{member.name}'s avatar", url=member.avatar_url, color=member.color)
		embed.set_image(url=member.avatar_url)
		await client.say(embed=embed)

@client.command(pass_context=True)
async def ping(ctx):
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await client.send_typing(channel)
    t2 = time.perf_counter()
    ping=discord.Embed(title="Pong!", description='It took {}ms.'.format(round((t2-t1)*1000)), color=discord.Colour.green())
    await client.say(embed=ping)

@client.command(pass_context=True)
async def uptime(ctx):
        if ctx.message.author.id == 384866449174429698:
                delta_uptime = datetime.utcnow() - client.launch_time
                hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
                minutes, seconds = divmod(remainder, 60)
                days, hours = divmod(hours, 24)
                embed = discord.Embed(color=discord.Colour(0x6484BF))
                embed.set_author(name="Bot Uptime", icon_url="https://pivps.com/wp-content/uploads/2016/04/uptime-icon.png")
                embed.set_thumbnail(url='https://cdn2.iconfinder.com/data/icons/hosting-cloud-1/64/Uptime-512.png')
                embed.add_field(name='Days', value=f"{days}")
                embed.add_field(name='Hours', value=f"{hours}")
                embed.add_field(name='Minutes', value=f"{minutes}")
                embed.add_field(name='Seconds', value=f"{seconds}")
                await client.say(embed=embed)
        else:
                return


#Other

@client.group(pass_context=True)
async def subscribe(ctx):
    if ctx.invoked_subcommand is None:
        await client.say('Invalid feed. Use `j!subscribe <feed type>`')

@subscribe.command(name="youtube",pass_context=True)
async def _youtube(ctx):
    user = ctx.message.author
    role = discord.utils.get(user.server.roles, name="YouTube Feed")
    await client.add_roles(user, role)
    await client.say(f"{user.mention}, you are now subscribed to the YouTube Feed.")

@subscribe.command(name="twitter",pass_context=True)
async def _twitter(ctx):
    user = ctx.message.author
    role = discord.utils.get(user.server.roles, name="Twitter Feed")
    await client.add_roles(user, role)
    await client.say(f"{user.mention}, you are now subscribed to the Twitter Feed.")

@client.group(pass_context=True)
async def unsubscribe(ctx):
    if ctx.invoked_subcommand is None:
        await client.say('Invalid feed. Use `j!unsubscribe <feed type>`')

@unsubscribe.command(name="youtube",pass_context=True)
async def _youtube(ctx):
    user = ctx.message.author
    role = discord.utils.get(user.server.roles, name="YouTube Feed")
    await client.remove_roles(user, role)
    await client.say(f"{user.mention}, you are now unsubscribed to the YouTube Feed.")

@unsubscribe.command(name="twitter",pass_context=True)
async def _twitter(ctx):
    user = ctx.message.author
    role = discord.utils.get(user.server.roles, name="Twitter Feed")
    await client.remove_roles(user, role)
    await client.say(f"{user.mention}, you are now unsubscribed to the Twitter Feed.")

@client.command(pass_context=True)
async def suggest(ctx, *args):
    output = ''
    for word in args:
        output += word
        output += ' '
        embed = discord.Embed(color=discord.Colour(0x4D6FAF))
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        embed.add_field(name=f"{ctx.message.author.name}#{ctx.message.author.discriminator}", value=f"{output}")
        if ctx.message.attachments:
        	attachments = ctx.message.attachments[0]["url"]
        	embed.set_image(url=attachments)
        channel = discord.utils.get(ctx.message.server.channels, name="suggestions")
    sgs = await client.send_message(channel, embed=embed)
    emoji1 = get(client.get_all_emojis(), name='s_upvote')
    emoji2 = get(client.get_all_emojis(), name='s_downvote')
    await client.add_reaction(sgs, emoji1)
    await client.add_reaction(sgs, emoji2)
    await client.say(f"**Success!** Your suggestion has appeared in the {channel} channel!")

@commands.has_permissions(view_audit_logs=True)
@client.command(pass_context=True)
async def accept(ctx, id):
	suggestions = discord.utils.get(ctx.message.server.channels, name="suggestions")
	m = await client.get_message(suggestions, id)
	emoji = get(client.get_all_emojis(), name='tick1Green')
	await client.add_reaction(m, emoji)
	await client.say(f"{emoji} Suggestion marked as **accepted**.")

@commands.has_permissions(view_audit_logs=True)
@client.command(pass_context=True)
async def reject(ctx, id):
	suggestions = discord.utils.get(ctx.message.server.channels, name="suggestions")
	m = await client.get_message(suggestions, id)
	emoji = get(client.get_all_emojis(), name='tick3Red')
	await client.add_reaction(m, emoji)
	await client.say(f"{emoji} Suggestion marked as **rejected**.")

@commands.has_permissions(view_audit_logs=True)
@client.command(pass_context=True)
async def ignore(ctx, id):
	suggestions = discord.utils.get(ctx.message.server.channels, name="suggestions")
	m = await client.get_message(suggestions, id)
	emoji = get(client.get_all_emojis(), name='tick2Gray')
	await client.add_reaction(m, emoji)
	await client.say(f"{emoji} Suggestion marked as **ignored**.")

@commands.has_permissions(view_audit_logs=True)
@client.command(pass_context=True)
async def poll(ctx, question, *options: str):
        if len(options) <= 1:
            await client.say('You need more than one option to make a poll!')
            return
        if len(options) > 10:
            await client.say('You cannot make a poll for more than 10 things!')
            return

        if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
            reactions = ['\U0001f44d', '\U0001f44e']
        else:
            reactions = ['1\u20e3', '2\u20e3', '3\u20e3', '4\u20e3', '5\u20e3', '6\u20e3', '7\u20e3', '8\u20e3', '9\u20e3', '\U0001f51f']

        description = []
        for x, option in enumerate(options):
            description += '\n{} {}'.format(reactions[x], option)
        embed = discord.Embed(title=question, description=''.join(description), color=discord.Color.dark_green())
        react_message = await client.say(embed=embed)
        for reaction in reactions[:len(options)]:
            await client.add_reaction(react_message, reaction)
        embed.set_footer(text='Poll ID: {}'.format(react_message.id))
        await client.delete_message(ctx.message)
        await client.edit_message(react_message, embed=embed)


#Moderation

@commands.has_permissions(administrator=True)
@client.command(pass_context=True)
async def punish(ctx, member:discord.Member=None, *, reason=None):
	if member is None:
		await client.say('**Please specify a member! Use ping, ID, or name.**')
		return
	if member.server_permissions.view_audit_logs:
		await client.say('**You cannot punish a moderator!**')
		return
	if ctx.message.author.bot:
		return
	if reason is None:
		reason = "Unspecified"
	modlog = client.get_channel("515672869666029568")
	puns = 0
	msgs = []
	async for x in client.logs_from(modlog):
		msgs.append(x)
	for message in msgs:
		if str(member.id) in message.content:
			puns += 1
	if puns == 0:
		user = member
		modlog = discord.utils.get(ctx.message.server.channels, name="moderation-log")
		embed = discord.Embed(colour=discord.Colour(0xd3d3d3), timestamp=datetime.now())
		embed.set_author(name="Warn", icon_url="https://cdn.discordapp.com/attachments/362056767284445187/508026169971572743/628px-Attention_Sign.svg.png")
		embed.set_thumbnail(url=user.avatar_url)
		embed.add_field(name="User", value=f"{user.mention} ({user})")
		embed.add_field(name="Moderator", value=f"{ctx.message.author.mention} ({ctx.message.author})")
		embed.add_field(name="Reason", value=f"{reason}")
		await client.send_message(modlog, f"`+1 Infraction for {user}:` {user.id}", embed=embed)
		embed2 = discord.Embed(colour=discord.Colour(0xd3d3d3))
		embed2.set_author(name="Warning", icon_url="https://cdn.discordapp.com/attachments/362056767284445187/508026169971572743/628px-Attention_Sign.svg.png")
		await client.say(f'{user.mention}, you have been **warned** by {ctx.message.author.mention} for "**{reason}**"', embed=embed2)
	elif puns == 1:
                user = member
                modlog = discord.utils.get(ctx.message.server.channels, name="moderation-log")
                embed = discord.Embed(colour=discord.Colour(0xd3d3d3), timestamp=datetime.now())
                embed.set_author(name="Warn", icon_url="https://cdn.discordapp.com/attachments/362056767284445187/508026169971572743/628px-Attention_Sign.svg.png")
                embed.set_thumbnail(url=user.avatar_url)
                embed.add_field(name="User", value=f"{user.mention} ({user})")
                embed.add_field(name="Moderator", value=f"{ctx.message.author.mention} ({ctx.message.author})")
                embed.add_field(name="Reason", value=f"{reason}")
                await client.send_message(modlog, f"`+1 Infraction for {user}:` {user.id}", embed=embed)
                embed2 = discord.Embed(colour=discord.Colour(0xd3d3d3))
                embed2.set_author(name="Warning", icon_url="https://cdn.discordapp.com/attachments/362056767284445187/508026169971572743/628px-Attention_Sign.svg.png")
                await client.say(f'{user.mention}, you have been **warned** by {ctx.message.author.mention} for "**{reason}**"', embed=embed2)
	elif puns == 2:
                user = member
                duration = int(1 * 3600)
                modlog = discord.utils.get(ctx.message.server.channels, name="moderation-log")
                embed = discord.Embed(colour=discord.Colour(0xffff00), timestamp=datetime.now())
                embed.set_author(name="Tempmute", icon_url="https://img.icons8.com/metro/1600/mute.png")
                embed.set_thumbnail(url=user.avatar_url)
                embed.add_field(name="User", value=f"{user.mention} ({user})")
                embed.add_field(name="Moderator", value=f"{ctx.message.author.mention} ({ctx.message.author})")
                embed.add_field(name="Reason", value=f"{reason}")
                embed.add_field(name="Duration", value=f"1 hours")
                await client.send_message(modlog, f"`+1 Infraction for {user}:` {user.id}", embed=embed)
                embed2 = discord.Embed(colour=discord.Colour(0xffff00))
                embed2.set_author(name="Tempmute", icon_url="https://img.icons8.com/metro/1600/mute.png")
                await client.say(f'{user.mention}, you have been **muted** by {ctx.message.author.mention} for "**{reason}**" Duration: `1 hours`', embed=embed2)
                mute = discord.utils.get(member.server.roles, name="Muted")
                await client.add_roles(user, mute)
                await asyncio.sleep(duration)

                user = member
                modlog = discord.utils.get(ctx.message.server.channels, name="moderation-log")
                embed = discord.Embed(colour=discord.Colour(0x00ff00), timestamp=datetime.now())
                embed.set_author(name="Unmute", icon_url="https://www.cityphones.com.au/wp-content/uploads/2017/06/volume_mute-key-repair-200x200.png")
                embed.set_thumbnail(url=user.avatar_url)
                embed.add_field(name="User", value=f"{user.mention} ({user})")
                embed.add_field(name="Moderator", value=f"{ctx.message.author.mention} ({ctx.message.author})")
                embed.add_field(name="Reason", value=f"Duration of `1 hours` is finished")
                await client.send_message(modlog, embed=embed)
                embed2 = discord.Embed(colour=discord.Colour(0x00ff00))
                embed2.set_author(name="Unmute", icon_url="https://www.cityphones.com.au/wp-content/uploads/2017/06/volume_mute-key-repair-200x200.png")
                await client.say(f'{user.mention}, you have been **unmuted** for "**Duration of `1 hours` is finished**"', embed=embed2)
                await client.remove_roles(user, mute)
	elif puns == 3:
                user = member
                modlog = discord.utils.get(ctx.message.server.channels, name="moderation-log")
                embed = discord.Embed(colour=discord.Colour(0xffff00), timestamp=datetime.now())
                embed.set_author(name="Mute", icon_url="https://img.icons8.com/metro/1600/mute.png")
                embed.set_thumbnail(url=user.avatar_url)
                embed.add_field(name="User", value=f"{user.mention} ({user})")
                embed.add_field(name="Moderator", value=f"{ctx.message.author.mention} ({ctx.message.author})")
                embed.add_field(name="Reason", value=f"{reason}")
                await client.send_message(modlog, f"`+1 Infraction for {user}:` {user.id}", embed=embed)
                embed2 = discord.Embed(colour=discord.Colour(0xffff00))
                embed2.set_author(name="Mute", icon_url="https://img.icons8.com/metro/1600/mute.png")
                await client.say(f'{user.mention}, you have been **muted** by {ctx.message.author.mention} for "**{reason}**"', embed=embed2)
                mute = discord.utils.get(member.server.roles, name="Muted")
                await client.add_roles(user, mute)
	elif puns == 4:
                user = member
                modlog = discord.utils.get(ctx.message.server.channels, name="moderation-log")
                embed = discord.Embed(colour=discord.Colour(0xffff00), timestamp=datetime.now())
                embed.set_author(name="Mute", icon_url="https://img.icons8.com/metro/1600/mute.png")
                embed.set_thumbnail(url=user.avatar_url)
                embed.add_field(name="User", value=f"{user.mention} ({user})")
                embed.add_field(name="Moderator", value=f"{ctx.message.author.mention} ({ctx.message.author})")
                embed.add_field(name="Reason", value=f"{reason}")
                await client.send_message(modlog, f"`+1 Infraction for {user}:` {user.id}", embed=embed)
                embed2 = discord.Embed(colour=discord.Colour(0xffff00))
                embed2.set_author(name="Mute", icon_url="https://img.icons8.com/metro/1600/mute.png")
                await client.say(f'{user.mention}, you have been **muted** by {ctx.message.author.mention} for "**{reason}**"', embed=embed2)
                mute = discord.utils.get(member.server.roles, name="Muted")
                await client.add_roles(user, mute)
	else:
                await client.say(f"You decide. this person has {puns} infractions.")

@commands.has_permissions(view_audit_logs=True)
@client.command(pass_context=True)
async def infractions(ctx, member:discord.Member=None):
	if member is None:
		member = ctx.message.author
	if ctx.message.author.bot:
		return
	modlog = client.get_channel("515672869666029568")
	puns = 0
	msgs = []
	async for x in client.logs_from(modlog):
		msgs.append(x)
	for message in msgs:
		if str(member.id) in message.content:
			puns += 1
	if member.server_permissions.view_audit_logs:
                pun = "None"
	elif puns == 0:
		pun = "**Warn**"
	elif puns == 1:
		pun = "**Warn**"
	elif puns == 2:
		pun = "**1 Hour Mute**"
	elif puns == 3:
		pun = "**3 Day Mute**"
	elif puns == 4:
		pun = "**7 Day Mute**"
	else:
		pun = "**Undecided**"
	embed = discord.Embed(description=f"**{puns}** Infractions")
	embed.set_author(name=member, icon_url=member.avatar_url)
	embed.add_field(name="Next Punishment", value=pun, inline=False)
	await client.say(embed=embed)

@commands.has_permissions(view_audit_logs=True)
@client.command(pass_context=True)
async def warn(ctx,member:discord.Member=None, *, reason=None):
        if member is None:
                await client.say('**Please specify a member! Use ping, ID, or name.**')
                return
        if member.server_permissions.view_audit_logs:
                await client.say('**You cannot warn a moderator!**')
                return
        if ctx.message.author.bot:
                return
        if reason is None:
                user = member
                modlog = discord.utils.get(ctx.message.server.channels, name="moderation-log")
                embed = discord.Embed(colour=discord.Colour(0xd3d3d3), timestamp=datetime.now())
                embed.set_author(name="Warn", icon_url="https://cdn.discordapp.com/attachments/362056767284445187/508026169971572743/628px-Attention_Sign.svg.png")
                embed.set_thumbnail(url=user.avatar_url)
                embed.add_field(name="User", value=f"{user.mention} ({user})")
                embed.add_field(name="Moderator", value=f"{ctx.message.author.mention} ({ctx.message.author})")
                embed.add_field(name="Reason", value=f"Unspecified")
                await client.send_message(modlog, f"`+1 Infraction for {user}:` {user.id}", embed=embed)
                embed2 = discord.Embed(colour=discord.Colour(0xd3d3d3))
                embed2.set_author(name="Warning", icon_url="https://cdn.discordapp.com/attachments/362056767284445187/508026169971572743/628px-Attention_Sign.svg.png")
                await client.say(f'{user.mention}, you have been **warned** by {ctx.message.author.mention} for "**Unspecified**"', embed=embed2)
        else:
                user = member
                modlog = discord.utils.get(ctx.message.server.channels, name="moderation-log")
                embed = discord.Embed(colour=discord.Colour(0xd3d3d3), timestamp=datetime.now())
                embed.set_author(name="Warn", icon_url="https://cdn.discordapp.com/attachments/362056767284445187/508026169971572743/628px-Attention_Sign.svg.png")
                embed.set_thumbnail(url=user.avatar_url)
                embed.add_field(name="User", value=f"{user.mention} ({user})")
                embed.add_field(name="Moderator", value=f"{ctx.message.author.mention} ({ctx.message.author})")
                embed.add_field(name="Reason", value=f"{reason}")
                await client.send_message(modlog, f"`+1 Infraction for {user}:` {user.id}", embed=embed)
                embed2 = discord.Embed(colour=discord.Colour(0xd3d3d3))
                embed2.set_author(name="Warning", icon_url="https://cdn.discordapp.com/attachments/362056767284445187/508026169971572743/628px-Attention_Sign.svg.png")
                await client.say(f'{user.mention}, you have been **warned** by {ctx.message.author.mention} for "**{reason}**"', embed=embed2)

@commands.has_permissions(mute_members=True)
@client.command(pass_context=True)
async def tempmute(ctx,member:discord.Member=None, mutetime:int=None, *, reason=None):
        if member is None:
                await client.say('**Please specify a member! Use ping, ID, or name.**')
                return
        if member.server_permissions.view_audit_logs:
                await client.say('**You cannot mute/unmute a moderator!**')
                return
        if ctx.message.author.bot:
                return
        if mutetime is None:
                await client.say('**Please specify a mute time! Mute time is in hours.**')
                return
        if reason is None:
                user = member
                duration = int(mutetime * 3600)
                modlog = discord.utils.get(ctx.message.server.channels, name="moderation-log")
                embed = discord.Embed(colour=discord.Colour(0xffff00), timestamp=datetime.now())
                embed.set_author(name="Tempmute", icon_url="https://img.icons8.com/metro/1600/mute.png")
                embed.set_thumbnail(url=user.avatar_url)
                embed.add_field(name="User", value=f"{user.mention} ({user})")
                embed.add_field(name="Moderator", value=f"{ctx.message.author.mention} ({ctx.message.author})")
                embed.add_field(name="Reason", value=f"Unspecified")
                embed.add_field(name="Duration", value=f"{mutetime} hours")
                await client.send_message(modlog, f"`+1 Infraction for {user}:` {user.id}", embed=embed)
                embed2 = discord.Embed(colour=discord.Colour(0xffff00))
                embed2.set_author(name="Tempmute", icon_url="https://img.icons8.com/metro/1600/mute.png")
                await client.say(f'{user.mention}, you have been **muted** by {ctx.message.author.mention} for "**Unspecified**" Duration: `{mutetime} hours`', embed=embed2)
                mute = discord.utils.get(member.server.roles, name="Muted")
                await client.add_roles(user, mute)
                await asyncio.sleep(duration)
                
                user = member
                modlog = discord.utils.get(ctx.message.server.channels, name="moderation-log")
                embed = discord.Embed(colour=discord.Colour(0x00ff00), timestamp=datetime.now())
                embed.set_author(name="Unmute", icon_url="https://www.cityphones.com.au/wp-content/uploads/2017/06/volume_mute-key-repair-200x200.png")
                embed.set_thumbnail(url=user.avatar_url)
                embed.add_field(name="User", value=f"{user.mention} ({user})")
                embed.add_field(name="Moderator", value=f"{ctx.message.author.mention} ({ctx.message.author})")
                embed.add_field(name="Reason", value=f"Duration of `{mutetime} hours` is finished")
                await client.send_message(modlog, embed=embed)
                embed2 = discord.Embed(colour=discord.Colour(0x00ff00))
                embed2.set_author(name="Unmute", icon_url="https://www.cityphones.com.au/wp-content/uploads/2017/06/volume_mute-key-repair-200x200.png")
                await client.say(f'{user.mention}, you have been **unmuted** for "**Duration of `{mutetime} hours` is finished**"', embed=embed2)
                await client.remove_roles(user, mute)
        else:
                user = member
                duration = int(mutetime * 3600)
                modlog = discord.utils.get(ctx.message.server.channels, name="moderation-log")
                embed = discord.Embed(colour=discord.Colour(0xffff00), timestamp=datetime.now())
                embed.set_author(name="Tempmute", icon_url="https://img.icons8.com/metro/1600/mute.png")
                embed.set_thumbnail(url=user.avatar_url)
                embed.add_field(name="User", value=f"{user.mention} ({user})")
                embed.add_field(name="Moderator", value=f"{ctx.message.author.mention} ({ctx.message.author})")
                embed.add_field(name="Reason", value=f"{reason}")
                embed.add_field(name="Duration", value=f"{mutetime} hours")
                await client.send_message(modlog, f"`+1 Infraction for {user}:` {user.id}", embed=embed)
                embed2 = discord.Embed(colour=discord.Colour(0xffff00))
                embed2.set_author(name="Tempmute", icon_url="https://img.icons8.com/metro/1600/mute.png")
                await client.say(f'{user.mention}, you have been **muted** by {ctx.message.author.mention} for "**{reason}**" Duration: `{mutetime} hours`', embed=embed2)
                mute = discord.utils.get(member.server.roles, name="Muted")
                await client.add_roles(user, mute)
                await asyncio.sleep(duration)
                
                user = member
                modlog = discord.utils.get(ctx.message.server.channels, name="moderation-log")
                embed = discord.Embed(colour=discord.Colour(0x00ff00), timestamp=datetime.now())
                embed.set_author(name="Unmute", icon_url="https://www.cityphones.com.au/wp-content/uploads/2017/06/volume_mute-key-repair-200x200.png")
                embed.set_thumbnail(url=user.avatar_url)
                embed.add_field(name="User", value=f"{user.mention} ({user})")
                embed.add_field(name="Moderator", value=f"{ctx.message.author.mention} ({ctx.message.author})")
                embed.add_field(name="Reason", value=f"Duration of `{mutetime} hours` is finished")
                await client.send_message(modlog, embed=embed)
                embed2 = discord.Embed(colour=discord.Colour(0x00ff00))
                embed2.set_author(name="Unmute", icon_url="https://www.cityphones.com.au/wp-content/uploads/2017/06/volume_mute-key-repair-200x200.png")
                await client.say(f'{user.mention}, you have been **unmuted** for "**Duration of `{mutetime} hours` is finished**"', embed=embed2)
                await client.remove_roles(user, mute)

@commands.has_permissions(mute_members=True)
@client.command(pass_context=True)
async def mute(ctx,member:discord.Member=None, *, reason=None):
        if member is None:
                await client.say('**Please specify a member! Use ping, ID, or name.**')
                return
        if member.server_permissions.view_audit_logs:
                await client.say('**You cannot mute/unmute a moderator!**')
                return
        if ctx.message.author.bot:
                return
        if reason is None:
                user = member
                modlog = discord.utils.get(ctx.message.server.channels, name="moderation-log")
                embed = discord.Embed(colour=discord.Colour(0xffff00), timestamp=datetime.now())
                embed.set_author(name="Mute", icon_url="https://img.icons8.com/metro/1600/mute.png")
                embed.set_thumbnail(url=user.avatar_url)
                embed.add_field(name="User", value=f"{user.mention} ({user})")
                embed.add_field(name="Moderator", value=f"{ctx.message.author.mention} ({ctx.message.author})")
                embed.add_field(name="Reason", value=f"Unspecified")
                await client.send_message(modlog, f"`+1 Infraction for {user}:` {user.id}", embed=embed)
                embed2 = discord.Embed(colour=discord.Colour(0xffff00))
                embed2.set_author(name="Mute", icon_url="https://img.icons8.com/metro/1600/mute.png")
                await client.say(f'{user.mention}, you have been **muted** by {ctx.message.author.mention} for "**Unspecified**"', embed=embed2)
                mute = discord.utils.get(member.server.roles, name="Muted")
                await client.add_roles(user, mute)
        else:
                user = member
                modlog = discord.utils.get(ctx.message.server.channels, name="moderation-log")
                embed = discord.Embed(colour=discord.Colour(0xffff00), timestamp=datetime.now())
                embed.set_author(name="Mute", icon_url="https://img.icons8.com/metro/1600/mute.png")
                embed.set_thumbnail(url=user.avatar_url)
                embed.add_field(name="User", value=f"{user.mention} ({user})")
                embed.add_field(name="Moderator", value=f"{ctx.message.author.mention} ({ctx.message.author})")
                embed.add_field(name="Reason", value=f"{reason}")
                await client.send_message(modlog, f"`+1 Infraction for {user}:` {user.id}", embed=embed)
                embed2 = discord.Embed(colour=discord.Colour(0xffff00))
                embed2.set_author(name="Mute", icon_url="https://img.icons8.com/metro/1600/mute.png")
                await client.say(f'{user.mention}, you have been **muted** by {ctx.message.author.mention} for "**{reason}**"', embed=embed2)
                mute = discord.utils.get(member.server.roles, name="Muted")
                await client.add_roles(user, mute)

@commands.has_permissions(mute_members=True)
@client.command(pass_context=True)
async def unmute(ctx,member:discord.Member=None, *, reason=None):
        if member is None:
                await client.say('**Please specify a member! Use ping, ID, or name.**')
                return
        if member.server_permissions.view_audit_logs:
                await client.say('**You cannot mute/unmute a moderator!**')
                return
        if ctx.message.author.bot:
                return
        if reason is None:
                user = member
                modlog = discord.utils.get(ctx.message.server.channels, name="moderation-log")
                embed = discord.Embed(colour=discord.Colour(0x00ff00), timestamp=datetime.now())
                embed.set_author(name="Unmute", icon_url="https://www.cityphones.com.au/wp-content/uploads/2017/06/volume_mute-key-repair-200x200.png")
                embed.set_thumbnail(url=user.avatar_url)
                embed.add_field(name="User", value=f"{user.mention} ({user})")
                embed.add_field(name="Moderator", value=f"{ctx.message.author.mention} ({ctx.message.author})")
                embed.add_field(name="Reason", value=f"Unspecified")
                await client.send_message(modlog, embed=embed)
                embed2 = discord.Embed(colour=discord.Colour(0x00ff00))
                embed2.set_author(name="Unmute", icon_url="https://www.cityphones.com.au/wp-content/uploads/2017/06/volume_mute-key-repair-200x200.png")
                await client.say(f'{user.mention}, you have been **unmuted** by {ctx.message.author.mention} for "**Unspecified**"', embed=embed2)
                unmute = discord.utils.get(member.server.roles, name="Muted")
                await client.remove_roles(user, unmute)
        else:
                user = member
                modlog = discord.utils.get(ctx.message.server.channels, name="moderation-log")
                embed = discord.Embed(colour=discord.Colour(0x00ff00), timestamp=datetime.now())
                embed.set_author(name="Unmute", icon_url="https://www.cityphones.com.au/wp-content/uploads/2017/06/volume_mute-key-repair-200x200.png")
                embed.set_thumbnail(url=user.avatar_url)
                embed.add_field(name="User", value=f"{user.mention} ({user})")
                embed.add_field(name="Moderator", value=f"{ctx.message.author.mention} ({ctx.message.author})")
                embed.add_field(name="Reason", value=f"{reason}")
                await client.send_message(modlog, embed=embed)
                embed2 = discord.Embed(colour=discord.Colour(0x00ff00))
                embed2.set_author(name="Unmute", icon_url="https://www.cityphones.com.au/wp-content/uploads/2017/06/volume_mute-key-repair-200x200.png")
                await client.say(f'{user.mention}, you have been **unmuted** by {ctx.message.author.mention} for "**{reason}**"', embed=embed2)
                unmute = discord.utils.get(member.server.roles, name="Muted")
                await client.remove_roles(user, unmute)

@commands.has_permissions(kick_members=True)
@client.command(pass_context=True)
async def kick(ctx,member:discord.Member=None, *, reason=None):
        if member is None:
                await client.say('**Please specify a member! Use ping, ID, or name.**')
                return
        if member.server_permissions.view_audit_logs:
                await client.say('**You cannot kick a moderator!**')
                return
        if ctx.message.author.bot:
                return
        if reason is None:
                user = member
                modlog = discord.utils.get(ctx.message.server.channels, name="moderation-log")
                embed = discord.Embed(colour=discord.Colour(0xffa500), timestamp=datetime.now())
                embed.set_author(name="Kick", icon_url="https://static.thenounproject.com/png/380644-200.png")
                embed.set_thumbnail(url=user.avatar_url)
                embed.add_field(name="User", value=f"{user.mention} ({user})")
                embed.add_field(name="Moderator", value=f"{ctx.message.author.mention} ({ctx.message.author})")
                embed.add_field(name="Reason", value=f"Unspecified")
                await client.send_message(modlog, f"`+1 Infraction for {user}:` {user.id}", embed=embed)
                embed2 = discord.Embed(colour=discord.Colour(0xffa500))
                embed2.set_author(name="Kick", icon_url="https://static.thenounproject.com/png/380644-200.png")
                await client.say(f'**{user}** has been **kicked** by {ctx.message.author.mention} for "**Unspecified**"', embed=embed2)
                await client.kick(user)
        else:
                user = member
                modlog = discord.utils.get(ctx.message.server.channels, name="moderation-log")
                embed = discord.Embed(colour=discord.Colour(0xffa500), timestamp=datetime.now())
                embed.set_author(name="Kick", icon_url="https://static.thenounproject.com/png/380644-200.png")
                embed.set_thumbnail(url=user.avatar_url)
                embed.add_field(name="User", value=f"{user.mention} ({user})")
                embed.add_field(name="Moderator", value=f"{ctx.message.author.mention} ({ctx.message.author})")
                embed.add_field(name="Reason", value=f"{reason}")
                await client.send_message(modlog, f"`+1 Infraction for {user}:` {user.id}", embed=embed)
                embed2 = discord.Embed(colour=discord.Colour(0xffa500))
                embed2.set_author(name="Kick", icon_url="https://static.thenounproject.com/png/380644-200.png")
                await client.say(f'**{user}** has been **kicked** by {ctx.message.author.mention} for "**{reason}**"', embed=embed2)
                await client.kick(user)

@commands.has_permissions(ban_members=True)
@client.command(pass_context=True)
async def ban(ctx,member:discord.Member=None, *, reason=None):
        if member is None:
                await client.say('**Please specify a member! Use ping, ID, or name.**')
                return
        if member.server_permissions.view_audit_logs:
                await client.say('**You cannot ban a moderator!**')
                return
        if ctx.message.author.bot:
                return
        if reason is None:
                user = member
                modlog = discord.utils.get(ctx.message.server.channels, name="moderation-log")
                embed = discord.Embed(colour=discord.Colour(0xff0000), timestamp=datetime.now())
                embed.set_author(name="Ban", icon_url="https://i.imgur.com/tq43DIX.jpg")
                embed.set_thumbnail(url=user.avatar_url)
                embed.add_field(name="User", value=f"{user.mention} ({user})")
                embed.add_field(name="Moderator", value=f"{ctx.message.author.mention} ({ctx.message.author})")
                embed.add_field(name="Reason", value=f"Unspesified")
                await client.send_message(modlog, f"`+1 Infraction for {user}:` {user.id}", embed=embed)
                embed2 = discord.Embed(colour=discord.Colour(0xff0000))
                embed2.set_author(name="Ban", icon_url="https://i.imgur.com/tq43DIX.jpg")
                embed2.set_image(url="https://i.imgur.com/O3DHIA5.gif")
                await client.say(f'**{user}** has been **BANNED** by {ctx.message.author.mention} for "**Unspecified**"', embed=embed2)
                await client.ban(user)
        else:
                user = member
                modlog = discord.utils.get(ctx.message.server.channels, name="moderation-log")
                embed = discord.Embed(colour=discord.Colour(0xff0000), timestamp=datetime.now())
                embed.set_author(name="Ban", icon_url="https://i.imgur.com/tq43DIX.jpg")
                embed.set_thumbnail(url=user.avatar_url)
                embed.add_field(name="User", value=f"{user.mention} ({user})")
                embed.add_field(name="Moderator", value=f"{ctx.message.author.mention} ({ctx.message.author})")
                embed.add_field(name="Reason", value=f"{reason}")
                await client.send_message(modlog, f"`+1 Infraction for {user}:` {user.id}", embed=embed)
                embed2 = discord.Embed(colour=discord.Colour(0xff0000))
                embed2.set_author(name="Ban", icon_url="https://i.imgur.com/tq43DIX.jpg")
                embed2.set_image(url="https://i.imgur.com/O3DHIA5.gif")
                await client.say(f'**{user}** has been **BANNED** by {ctx.message.author.mention} for "**{reason}**"', embed=embed2)
                await client.ban(user)

@commands.has_permissions(manage_messages=True)
@client.command(pass_context=True)
async def clear(ctx, amount=10):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await client.delete_messages(messages)
    dmsg = await client.say('Messages deleted.')
    await asyncio.sleep(5)
    await client.delete_message(dmsg)

@commands.has_permissions(manage_channels=True)
@client.command(pass_context=True)
async def lock(ctx):
    server = ctx.message.server
    author = ctx.message.author
    channel = ctx.message.channel
    role = server.default_role
    overwrite = channel.overwrites_for(role)
    overwrite.send_messages = False
    overwrite.add_reactions = False
    await client.edit_channel_permissions(channel, role, overwrite)
    embed=discord.Embed(title="Channel Locked!", description=f"Chat was locked by **{author}**!", color=0xff0000)
    await client.say(embed=embed)
    await client.delete_message(ctx.message)

@commands.has_permissions(manage_channels=True)
@client.command(pass_context=True)
async def unlock(ctx):
    server = ctx.message.server
    author = ctx.message.author
    channel = ctx.message.channel
    role = server.default_role
    overwrite = channel.overwrites_for(role)
    overwrite.send_messages = True
    overwrite.add_reactions = True
    await client.edit_channel_permissions(channel, role, overwrite)
    embed=discord.Embed(title="Channel Unlocked!", description=f"Chat was unlocked by **{author}**!", color=0x00ff00)
    await client.say(embed=embed)
    await client.delete_message(ctx.message)


#Fun

@client.command(pass_context=True, aliases=['dice'])
async def roll(ctx, dice : str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await client.say('Format has to be in NdN!')
        return
    author = ctx.message.author
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await client.say(f"{author.mention} :game_die: \n**Dice:** {dice} \n**Result:** {result}")

@client.command(name='8ball', aliases=['8'], pass_context=True)
async def eight_ball(ctx):
    author = ctx.message.author
    content = ctx.message.content
    possible_responses = [
        ':white_check_mark: It is certain.',
        ':white_check_mark: It is decidedly so.',
        ':white_check_mark: Without a doubt.',
        ':white_check_mark: Yes. Definitely.',
        ':white_check_mark: You may rely on it.',
        ':white_check_mark: As I see it, yes.',
        ':white_check_mark: Most likely.',
        ':white_check_mark: Outlook good.',
        ':white_check_mark: Yes.',
        ':white_check_mark: Signs point to yes.',
        ':8ball: Reply hazy. Try again.',
        ':8ball: Ask again later.',
        ':8ball: Better not tell you now.',
        ':8ball: Cannot predict now.',
        ':8ball: Concentrate and ask again.',
        ":no_entry_sign: Don't count on it.",
        ':no_entry_sign: My reply is no.',
        ':no_entry_sign: My sources say no.',
        ':no_entry_sign: Outlook not so good.',
        ':no_entry_sign: Very doubtful.',
    ]
    question=discord.Embed(title="{}".format(author), description='{}'.format(content.replace("j!8ball", "**Question:** ")), color=discord.Colour.blue())

    await client.say(random.choice(possible_responses), embed=question)

@client.command(name='coinflip', aliases=['cf'], pass_context=True)
async def coin(ctx):
    author = ctx.message.author
    possible_responses = [
        '{} flips a coin. It lands on **Heads**!'.format(author.mention),
        '{} flips a coin. It lands on **Tails**!'.format(author.mention),
    ]
    await client.say(random.choice(possible_responses))
    
@client.command()
async def protip():
	protip1 = discord.Embed(description='Use A Toilet Seat To Put Your Plate On While Watching TV', color=random.randint(0, 0xFFFFFF))
	protip1.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-41-5891ea45d1044__605.jpg')
	
	protip2 = discord.Embed(description="Take A Selfie Through A Toilet Roll Tube And Pretend You're The Moon", color=random.randint(0, 0xFFFFFF))
	protip2.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-3-5891bd5f4942c__605.jpg')
	
	protip3 = discord.Embed(description='Cut Your Tennis Balls In Half To Store Two More Balls In Each Can, Saving Space', color=random.randint(0, 0xFFFFFF))
	protip3.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-14-5891bd7badf7a__605.jpg')
	
	protip4 = discord.Embed(description='Sneak A Chocolate Into American Movie Theatres With This Trick', color=random.randint(0, 0xFFFFFF))
	protip4.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-45-5891dd7067b4d__605.jpg')
	
	protip5 = discord.Embed(description='Use The Metal Part Of Your Seat Belt To Open Beers While Driving', color=random.randint(0, 0xFFFFFF))
	protip5.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-20-5891bd8a69ce4__605.jpg')
	
	protip6 = discord.Embed(description="Magnify Your Phone's Screen By Putting It In A Glass Of Water", color=random.randint(0, 0xFFFFFF))
	protip6.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-5891d320973de__605.jpg')
	
	protip7 = discord.Embed(description="Put Your New Tv Box On Your Neighbor's Side So You Wouldn't Get Robbed", color=random.randint(0, 0xFFFFFF))
	protip7.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-30-5891e0bf62a3f__605.jpg')
	
	protip8 = discord.Embed(description="Use Laptop Chargers To Heat Snacks Up", color=random.randint(0, 0xFFFFFF))
	protip8.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-76-5891f8824f2cb__605.jpg')
	
	protip9 = discord.Embed(description="Put A Bean Filled Glove On Your Baby's Back When You Want Your Kids To Feel Loved, But You're Too Tired", color=random.randint(0, 0xFFFFFF))
	protip9.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-17-5891bd8487d24__605.jpg')
	
	protip10 = discord.Embed(description='Tired Of Ironing Your Shirts? Get Fat And Watch Those Creases Vanish', color=random.randint(0, 0xFFFFFF))
	protip10.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-41-5891e2d419864__605.jpg')
	
	protip11 = discord.Embed(description='If You See Someone Crying, Ask If It Is Because Of Their Haircut', color=random.randint(0, 0xFFFFFF))
	protip11.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-53-5891e03332723__605.jpg')
	
	protip12 = discord.Embed(description='Stop Tears In The Kitchen With This Life Hack', color=random.randint(0, 0xFFFFFF))
	protip12.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-74-5891f5e143a59__605.jpg')
	
	protip13 = discord.Embed(description='Save Time By Adding Toothpaste To Your Food', color=random.randint(0, 0xFFFFFF))
	protip13.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-4-5891bd616ad54__605.jpg')
	
	protip14 = discord.Embed(description='Use This Tip When You Want To Take A S**t Discretely', color=random.randint(0, 0xFFFFFF))
	protip14.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-55-5891e0aae6989__605.jpg')
	
	protip15 = discord.Embed(description='Use Your Hood As A Bowl For Popcorns', color=random.randint(0, 0xFFFFFF))
	protip15.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-44-5891f014bf47e__605.jpg')
	
	protip16 = discord.Embed(description='Use Your Cat To Clean Your Floors And Save On Expensive Store-Bought Cleaners', color=random.randint(0, 0xFFFFFF))
	protip16.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-45-5891f2305773e__605.jpg')
	
	protip17 = discord.Embed(description='Plug A Surge Protector Into Itself For Infinite Power', color=random.randint(0, 0xFFFFFF))
	protip17.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-32-5891d6d36aee2__605.jpg')
	
	protip18 = discord.Embed(description='Use This Go Go Gadget On A Sunny Day Out For A Hands Free Experience', color=random.randint(0, 0xFFFFFF))
	protip18.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-75-5891f6b18e45a__605.jpg')
	
	protip19 = discord.Embed(description='Just Add Water For A Quick And Easy Pasta', color=random.randint(0, 0xFFFFFF))
	protip19.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-36-5891db3ce6535__605.jpg')
	
	protip20 = discord.Embed(description='Check If You Are Colorblind With This Useful Image', color=random.randint(0, 0xFFFFFF))
	protip20.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-9-5891bd6ea8cc3__605.jpg')
	
	protip21 = discord.Embed(description="Eat For Free For The Rest Of Your Life", color=random.randint(0, 0xFFFFFF))
	protip21.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-56-5891e0f438743__605.jpg')
	
	protip22 = discord.Embed(description="Reverse Your Window A/C Unit Like So To Save On A Costly Heating. It's Also Good For The Environment Because It Cools The Outside, Reducing Global Warming", color=random.randint(0, 0xFFFFFF))
	protip22.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-35-5891d756ad7ba__605.jpg')
	
	protip23 = discord.Embed(description="Use This Hack When Your Car Heater Doesn't Work", color=random.randint(0, 0xFFFFFF))
	protip23.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-32-5891e4907d329__605.jpg')
	
	protip24 = discord.Embed(description="Use A Fork In Case You Haven't Mastered Chopsticks Yet", color=random.randint(0, 0xFFFFFF))
	protip24.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-72-5891f2cd2b10b__605.jpg')
	
	protip25 = discord.Embed(description="Put A Plastic Bag Over Your Head To Make You Pass Out So Work Feels Shorter", color=random.randint(0, 0xFFFFFF))
	protip25.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-70-5891eef13e1da__605.jpg')
	
	protip26 = discord.Embed(description="Buy As Many Tickets As You Can Afford", color=random.randint(0, 0xFFFFFF))
	protip26.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-47-5891de3a01177__605.jpg')
	
	protip27 = discord.Embed(description="Sign All Of Your Blank Checks Now To Save Time Writing Future Checks", color=random.randint(0, 0xFFFFFF))
	protip27.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-42-5891ec8133083__605.jpg')
	
	protip28 = discord.Embed(description="Use These To Make Your Car Stop Beeping", color=random.randint(0, 0xFFFFFF))
	protip28.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-1-5891bd59e031c__605.jpg')
	
	protip29 = discord.Embed(description="Use This Trick To Make Teacher Think You Are Studying While You're Eating Spaghetti", color=random.randint(0, 0xFFFFFF))
	protip29.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-48-5891de6d71798__605.jpg')
	
	protip30 = discord.Embed(description="Don't Waste Money On A Can Of Air, Just Wash Your Dusty Motherboard With Your Dishes", color=random.randint(0, 0xFFFFFF))
	protip30.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-50-5891df264c53a__605.jpg')
	
	protip31 = discord.Embed(description="Secure Your Lunch With A Padlock", color=random.randint(0, 0xFFFFFF))
	protip31.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-69-5891ee0d61cff__605.jpg')
	
	protip32 = discord.Embed(description="Use Old Keyboard When You Are Short Of Hangers", color=random.randint(0, 0xFFFFFF))
	protip32.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-79-5891fe382fb7e__605.jpg')
	
	protip33 = discord.Embed(description="Release Ants Into Your Toaster To Remove Bread Crumbs That Accumulate At The Bottom Which Can Pose A Fire Hazard", color=random.randint(0, 0xFFFFFF))
	protip33.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-35-5891e6de35da0__605.jpg')
	
	protip34 = discord.Embed(description="Change Your Iphone 5s Color Within Seconds", color=random.randint(0, 0xFFFFFF))
	protip34.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-54-5891e08847d10__605.jpg')
	
	protip35 = discord.Embed(description="Money Tip", color=random.randint(0, 0xFFFFFF))
	protip35.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-15-5891bd7e8bbd8__605.jpg')
	
	protip36 = discord.Embed(description="Water Cool Your Computer When It's Running Too Hot To Keep The Temperatures Down", color=random.randint(0, 0xFFFFFF))
	protip36.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-64-5891e38a1997b__605.jpg')
	
	protip37 = discord.Embed(description="Use A High-Powered Box Fan And Funnel To Quickly Paint Interior Walls", color=random.randint(0, 0xFFFFFF))
	protip37.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-38-5891e7f88fbae__605.jpg')
	
	protip38 = discord.Embed(description="Put Earplugs In Your Nose To Make It Harder To Breathe", color=random.randint(0, 0xFFFFFF))
	protip38.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-19-5891bd88668ef__605.jpg')
	
	protip39 = discord.Embed(description="Make Homemade Wet Wipes By Soaking Toilet Paper Under Warm Water", color=random.randint(0, 0xFFFFFF))
	protip39.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-39-5891dc29b62fd__605.jpg') 
	
	protip40 = discord.Embed(description="Put A Can Of Beer Between Your Legs When There Is No Beer Holder In Your Car", color=random.randint(0, 0xFFFFFF))
	protip40.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-51-5891df6d121b5__605.jpg')
	
	protip41 = discord.Embed(description="Access iPhone 7 Headphone Jack With This Simple Hack", color=random.randint(0, 0xFFFFFF))
	protip41.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-65-5891e4333fe61__605.jpg')
	
	protip42 = discord.Embed(description="Roll Your Window Down, Put A Six Pack Of Beer On It And Roll It Back Up To Keep Half Your Beer Cold On Your Commute To Work", color=random.randint(0, 0xFFFFFF))
	protip42.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-58-5891e175232fb__605.jpg')
	
	protip43 = discord.Embed(description="Spray Yourself In The Eyes With Windex To Quickly Clean Your Contacts Without The Hassle Of Removing Them", color=random.randint(0, 0xFFFFFF))
	protip43.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-48-5891f4f12575c__605.jpg')
	
	protip44 = discord.Embed(description="Use A Hair Dryer And An Iron To Preheat A Pizza If You Don't Have A Microwave", color=random.randint(0, 0xFFFFFF))
	protip44.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-5-5891bd64af36c__605.jpg')
	
	protip45 = discord.Embed(description="Use Plastic Wrap As A Waterproof Phone Case", color=random.randint(0, 0xFFFFFF))
	protip45.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-24-5891bd948a3bd__605.jpg')
	
	protip46 = discord.Embed(description="Use An Extension Cord To Maximize The Length When Phone Charger Is Too Short To Reach The Outlet", color=random.randint(0, 0xFFFFFF))
	protip46.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-46-5891dde0080ff__605.jpg')
	
	protip47 = discord.Embed(description="Use Knives To Hang Shit Without Damaging Anything", color=random.randint(0, 0xFFFFFF))
	protip47.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-37-5891db8565c6f__605.jpg')
	
	protip48 = discord.Embed(description="Combine Bathroom Breaks And Lunch Breaks To Maximise Time Efficiency", color=random.randint(0, 0xFFFFFF))
	protip48.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-59-5891e1afdc4a4__605.jpg')
	
	protip49 = discord.Embed(description="Use This Tip If You Are A Student", color=random.randint(0, 0xFFFFFF))
	protip49.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-46-5891f3b29934b__605.jpg')
	
	protip50 = discord.Embed(description="Spilt Coffee On Your Pants And Don't Want To Look Like A Clumsy Dork? Just Soak Your Pants In A Tub Of Coffee So They Turn Into A Uniform Color Again", color=random.randint(0, 0xFFFFFF))
	protip50.set_image(url='https://static.boredpanda.com/blog/wp-content/uploads/2017/02/shitty-life-pro-tips-18-5891bd8681237__605.jpg')
	
	
	choices = [protip1,
	protip2,
	protip3,
	protip4,
	protip5,
	protip6,
	protip7,
	protip8,
	protip9,
	protip10,
	protip11,
	protip12,
	protip13,
	protip14,
	protip15,
	protip16,
	protip17,
	protip18,
	protip19,
	protip20,
	protip21,
	protip22,
	protip23,
	protip24,
	protip25,
	protip26,
	protip27,
	protip28,
	protip29,
	protip30,
	protip31,
	protip32,
	protip33,
	protip34,
	protip35,
	protip36,
	protip37,
	protip38,
	protip39,
	protip40,
	protip41,
	protip42,
	protip43,
	protip44,
	protip45,
	protip46,
	protip47,
	protip48,
	protip49,
	protip50]
	
	protip = random.choice(choices)
	
	await client.say(embed=protip)


@client.command(pass_context=True)
async def cat(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get('http://aws.random.cat/meow') as r:
            res = await r.json()
            embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
            embed.set_image(url=res['file'])
            await client.say(embed=embed)

@client.command(pass_context=True)
async def dog(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://dog.ceo/api/breeds/image/random') as r:
            res = await r.json()
            embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
            embed.set_image(url=res['message'])
            await client.say(embed=embed)

@client.command(pass_context=True)
async def umbo(ctx, emoji:discord.Emoji=None):
	embed = discord.Embed()
	embed.set_image(url=emoji.url)
	await client.say(embed=embed)

@client.command(aliases=["amp"], pass_context = True)
async def amplify(ctx, *, inp):
        if "@everyone" in ctx.message.content:
                await client.say('niCE TrY Guy')
                return
        if "@here" in ctx.message.content:
                await client.say('NiCE tRY guY')
                return
        else:
                await client.say(''.join(c.upper() if random.randint(0, 1) == 1 else c.lower() for c in inp))

@client.command(pass_context=True, aliases=["clap"])
async def clapify(ctx, *args):
        if "@everyone" in ctx.message.content:
                await client.say('\U0001f44f Forget \U0001f44f that \U0001f44f')
                return
        if "@here" in ctx.message.content:
                await client.say('\U0001f44f Forget \U0001f44f that \U0001f44f')
                return
        else:
                output = '\U0001f44f '
                for word in args:
                        output += word
                        output += ' \U0001f44f '
                await client.say(output)

@client.command(pass_context=True)
async def split(ctx, split, *args):
        if "@everyone" in ctx.message.content:
                await client.say(f'{split} Forget {split} that {split}')
                return
        if "@here" in ctx.message.content:
                await client.say(f'{split} Forget {split} that {split}')
                return
        else:
                output = f'{split} '
                for word in args:
                        output += word
                        output += f' {split} '
                await client.say(output)

@client.command(pass_context=True)
async def quote(ctx, id=None, chan=None):
        if id is None:
                await client.say('Please specify the ID of the message!')
                return
        else:
                try:
                        if chan is None:
                                chan = ctx.message.channel
                        m = await client.get_message(chan, id)
                        embed = discord.Embed(description=m.content, timestamp=m.timestamp)
                        if m.attachments:
                                attachments = m.attachments[0]["url"]
                                embed.set_image(url=attachments)
                        embed.set_author(name=m.author, icon_url=m.author.avatar_url)
                        await client.say(embed=embed)
                except:
                        await client.say("Message not found. If the message is in another channel, specify the message channel after the message ID.")
                        return

"""
async def snipe():
	@client.event
	async def on_message_delete(message):
		
		@client.command()
		async def snipe():
			embed = discord.Embed(description=message.content, timestamp=message.timestamp)
			embed.set_author(name=message.author, icon_url=message.author.avatar_url)
			await client.send_message(message.channel, embed=embed)

client.loop.create_task(snipe())
"""
@client.command(pass_context=True)
async def rps(ctx):
    os.system('cls' if os.name=='nt' else 'clear')
    while (1 < 2):
        R = "\U0001f5ff"
        P = "\U0001f4c4"
        S = "\U00002702"
        choices = [R, P, S]
        reactu = await client.say("Rock, Paper, Scissors - Shoot!")
        await client.add_reaction(reactu, emoji=R)
        await client.add_reaction(reactu, emoji=P)
        await client.add_reaction(reactu, emoji=S)
        
        userChoice = await client.wait_for_reaction(emoji=choices, user=ctx.message.author, message=reactu)
        opponenetChoice = random.choice(choices)
        
        embed = discord.Embed()
        embed.add_field(name=f"{ctx.message.author.name} chose:", value=userChoice.reaction.emoji, inline=True)
        embed.add_field(name="I chose:", value=opponenetChoice, inline=True)
        
        if opponenetChoice == userChoice.reaction.emoji:
            embed.set_author(name="It's a draw! ", icon_url="https://cdn.discordapp.com/attachments/516376650230005760/531975616296124457/SmartSelect_20181222-090652_Gallery.png")
        elif opponenetChoice == R and userChoice.reaction.emoji == S:
            embed.set_author(name="Rock beats scissors, I win! ", icon_url="https://cdn.discordapp.com/attachments/516376650230005760/531975616745177128/SmartSelect_20181222-090546_Gallery.png")
        elif opponenetChoice == S and userChoice.reaction.emoji == P:
            embed.set_author(name="Scissors beats paper! I win! ", icon_url="https://cdn.discordapp.com/attachments/516376650230005760/531975616745177128/SmartSelect_20181222-090546_Gallery.png")
        elif opponenetChoice == P and userChoice.reaction.emoji == R:
            embed.set_author(name="Paper beats rock, I win! ", icon_url="https://cdn.discordapp.com/attachments/516376650230005760/531975616745177128/SmartSelect_20181222-090546_Gallery.png")
        else:
            embed.set_author(name=f"{ctx.message.author.name} wins!", icon_url="https://cdn.discordapp.com/attachments/516376650230005760/531975616296124456/SmartSelect_20181222-090844_Gallery.png")
        await client.say(embed=embed)
        return


#Starboard
	
@client.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    message = reaction.message
    author = reaction.message.author
    starboard = discord.utils.get(reaction.message.server.channels, name="starboard")
    if reaction.message.author.bot:
    	return
    if reaction.emoji == "\U00002b50" and user == reaction.message.author:
    	await client.remove_reaction(message, reaction.emoji, author)
    if reaction.emoji == "\U00002b50" and user != reaction.message.author:
    	if str(reaction.count) == "3":
    		embed = discord.Embed(description=f"{message.content} \n\n➜[Jump to message](https://discordapp.com/channels/{reaction.message.server.id}/{reaction.message.channel.id}/{reaction.message.id})", color=discord.Colour.gold(), timestamp=message.timestamp)
    		embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
    		if message.attachments:
    			attachments = reaction.message.attachments[0]["url"]
    			embed.set_image(url=attachments)
    		starbom = await client.send_message(starboard, f"{reaction.emoji} <#{channel.id}> ID: {message.id}", embed=embed)
    		@client.event
    		async def on_reaction_remove(reaction, user):
    			if reaction.message.author.bot:
    				return
    			if reaction.emoji == "\U00002b50":
    				if str(reaction.count) == "2":
    					await client.delete_message(starbom)


#Support DM

@client.event
async def on_message(message):
	support = client.get_channel("543108414893719612")
	if message.server is None and message.author != client.user:
		yay = await client.send_message(message.channel, f"{message.author.mention}, message sent to the support team! Give them some time to reply and thanks for reaching out!")
		embed = discord.Embed(description=message.content)
		embed.set_author(name=message.author, icon_url=message.author.avatar_url)
		await client.send_message(support, f"`j!reply {message.author.id}`", embed=embed)
		await asyncio.sleep(10)
		await client.delete_message(yay)
	await client.process_commands(message)

@client.command(pass_context=True, aliases=["msg", "reply"])
async def message(ctx, user, *, words):
        if str(ctx.message.channel.id) == "543108414893719612":
                helper = ctx.message.author
                jon = discord.utils.get(ctx.message.server.roles, name="John Bob")
                dev = discord.utils.get(ctx.message.server.roles, name="Developer")
                admin = discord.utils.get(ctx.message.server.roles, name="Admins")
                mod = discord.utils.get(ctx.message.server.roles, name="Mods")
                if jon in helper.roles:
                        pos = "[John Bob] "
                elif dev in helper.roles:
                        pos = "[Developer] "
                elif admin in helper.roles:
                        pos = "[Admin] "
                elif mod in helper.roles:
                        pos = "[Mod] "
                else:
                        pos = ""
                        return
                
                person = await client.get_user_info(user)
                bigchan = client.get_channel("543108414893719612")
                
                embed = discord.Embed(description=words, color=helper.color)
                embed.set_author(name=f"{pos}{helper}", icon_url=helper.avatar_url)
                embed.set_footer(text="Send a message to reply...")
                
                cool = discord.Embed(description=words, color=helper.color)
                cool.set_author(name=f"{pos}{helper}", icon_url=helper.avatar_url)
                cool.set_footer(text=f"Replying to {person}")
                
                await client.send_message(person, embed=embed)
                await client.send_message(bigchan, f"`j!reply {person.id}`", embed=cool)
                await client.delete_message(ctx.message)
        else:
                return



#Errors

@client.event
async def on_command_error(error, ctx):
	place = ctx.message.server
	if isinstance(error, commands.CommandNotFound):
                return
	if isinstance(error, commands.UserInputError):
                return
	dude = ctx.message.author
	command = ctx.message.content
	channel = client.get_channel('542183507649232907')
	await client.send_message(channel, f"<:priority2:542154064218292226> __**{place}**__ \n**{dude}**: `{command}` \n\n```{error}```")
#	embed = discord.Embed()
#	embed.add_field(name="<:priority2:542154064218292226> Error", value=f"Server: **{place}** \nUser: **{dude}** \nCommand: `{command}`", inline=False)
#	embed.add_field(name="Traceback", value=f"```{error}```", inline=False)
#	await client.send_message(channel, embed=embed)




client.run('NTA3NDMyMjk5NDAzNTQyNTM5.DzuCFg.J6jZaXibF-Xw8D5Dx76ZOD4uddE')
