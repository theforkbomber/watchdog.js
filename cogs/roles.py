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
            norm = False
            rare = False
            legacy = False
            server = ctx.message.server
            user = server.get_member(ctx.message.author.id)
            server = self.bot.get_server('369252350927306752')
            NatNorm = discord.utils.get(ctx.message.server.roles, name='Natsuki')
            PenNorm = discord.utils.get(ctx.message.server.roles, name='Yuri')
            FagNorm = discord.utils.get(ctx.message.server.roles, name='Misao')
            CinnamonNorm = discord.utils.get(ctx.message.server.roles, name='Sayori')
            BestBoyNorm = discord.utils.get(ctx.message.server.roles, name='Protagonist')
            NatRare = discord.utils.get(ctx.message.server.roles, name='Natsuki (Rare)')
            PenRare = discord.utils.get(ctx.message.server.roles, name='Yuri (Rare)')
            FagRare = discord.utils.get(ctx.message.server.roles, name='Misao (Rare)')
            CinnamonRare = discord.utils.get(ctx.message.server.roles, name='Sayori (Rare)')
            BestBoyRare = discord.utils.get(ctx.message.server.roles, name='Protagonist (Rare)')
            NatLegacy = discord.utils.get(ctx.message.server.roles, name='Natsuki (Legacy)')
            PenLegacy = discord.utils.get(ctx.message.server.roles, name='Yuri (Legacy)')
            FagLegacy = discord.utils.get(ctx.message.server.roles, name='Misao (Legacy)')
            CinnamonLegacy = discord.utils.get(ctx.message.server.roles, name='Sayori (Legacy)')
            BestBoyLegacy = discord.utils.get(ctx.message.server.roles, name='Protagonist (Legacy)')
            Moni = discord.utils.get(ctx.message.server.roles, name='Monika')
            MoniRare = discord.utils.get(ctx.message.server.roles, name='Monika (Rare)')
            MoniLegacy = discord.utils.get(ctx.message.server.roles, name='Monika (Legacy)')

            if NatNorm in ctx.message.author.roles:
                rolestoremove.extend(NatNorm)
                rolestogive.append(PenNorm)
            if NatRare in ctx.message.author.roles:
                rolestoremove.extend(NatRare)
                rolestogive.append(PenRare)
            if NatLegacy in ctx.message.author.roles:
                rolestoremove.extend(NatLegacy)
                rolestogive.append(PenLegacy)

            if PenNorm in ctx.message.author.roles:
                rolestoremove.extend(PenNorm)
                rolestogive.append(PenNorm)
            if PenRare in ctx.message.author.roles:
                rolestoremove.extend(PenRare)
                rolestogive.append(PenRare)
            if PenLegacy in ctx.message.author.roles:
                rolestoremove.extend(PenLegacy)
                rolestogive.append(PenLegacy)
            
            if CinnamonNorm in ctx.message.author.roles:
                rolestoremove.extend(CinnamonNorm)
                rolestogive.append(PenNorm)
            if CinnamonRare in ctx.message.author.roles:
                rolestoremove.extend(CinnamonRare)
                rolestogive.append(PenRare)
            if CinnamonLegacy in ctx.message.author.roles:
                rolestoremove.extend(CinnamonLegacy)
                rolestogive.append(PenLegacy)
                
            if FagNorm in ctx.message.author.roles:
                rolestoremove.extend(FagNorm)
                rolestogive.append(PenNorm)
            if FagRare in ctx.message.author.roles:
                rolestoremove.extend(FagRare)
                rolestogive.append(PenRare)
            if FagLegacy in ctx.message.author.roles:
                rolestoremove.extend(FagLegacy)
                rolestogive.append(PenLegacy)

            if BestBoyNorm in ctx.message.author.roles:
                rolestoremove.extend(BestBoyNorm)
                rolestogive.append(PenNorm)
            if BestBoyRare in ctx.message.author.roles:
                rolestoremove.extend(BestBoyRare)
                rolestogive.append(PenRare)
            if BestBoyLegacy in ctx.message.author.roles:
                rolestoremove.extend(BestBoyLegacy)
                rolestogive.append(PenLegacy)
            
            if Moni in ctx.message.author.roles:
                rolestoremove.extend(Moni)
                rolestogive.append(PenNorm)
            if MoniRare in ctx.message.author.roles:
                rolestoremove.extend(MoniRare)
                rolestogive.append(PenRare)
            if MoniLegacy in ctx.message.author.roles:
                rolestoremove.extend(MoniLegacy)
                rolestogive.append(PenLegacy)

            await self.bot.add_roles(ctx.message.author, *rolestogive)
            await asyncio.sleep(2)
            await self.bot.remove_roles(ctx.message.author, *rolestoremove)
            await self.bot.say("`Assigned user "+ctx.message.author.name+" the {Yuri} flag.`")
        elif chooser(ctx.message.author.id) == "monika":
            rolestoremove = []
            rolestogive = []
            norm = False
            rare = False
            legacy = False
            server = ctx.message.server
            user = server.get_member(ctx.message.author.id)
            server = self.bot.get_server('369252350927306752')
            NatNorm = discord.utils.get(ctx.message.server.roles, name='Natsuki')
            PenNorm = discord.utils.get(ctx.message.server.roles, name='Yuri')
            FagNorm = discord.utils.get(ctx.message.server.roles, name='Misao')
            CinnamonNorm = discord.utils.get(ctx.message.server.roles, name='Sayori')
            BestBoyNorm = discord.utils.get(ctx.message.server.roles, name='Protagonist')
            NatRare = discord.utils.get(ctx.message.server.roles, name='Natsuki (Rare)')
            PenRare = discord.utils.get(ctx.message.server.roles, name='Yuri (Rare)')
            FagRare = discord.utils.get(ctx.message.server.roles, name='Misao (Rare)')
            CinnamonRare = discord.utils.get(ctx.message.server.roles, name='Sayori (Rare)')
            BestBoyRare = discord.utils.get(ctx.message.server.roles, name='Protagonist (Rare)')
            NatLegacy = discord.utils.get(ctx.message.server.roles, name='Natsuki (Legacy)')
            PenLegacy = discord.utils.get(ctx.message.server.roles, name='Yuri (Legacy)')
            FagLegacy = discord.utils.get(ctx.message.server.roles, name='Misao (Legacy)')
            CinnamonLegacy = discord.utils.get(ctx.message.server.roles, name='Sayori (Legacy)')
            BestBoyLegacy = discord.utils.get(ctx.message.server.roles, name='Protagonist (Legacy)')
            Moni = discord.utils.get(ctx.message.server.roles, name='Monika')
            MoniRare = discord.utils.get(ctx.message.server.roles, name='Monika (Rare)')
            MoniLegacy = discord.utils.get(ctx.message.server.roles, name='Monika (Legacy)')
            if NatNorm in ctx.message.author.roles:
                rolestoremove.extend(NatNorm)
                rolestogive.append(Moni)
            if NatRare in ctx.message.author.roles:
                rolestoremove.extend(NatRare)
                rolestogive.append(MoniRare)
            if NatLegacy in ctx.message.author.roles:
                rolestoremove.extend(NatLegacy)
                rolestogive.append(MoniLegacy)

            if PenNorm in ctx.message.author.roles:
                rolestoremove.extend(PenNorm)
                rolestogive.append(Moni)
            if PenRare in ctx.message.author.roles:
                rolestoremove.extend(PenRare)
                rolestogive.append(MoniRare)
            if PenLegacy in ctx.message.author.roles:
                rolestoremove.extend(PenLegacy)
                rolestogive.append(MoniLegacy)
            
            if CinnamonNorm in ctx.message.author.roles:
                rolestoremove.extend(CinnamonNorm)
                rolestogive.append(Moni)
            if CinnamonRare in ctx.message.author.roles:
                rolestoremove.extend(CinnamonRare)
                rolestogive.append(MoniRare)
            if CinnamonLegacy in ctx.message.author.roles:
                rolestoremove.extend(CinnamonLegacy)
                rolestogive.append(MoniLegacy)
                
            if FagNorm in ctx.message.author.roles:
                rolestoremove.extend(FagNorm)
                rolestogive.append(Moni)
            if FagRare in ctx.message.author.roles:
                rolestoremove.extend(FagRare)
                rolestogive.append(MoniRare)
            if FagLegacy in ctx.message.author.roles:
                rolestoremove.extend(FagLegacy)
                rolestogive.append(MoniLegacy)

            if BestBoyNorm in ctx.message.author.roles:
                rolestoremove.extend(BestBoyNorm)
                rolestogive.append(Moni)
            if BestBoyRare in ctx.message.author.roles:
                rolestoremove.extend(BestBoyRare)
                rolestogive.append(MoniRare)
            if BestBoyLegacy in ctx.message.author.roles:
                rolestoremove.extend(BestBoyLegacy)
                rolestogive.append(MoniLegacy)
            await self.bot.add_roles(ctx.message.author, *rolestogive)
            await asyncio.sleep(2)
            await self.bot.remove_roles(ctx.message.author, *rolestoremove)
            await self.bot.say("`Assigned user "+ctx.message.author.name+" the {Monika} flag.`")
        elif chooser(ctx.message.author.id) == "misao":
            rolestoremove = []
            rolestogive = []
            norm = False
            rare = False
            legacy = False
            server = ctx.message.server
            user = server.get_member(ctx.message.author.id)
            server = self.bot.get_server('369252350927306752')
            NatNorm = discord.utils.get(ctx.message.server.roles, name='Natsuki')
            PenNorm = discord.utils.get(ctx.message.server.roles, name='Yuri')
            FagNorm = discord.utils.get(ctx.message.server.roles, name='Misao')
            CinnamonNorm = discord.utils.get(ctx.message.server.roles, name='Sayori')
            BestBoyNorm = discord.utils.get(ctx.message.server.roles, name='Protagonist')
            NatRare = discord.utils.get(ctx.message.server.roles, name='Natsuki (Rare)')
            PenRare = discord.utils.get(ctx.message.server.roles, name='Yuri (Rare)')
            FagRare = discord.utils.get(ctx.message.server.roles, name='Misao (Rare)')
            CinnamonRare = discord.utils.get(ctx.message.server.roles, name='Sayori (Rare)')
            BestBoyRare = discord.utils.get(ctx.message.server.roles, name='Protagonist (Rare)')
            NatLegacy = discord.utils.get(ctx.message.server.roles, name='Natsuki (Legacy)')
            PenLegacy = discord.utils.get(ctx.message.server.roles, name='Yuri (Legacy)')
            FagLegacy = discord.utils.get(ctx.message.server.roles, name='Misao (Legacy)')
            CinnamonLegacy = discord.utils.get(ctx.message.server.roles, name='Sayori (Legacy)')
            BestBoyLegacy = discord.utils.get(ctx.message.server.roles, name='Protagonist (Legacy)')
            Moni = discord.utils.get(ctx.message.server.roles, name='Monika')
            MoniRare = discord.utils.get(ctx.message.server.roles, name='Monika (Rare)')
            MoniLegacy = discord.utils.get(ctx.message.server.roles, name='Monika (Legacy)')

            if NatNorm in ctx.message.author.roles:
                rolestoremove.extend(NatNorm)
                rolestogive.append(FagNorm)
            if NatRare in ctx.message.author.roles:
                rolestoremove.extend(NatRare)
                rolestogive.append(FagRare)
            if NatLegacy in ctx.message.author.roles:
                rolestoremove.extend(NatLegacy)
                rolestogive.append(FagLegacy)

            if PenNorm in ctx.message.author.roles:
                rolestoremove.extend(PenNorm)
                rolestogive.append(FagNorm)
            if PenRare in ctx.message.author.roles:
                rolestoremove.extend(PenRare)
                rolestogive.append(FagRare)
            if PenLegacy in ctx.message.author.roles:
                rolestoremove.extend(PenLegacy)
                rolestogive.append(FagLegacy)
            
            if CinnamonNorm in ctx.message.author.roles:
                rolestoremove.extend(CinnamonNorm)
                rolestogive.append(FagNorm)
            if CinnamonRare in ctx.message.author.roles:
                rolestoremove.extend(CinnamonRare)
                rolestogive.append(FagRare)
            if CinnamonLegacy in ctx.message.author.roles:
                rolestoremove.extend(CinnamonLegacy)
                rolestogive.append(FagLegacy)
                
            # if FagNorm in ctx.message.author.roles:
            #     rolestoremove.extend(FagNorm)
            #     rolestogive.append(PenNorm)
            # if FagRare in ctx.message.author.roles:
            #     rolestoremove.extend(FagRare)
            #     rolestogive.append(PenRare)
            # if FagLegacy in ctx.message.author.roles:
            #     rolestoremove.extend(FagLegacy)
            #     rolestogive.append(PenLegacy)

            if BestBoyNorm in ctx.message.author.roles:
                rolestoremove.extend(BestBoyNorm)
                rolestogive.append(FagNorm)
            if BestBoyRare in ctx.message.author.roles:
                rolestoremove.extend(BestBoyRare)
                rolestogive.append(FagRare)
            if BestBoyLegacy in ctx.message.author.roles:
                rolestoremove.extend(BestBoyLegacy)
                rolestogive.append(FagLegacy)
            
            if Moni in ctx.message.author.roles:
                rolestoremove.extend(Moni)
                rolestogive.append(FagNorm)
            if MoniRare in ctx.message.author.roles:
                rolestoremove.extend(MoniRare)
                rolestogive.append(FagRare)
            if MoniLegacy in ctx.message.author.roles:
                rolestoremove.extend(MoniLegacy)
                rolestogive.append(FagLegacy)

            await self.bot.add_roles(ctx.message.author, *rolestogive)
            await asyncio.sleep(2)
            await self.bot.remove_roles(ctx.message.author, *rolestoremove)
            await self.bot.say("`Assigned user "+ctx.message.author.name+" the {Misao} flag.`")
        elif chooser(ctx.message.author.id) == "sayori":
            rolestoremove = []
            rolestogive = []
            norm = False
            rare = False
            legacy = False
            server = ctx.message.server
            user = server.get_member(ctx.message.author.id)
            server = self.bot.get_server('369252350927306752')
            NatNorm = discord.utils.get(ctx.message.server.roles, name='Natsuki')
            PenNorm = discord.utils.get(ctx.message.server.roles, name='Yuri')
            FagNorm = discord.utils.get(ctx.message.server.roles, name='Misao')
            CinnamonNorm = discord.utils.get(ctx.message.server.roles, name='Sayori')
            BestBoyNorm = discord.utils.get(ctx.message.server.roles, name='Protagonist')
            NatRare = discord.utils.get(ctx.message.server.roles, name='Natsuki (Rare)')
            PenRare = discord.utils.get(ctx.message.server.roles, name='Yuri (Rare)')
            FagRare = discord.utils.get(ctx.message.server.roles, name='Misao (Rare)')
            CinnamonRare = discord.utils.get(ctx.message.server.roles, name='Sayori (Rare)')
            BestBoyRare = discord.utils.get(ctx.message.server.roles, name='Protagonist (Rare)')
            NatLegacy = discord.utils.get(ctx.message.server.roles, name='Natsuki (Legacy)')
            PenLegacy = discord.utils.get(ctx.message.server.roles, name='Yuri (Legacy)')
            FagLegacy = discord.utils.get(ctx.message.server.roles, name='Misao (Legacy)')
            CinnamonLegacy = discord.utils.get(ctx.message.server.roles, name='Sayori (Legacy)')
            BestBoyLegacy = discord.utils.get(ctx.message.server.roles, name='Protagonist (Legacy)')
            Moni = discord.utils.get(ctx.message.server.roles, name='Monika')
            MoniRare = discord.utils.get(ctx.message.server.roles, name='Monika (Rare)')
            MoniLegacy = discord.utils.get(ctx.message.server.roles, name='Monika (Legacy)')
            if NatNorm in ctx.message.author.roles:
                rolestoremove.extend(NatNorm)
                rolestogive.append(CinnamonNorm)
            if NatRare in ctx.message.author.roles:
                rolestoremove.extend(NatRare)
                rolestogive.append(CinnamonRare)
            if NatLegacy in ctx.message.author.roles:
                rolestoremove.extend(NatLegacy)
                rolestogive.append(CinnamonLegacy)

            if PenNorm in ctx.message.author.roles:
                rolestoremove.extend(PenNorm)
                rolestogive.append(CinnamonNorm)
            if PenRare in ctx.message.author.roles:
                rolestoremove.extend(PenRare)
                rolestogive.append(CinnamonRare)
            if PenLegacy in ctx.message.author.roles:
                rolestoremove.extend(PenLegacy)
                rolestogive.append(CinnamonLegacy)
            
            # if CinnamonNorm in ctx.message.author.roles:
            #     rolestoremove.extend(CinnamonNorm)
            #     rolestogive.append(Moni)
            # if CinnamonRare in ctx.message.author.roles:
            #     rolestoremove.extend(CinnamonRare)
            #     rolestogive.append(MoniRare)
            # if CinnamonLegacy in ctx.message.author.roles:
            #     rolestoremove.extend(CinnamonLegacy)
            #     rolestogive.append(MoniLegacy)
                
            if FagNorm in ctx.message.author.roles:
                rolestoremove.extend(FagNorm)
                rolestogive.append(CinnamonNorm)
            if FagRare in ctx.message.author.roles:
                rolestoremove.extend(FagRare)
                rolestogive.append(CinnamonRare)
            if FagLegacy in ctx.message.author.roles:
                rolestoremove.extend(FagLegacy)
                rolestogive.append(CinnamonLegacy)

            if BestBoyNorm in ctx.message.author.roles:
                rolestoremove.extend(BestBoyNorm)
                rolestogive.append(CinnamonNorm)
            if BestBoyRare in ctx.message.author.roles:
                rolestoremove.extend(BestBoyRare)
                rolestogive.append(CinnamonRare)
            if BestBoyLegacy in ctx.message.author.roles:
                rolestoremove.extend(BestBoyLegacy)
                rolestogive.append(CinnamonLegacy)
            
            if Moni in ctx.message.author.roles:
                rolestoremove.extend(Moni)
                rolestogive.append(CinnamonNorm)
            if MoniRare in ctx.message.author.roles:
                rolestoremove.extend(MoniRare)
                rolestogive.append(CinnamonRare)
            if MoniLegacy in ctx.message.author.roles:
                rolestoremove.extend(MoniLegacy)
                rolestogive.append(CinnamonLegacy)

            await self.bot.add_roles(ctx.message.author, *rolestogive)
            await asyncio.sleep(2)
            await self.bot.remove_roles(ctx.message.author, *rolestoremove)
            await self.bot.say("`Assigned user "+ctx.message.author.name+" the {Sayori} flag.`")
        elif chooser(ctx.message.author.id) == "natsuki":
            rolestoremove = []
            rolestogive = []
            norm = False
            rare = False
            legacy = False
            server = ctx.message.server
            user = server.get_member(ctx.message.author.id)
            server = self.bot.get_server('369252350927306752')
            NatNorm = discord.utils.get(ctx.message.server.roles, name='Natsuki')
            PenNorm = discord.utils.get(ctx.message.server.roles, name='Yuri')
            FagNorm = discord.utils.get(ctx.message.server.roles, name='Misao')
            CinnamonNorm = discord.utils.get(ctx.message.server.roles, name='Sayori')
            BestBoyNorm = discord.utils.get(ctx.message.server.roles, name='Protagonist')
            NatRare = discord.utils.get(ctx.message.server.roles, name='Natsuki (Rare)')
            PenRare = discord.utils.get(ctx.message.server.roles, name='Yuri (Rare)')
            FagRare = discord.utils.get(ctx.message.server.roles, name='Misao (Rare)')
            CinnamonRare = discord.utils.get(ctx.message.server.roles, name='Sayori (Rare)')
            BestBoyRare = discord.utils.get(ctx.message.server.roles, name='Protagonist (Rare)')
            NatLegacy = discord.utils.get(ctx.message.server.roles, name='Natsuki (Legacy)')
            PenLegacy = discord.utils.get(ctx.message.server.roles, name='Yuri (Legacy)')
            FagLegacy = discord.utils.get(ctx.message.server.roles, name='Misao (Legacy)')
            CinnamonLegacy = discord.utils.get(ctx.message.server.roles, name='Sayori (Legacy)')
            BestBoyLegacy = discord.utils.get(ctx.message.server.roles, name='Protagonist (Legacy)')
            Moni = discord.utils.get(ctx.message.server.roles, name='Monika')
            MoniRare = discord.utils.get(ctx.message.server.roles, name='Monika (Rare)')
            MoniLegacy = discord.utils.get(ctx.message.server.roles, name='Monika (Legacy)')
            # if NatNorm in ctx.message.author.roles:
            #     rolestoremove.extend(NatNorm)
            #     rolestogive.append(Cinnamon)
            # if NatRare in ctx.message.author.roles:
            #     rolestoremove.extend(NatRare)
            #     rolestogive.append(CinnamonRare)
            # if NatLegacy in ctx.message.author.roles:
            #     rolestoremove.extend(NatLegacy)
            #     rolestogive.append(CinnamonLegacy)

            if PenNorm in ctx.message.author.roles:
                rolestoremove.extend(PenNorm)
                rolestogive.append(NatNorm)
            if PenRare in ctx.message.author.roles:
                rolestoremove.extend(PenRare)
                rolestogive.append(NatRare)
            if PenLegacy in ctx.message.author.roles:
                rolestoremove.extend(PenLegacy)
                rolestogive.append(NatLegacy)
            
            if CinnamonNorm in ctx.message.author.roles:
                rolestoremove.extend(CinnamonNorm)
                rolestogive.append(NatNorm)
            if CinnamonRare in ctx.message.author.roles:
                rolestoremove.extend(CinnamonRare)
                rolestogive.append(NatRare)
            if CinnamonLegacy in ctx.message.author.roles:
                rolestoremove.extend(CinnamonLegacy)
                rolestogive.append(NatLegacy)
                
            if FagNorm in ctx.message.author.roles:
                rolestoremove.extend(FagNorm)
                rolestogive.append(NatNorm)
            if FagRare in ctx.message.author.roles:
                rolestoremove.extend(FagRare)
                rolestogive.append(NatRare)
            if FagLegacy in ctx.message.author.roles:
                rolestoremove.extend(FagLegacy)
                rolestogive.append(NatLegacy)

            if BestBoyNorm in ctx.message.author.roles:
                rolestoremove.extend(BestBoyNorm)
                rolestogive.append(NatNorm)
            if BestBoyRare in ctx.message.author.roles:
                rolestoremove.extend(BestBoyRare)
                rolestogive.append(NatRare)
            if BestBoyLegacy in ctx.message.author.roles:
                rolestoremove.extend(BestBoyLegacy)
                rolestogive.append(NatLegacy)
            
            if Moni in ctx.message.author.roles:
                rolestoremove.extend(Moni)
                rolestogive.append(NatNorm)
            if MoniRare in ctx.message.author.roles:
                rolestoremove.extend(MoniRare)
                rolestogive.append(NatRare)
            if MoniLegacy in ctx.message.author.roles:
                rolestoremove.extend(MoniLegacy)
                rolestogive.append(NatLegacy)

            await self.bot.add_roles(ctx.message.author, *rolestogive)
            await asyncio.sleep(2)
            await self.bot.remove_roles(ctx.message.author, *rolestoremove)
            await self.bot.say("`Assigned user "+ctx.message.author.name+" the {Natsuki} flag.`")
        elif chooser(ctx.message.author.id) == "dan":
            rolestoremove = []
            rolestogive = []
            norm = False
            rare = False
            legacy = False
            server = ctx.message.server
            user = server.get_member(ctx.message.author.id)
            server = self.bot.get_server('369252350927306752')
            NatNorm = discord.utils.get(ctx.message.server.roles, name='Natsuki')
            PenNorm = discord.utils.get(ctx.message.server.roles, name='Yuri')
            FagNorm = discord.utils.get(ctx.message.server.roles, name='Misao')
            CinnamonNorm = discord.utils.get(ctx.message.server.roles, name='Sayori')
            BestBoyNorm = discord.utils.get(ctx.message.server.roles, name='Protagonist')
            NatRare = discord.utils.get(ctx.message.server.roles, name='Natsuki (Rare)')
            PenRare = discord.utils.get(ctx.message.server.roles, name='Yuri (Rare)')
            FagRare = discord.utils.get(ctx.message.server.roles, name='Misao (Rare)')
            CinnamonRare = discord.utils.get(ctx.message.server.roles, name='Sayori (Rare)')
            BestBoyRare = discord.utils.get(ctx.message.server.roles, name='Protagonist (Rare)')
            NatLegacy = discord.utils.get(ctx.message.server.roles, name='Natsuki (Legacy)')
            PenLegacy = discord.utils.get(ctx.message.server.roles, name='Yuri (Legacy)')
            FagLegacy = discord.utils.get(ctx.message.server.roles, name='Misao (Legacy)')
            CinnamonLegacy = discord.utils.get(ctx.message.server.roles, name='Sayori (Legacy)')
            BestBoyLegacy = discord.utils.get(ctx.message.server.roles, name='Protagonist (Legacy)')
            Moni = discord.utils.get(ctx.message.server.roles, name='Monika')
            MoniRare = discord.utils.get(ctx.message.server.roles, name='Monika (Rare)')
            MoniLegacy = discord.utils.get(ctx.message.server.roles, name='Monika (Legacy)')

            if NatNorm in ctx.message.author.roles:
                rolestoremove.extend(NatNorm)
                rolestogive.append(BestBoyNorm)
            if NatRare in ctx.message.author.roles:
                rolestoremove.extend(NatRare)
                rolestogive.append(BestBoyRare)
            if NatLegacy in ctx.message.author.roles:
                rolestoremove.extend(NatLegacy)
                rolestogive.append(BestBoyLegacy)

            if PenNorm in ctx.message.author.roles:
                rolestoremove.extend(PenNorm)
                rolestogive.append(BestBoyNorm)
            if PenRare in ctx.message.author.roles:
                rolestoremove.extend(PenRare)
                rolestogive.append(BestBoyRare)
            if PenLegacy in ctx.message.author.roles:
                rolestoremove.extend(PenLegacy)
                rolestogive.append(BestBoyLegacy)
            
            if CinnamonNorm in ctx.message.author.roles:
                rolestoremove.extend(CinnamonNorm)
                rolestogive.append(BestBoyNorm)
            if CinnamonRare in ctx.message.author.roles:
                rolestoremove.extend(CinnamonRare)
                rolestogive.append(BestBoyRare)
            if CinnamonLegacy in ctx.message.author.roles:
                rolestoremove.extend(CinnamonLegacy)
                rolestogive.append(BestBoyLegacy)
                
            if FagNorm in ctx.message.author.roles:
                rolestoremove.extend(FagNorm)
                rolestogive.append(BestBoyNorm)
            if FagRare in ctx.message.author.roles:
                rolestoremove.extend(FagRare)
                rolestogive.append(BestBoyRare)
            if FagLegacy in ctx.message.author.roles:
                rolestoremove.extend(FagLegacy)
                rolestogive.append(BestBoyLegacy)

            # if BestBoyNorm in ctx.message.author.roles:
            #     rolestoremove.extend(BestBoyNorm)
            #     rolestogive.append(FagNorm)
            # if BestBoyRare in ctx.message.author.roles:
            #     rolestoremove.extend(BestBoyRare)
            #     rolestogive.append(FagRare)
            # if BestBoyLegacy in ctx.message.author.roles:
            #     rolestoremove.extend(BestBoyLegacy)
            #     rolestogive.append(FagLegacy)
            
            if Moni in ctx.message.author.roles:
                rolestoremove.extend(Moni)
                rolestogive.append(BestBoyNorm)
            if MoniRare in ctx.message.author.roles:
                rolestoremove.extend(MoniRare)
                rolestogive.append(BestBoyRare)
            if MoniLegacy in ctx.message.author.roles:
                rolestoremove.extend(MoniLegacy)
                rolestogive.append(BestBoyLegacy)

            await self.bot.add_roles(ctx.message.author, *rolestogive)
            await asyncio.sleep(2)
            await self.bot.remove_roles(ctx.message.author, *rolestoremove)
            await self.bot.say("`Assigned user "+ctx.message.author.name+" the {Protagonist} flag.`")

def setup(bot):
    bot.add_cog(Roles(bot))