    @commands.command(pass_context=True, aliases = ["Monika", "moni","Moni"])
    async def monika(self, ctx, user : discord.User):
        rolestoremove = []
        rolestogive = []
        norm = False
        rare = False
        legacy = False
        server = ctx.message.server
        user = server.get_member(user.id)
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
        if NatNorm in user.roles:
            rolestoremove.append(NatNorm)
            rolestogive.append(Moni)
        if NatRare in user.roles:
            rolestoremove.append(NatRare)
            rolestogive.append(MoniRare)
        if NatLegacy in user.roles:
            rolestoremove.append(NatLegacy)
            rolestogive.append(MoniLegacy)

        if PenNorm in user.roles:
            rolestoremove.append(PenNorm)
            rolestogive.append(Moni)
        if PenRare in user.roles:
            rolestoremove.append(PenRare)
            rolestogive.append(MoniRare)
        if PenLegacy in user.roles:
            rolestoremove.append(PenLegacy)
            rolestogive.append(MoniLegacy)
        
        if CinnamonNorm in user.roles:
            rolestoremove.append(CinnamonNorm)
            rolestogive.append(Moni)
        if CinnamonRare in user.roles:
            rolestoremove.append(CinnamonRare)
            rolestogive.append(MoniRare)
        if CinnamonLegacy in user.roles:
            rolestoremove.append(CinnamonLegacy)
            rolestogive.append(MoniLegacy)
            
        if FagNorm in user.roles:
            rolestoremove.append(FagNorm)
            rolestogive.append(Moni)
        if FagRare in user.roles:
            rolestoremove.append(FagRare)
            rolestogive.append(MoniRare)
        if FagLegacy in user.roles:
            rolestoremove.append(FagLegacy)
            rolestogive.append(MoniLegacy)

        if BestBoyNorm in user.roles:
            rolestoremove.append(BestBoyNorm)
            rolestogive.append(Moni)
        if BestBoyRare in user.roles:
            rolestoremove.append(BestBoyRare)
            rolestogive.append(MoniRare)
        if BestBoyLegacy in user.roles:
            rolestoremove.append(BestBoyLegacy)
            rolestogive.append(MoniLegacy)
        
        # if Moni in user.roles:
        #     rolestoremove.append(Moni)
        #     rolestogive.append(Moni)
        # if MoniRare in user.roles:
        #     rolestoremove.append(MoniRare)
        #     rolestogive.append(MoniRare)
        # if MoniLegacy in user.roles:
        #     rolestoremove.append(MoniLegacy)
        #     rolestogive.append(MoniLegacy)

        await self.bot.add_roles(user, *rolestogive)
        await asyncio.sleep(2)
        await self.bot.remove_roles(user, *rolestoremove)
        await self.bot.say("`Assigned user "+user.name+" the {Monika} flag.`")

    @commands.command(pass_context=True, aliases = ["Cinnamon bun", "Cinnamon Bun", "cinnamon bun", "cinnamon Bun", "Sayori", "sayo", "Sayo"])
    async def sayori(self, ctx, user : discord.User):
        rolestoremove = []
        rolestogive = []
        norm = False
        rare = False
        legacy = False
        server = ctx.message.server
        user = server.get_member(user.id)
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
        if NatNorm in user.roles:
            rolestoremove.append(NatNorm)
            rolestogive.append(CinnamonNorm)
        if NatRare in user.roles:
            rolestoremove.append(NatRare)
            rolestogive.append(CinnamonRare)
        if NatLegacy in user.roles:
            rolestoremove.append(NatLegacy)
            rolestogive.append(CinnamonLegacy)

        if PenNorm in user.roles:
            rolestoremove.append(PenNorm)
            rolestogive.append(CinnamonNorm)
        if PenRare in user.roles:
            rolestoremove.append(PenRare)
            rolestogive.append(CinnamonRare)
        if PenLegacy in user.roles:
            rolestoremove.append(PenLegacy)
            rolestogive.append(CinnamonLegacy)
        
        # if CinnamonNorm in user.roles:
        #     rolestoremove.append(CinnamonNorm)
        #     rolestogive.append(Moni)
        # if CinnamonRare in user.roles:
        #     rolestoremove.append(CinnamonRare)
        #     rolestogive.append(MoniRare)
        # if CinnamonLegacy in user.roles:
        #     rolestoremove.append(CinnamonLegacy)
        #     rolestogive.append(MoniLegacy)
            
        if FagNorm in user.roles:
            rolestoremove.append(FagNorm)
            rolestogive.append(CinnamonNorm)
        if FagRare in user.roles:
            rolestoremove.append(FagRare)
            rolestogive.append(CinnamonRare)
        if FagLegacy in user.roles:
            rolestoremove.append(FagLegacy)
            rolestogive.append(CinnamonLegacy)

        if BestBoyNorm in user.roles:
            rolestoremove.append(BestBoyNorm)
            rolestogive.append(CinnamonNorm)
        if BestBoyRare in user.roles:
            rolestoremove.append(BestBoyRare)
            rolestogive.append(CinnamonRare)
        if BestBoyLegacy in user.roles:
            rolestoremove.append(BestBoyLegacy)
            rolestogive.append(CinnamonLegacy)
        
        if Moni in user.roles:
            rolestoremove.append(Moni)
            rolestogive.append(CinnamonNorm)
        if MoniRare in user.roles:
            rolestoremove.append(MoniRare)
            rolestogive.append(CinnamonRare)
        if MoniLegacy in user.roles:
            rolestoremove.append(MoniLegacy)
            rolestogive.append(CinnamonLegacy)

        await self.bot.add_roles(user, *rolestogive)
        await asyncio.sleep(2)
        await self.bot.remove_roles(user, *rolestoremove)
        await self.bot.say("`Assigned user "+user.name+" the {Sayori} flag.`")

    @commands.command(pass_context=True, aliases = ["Nat", "Natsuki", "nat", "tsundere"])
    async def natsuki(self, ctx, user : discord.User):
        rolestoremove = []
        rolestogive = []
        norm = False
        rare = False
        legacy = False
        server = ctx.message.server
        user = server.get_member(user.id)
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
        # if NatNorm in user.roles:
        #     rolestoremove.append(NatNorm)
        #     rolestogive.append(Cinnamon)
        # if NatRare in user.roles:
        #     rolestoremove.append(NatRare)
        #     rolestogive.append(CinnamonRare)
        # if NatLegacy in user.roles:
        #     rolestoremove.append(NatLegacy)
        #     rolestogive.append(CinnamonLegacy)

        if PenNorm in user.roles:
            rolestoremove.append(PenNorm)
            rolestogive.append(NatNorm)
        if PenRare in user.roles:
            rolestoremove.append(PenRare)
            rolestogive.append(NatRare)
        if PenLegacy in user.roles:
            rolestoremove.append(PenLegacy)
            rolestogive.append(NatLegacy)
        
        if CinnamonNorm in user.roles:
            rolestoremove.append(CinnamonNorm)
            rolestogive.append(NatNorm)
        if CinnamonRare in user.roles:
            rolestoremove.append(CinnamonRare)
            rolestogive.append(NatRare)
        if CinnamonLegacy in user.roles:
            rolestoremove.append(CinnamonLegacy)
            rolestogive.append(NatLegacy)
            
        if FagNorm in user.roles:
            rolestoremove.append(FagNorm)
            rolestogive.append(NatNorm)
        if FagRare in user.roles:
            rolestoremove.append(FagRare)
            rolestogive.append(NatRare)
        if FagLegacy in user.roles:
            rolestoremove.append(FagLegacy)
            rolestogive.append(NatLegacy)

        if BestBoyNorm in user.roles:
            rolestoremove.append(BestBoyNorm)
            rolestogive.append(NatNorm)
        if BestBoyRare in user.roles:
            rolestoremove.append(BestBoyRare)
            rolestogive.append(NatRare)
        if BestBoyLegacy in user.roles:
            rolestoremove.append(BestBoyLegacy)
            rolestogive.append(NatLegacy)
        
        if Moni in user.roles:
            rolestoremove.append(Moni)
            rolestogive.append(NatNorm)
        if MoniRare in user.roles:
            rolestoremove.append(MoniRare)
            rolestogive.append(NatRare)
        if MoniLegacy in user.roles:
            rolestoremove.append(MoniLegacy)
            rolestogive.append(NatLegacy)

        await self.bot.add_roles(user, *rolestogive)
        await asyncio.sleep(2)
        await self.bot.remove_roles(user, *rolestoremove)
        await self.bot.say("`Assigned user "+user.name+" the {Natsuki} flag.`")

    @commands.command(pass_context=True, aliases = ["Misao"])
    async def misao(self, ctx, user : discord.User):
        rolestoremove = []
        rolestogive = []
        norm = False
        rare = False
        legacy = False
        server = ctx.message.server
        user = server.get_member(user.id)
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

        if NatNorm in user.roles:
            rolestoremove.append(NatNorm)
            rolestogive.append(FagNorm)
        if NatRare in user.roles:
            rolestoremove.append(NatRare)
            rolestogive.append(FagRare)
        if NatLegacy in user.roles:
            rolestoremove.append(NatLegacy)
            rolestogive.append(FagLegacy)

        if PenNorm in user.roles:
            rolestoremove.append(PenNorm)
            rolestogive.append(FagNorm)
        if PenRare in user.roles:
            rolestoremove.append(PenRare)
            rolestogive.append(FagRare)
        if PenLegacy in user.roles:
            rolestoremove.append(PenLegacy)
            rolestogive.append(FagLegacy)
        
        if CinnamonNorm in user.roles:
            rolestoremove.append(CinnamonNorm)
            rolestogive.append(FagNorm)
        if CinnamonRare in user.roles:
            rolestoremove.append(CinnamonRare)
            rolestogive.append(FagRare)
        if CinnamonLegacy in user.roles:
            rolestoremove.append(CinnamonLegacy)
            rolestogive.append(FagLegacy)
            
        # if FagNorm in user.roles:
        #     rolestoremove.append(FagNorm)
        #     rolestogive.append(PenNorm)
        # if FagRare in user.roles:
        #     rolestoremove.append(FagRare)
        #     rolestogive.append(PenRare)
        # if FagLegacy in user.roles:
        #     rolestoremove.append(FagLegacy)
        #     rolestogive.append(PenLegacy)

        if BestBoyNorm in user.roles:
            rolestoremove.append(BestBoyNorm)
            rolestogive.append(FagNorm)
        if BestBoyRare in user.roles:
            rolestoremove.append(BestBoyRare)
            rolestogive.append(FagRare)
        if BestBoyLegacy in user.roles:
            rolestoremove.append(BestBoyLegacy)
            rolestogive.append(FagLegacy)
        
        if Moni in user.roles:
            rolestoremove.append(Moni)
            rolestogive.append(FagNorm)
        if MoniRare in user.roles:
            rolestoremove.append(MoniRare)
            rolestogive.append(FagRare)
        if MoniLegacy in user.roles:
            rolestoremove.append(MoniLegacy)
            rolestogive.append(FagLegacy)

        await self.bot.add_roles(user, *rolestogive)
        await asyncio.sleep(2)
        await self.bot.remove_roles(user, *rolestoremove)
        await self.bot.say("`Assigned user "+user.name+" the {Misao} flag.`")

    @commands.command(pass_context=True, aliases = ["Dan","Protag"])
    async def protag(self, ctx, user : discord.User):
        rolestoremove = []
        rolestogive = []
        norm = False
        rare = False
        legacy = False
        server = ctx.message.server
        user = server.get_member(user.id)
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

        if NatNorm in user.roles:
            rolestoremove.append(NatNorm)
            rolestogive.append(BestBoyNorm)
        if NatRare in user.roles:
            rolestoremove.append(NatRare)
            rolestogive.append(BestBoyRare)
        if NatLegacy in user.roles:
            rolestoremove.append(NatLegacy)
            rolestogive.append(BestBoyLegacy)

        if PenNorm in user.roles:
            rolestoremove.append(PenNorm)
            rolestogive.append(BestBoyNorm)
        if PenRare in user.roles:
            rolestoremove.append(PenRare)
            rolestogive.append(BestBoyRare)
        if PenLegacy in user.roles:
            rolestoremove.append(PenLegacy)
            rolestogive.append(BestBoyLegacy)
        
        if CinnamonNorm in user.roles:
            rolestoremove.append(CinnamonNorm)
            rolestogive.append(BestBoyNorm)
        if CinnamonRare in user.roles:
            rolestoremove.append(CinnamonRare)
            rolestogive.append(BestBoyRare)
        if CinnamonLegacy in user.roles:
            rolestoremove.append(CinnamonLegacy)
            rolestogive.append(BestBoyLegacy)
            
        if FagNorm in user.roles:
            rolestoremove.append(FagNorm)
            rolestogive.append(BestBoyNorm)
        if FagRare in user.roles:
            rolestoremove.append(FagRare)
            rolestogive.append(BestBoyRare)
        if FagLegacy in user.roles:
            rolestoremove.append(FagLegacy)
            rolestogive.append(BestBoyLegacy)

        # if BestBoyNorm in user.roles:
        #     rolestoremove.append(BestBoyNorm)
        #     rolestogive.append(FagNorm)
        # if BestBoyRare in user.roles:
        #     rolestoremove.append(BestBoyRare)
        #     rolestogive.append(FagRare)
        # if BestBoyLegacy in user.roles:
        #     rolestoremove.append(BestBoyLegacy)
        #     rolestogive.append(FagLegacy)
        
        if Moni in user.roles:
            rolestoremove.append(Moni)
            rolestogive.append(BestBoyNorm)
        if MoniRare in user.roles:
            rolestoremove.append(MoniRare)
            rolestogive.append(BestBoyRare)
        if MoniLegacy in user.roles:
            rolestoremove.append(MoniLegacy)
            rolestogive.append(BestBoyLegacy)

        await self.bot.add_roles(user, *rolestogive)
        await asyncio.sleep(2)
        await self.bot.remove_roles(user, *rolestoremove)
        await self.bot.say("`Assigned user"+user.name+" the {Protagonist} flag.`")

    @commands.command(pass_context=True, aliases = ["Yuri"])
    async def yuri(self, ctx, user : discord.User):
        rolestoremove = []
        rolestogive = []
        norm = False
        rare = False
        legacy = False
        server = ctx.message.server
        user = server.get_member(user.id)
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

        if NatNorm in user.roles:
            rolestoremove.append(NatNorm)
            rolestogive.append(PenNorm)
        if NatRare in user.roles:
            rolestoremove.append(NatRare)
            rolestogive.append(PenRare)
        if NatLegacy in user.roles:
            rolestoremove.append(NatLegacy)
            rolestogive.append(PenLegacy)

        if PenNorm in user.roles:
            rolestoremove.append(PenNorm)
            rolestogive.append(PenNorm)
        if PenRare in user.roles:
            rolestoremove.append(PenRare)
            rolestogive.append(PenRare)
        if PenLegacy in user.roles:
            rolestoremove.append(PenLegacy)
            rolestogive.append(PenLegacy)
        
        if CinnamonNorm in user.roles:
            rolestoremove.append(CinnamonNorm)
            rolestogive.append(PenNorm)
        if CinnamonRare in user.roles:
            rolestoremove.append(CinnamonRare)
            rolestogive.append(PenRare)
        if CinnamonLegacy in user.roles:
            rolestoremove.append(CinnamonLegacy)
            rolestogive.append(PenLegacy)
            
        if FagNorm in user.roles:
            rolestoremove.append(FagNorm)
            rolestogive.append(PenNorm)
        if FagRare in user.roles:
            rolestoremove.append(FagRare)
            rolestogive.append(PenRare)
        if FagLegacy in user.roles:
            rolestoremove.append(FagLegacy)
            rolestogive.append(PenLegacy)

        if BestBoyNorm in user.roles:
            rolestoremove.append(BestBoyNorm)
            rolestogive.append(PenNorm)
        if BestBoyRare in user.roles:
            rolestoremove.append(BestBoyRare)
            rolestogive.append(PenRare)
        if BestBoyLegacy in user.roles:
            rolestoremove.append(BestBoyLegacy)
            rolestogive.append(PenLegacy)
        
        if Moni in user.roles:
            rolestoremove.append(Moni)
            rolestogive.append(PenNorm)
        if MoniRare in user.roles:
            rolestoremove.append(MoniRare)
            rolestogive.append(PenRare)
        if MoniLegacy in user.roles:
            rolestoremove.append(MoniLegacy)
            rolestogive.append(PenLegacy)

        await self.bot.add_roles(user, *rolestogive)
        await asyncio.sleep(2)
        await self.bot.remove_roles(user, *rolestoremove)
        await self.bot.say("`Assigned user "+user.name+" the {Yuri} flag.`")