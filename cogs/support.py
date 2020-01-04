import discord
from discord.ext import commands
from discord.utils import get

class support:
    def __init__(self, client):
        self.client = client
        
    async def on_message(self, message):
        support = self.client.get_channel("543108414893719612")
        if message.server is None and message.author != self.client.user:
            #yay = await self.client.send_message(message.channel, f"{message.author.mention}, message sent to the support team! Give them some time to reply and thanks for reaching out!")
            embed = discord.Embed(description=message.content)
            embed.set_author(name=message.author, icon_url=message.author.avatar_url)
            await self.client.send_message(support, f"`j!reply {message.author.id}`", embed=embed)
            #await asyncio.sleep(10)
            #await self.client.delete_message(yay)
        await client.process_commands(message)

    @commands.command(pass_context=True, aliases=["msg", "reply"])
    async def message(self, ctx, user, *, words):
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

            person = await self.client.get_user_info(user)
            bigchan = self.client.get_channel("543108414893719612")

            embed = discord.Embed(description=words, color=helper.color)
            embed.set_author(name=f"{pos}{helper}", icon_url=helper.avatar_url)
            embed.set_footer(text="Send a message to reply...")

            cool = discord.Embed(description=words, color=helper.color)
            cool.set_author(name=f"{pos}{helper}", icon_url=helper.avatar_url)
            cool.set_footer(text=f"Replying to {person}")

            await self.client.send_message(person, embed=embed)
            await self.client.send_message(bigchan, f"`j!reply {person.id}`", embed=cool)
            await self.client.delete_message(ctx.message)

        
def setup(client):
    client.add_cog(support(client))
