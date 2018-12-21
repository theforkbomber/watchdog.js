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
            rolestoremove.append(NatNorm)
            rolestogive.append(Moni)
        if NatRare in ctx.message.author.roles:
            rolestoremove.append(NatRare)
            rolestogive.append(MoniRare)
        if NatLegacy in ctx.message.author.roles:
            rolestoremove.append(NatLegacy)
            rolestogive.append(MoniLegacy)

        if PenNorm in ctx.message.author.roles:
            rolestoremove.append(PenNorm)
            rolestogive.append(Moni)
        if PenRare in ctx.message.author.roles:
            rolestoremove.append(PenRare)
            rolestogive.append(MoniRare)
        if PenLegacy in ctx.message.author.roles:
            rolestoremove.append(PenLegacy)
            rolestogive.append(MoniLegacy)
        
        if CinnamonNorm in ctx.message.author.roles:
            rolestoremove.append(CinnamonNorm)
            rolestogive.append(Moni)
        if CinnamonRare in ctx.message.author.roles:
            rolestoremove.append(CinnamonRare)
            rolestogive.append(MoniRare)
        if CinnamonLegacy in ctx.message.author.roles:
            rolestoremove.append(CinnamonLegacy)
            rolestogive.append(MoniLegacy)
            
        if FagNorm in ctx.message.author.roles:
            rolestoremove.append(FagNorm)
            rolestogive.append(Moni)
        if FagRare in ctx.message.author.roles:
            rolestoremove.append(FagRare)
            rolestogive.append(MoniRare)
        if FagLegacy in ctx.message.author.roles:
            rolestoremove.append(FagLegacy)
            rolestogive.append(MoniLegacy)

        if BestBoyNorm in ctx.message.author.roles:
            rolestoremove.append(BestBoyNorm)
            rolestogive.append(Moni)
        if BestBoyRare in ctx.message.author.roles:
            rolestoremove.append(BestBoyRare)
            rolestogive.append(MoniRare)
        if BestBoyLegacy in ctx.message.author.roles:
            rolestoremove.append(BestBoyLegacy)
            rolestogive.append(MoniLegacy)
        
        # if Moni in ctx.message.author.roles:
        #     rolestoremove.append(Moni)
        #     rolestogive.append(Moni)
        # if MoniRare in ctx.message.author.roles:
        #     rolestoremove.append(MoniRare)
        #     rolestogive.append(MoniRare)
        # if MoniLegacy in ctx.message.author.roles:
        #     rolestoremove.append(MoniLegacy)
        #     rolestogive.append(MoniLegacy)

        await self.bot.add_roles(ctx.message.author, *rolestogive)
        await asyncio.sleep(2)
        await self.bot.remove_roles(ctx.message.author, *rolestoremove)
        await self.bot.say("`Assigned user "+ctx.message.author.name+" the {Monika} flag.`")

    @roleme.command(pass_context=True, aliases = ["Cinnamon bun", "Cinnamon Bun", "cinnamon bun", "cinnamon Bun", "Sayori", "sayo", "Sayo"])
    async def sayori(self, ctx):
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
            rolestoremove.append(NatNorm)
            rolestogive.append(CinnamonNorm)
        if NatRare in ctx.message.author.roles:
            rolestoremove.append(NatRare)
            rolestogive.append(CinnamonRare)
        if NatLegacy in ctx.message.author.roles:
            rolestoremove.append(NatLegacy)
            rolestogive.append(CinnamonLegacy)

        if PenNorm in ctx.message.author.roles:
            rolestoremove.append(PenNorm)
            rolestogive.append(CinnamonNorm)
        if PenRare in ctx.message.author.roles:
            rolestoremove.append(PenRare)
            rolestogive.append(CinnamonRare)
        if PenLegacy in ctx.message.author.roles:
            rolestoremove.append(PenLegacy)
            rolestogive.append(CinnamonLegacy)
        
        # if CinnamonNorm in ctx.message.author.roles:
        #     rolestoremove.append(CinnamonNorm)
        #     rolestogive.append(Moni)
        # if CinnamonRare in ctx.message.author.roles:
        #     rolestoremove.append(CinnamonRare)
        #     rolestogive.append(MoniRare)
        # if CinnamonLegacy in ctx.message.author.roles:
        #     rolestoremove.append(CinnamonLegacy)
        #     rolestogive.append(MoniLegacy)
            
        if FagNorm in ctx.message.author.roles:
            rolestoremove.append(FagNorm)
            rolestogive.append(CinnamonNorm)
        if FagRare in ctx.message.author.roles:
            rolestoremove.append(FagRare)
            rolestogive.append(CinnamonRare)
        if FagLegacy in ctx.message.author.roles:
            rolestoremove.append(FagLegacy)
            rolestogive.append(CinnamonLegacy)

        if BestBoyNorm in ctx.message.author.roles:
            rolestoremove.append(BestBoyNorm)
            rolestogive.append(CinnamonNorm)
        if BestBoyRare in ctx.message.author.roles:
            rolestoremove.append(BestBoyRare)
            rolestogive.append(CinnamonRare)
        if BestBoyLegacy in ctx.message.author.roles:
            rolestoremove.append(BestBoyLegacy)
            rolestogive.append(CinnamonLegacy)
        
        if Moni in ctx.message.author.roles:
            rolestoremove.append(Moni)
            rolestogive.append(CinnamonNorm)
        if MoniRare in ctx.message.author.roles:
            rolestoremove.append(MoniRare)
            rolestogive.append(CinnamonRare)
        if MoniLegacy in ctx.message.author.roles:
            rolestoremove.append(MoniLegacy)
            rolestogive.append(CinnamonLegacy)

        await self.bot.add_roles(ctx.message.author, *rolestogive)
        await asyncio.sleep(2)
        await self.bot.remove_roles(ctx.message.author, *rolestoremove)
        await self.bot.say("`Assigned user "+ctx.message.author.name+" the {Sayori} flag.`")

    @roleme.command(pass_context=True, aliases = ["Nat", "Natsuki", "nat", "tsundere"])
    async def natsuki(self, ctx):
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
        #     rolestoremove.append(NatNorm)
        #     rolestogive.append(Cinnamon)
        # if NatRare in ctx.message.author.roles:
        #     rolestoremove.append(NatRare)
        #     rolestogive.append(CinnamonRare)
        # if NatLegacy in ctx.message.author.roles:
        #     rolestoremove.append(NatLegacy)
        #     rolestogive.append(CinnamonLegacy)

        if PenNorm in ctx.message.author.roles:
            rolestoremove.append(PenNorm)
            rolestogive.append(NatNorm)
        if PenRare in ctx.message.author.roles:
            rolestoremove.append(PenRare)
            rolestogive.append(NatRare)
        if PenLegacy in ctx.message.author.roles:
            rolestoremove.append(PenLegacy)
            rolestogive.append(NatLegacy)
        
        if CinnamonNorm in ctx.message.author.roles:
            rolestoremove.append(CinnamonNorm)
            rolestogive.append(NatNorm)
        if CinnamonRare in ctx.message.author.roles:
            rolestoremove.append(CinnamonRare)
            rolestogive.append(NatRare)
        if CinnamonLegacy in ctx.message.author.roles:
            rolestoremove.append(CinnamonLegacy)
            rolestogive.append(NatLegacy)
            
        if FagNorm in ctx.message.author.roles:
            rolestoremove.append(FagNorm)
            rolestogive.append(NatNorm)
        if FagRare in ctx.message.author.roles:
            rolestoremove.append(FagRare)
            rolestogive.append(NatRare)
        if FagLegacy in ctx.message.author.roles:
            rolestoremove.append(FagLegacy)
            rolestogive.append(NatLegacy)

        if BestBoyNorm in ctx.message.author.roles:
            rolestoremove.append(BestBoyNorm)
            rolestogive.append(NatNorm)
        if BestBoyRare in ctx.message.author.roles:
            rolestoremove.append(BestBoyRare)
            rolestogive.append(NatRare)
        if BestBoyLegacy in ctx.message.author.roles:
            rolestoremove.append(BestBoyLegacy)
            rolestogive.append(NatLegacy)
        
        if Moni in ctx.message.author.roles:
            rolestoremove.append(Moni)
            rolestogive.append(NatNorm)
        if MoniRare in ctx.message.author.roles:
            rolestoremove.append(MoniRare)
            rolestogive.append(NatRare)
        if MoniLegacy in ctx.message.author.roles:
            rolestoremove.append(MoniLegacy)
            rolestogive.append(NatLegacy)

        await self.bot.add_roles(ctx.message.author, *rolestogive)
        await asyncio.sleep(2)
        await self.bot.remove_roles(ctx.message.author, *rolestoremove)
        await self.bot.say("`Assigned user "+ctx.message.author.name+" the {Natsuki} flag.`")

    @roleme.command(pass_context=True, aliases = ["Misao"])
    async def misao(self, ctx):
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
            rolestoremove.append(NatNorm)
            rolestogive.append(FagNorm)
        if NatRare in ctx.message.author.roles:
            rolestoremove.append(NatRare)
            rolestogive.append(FagRare)
        if NatLegacy in ctx.message.author.roles:
            rolestoremove.append(NatLegacy)
            rolestogive.append(FagLegacy)

        if PenNorm in ctx.message.author.roles:
            rolestoremove.append(PenNorm)
            rolestogive.append(FagNorm)
        if PenRare in ctx.message.author.roles:
            rolestoremove.append(PenRare)
            rolestogive.append(FagRare)
        if PenLegacy in ctx.message.author.roles:
            rolestoremove.append(PenLegacy)
            rolestogive.append(FagLegacy)
        
        if CinnamonNorm in ctx.message.author.roles:
            rolestoremove.append(CinnamonNorm)
            rolestogive.append(FagNorm)
        if CinnamonRare in ctx.message.author.roles:
            rolestoremove.append(CinnamonRare)
            rolestogive.append(FagRare)
        if CinnamonLegacy in ctx.message.author.roles:
            rolestoremove.append(CinnamonLegacy)
            rolestogive.append(FagLegacy)
            
        # if FagNorm in ctx.message.author.roles:
        #     rolestoremove.append(FagNorm)
        #     rolestogive.append(PenNorm)
        # if FagRare in ctx.message.author.roles:
        #     rolestoremove.append(FagRare)
        #     rolestogive.append(PenRare)
        # if FagLegacy in ctx.message.author.roles:
        #     rolestoremove.append(FagLegacy)
        #     rolestogive.append(PenLegacy)

        if BestBoyNorm in ctx.message.author.roles:
            rolestoremove.append(BestBoyNorm)
            rolestogive.append(FagNorm)
        if BestBoyRare in ctx.message.author.roles:
            rolestoremove.append(BestBoyRare)
            rolestogive.append(FagRare)
        if BestBoyLegacy in ctx.message.author.roles:
            rolestoremove.append(BestBoyLegacy)
            rolestogive.append(FagLegacy)
        
        if Moni in ctx.message.author.roles:
            rolestoremove.append(Moni)
            rolestogive.append(FagNorm)
        if MoniRare in ctx.message.author.roles:
            rolestoremove.append(MoniRare)
            rolestogive.append(FagRare)
        if MoniLegacy in ctx.message.author.roles:
            rolestoremove.append(MoniLegacy)
            rolestogive.append(FagLegacy)

        await self.bot.add_roles(ctx.message.author, *rolestogive)
        await asyncio.sleep(2)
        await self.bot.remove_roles(ctx.message.author, *rolestoremove)
        await self.bot.say("`Assigned user "+ctx.message.author.name+" the {Misao} flag.`")

    @roleme.command(pass_context=True, aliases = ["Dan","Protag"])
    async def protag(self, ctx):
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
            rolestoremove.append(NatNorm)
            rolestogive.append(BestBoyNorm)
        if NatRare in ctx.message.author.roles:
            rolestoremove.append(NatRare)
            rolestogive.append(BestBoyRare)
        if NatLegacy in ctx.message.author.roles:
            rolestoremove.append(NatLegacy)
            rolestogive.append(BestBoyLegacy)

        if PenNorm in ctx.message.author.roles:
            rolestoremove.append(PenNorm)
            rolestogive.append(BestBoyNorm)
        if PenRare in ctx.message.author.roles:
            rolestoremove.append(PenRare)
            rolestogive.append(BestBoyRare)
        if PenLegacy in ctx.message.author.roles:
            rolestoremove.append(PenLegacy)
            rolestogive.append(BestBoyLegacy)
        
        if CinnamonNorm in ctx.message.author.roles:
            rolestoremove.append(CinnamonNorm)
            rolestogive.append(BestBoyNorm)
        if CinnamonRare in ctx.message.author.roles:
            rolestoremove.append(CinnamonRare)
            rolestogive.append(BestBoyRare)
        if CinnamonLegacy in ctx.message.author.roles:
            rolestoremove.append(CinnamonLegacy)
            rolestogive.append(BestBoyLegacy)
            
        if FagNorm in ctx.message.author.roles:
            rolestoremove.append(FagNorm)
            rolestogive.append(BestBoyNorm)
        if FagRare in ctx.message.author.roles:
            rolestoremove.append(FagRare)
            rolestogive.append(BestBoyRare)
        if FagLegacy in ctx.message.author.roles:
            rolestoremove.append(FagLegacy)
            rolestogive.append(BestBoyLegacy)

        # if BestBoyNorm in ctx.message.author.roles:
        #     rolestoremove.append(BestBoyNorm)
        #     rolestogive.append(FagNorm)
        # if BestBoyRare in ctx.message.author.roles:
        #     rolestoremove.append(BestBoyRare)
        #     rolestogive.append(FagRare)
        # if BestBoyLegacy in ctx.message.author.roles:
        #     rolestoremove.append(BestBoyLegacy)
        #     rolestogive.append(FagLegacy)
        
        if Moni in ctx.message.author.roles:
            rolestoremove.append(Moni)
            rolestogive.append(BestBoyNorm)
        if MoniRare in ctx.message.author.roles:
            rolestoremove.append(MoniRare)
            rolestogive.append(BestBoyRare)
        if MoniLegacy in ctx.message.author.roles:
            rolestoremove.append(MoniLegacy)
            rolestogive.append(BestBoyLegacy)

        await self.bot.add_roles(ctx.message.author, *rolestogive)
        await asyncio.sleep(2)
        await self.bot.remove_roles(ctx.message.author, *rolestoremove)
        await self.bot.say("`Assigned user"+ctx.message.author.name+" the {Protagonist} flag.`")

    @roleme.command(pass_context=True, aliases = ["Yuri"])
    async def yuri(self, ctx):
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
                rolestoremove.append(NatNorm)
                rolestogive.append(PenNorm)
            if NatRare in ctx.message.author.roles:
                rolestoremove.append(NatRare)
                rolestogive.append(PenRare)
            if NatLegacy in ctx.message.author.roles:
                rolestoremove.append(NatLegacy)
                rolestogive.append(PenLegacy)

            if PenNorm in ctx.message.author.roles:
                rolestoremove.append(PenNorm)
                rolestogive.append(PenNorm)
            if PenRare in ctx.message.author.roles:
                rolestoremove.append(PenRare)
                rolestogive.append(PenRare)
            if PenLegacy in ctx.message.author.roles:
                rolestoremove.append(PenLegacy)
                rolestogive.append(PenLegacy)
            
            if CinnamonNorm in ctx.message.author.roles:
                rolestoremove.append(CinnamonNorm)
                rolestogive.append(PenNorm)
            if CinnamonRare in ctx.message.author.roles:
                rolestoremove.append(CinnamonRare)
                rolestogive.append(PenRare)
            if CinnamonLegacy in ctx.message.author.roles:
                rolestoremove.append(CinnamonLegacy)
                rolestogive.append(PenLegacy)
                
            if FagNorm in ctx.message.author.roles:
                rolestoremove.append(FagNorm)
                rolestogive.append(PenNorm)
            if FagRare in ctx.message.author.roles:
                rolestoremove.append(FagRare)
                rolestogive.append(PenRare)
            if FagLegacy in ctx.message.author.roles:
                rolestoremove.append(FagLegacy)
                rolestogive.append(PenLegacy)

            if BestBoyNorm in ctx.message.author.roles:
                rolestoremove.append(BestBoyNorm)
                rolestogive.append(PenNorm)
            if BestBoyRare in ctx.message.author.roles:
                rolestoremove.append(BestBoyRare)
                rolestogive.append(PenRare)
            if BestBoyLegacy in ctx.message.author.roles:
                rolestoremove.append(BestBoyLegacy)
                rolestogive.append(PenLegacy)
            
            if Moni in ctx.message.author.roles:
                rolestoremove.append(Moni)
                rolestogive.append(PenNorm)
            if MoniRare in ctx.message.author.roles:
                rolestoremove.append(MoniRare)
                rolestogive.append(PenRare)
            if MoniLegacy in ctx.message.author.roles:
                rolestoremove.append(MoniLegacy)
                rolestogive.append(PenLegacy)

            await self.bot.add_roles(ctx.message.author, *rolestogive)
            await asyncio.sleep(2)
            await self.bot.remove_roles(ctx.message.author, *rolestoremove)
            await self.bot.say("`Assigned user "+ctx.message.author.name+" the {Yuri} flag.`")

def setup(bot):
    bot.add_cog(Roles(bot))