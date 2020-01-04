import discord
from discord.ext import commands
import random
import aiohttp
import os

upsidedown_lowercase = "ɐqɔpǝɟƃɥᴉɾʞlɯuodbɹsʇnʌʍxʎzƖᄅƐㄣϛ9ㄥ860"
upsidedown_uppercase = "∀qƆpƎℲפHIſʞ˥WNOԀQɹS┴∩ΛMX⅄Z"

alphabet = dict(zip("abcdefghijklmnopqrstuvwxyz1234567890", range(0, 36)))
uppercase_alphabet = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(0, 26)))
punctuation = dict(zip("§½!\"#¤%&/()=?`´@£$€{[]}\\^¨~'*<>|,.-_:", range(0, 37)))
punc = "§½!\"#¤%&/()=?`´@£$€{[]}\\^¨~'*<>|,.-_:"
space = " "

class fun:
    def __init__(self, client):
        self.client = client
        
    @commands.command(pass_context=True, aliases=['dice'])
    async def roll(self, ctx, dice : str):
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await self.client.say('Format has to be in NdN!')
            return
        author = ctx.message.author
        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await self.client.say(f"{author.mention} :game_die: \n**Dice:** {dice} \n**Result:** {result}")

    @commands.command(name='8ball', aliases=['8'], pass_context=True)
    async def eight_ball(self, ctx, *, text=None):
        if text is None:
            await self.client.say("Please ask a question. Use `!8ball <question>`")
            return
        author = ctx.message.author
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

        question=discord.Embed(title=f"{author}", description=f'**Question:** {text}', color=discord.Colour(0x4D6FAF))
        await self.client.say(random.choice(possible_responses), embed=question)

    @commands.command(pass_context=True)
    async def flip(self, ctx, user:discord.Member=None):
        if user is None:
            author = ctx.message.author
            possible_responses = ["Heads", "Tails"]
            await self.client.say(f"<:discoin:545854263042244608> {author.mention} flips a coin. It lands on **{random.choice(possible_responses)}**!")
            return
        returnthis = ""
        for word in user.name:
            for letter in word:
                if letter in alphabet:
                    returnthis += upsidedown_lowercase[alphabet[letter]]
                elif letter in uppercase_alphabet:
                    returnthis += upsidedown_uppercase[uppercase_alphabet[letter]]
                elif letter in punctuation:
                    returnthis += punc[punctuation[letter]]
                elif letter == space:
                    returnthis += space
                else:
                    returnthis += letter
        await self.client.say("(╯°□°）╯︵   " + returnthis[::-1])

    @commands.command(pass_context=True)
    async def protip(self, ctx):
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

        await self.client.say(embed=protip)


    @commands.command(pass_context=True)
    async def cat(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('http://aws.random.cat/meow') as r:
                res = await r.json()
                embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
                embed.set_image(url=res['file'])
                await self.client.say(embed=embed)

    @commands.command(pass_context=True)
    async def dog(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://dog.ceo/api/breeds/image/random') as r:
                res = await r.json()
                embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
                embed.set_image(url=res['message'])
                await self.client.say(embed=embed)

    @commands.command(aliases=["amp"], pass_context = True)
    async def amplify(self, ctx, *, inp):
        if "@everyone" in ctx.message.content:
            await self.client.say('niCE TrY Guy')
            return
        if "@here" in ctx.message.content:
            await self.client.say('NiCE tRY guY')
            return
        else:
            await self.client.say(''.join(c.upper() if random.randint(0, 1) == 1 else c.lower() for c in inp))

    @commands.command(pass_context=True, aliases=["clap"])
    async def clapify(self, ctx, *args):
        if "@everyone" in ctx.message.content:
            await self.client.say('\U0001f44f Forget \U0001f44f that \U0001f44f')
            return
        if "@here" in ctx.message.content:
            await self.client.say('\U0001f44f Forget \U0001f44f that \U0001f44f')
            return
        else:
            output = '\U0001f44f '
            for word in args:
                output += word
                output += ' \U0001f44f '
            await self.client.say(output)

    @commands.command(pass_context=True)
    async def split(self, ctx, split, *args):
        if "@everyone" in ctx.message.content:
            await self.client.say(f'{split} Forget {split} that {split}')
            return
        if "@here" in ctx.message.content:
            await self.client.say(f'{split} Forget {split} that {split}')
            return
        else:
            output = f'{split} '
            for word in args:
                output += word
                output += f' {split} '
            await self.client.say(output)

    @commands.command(pass_context=True)
    async def rps(self, ctx):
        os.system('cls' if os.name=='nt' else 'clear')
        while (1 < 2):
            R = "\U0001f5ff"
            P = "\U0001f4c4"
            S = "\U00002702"
            choices = [R, P, S]
            reactu = await self.client.say("Rock, Paper, Scissors - Shoot!")
            await self.client.add_reaction(reactu, emoji=R)
            await self.client.add_reaction(reactu, emoji=P)
            await self.client.add_reaction(reactu, emoji=S)

            userChoice = await self.client.wait_for_reaction(emoji=choices, user=ctx.message.author, message=reactu)
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
            await self.client.say(embed=embed)
            return
    
    @commands.command(pass_context=True)
    async def hug(self, ctx, user:discord.Member=None):
        hug = ["HUGS!", "Awww...", "<3"]
        image = ["https://cdn.discordapp.com/attachments/580969357266386954/580970940578660352/20190326_231424.gif", "https://cdn.discordapp.com/attachments/580969357266386954/580970940578660353/John_Huggo.gif", "https://cdn.discordapp.com/attachments/580969357266386954/580970941165731843/ok.png", "https://cdn.discordapp.com/attachments/580969357266386954/580970941165731845/johnhug-1.png", "https://cdn.discordapp.com/attachments/580969357266386954/580970941643751450/image0.png", "https://cdn.discordapp.com/attachments/580969357266386954/580970942369628170/johnhug.png", "https://cdn.discordapp.com/attachments/580969357266386954/580970942369628172/Johndeathloveyoubby.gif", "https://cdn.discordapp.com/attachments/580969357266386954/580970943086723072/image0-2.jpg"]
        weow = ["The artwork for this command is fan created!"]
        if user is None:
            await self.client.say(f"Error, `user:discord.Member=None`")
        elif user == self.client.user:
            await self.client.say("Ewww! Get your greasy, human hands off of me!")
        elif user is ctx.message.author:
            embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
            embed.set_author(name=f"{self.client.user.name} hugs {user.name}!", icon_url=self.client.user.avatar_url)
            embed.set_image(url=random.choice(image))
            embed.set_footer(text=random.choice(weow))
            await self.client.say(random.choice(hug), embed=embed)
        else:
            embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
            embed.set_author(name=f"{ctx.message.author.name} hugs {user.name}!", icon_url=ctx.message.author.avatar_url)
            embed.set_image(url=random.choice(image))
            embed.set_footer(text=random.choice(weow))
            await self.client.say(random.choice(hug), embed=embed)
        
def setup(client):
    client.add_cog(fun(client))
