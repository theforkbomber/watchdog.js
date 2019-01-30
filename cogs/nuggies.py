from discord.ext import commands
import discord
import psycopg2
import asyncio
import config

async def chck(self, server, name, member):
    if name == "doki doki":
        role = discord.utils.get(server.roles, name = "Doki Doki")
        await self.bot.add_roles(member, role)
        # if name == "protagonist":
        #     role = discord.utils.get(server.roles, name = "Protagonist")
        #     await self.bot.add_roles(member, role)
    if name == "miyuki":
        role = discord.utils.get(server.roles, name = "Miyuki")
        await self.bot.add_roles(member, role)
    if name == "rare":
        monirole = discord.utils.get(server.roles, name = "Monika")
        yurirole = discord.utils.get(server.roles, name = "Yuri")
        natsrole = discord.utils.get(server.roles, name = "Natsuki")
        sayorole = discord.utils.get(server.roles, name = "Sayori")
        misarole = discord.utils.get(server.roles, name = "Misao")
        protrole = discord.utils.get(server.roles, name = "Protagonist")
        if monirole in member.roles:
            role = discord.utils.get(server.roles, name = "Monika (Rare)")
            await self.bot.add_roles(member, role)
        if yurirole in member.roles:
            role = discord.utils.get(server.roles, name = "Yuri (Rare)")
            await self.bot.add_roles(member, role)
        if natsrole in member.roles:
            role = discord.utils.get(server.roles, name = "Natsuki (Rare)")
            await self.bot.add_roles(member, role)
        if misarole in member.roles:
            role = discord.utils.get(server.roles, name = "Misao (Rare)")
            await self.bot.add_roles(member, role)
        if protrole in member.roles:
            role = discord.utils.get(server.roles, name = "Protagonist (Rare)")
            await self.bot.add_roles(member, role)
        if sayorole in member.roles:
            role = discord.utils.get(server.roles, name = "Sayori (Rare)")
            await self.bot.add_roles(member, role)

    if name == "legacy":
        monirole = discord.utils.get(server.roles, name = "Monika")
        yurirole = discord.utils.get(server.roles, name = "Yuri")
        natsrole = discord.utils.get(server.roles, name = "Natsuki")
        sayorole = discord.utils.get(server.roles, name = "Sayori")
        misarole = discord.utils.get(server.roles, name = "Misao")
        protrole = discord.utils.get(server.roles, name = "Protagonist")
        if monirole in member.roles:
            role = discord.utils.get(server.roles, name = "Monika (Legacy)")
            await self.bot.add_roles(member, role)
        if yurirole in member.roles:
            role = discord.utils.get(server.roles, name = "Yuri (Legacy)")
            await self.bot.add_roles(member, role)
        if natsrole in member.roles:
            role = discord.utils.get(server.roles, name = "Natsuki (Legacy)")
            await self.bot.add_roles(member, role)
        if misarole in member.roles:
            role = discord.utils.get(server.roles, name = "Misao (Legacy)")
            await self.bot.add_roles(member, role)
        if protrole in member.roles:
            role = discord.utils.get(server.roles, name = "Protagonist (Legacy)")
            await self.bot.add_roles(member, role)
        if sayorole in member.roles:
            role = discord.utils.get(server.roles, name = "Sayori (Legacy)")
            await self.bot.add_roles(member, role)
    if name == "protagonist":
        rolestoremove = []
        rolestogive = []
        norm = False
        rare = False
        legacy = False
        server = self.bot.get_server('369252350927306752')
        NatNorm = discord.utils.get(server.roles, name='Natsuki')
        PenNorm = discord.utils.get(server.roles, name='Yuri')
        FagNorm = discord.utils.get(server.roles, name='Misao')
        CinnamonNorm = discord.utils.get(server.roles, name='Sayori')
        BestBoyNorm = discord.utils.get(server.roles, name='Protagonist')
        NatRare = discord.utils.get(server.roles, name='Natsuki (Rare)')
        PenRare = discord.utils.get(server.roles, name='Yuri (Rare)')
        FagRare = discord.utils.get(server.roles, name='Misao (Rare)')
        CinnamonRare = discord.utils.get(server.roles, name='Sayori (Rare)')
        BestBoyRare = discord.utils.get(server.roles, name='Protagonist (Rare)')
        NatLegacy = discord.utils.get(server.roles, name='Natsuki (Legacy)')
        PenLegacy = discord.utils.get(server.roles, name='Yuri (Legacy)')
        FagLegacy = discord.utils.get(server.roles, name='Misao (Legacy)')
        CinnamonLegacy = discord.utils.get(server.roles, name='Sayori (Legacy)')
        BestBoyLegacy = discord.utils.get(server.roles, name='Protagonist (Legacy)')
        Moni = discord.utils.get(server.roles, name='Monika')
        MoniRare = discord.utils.get(server.roles, name='Monika (Rare)')
        MoniLegacy = discord.utils.get(server.roles, name='Monika (Legacy)')

        if NatNorm in member.roles.roles:
            rolestoremove.append(NatNorm)
            rolestogive.append(BestBoyNorm)
        if NatRare in member.roles.roles:
            rolestoremove.append(NatRare)
            rolestogive.append(BestBoyRare)
        if NatLegacy in member.roles.roles:
            rolestoremove.append(NatLegacy)
            rolestogive.append(BestBoyLegacy)

        if PenNorm in member.roles.roles:
            rolestoremove.append(PenNorm)
            rolestogive.append(BestBoyNorm)
        if PenRare in member.roles.roles:
            rolestoremove.append(PenRare)
            rolestogive.append(BestBoyRare)
        if PenLegacy in member.roles.roles:
            rolestoremove.append(PenLegacy)
            rolestogive.append(BestBoyLegacy)
        
        if CinnamonNorm in member.roles.roles:
            rolestoremove.append(CinnamonNorm)
            rolestogive.append(BestBoyNorm)
        if CinnamonRare in member.roles.roles:
            rolestoremove.append(CinnamonRare)
            rolestogive.append(BestBoyRare)
        if CinnamonLegacy in member.roles.roles:
            rolestoremove.append(CinnamonLegacy)
            rolestogive.append(BestBoyLegacy)
            
        if FagNorm in member.roles.roles:
            rolestoremove.append(FagNorm)
            rolestogive.append(BestBoyNorm)
        if FagRare in member.roles.roles:
            rolestoremove.append(FagRare)
            rolestogive.append(BestBoyRare)
        if FagLegacy in member.roles.roles:
            rolestoremove.append(FagLegacy)
            rolestogive.append(BestBoyLegacy)

        # if BestBoyNorm in member.roles.roles:
        #     rolestoremove.append(BestBoyNorm)
        #     rolestogive.append(FagNorm)
        # if BestBoyRare in member.roles.roles:
        #     rolestoremove.append(BestBoyRare)
        #     rolestogive.append(FagRare)
        # if BestBoyLegacy in member.roles.roles:
        #     rolestoremove.append(BestBoyLegacy)
        #     rolestogive.append(FagLegacy)
        
        if Moni in member.roles.roles:
            rolestoremove.append(Moni)
            rolestogive.append(BestBoyNorm)
        if MoniRare in member.roles.roles:
            rolestoremove.append(MoniRare)
            rolestogive.append(BestBoyRare)
        if MoniLegacy in member.roles.roles:
            rolestoremove.append(MoniLegacy)
            rolestogive.append(BestBoyLegacy)

        await self.bot.add_roles(member, *rolestogive)
        await asyncio.sleep(2)
        await self.bot.remove_roles(member, *rolestoremove)
    if name == "$player$":
        role = discord.utils.get(server.roles, name = "$PLAYER$")
        await self.bot.add_roles(member, role)
    if name == "princess' bedroom":
        role = discord.utils.get(server.roles, name = "Princess' Bedroom")
        await self.bot.add_roles(member, role)
    if name == "n word pass":
        role = discord.utils.get(server.roles, name = "N-Word Pass")
        await self.bot.add_roles(member, role)
    if name == "gold member":
        role = discord.utils.get(server.roles, name = "Gold Member")
        await self.bot.add_roles(member, role)
    if name == "custom role":
        await self.bot.send_message(self.bot.get_channel('526179783994900491'), member.name+" wants a custom role!")
    if name == "custom pic":
        c = await self.bot.application_info()
        owner = c.owner.id
        await self.bot.send_message(owner, member.name+" wants a custom command!")


class NuggiesCommands():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def balance(self, ctx):
        db = psycopg2.connect(host=config.host,database=config.database, user=config.user, password=config.password)
        cursor = db.cursor()
        cursor.execute("""SELECT nuggies FROM nuggies WHERE playerid = '%s'"""% ctx.message.author.id)
        balance = cursor.fetchone()
        balance = balance[0]
        await self.bot.say("Current Balance: "+str(balance)+" <:nuggies:539932838318047244>")
        db.close()

    @commands.command(pass_context=True)
    async def donate(self, ctx, user : discord.User, n : int):
        if user.id == ctx.message.author.id:
            await self.bot.say("Nice try, but no lol")
            return
        db = psycopg2.connect(host=config.host,database=config.database, user=config.user, password=config.password)
        cursor = db.cursor()
        cursor.execute("""SELECT nuggies FROM nuggies WHERE playerid = '%s'"""% ctx.message.author.id)
        balance = cursor.fetchone()
        balance = balance[0]
        if n > balance:
            await self.bot.say("You don't have enough nugs to give away the amount passed.")
        else:
            cursor.execute("""UPDATE nuggies SET nuggies = %s WHERE playerid = %s""", (balance-n, ctx.message.author.id))
            cursor.execute("""SELECT nuggies FROM nuggies WHERE playerid = '%s'"""% user.id)
            balance = cursor.fetchone()
            balance = balance[0]
            cursor.execute("""UPDATE nuggies SET nuggies = %s WHERE playerid = %s""", (balance+n, user.id))
            await self.bot.say(f"{str(n)} <:nuggies:539932838318047244> have successfully been transferred to {user.name}'s account!'")
        db.commit()
        db.close()

    @commands.command(pass_context=True)
    async def shop(self, ctx):
        jserver = self.bot.get_server("369252350927306752")
        reactioned = [discord.utils.get(jserver.emojis, id = "388471019914002433"), discord.utils.get(jserver.emojis, id = "388471020417318912"), discord.utils.get(jserver.emojis, id = "388471020341821450"), discord.utils.get(jserver.emojis, id = "388471020220055553"), discord.utils.get(jserver.emojis, id = "388471020220186626"), discord.utils.get(jserver.emojis, id = "388471020593479681"), discord.utils.get(jserver.emojis, id = "388471020190695426"), discord.utils.get(jserver.emojis, id = "388471020362661890"), discord.utils.get(jserver.emojis, id = "388471020581027844"), discord.utils.get(jserver.emojis, id = "388471020572377099")]
        def reactioncheck(reaction):
            if reaction == reactioned[0]:
                return 1
            if reaction == reactioned[1]:
                return 2
            if reaction == reactioned[2]:
                return 3
            if reaction == reactioned[3]:
                return 4
            if reaction == reactioned[4]:
                return 5
            if reaction == reactioned[5]:
                return 6
            if reaction == reactioned[6]:
                return 7
            if reaction == reactioned[7]:
                return 8
            if reaction == reactioned[8]:
                return 9
            if reaction == reactioned[9]:
                return 10
        db = psycopg2.connect(host=config.host,database=config.database, user=config.user, password=config.password)
        cursor = db.cursor()
        cursor.execute("""SELECT nuggies FROM nuggies WHERE playerid = '%s'"""% ctx.message.author.id)
        balance = cursor.fetchone()
        balance = balance[0]
        cursor.execute("""SELECT * FROM nuggies WHERE playerid = '%s'"""% ctx.message.author.id)
        found = cursor.fetchone()
        roles_available = ""
        keys = ""
        passes = ""
        custom = ""
        emotes = {}
        buyables = {}
        x = 0
        em = False
        embed = discord.Embed(title = f"{discord.utils.get(self.bot.get_server('427450243253272598').emojis, id = '539932838170984489')} MIYUKI'S NICE NUGGIE MARKET {discord.utils.get(self.bot.get_server('427450243253272598').emojis, id = '539932838170984489')}", description = "Current Balance: "+str(balance)+" <:nuggies:539932838318047244>")
        embed.set_footer(text = "Use the :votex: emotes to purchase goods")
        if found[0] != None:
            # try:
            #     itemlist = found[5].split("|")
            # else:

            user_roles = [r.name for r in ctx.message.author.roles]
            rare_roles = [r.name for r in ctx.message.author.roles if "(Rare)" in r.name]
            legacy_roles = [r.name for r in ctx.message.author.roles if "(Legacy)" in r.name]
            if rare_roles == [] and legacy_roles == []:
                x += 1
                roles_available += f"""{reactioned[x-1]} 1k <:nuggies:539932838318047244> Unlock Rare Tier (:arrow_double_up: UPGRADE) - "The second tier role, if you were lucky, you were given this when you joined, or given it later on. If you're less than lucky, buy this and you'll have the rare roles unlocked in your <#390197949780590603> flags"\n"""
                buyables.update({"rare":1000})
                emotes.update({x:"rare"})
            elif rare_roles != [] and legacy_roles == []:
                x += 1
                roles_available += f"""{reactioned[x-1]} 100k <:nuggies:539932838318047244> Unlock Legacy Tier (:arrow_double_up: UPGRADE) - "The third tier role, you were eligible for this role if you joined before a certain date. People with this role are a rare breed. Buy this and you'll have the legacy roles unlocked in your #role-requests flags"\n"""
                buyables.update({"legacy":100000})
                emotes.update({x:"legacy"})
            elif rare_roles == [] and legacy_roles != []:
                roles_available += f"""{reactioned[x-1]} 1k <:nuggies:539932838318047244> Unlock Rare Tier (:arrow_double_up: UPGRADE) - "The second tier role, if you were lucky, you were given this when you joined, or given it later on. If you're less than lucky, buy this and you'll have the rare roles unlocked in your #role-requests flags"\n"""
                buyables.update({"rare":1000})
                emotes.update({x:"rare"})
            if not "Protagonist" in user_roles:
                x += 1
                roles_available += f"""{reactioned[x-1]} 5k <:nuggies:539932838318047244> Protagonist - "An exclusive role, this one is me!!! The colour of my eyes! :slight_smile:"\n"""
                buyables.update({"protagonist":5000})
                emotes.update({x:"protagonist"})
            if not "Miyuki" in user_roles:
                x += 1
                roles_available += f"""{reactioned[x-1]} 10k <:nuggies:539932838318047244> Miyuki - "An exclusive role, this one is me!!! The colour of my eyes! :slight_smile:"\n"""
                buyables.update({"miyuki":10000})
                emotes.update({x:"miyuki"})
            if not "$PLAYER$" in user_roles:
                x += 1
                roles_available += f"""{reactioned[x-1]} 5151 <:nuggies:539932838318047244> $PLAYER$ - "An exclusive role, this one is you!!! The faint colour emitting from the other side of your monitor. :eyes:"\n"""
                buyables.update({"$player$":5151})
                emotes.update({x:"$player$"})
            if not "Gold Member" in user_roles:
                x += 1
                keys += f"""{reactioned[x-1]} 100k <:nuggies:539932838318047244> Gold Member "Gain access to all six waifu wars channels, and a few new exclusives!"\n"""
                buyables.update({"gold member":100000})
                emotes.update({x:"gold member"})
            if not "Doki Doki" in user_roles:
                x += 1
                keys += f"""{reactioned[x-1]} <:dokidokey:539971188387086336> 200 <:nuggies:539932838318047244> Doki Do-key :heart: "A special role that will give you access to the server's venting text channel.  To join the voice channel, the venter needs to allow you access."\n"""
                buyables.update({"doki doki":200})
                emotes.update({x:"doki doki"})
            if not "Princess' Bedroom" in user_roles:
                x += 1
                keys += f"""{reactioned[x-1]} <:princesskey:539971188638613554>  900 <:nuggies:539932838318047244> Princess Key - "Grants access to Marissa's bedroom. Not sure why you'd want this, but if you're into that sort of thing..."\n"""
                buyables.update({"princess' bedroom":900})
                emotes.update({x:"princess' bedroom"})
            if not "N-Word Pass" in user_roles:
                x += 1
                passes += f"""{reactioned[x-1]} 200 <:nuggies:539932838318047244> N Card - "I knew a guy who knew a guy who knew an African American, and with this, you can say it all you want! (Just don't go too overboard.)"\n"""
                buyables.update({"n word pass":200})
                emotes.update({x:"n word pass"})
            
            x += 1
            custom += f"""{reactioned[x-1]} 100k <:nuggies:539932838318047244> Custom Pictures Command - "Get your own little pictures command, like >os.rolo!"\n"""""
            buyables.update({"custom pic":100000})
            emotes.update({x:"custom pic"})
            x += 1
            custom += f"""{reactioned[x-1]} 100k <:nuggies:539932838318047244> Custom Role - "Your very own role, fit with a separate listing above Gold Member, and a colour of your choice! :confetti_ball:"\n"""
            buyables.update({"custom role":100000})
            emotes.update({x:"custom role"})
            if roles_available != "":
                em = True
                embed.add_field(name = "Roles", value = roles_available)
            if keys != "":
                em = True
                embed.add_field(name = "Keys", value = keys)
            if passes != "":
                em = True
                embed.add_field(name = "Passes", value = passes)
            if custom != "":
                em = True
                embed.add_field(name = "Custom", value = custom)
            if em != True:
                await self.bot.say("Nothing new in the shop yet, chief.")
            else:
                newmessage = await self.bot.send_message(ctx.message.channel, embed = embed)
                cancelled = False
                while cancelled == False:
                    # checker = await self.bot.wait_for_message(author = ctx.message.author, channel = ctx.message.channel, timeout = 60)
                    # if checker == None:
                    #     await self.bot.say("Hurry up and make your mind -.-")
                    #     cancelled = True
                    # else:
                    #     if checker.content == "cancel":
                    #         await self.bot.say(":ok_hand:")
                    #         cancelled = True
                    #     elif checker.content.lower() in buyables:
                            # cost = buyables[checker.content.lower()]
                            # cursor.execute("""SELECT nuggies FROM nuggies WHERE playerid = '%s'"""% ctx.message.author.id)
                            # balance = cursor.fetchone()
                            # balance = balance[0]
                            # if balance >= cost:
                            #     balance = balance - cost
                    #             #UPDATE
                    #         else:
                    #             await self.bot.say("I'm sorry, but you can't buy that, chief.")
                    #     else:
                    #         await self.bot.say("That's not in the store, chief, did you use the exact name :/")
                    for x in reactioned:
                        await self.bot.add_reaction(newmessage, x)
                        await asyncio.sleep(0.4)
                    checker = await self.bot.wait_for_reaction(user = ctx.message.author, message = newmessage, timeout = 60)
                    try:
                        if checker.reaction.emoji == None:
                            reaction = discord.utils.get(ctx.message.server.emojis, id = "389266641348853760")
                            embed = discord.Embed(title="Time's up!")
                            await self.bot.say(f"Time's up! Come again soon when you've thought about your purchase! {reaction}")
                            cancelled = True
                            break
                        try:
                            print(checker.reaction.emoji)
                        except:
                            pass
                        # await self.bot.say(str(checker.reaction.emoji in reactioned))
                        if checker.reaction.emoji in reactioned:
                            reacted = reactioncheck(checker.reaction.emoji)
                            item = emotes[reacted]
                            cost = buyables[item]
                            cursor.execute("""SELECT nuggies FROM nuggies WHERE playerid = '%s'"""% ctx.message.author.id)
                            balance = cursor.fetchone()
                            balance = balance[0]
                            if balance >= cost:
                                balance = balance - cost
                                await chck(self, ctx.message.server, item, ctx.message.author)
                                # ser nam mem
                                cursor.execute("""UPDATE nuggies SET nuggies = %s WHERE playerid = %s""", (balance, ctx.message.author.id))
                                db.commit()
                                await self.bot.say(f"You have successfully bought: `{item}`!")
                            else:
                                t = await self.bot.say("I'm sorry, but you can't buy that, chief.")
                                await asyncio.sleep(3)
                                await self.bot.delete_message(t)
                        else:
                            t = await self.bot.say("That's not in the store, chief, did you use the exact name :/")
                            await asyncio.sleep(3)
                            await self.bot.delete_message(t)
                    except:
                        pass
        db.commit()
        db.close()
def setup(bot):
    bot.add_cog(NuggiesCommands(bot))
