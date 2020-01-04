import discord
from discord.ext import commands

class artcomp:
    def __init__(self, client):
        self.client = client
        
    @commands.command(pass_context=True)
    async def submit(self, ctx, text=None):
        if ctx.message.attachments:
            if ctx.message.attachments[1] is True:
                return
            await self.client.say("yay")
            #do stuff
            return
        else:
            await self.client.say(p)
            
    @commands.command(pass_context=True)
    async def resubmit(self, ctx, text=None):
        if ctx.message.attachments:
            if ctx.message.attachments[1] is True:
                return
            await self.client.say("yay")
            #do stuff
            return
        else:
            await self.client.say(p)
            
    @commands.command(pass_context=True)
    async def vote(self, ctx, id=None):
        if id == ctx.message.author.id:
            await self.client.say(f"{ctx.message.author}, you cannot vote for yourself!")
            return
        #edit message to show votes #
        
def setup(client):
    client.add_cog(artcomp(client))
