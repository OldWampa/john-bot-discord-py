import discord
from discord.ext import commands

bad_words = ["handbrake", "handbreak", "hand break", "hand brake"]
good_boys = []

class chat:
    def __init__(self, client):
        self.client = client
        
    async def on_message(self, message):
        for word in message.content.split(" "):
            if word.lower() in bad_words:
                if not message.author.id in good_boys:
                    try:
                        await self.client.delete_message(message)
                    except discord.errors.NotFound:
                        return
        
def setup(client):
    client.add_cog(chat(client))
