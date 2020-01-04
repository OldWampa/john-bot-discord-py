import discord
from discord.ext import commands
from discord.utils import get
#import requests

class suggest:
    def __init__(self, client):
        self.client = client
        
    @commands.command(pass_context=True)
    async def suggest(self, ctx, *args):
        output = ''
        for word in args:
            output += word
            output += ' '
        embed = discord.Embed(description=output, color=discord.Colour(0x00c4ff))
        embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        if ctx.message.attachments:
            attachments = ctx.message.attachments[0]["url"]
            embed.set_thumbnail(url=attachments)
        channel = discord.utils.get(ctx.message.server.channels, name="suggestions")
        sgs = await self.client.send_message(channel, embed=embed)
        #data = {}
        #data["content"] = output
        #data["username"] = ctx.message.author.name
        #data["avatar_url"] = ctx.message.author.avatar_url
        #result = requests.post("https://ptb.discordapp.com/api/webhooks/661405400591106048/rKmDECLm8vUKy8TZsI3OtIVC78PcvBuRONiWvbfclczmmT0cbdlfQsGI04CK8snJ9jVe", data=json.dumps(data), headers={"Content-Type": "application/json"})
        emoji1 = get(self.client.get_all_emojis(), name='s_upvote')
        emoji2 = get(self.client.get_all_emojis(), name='s_downvote')
        await self.client.add_reaction(sgs, emoji1)
        await self.client.add_reaction(sgs, emoji2)
        await self.client.say(f"**Success!** Your suggestion has appeared in the {channel} channel!")

    @commands.has_permissions(view_audit_logs=True)
    @commands.command(pass_context=True)
    async def accept(self, ctx, id):
        suggestions = discord.utils.get(ctx.message.server.channels, name="suggestions")
        m = await self.client.get_message(suggestions, id)
        emoji = get(self.client.get_all_emojis(), name='tick1Green')
        await self.client.add_reaction(m, emoji)
        await self.client.say(f"{emoji} Suggestion marked as **accepted**.")

    @commands.has_permissions(view_audit_logs=True)
    @commands.command(pass_context=True)
    async def reject(self, ctx, id):
        suggestions = discord.utils.get(ctx.message.server.channels, name="suggestions")
        m = await self.client.get_message(suggestions, id)
        emoji = get(self.client.get_all_emojis(), name='tick3Red')
        await self.client.add_reaction(m, emoji)
        await self.client.say(f"{emoji} Suggestion marked as **rejected**.")

    @commands.has_permissions(view_audit_logs=True)
    @commands.command(pass_context=True)
    async def ignore(self, ctx, id):
        suggestions = discord.utils.get(ctx.message.server.channels, name="suggestions")
        m = await self.client.get_message(suggestions, id)
        emoji = get(self.client.get_all_emojis(), name='tick2Gray')
        await self.client.add_reaction(m, emoji)
        await self.client.say(f"{emoji} Suggestion marked as **ignored**.")
        
def setup(client):
    client.add_cog(suggest(client))
