from discord.ext import commands
import discord
import asyncio

###########role###################rolerare###############rolelegacy


class Roles:
    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True)
    @commands.cooldown(1, 60*60*6, commands.BucketType.user)
    async def roleme(self, ctx):
        if ctx.invoked_subcommand is None:
            return


    @roleme.command(pass_context=True, aliases = ["Monika", "moni","Moni"])
    async def monika(self, ctx):
        print("Test")
        rolestoremove = []
        rolestogive = []
        server = ctx.message.server
        NormalRoles = [discord.utils.get(ctx.message.server.roles, name='Natsuki'), discord.utils.get(ctx.message.server.roles, name='Yuri'), discord.utils.get(ctx.message.server.roles, name='Misao'), discord.utils.get(ctx.message.server.roles, name='Sayori'), discord.utils.get(ctx.message.server.roles, name='Protagonist'), discord.utils.get(ctx.message.server.roles, name='Monika')]
        RareRoles = [discord.utils.get(ctx.message.server.roles, name='Natsuki (Rare)'), discord.utils.get(ctx.message.server.roles, name='Yuri (Rare)'), discord.utils.get(ctx.message.server.roles, name='Misao (Rare)'), discord.utils.get(ctx.message.server.roles, name='Sayori (Rare)'), discord.utils.get(ctx.message.server.roles, name='Protagonist (Rare)'), discord.utils.get(ctx.message.server.roles, name='Monika (Rare)')]
        LegacyRoles= [discord.utils.get(ctx.message.server.roles, name='Natsuki (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Yuri (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Misao (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Sayori (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Protagonist (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Monika (Legacy)')]

        if any(i in NormalRoles for i in ctx.message.author.roles):
            rolestoremove.extend([i for i in NormalRoles if i in ctx.message.author.roles])
            rolestogive.append(discord.utils.get(ctx.message.server.roles, name='Monika'))
        if any(i for i in RareRoles if i in ctx.message.author.roles):
            rolestoremove.extend([i for i in RareRoles if i in ctx.message.author.roles])
            rolestogive.append(discord.utils.get(ctx.message.server.roles, name='Monika (Rare)'))
        if any(i for i in LegacyRoles if i in ctx.message.author.roles):
            rolestoremove.extend([i for i in LegacyRoles if i in ctx.message.author.roles])
            rolestogive.append(discord.utils.get(ctx.message.server.roles, name='Monika (Legacy)'))
        print(rolestogive, rolestoremove)
        await self.bot.remove_roles(ctx.message.author, *rolestoremove)
        await asyncio.sleep(2)
        await self.bot.add_roles(ctx.message.author, *rolestogive)
        await self.bot.say("`Assigned user "+ctx.message.author.name+" the {Monika} flag.`")

    @roleme.command(pass_context=True, aliases = ["Cinnamon bun", "Cinnamon Bun", "cinnamon bun", "cinnamon Bun", "Sayori", "sayo", "Sayo"])
    async def sayori(self, ctx):
        rolestoremove = []
        rolestogive = []
        server = ctx.message.server
        NormalRoles = [discord.utils.get(ctx.message.server.roles, name='Natsuki'), discord.utils.get(ctx.message.server.roles, name='Yuri'), discord.utils.get(ctx.message.server.roles, name='Misao'), discord.utils.get(ctx.message.server.roles, name='Sayori'), discord.utils.get(ctx.message.server.roles, name='Protagonist'), discord.utils.get(ctx.message.server.roles, name='Monika')]
        RareRoles = [discord.utils.get(ctx.message.server.roles, name='Natsuki (Rare)'), discord.utils.get(ctx.message.server.roles, name='Yuri (Rare)'), discord.utils.get(ctx.message.server.roles, name='Misao (Rare)'), discord.utils.get(ctx.message.server.roles, name='Sayori (Rare)'), discord.utils.get(ctx.message.server.roles, name='Protagonist (Rare)'), discord.utils.get(ctx.message.server.roles, name='Monika (Rare)')]
        LegacyRoles= [discord.utils.get(ctx.message.server.roles, name='Natsuki (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Yuri (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Misao (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Sayori (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Protagonist (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Monika (Legacy)')]

        if any(i in NormalRoles for i in ctx.message.author.roles):
            rolestoremove.extend([i for i in NormalRoles if i in ctx.message.author.roles])
            rolestogive.append(discord.utils.get(ctx.message.server.roles, name='Sayori'))
        if any(i for i in RareRoles if i in ctx.message.author.roles):
            rolestoremove.extend([i for i in RareRoles if i in ctx.message.author.roles])
            rolestogive.append(discord.utils.get(ctx.message.server.roles, name='Sayori (Rare)'))
        if any(i for i in LegacyRoles if i in ctx.message.author.roles):
            rolestoremove.extend([i for i in LegacyRoles if i in ctx.message.author.roles])
            rolestogive.append(discord.utils.get(ctx.message.server.roles, name='Sayori (Legacy)'))

        await self.bot.add_roles(ctx.message.author, *rolestogive)
        await asyncio.sleep(2)
        await self.bot.remove_roles(ctx.message.author, *rolestoremove)
        await self.bot.say("`Assigned user "+ctx.message.author.name+" the {Sayori} flag.`")

    @roleme.command(pass_context=True, aliases = ["Nat", "Natsuki", "nat", "tsundere"])
    async def natsuki(self, ctx):
        rolestoremove = []
        rolestogive = []
        server = ctx.message.server
        NormalRoles = [discord.utils.get(ctx.message.server.roles, name='Natsuki'), discord.utils.get(ctx.message.server.roles, name='Yuri'), discord.utils.get(ctx.message.server.roles, name='Misao'), discord.utils.get(ctx.message.server.roles, name='Sayori'), discord.utils.get(ctx.message.server.roles, name='Protagonist'), discord.utils.get(ctx.message.server.roles, name='Monika')]
        RareRoles = [discord.utils.get(ctx.message.server.roles, name='Natsuki (Rare)'), discord.utils.get(ctx.message.server.roles, name='Yuri (Rare)'), discord.utils.get(ctx.message.server.roles, name='Misao (Rare)'), discord.utils.get(ctx.message.server.roles, name='Sayori (Rare)'), discord.utils.get(ctx.message.server.roles, name='Protagonist (Rare)'), discord.utils.get(ctx.message.server.roles, name='Monika (Rare)')]
        LegacyRoles= [discord.utils.get(ctx.message.server.roles, name='Natsuki (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Yuri (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Misao (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Sayori (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Protagonist (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Monika (Legacy)')]

        if any(i in NormalRoles for i in ctx.message.author.roles):
            rolestoremove.extend([i for i in NormalRoles if i in ctx.message.author.roles])
            rolestogive.append(discord.utils.get(ctx.message.server.roles, name='Natsuki'))
        if any(i for i in RareRoles if i in ctx.message.author.roles):
            rolestoremove.extend([i for i in RareRoles if i in ctx.message.author.roles])
            rolestogive.append(discord.utils.get(ctx.message.server.roles, name='Natsuki (Rare)'))
        if any(i for i in LegacyRoles if i in ctx.message.author.roles):
            rolestoremove.extend([i for i in LegacyRoles if i in ctx.message.author.roles])
            rolestogive.append(discord.utils.get(ctx.message.server.roles, name='Natsuki (Legacy)'))

        await self.bot.add_roles(ctx.message.author, *rolestogive)
        await asyncio.sleep(2)
        await self.bot.remove_roles(ctx.message.author, *rolestoremove)
        await self.bot.say("`Assigned user "+ctx.message.author.name+" the {Natsuki} flag.`")

    @roleme.command(pass_context=True, aliases = ["Misao"])
    async def misao(self, ctx):
        rolestoremove = []
        rolestogive = []
        server = ctx.message.server
        NormalRoles = [discord.utils.get(ctx.message.server.roles, name='Natsuki'), discord.utils.get(ctx.message.server.roles, name='Yuri'), discord.utils.get(ctx.message.server.roles, name='Misao'), discord.utils.get(ctx.message.server.roles, name='Sayori'), discord.utils.get(ctx.message.server.roles, name='Protagonist'), discord.utils.get(ctx.message.server.roles, name='Monika')]
        RareRoles = [discord.utils.get(ctx.message.server.roles, name='Natsuki (Rare)'), discord.utils.get(ctx.message.server.roles, name='Yuri (Rare)'), discord.utils.get(ctx.message.server.roles, name='Misao (Rare)'), discord.utils.get(ctx.message.server.roles, name='Sayori (Rare)'), discord.utils.get(ctx.message.server.roles, name='Protagonist (Rare)'), discord.utils.get(ctx.message.server.roles, name='Monika (Rare)')]
        LegacyRoles= [discord.utils.get(ctx.message.server.roles, name='Natsuki (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Yuri (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Misao (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Sayori (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Protagonist (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Monika (Legacy)')]

        if any(i in NormalRoles for i in ctx.message.author.roles):
            rolestoremove.extend([i for i in NormalRoles if i in ctx.message.author.roles])
            rolestogive.append(discord.utils.get(ctx.message.server.roles, name='Misao'))
        if any(i for i in RareRoles if i in ctx.message.author.roles):
            rolestoremove.extend([i for i in RareRoles if i in ctx.message.author.roles])
            rolestogive.append(discord.utils.get(ctx.message.server.roles, name='Misao (Rare)'))
        if any(i for i in LegacyRoles if i in ctx.message.author.roles):
            rolestoremove.extend([i for i in LegacyRoles if i in ctx.message.author.roles])
            rolestogive.append(discord.utils.get(ctx.message.server.roles, name='Misao (Legacy)'))
        await self.bot.add_roles(ctx.message.author, *rolestogive)
        await asyncio.sleep(2)
        await self.bot.remove_roles(ctx.message.author, *rolestoremove)
        await self.bot.say("`Assigned user "+ctx.message.author.name+" the {Misao} flag.`")

    @roleme.command(pass_context=True, aliases = ["Dan","Protag"])
    async def protag(self, ctx):
        rolestoremove = []
        rolestogive = []
        server = ctx.message.server
        NormalRoles = [discord.utils.get(ctx.message.server.roles, name='Natsuki'), discord.utils.get(ctx.message.server.roles, name='Yuri'), discord.utils.get(ctx.message.server.roles, name='Misao'), discord.utils.get(ctx.message.server.roles, name='Sayori'), discord.utils.get(ctx.message.server.roles, name='Protagonist'), discord.utils.get(ctx.message.server.roles, name='Monika')]
        RareRoles = [discord.utils.get(ctx.message.server.roles, name='Natsuki (Rare)'), discord.utils.get(ctx.message.server.roles, name='Yuri (Rare)'), discord.utils.get(ctx.message.server.roles, name='Misao (Rare)'), discord.utils.get(ctx.message.server.roles, name='Sayori (Rare)'), discord.utils.get(ctx.message.server.roles, name='Protagonist (Rare)'), discord.utils.get(ctx.message.server.roles, name='Monika (Rare)')]
        LegacyRoles= [discord.utils.get(ctx.message.server.roles, name='Natsuki (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Yuri (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Misao (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Sayori (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Protagonist (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Monika (Legacy)')]

        if any(i in NormalRoles for i in ctx.message.author.roles):
            rolestoremove.extend([i for i in NormalRoles if i in ctx.message.author.roles])
            rolestogive.append(discord.utils.get(ctx.message.server.roles, name='Protagonist'))
        if any(i for i in RareRoles if i in ctx.message.author.roles):
            rolestoremove.extend([i for i in RareRoles if i in ctx.message.author.roles])
            rolestogive.append(discord.utils.get(ctx.message.server.roles, name='Protagonist (Rare)'))
        if any(i for i in LegacyRoles if i in ctx.message.author.roles):
            rolestoremove.extend([i for i in LegacyRoles if i in ctx.message.author.roles])
            rolestogive.append(discord.utils.get(ctx.message.server.roles, name='Protagonist (Legacy)'))

        await self.bot.add_roles(ctx.message.author, *rolestogive)
        await asyncio.sleep(2)
        await self.bot.remove_roles(ctx.message.author, *rolestoremove)
        await self.bot.say("`Assigned user "+ctx.message.author.name+" the {Protagonist} flag.`")

    @roleme.command(pass_context=True, aliases = ["Yuri"])
    async def yuri(self, ctx):
        rolestoremove = []
        rolestogive = []
        server = ctx.message.server
        NormalRoles = [discord.utils.get(ctx.message.server.roles, name='Natsuki'), discord.utils.get(ctx.message.server.roles, name='Yuri'), discord.utils.get(ctx.message.server.roles, name='Misao'), discord.utils.get(ctx.message.server.roles, name='Sayori'), discord.utils.get(ctx.message.server.roles, name='Protagonist'), discord.utils.get(ctx.message.server.roles, name='Monika')]
        RareRoles = [discord.utils.get(ctx.message.server.roles, name='Natsuki (Rare)'), discord.utils.get(ctx.message.server.roles, name='Yuri (Rare)'), discord.utils.get(ctx.message.server.roles, name='Misao (Rare)'), discord.utils.get(ctx.message.server.roles, name='Sayori (Rare)'), discord.utils.get(ctx.message.server.roles, name='Protagonist (Rare)'), discord.utils.get(ctx.message.server.roles, name='Monika (Rare)')]
        LegacyRoles= [discord.utils.get(ctx.message.server.roles, name='Natsuki (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Yuri (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Misao (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Sayori (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Protagonist (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Monika (Legacy)')]

        if any(i in NormalRoles for i in ctx.message.author.roles):
            rolestoremove.extend([i for i in NormalRoles if i in ctx.message.author.roles])
            rolestogive.append(discord.utils.get(ctx.message.server.roles, name='Yuri'))
        if any(i for i in RareRoles if i in ctx.message.author.roles):
            rolestoremove.extend([i for i in RareRoles if i in ctx.message.author.roles])
            rolestogive.append(discord.utils.get(ctx.message.server.roles, name='Yuri (Rare)'))
        if any(i for i in LegacyRoles if i in ctx.message.author.roles):
            rolestoremove.extend([i for i in LegacyRoles if i in ctx.message.author.roles])
            rolestogive.append(discord.utils.get(ctx.message.server.roles, name='Yuri (Legacy)'))

        await self.bot.add_roles(ctx.message.author, *rolestogive)
        await asyncio.sleep(2)
        await self.bot.remove_roles(ctx.message.author, *rolestoremove)
        await self.bot.say("`Assigned user "+ctx.message.author.name+" the {Yuri} flag.`")

    @roleme.command(pass_context=True)
    async def destined(self, ctx):
        def chooser(userid):
            numbered = int(userid[len(userid)-3:len(userid)])
            if numbered < 166:
                return "yuri"
                
            elif 166 <= numbered < 166*2:
                return "natsuki"
                
            elif 166*2 <= numbered < 166*3:
                return "monika"
                
            elif 166*3 <= numbered < 166*4:
                return "sayori"
                
            elif 166*4 <= numbered < 166*5:
                return "misao"
                
            elif 166*5 <= numbered < 999:
                return "dan"
                
        if chooser(ctx.message.author.id) == "yuri":
            rolestoremove = []
            rolestogive = []
            server = ctx.message.server
            NormalRoles = [discord.utils.get(ctx.message.server.roles, name='Natsuki'), discord.utils.get(ctx.message.server.roles, name='Yuri'), discord.utils.get(ctx.message.server.roles, name='Misao'), discord.utils.get(ctx.message.server.roles, name='Sayori'), discord.utils.get(ctx.message.server.roles, name='Protagonist'), discord.utils.get(ctx.message.server.roles, name='Monika')]
            RareRoles = [discord.utils.get(ctx.message.server.roles, name='Natsuki (Rare)'), discord.utils.get(ctx.message.server.roles, name='Yuri (Rare)'), discord.utils.get(ctx.message.server.roles, name='Misao (Rare)'), discord.utils.get(ctx.message.server.roles, name='Sayori (Rare)'), discord.utils.get(ctx.message.server.roles, name='Protagonist (Rare)'), discord.utils.get(ctx.message.server.roles, name='Monika (Rare)')]
            LegacyRoles= [discord.utils.get(ctx.message.server.roles, name='Natsuki (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Yuri (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Misao (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Sayori (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Protagonist (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Monika (Legacy)')]

            if any(i in NormalRoles for i in ctx.message.author.roles):
                rolestoremove.extend([i for i in NormalRoles if i in ctx.message.author.roles])
                rolestogive.append(discord.utils.get(ctx.message.server.roles, name='Yuri'))
            if any(i for i in RareRoles if i in ctx.message.author.roles):
                rolestoremove.extend([i for i in RareRoles if i in ctx.message.author.roles])
                rolestogive.append(discord.utils.get(ctx.message.server.roles, name='Yuri (Rare)'))
            if any(i for i in LegacyRoles if i in ctx.message.author.roles):
                rolestoremove.extend([i for i in LegacyRoles if i in ctx.message.author.roles])
                rolestogive.append(discord.utils.get(ctx.message.server.roles, name='Yuri (Legacy)'))

            await self.bot.add_roles(ctx.message.author, *rolestogive)
            await asyncio.sleep(2)
            await self.bot.remove_roles(ctx.message.author, *rolestoremove)
            await self.bot.say("`Assigned user "+ctx.message.author.name+" the {Yuri} flag.`")
        elif chooser(ctx.message.author.id) == "monika":
            rolestoremove = []
            rolestogive = []
            server = ctx.message.server
            NormalRoles = [discord.utils.get(ctx.message.server.roles, name='Natsuki'), discord.utils.get(ctx.message.server.roles, name='Yuri'), discord.utils.get(ctx.message.server.roles, name='Misao'), discord.utils.get(ctx.message.server.roles, name='Sayori'), discord.utils.get(ctx.message.server.roles, name='Protagonist'), discord.utils.get(ctx.message.server.roles, name='Monika')]
            RareRoles = [discord.utils.get(ctx.message.server.roles, name='Natsuki (Rare)'), discord.utils.get(ctx.message.server.roles, name='Yuri (Rare)'), discord.utils.get(ctx.message.server.roles, name='Misao (Rare)'), discord.utils.get(ctx.message.server.roles, name='Sayori (Rare)'), discord.utils.get(ctx.message.server.roles, name='Protagonist (Rare)'), discord.utils.get(ctx.message.server.roles, name='Monika (Rare)')]
            LegacyRoles= [discord.utils.get(ctx.message.server.roles, name='Natsuki (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Yuri (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Misao (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Sayori (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Protagonist (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Monika (Legacy)')]

            if any(i in NormalRoles for i in ctx.message.author.roles):
                rolestoremove.extend([i for i in NormalRoles if i in ctx.message.author.roles])
                rolestogive.append(discord.utils.get(ctx.message.server.roles, name='Monika'))
            if any(i for i in RareRoles if i in ctx.message.author.roles):
                rolestoremove.extend([i for i in RareRoles if i in ctx.message.author.roles])
                rolestogive.append(discord.utils.get(ctx.message.server.roles, name='Monika (Rare)'))
            if any(i for i in LegacyRoles if i in ctx.message.author.roles):
                rolestoremove.extend([i for i in LegacyRoles if i in ctx.message.author.roles])
                rolestogive.append(discord.utils.get(ctx.message.server.roles, name='Monika (Legacy)'))

            await self.bot.add_roles(ctx.message.author, *rolestogive)
            await asyncio.sleep(2)
            await self.bot.remove_roles(ctx.message.author, *rolestoremove)
            await self.bot.say("`Assigned user "+ctx.message.author.name+" the {Monika} flag.`")
        elif chooser(ctx.message.author.id) == "misao":
            rolestoremove = []
            rolestogive = []
            server = ctx.message.server
            NormalRoles = [discord.utils.get(ctx.message.server.roles, name='Natsuki'), discord.utils.get(ctx.message.server.roles, name='Yuri'), discord.utils.get(ctx.message.server.roles, name='Misao'), discord.utils.get(ctx.message.server.roles, name='Sayori'), discord.utils.get(ctx.message.server.roles, name='Protagonist'), discord.utils.get(ctx.message.server.roles, name='Monika')]
            RareRoles = [discord.utils.get(ctx.message.server.roles, name='Natsuki (Rare)'), discord.utils.get(ctx.message.server.roles, name='Yuri (Rare)'), discord.utils.get(ctx.message.server.roles, name='Misao (Rare)'), discord.utils.get(ctx.message.server.roles, name='Sayori (Rare)'), discord.utils.get(ctx.message.server.roles, name='Protagonist (Rare)'), discord.utils.get(ctx.message.server.roles, name='Monika (Rare)')]
            LegacyRoles= [discord.utils.get(ctx.message.server.roles, name='Natsuki (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Yuri (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Misao (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Sayori (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Protagonist (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Monika (Legacy)')]

            if any(i in NormalRoles for i in ctx.message.author.roles):
                rolestoremove.extend([i for i in NormalRoles if i in ctx.message.author.roles])
                rolestogive.append(discord.utils.get(ctx.message.server.roles, name='Misao'))
            if any(i for i in RareRoles if i in ctx.message.author.roles):
                rolestoremove.extend([i for i in RareRoles if i in ctx.message.author.roles])
                rolestogive.append(discord.utils.get(ctx.message.server.roles, name='Misao (Rare)'))
            if any(i for i in LegacyRoles if i in ctx.message.author.roles):
                rolestoremove.extend([i for i in LegacyRoles if i in ctx.message.author.roles])
                rolestogive.append(discord.utils.get(ctx.message.server.roles, name='Misao (Legacy)'))

            await self.bot.add_roles(ctx.message.author, *rolestogive)
            await asyncio.sleep(2)
            await self.bot.remove_roles(ctx.message.author, *rolestoremove)
            await self.bot.say("`Assigned user "+ctx.message.author.name+" the {Misao} flag.`")
        elif chooser(ctx.message.author.id) == "sayori":
            rolestoremove = []
            rolestogive = []
            server = ctx.message.server
            NormalRoles = [discord.utils.get(ctx.message.server.roles, name='Natsuki'), discord.utils.get(ctx.message.server.roles, name='Yuri'), discord.utils.get(ctx.message.server.roles, name='Misao'), discord.utils.get(ctx.message.server.roles, name='Sayori'), discord.utils.get(ctx.message.server.roles, name='Protagonist'), discord.utils.get(ctx.message.server.roles, name='Monika')]
            RareRoles = [discord.utils.get(ctx.message.server.roles, name='Natsuki (Rare)'), discord.utils.get(ctx.message.server.roles, name='Yuri (Rare)'), discord.utils.get(ctx.message.server.roles, name='Misao (Rare)'), discord.utils.get(ctx.message.server.roles, name='Sayori (Rare)'), discord.utils.get(ctx.message.server.roles, name='Protagonist (Rare)'), discord.utils.get(ctx.message.server.roles, name='Monika (Rare)')]
            LegacyRoles= [discord.utils.get(ctx.message.server.roles, name='Natsuki (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Yuri (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Misao (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Sayori (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Protagonist (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Monika (Legacy)')]

            if any(i in NormalRoles for i in ctx.message.author.roles):
                rolestoremove.extend([i for i in NormalRoles if i in ctx.message.author.roles])
                rolestogive.append(discord.utils.get(ctx.message.server.roles, name='Sayori'))
            if any(i for i in RareRoles if i in ctx.message.author.roles):
                rolestoremove.extend([i for i in RareRoles if i in ctx.message.author.roles])
                rolestogive.append(discord.utils.get(ctx.message.server.roles, name='Sayori (Rare)'))
            if any(i for i in LegacyRoles if i in ctx.message.author.roles):
                rolestoremove.extend([i for i in LegacyRoles if i in ctx.message.author.roles])
                rolestogive.append(discord.utils.get(ctx.message.server.roles, name='Sayori (Legacy)'))

            await self.bot.add_roles(ctx.message.author, *rolestogive)
            await asyncio.sleep(2)
            await self.bot.remove_roles(ctx.message.author, *rolestoremove)
            await self.bot.say("`Assigned user "+ctx.message.author.name+" the {Sayori} flag.`")
        elif chooser(ctx.message.author.id) == "natsuki":
            rolestoremove = []
            rolestogive = []
            server = ctx.message.server
            NormalRoles = [discord.utils.get(ctx.message.server.roles, name='Natsuki'), discord.utils.get(ctx.message.server.roles, name='Yuri'), discord.utils.get(ctx.message.server.roles, name='Misao'), discord.utils.get(ctx.message.server.roles, name='Sayori'), discord.utils.get(ctx.message.server.roles, name='Protagonist'), discord.utils.get(ctx.message.server.roles, name='Monika')]
            RareRoles = [discord.utils.get(ctx.message.server.roles, name='Natsuki (Rare)'), discord.utils.get(ctx.message.server.roles, name='Yuri (Rare)'), discord.utils.get(ctx.message.server.roles, name='Misao (Rare)'), discord.utils.get(ctx.message.server.roles, name='Sayori (Rare)'), discord.utils.get(ctx.message.server.roles, name='Protagonist (Rare)'), discord.utils.get(ctx.message.server.roles, name='Monika (Rare)')]
            LegacyRoles= [discord.utils.get(ctx.message.server.roles, name='Natsuki (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Yuri (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Misao (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Sayori (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Protagonist (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Monika (Legacy)')]

            if any(i in NormalRoles for i in ctx.message.author.roles):
                rolestoremove.extend([i for i in NormalRoles if i in ctx.message.author.roles])
                rolestogive.append(discord.utils.get(ctx.message.server.roles, name='Natsuki'))
            if any(i for i in RareRoles if i in ctx.message.author.roles):
                rolestoremove.extend([i for i in RareRoles if i in ctx.message.author.roles])
                rolestogive.append(discord.utils.get(ctx.message.server.roles, name='Natsuki (Rare)'))
            if any(i for i in LegacyRoles if i in ctx.message.author.roles):
                rolestoremove.extend([i for i in LegacyRoles if i in ctx.message.author.roles])
                rolestogive.append(discord.utils.get(ctx.message.server.roles, name='Natsuki (Legacy)'))

            await self.bot.add_roles(ctx.message.author, *rolestogive)
            await asyncio.sleep(2)
            await self.bot.remove_roles(ctx.message.author, *rolestoremove)
            await self.bot.say("`Assigned user "+ctx.message.author.name+" the {Natsuki} flag.`")
        elif chooser(ctx.message.author.id) == "dan":
            rolestoremove = []
            rolestogive = []
            server = ctx.message.server
            NormalRoles = [discord.utils.get(ctx.message.server.roles, name='Natsuki'), discord.utils.get(ctx.message.server.roles, name='Yuri'), discord.utils.get(ctx.message.server.roles, name='Misao'), discord.utils.get(ctx.message.server.roles, name='Sayori'), discord.utils.get(ctx.message.server.roles, name='Protagonist'), discord.utils.get(ctx.message.server.roles, name='Monika')]
            RareRoles = [discord.utils.get(ctx.message.server.roles, name='Natsuki (Rare)'), discord.utils.get(ctx.message.server.roles, name='Yuri (Rare)'), discord.utils.get(ctx.message.server.roles, name='Misao (Rare)'), discord.utils.get(ctx.message.server.roles, name='Sayori (Rare)'), discord.utils.get(ctx.message.server.roles, name='Protagonist (Rare)'), discord.utils.get(ctx.message.server.roles, name='Monika (Rare)')]
            LegacyRoles= [discord.utils.get(ctx.message.server.roles, name='Natsuki (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Yuri (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Misao (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Sayori (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Protagonist (Legacy)'), discord.utils.get(ctx.message.server.roles, name='Monika (Legacy)')]

            if any(i in NormalRoles for i in ctx.message.author.roles):
                rolestoremove.extend([i for i in NormalRoles if i in ctx.message.author.roles])
                rolestogive.append(discord.utils.get(ctx.message.server.roles, name='Protagonist'))
            if any(i for i in RareRoles if i in ctx.message.author.roles):
                rolestoremove.extend([i for i in RareRoles if i in ctx.message.author.roles])
                rolestogive.append(discord.utils.get(ctx.message.server.roles, name='Protagonist (Rare)'))
            if any(i for i in LegacyRoles if i in ctx.message.author.roles):
                rolestoremove.extend([i for i in LegacyRoles if i in ctx.message.author.roles])
                rolestogive.append(discord.utils.get(ctx.message.server.roles, name='Protagonist (Legacy)'))

            await self.bot.add_roles(ctx.message.author, *rolestogive)
            await asyncio.sleep(2)
            await self.bot.remove_roles(ctx.message.author, *rolestoremove)
            await self.bot.say("`Assigned user "+ctx.message.author.name+" the {Protagonist} flag.`")
def setup(bot):
    bot.add_cog(Roles(bot))