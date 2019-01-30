from discord.ext import commands
import discord
import psycopg2
import asyncio
import config

class NuggiesCommands:
    def __init__(self, bot):
        self.bot = bot
    jserver = bot.get_server("369252350927306752")
    reactioned = [discord.utils.get(jserver.emojis, id = "388471019914002433"), discord.utils.get(jserver.emojis, id = "388471020417318912"), discord.utils.get(jserver.emojis, id = "388471020341821450"), discord.utils.get(jserver.emojis, id = "388471020220055553"), discord.utils.get(jserver.emojis, id = "388471020220186626"), discord.utils.get(jserver.emojis, id = "388471020593479681"), discord.utils.get(jserver.emojis, id = "388471020190695426"), discord.utils.get(jserver.emojis, id = "388471020362661890"), discord.utils.get(jserver.emojis, id = "388471020581027844"), discord.utils.get(jserver.emojis, id = "388471020572377099")]

    def reactioncheck(reaction):
        if reaction == jserver[0]:
            return 1
        if reaction == jserver[1]:
            return 2
        if reaction == jserver[2]:
            return 3
        if reaction == jserver[3]:
            return 4
        if reaction == jserver[4]:
            return 5
        if reaction == jserver[5]:
            return 6
        if reaction == jserver[6]:
            return 7
        if reaction == jserver[7]:
            return 8
        if reaction == jserver[8]:
            return 9
        if reaction == jserver[9]:
            return 10
        


    def chck(server, name, member):
        if name == "doki doki":
            role = discord.utils.get(server.roles, name = "Doki Doki")
            await self.bot.add_roles(member, role)
            # if name == "protagonist":
            #     role = discord.utils.get(server.roles, name = "Protagonist")
            #     await self.bot.add_roles(member, role)
        if name == "miyuki":
            role = discord.utils.get(server.roles, name = "Miyuki")
            await self.bot.add_roles(member, role)
        if name == "$player$":
            role = discord.utils.get(server.roles, name = "$PLAYER$")
            await self.bot.add_roles(member, role)
        if name == "princess' bedroom":
            role = discord.utils.get(server.roles, name = "Princess' Bedroom")
            await self.bot.add_roles(member, role)
        if name == "n word pass":
            role = discord.utils.get(server.roles, name = "N-Word Pass")
            await self.bot.add_roles(member, role)
        if name == "custom role":
            await self.bot.send_message(self.bot.get_channel('526179783994900491'), member.name+" wants a custom role!")
        if name == "custom pic":
            c = await bot.application_info()
            owner = c.owner.id
            await self.bot.send_message(owner, member.name+" wants a custom command!")
    
    @commands.command
    async def nuggystore(self, ctx):
        db = psycopg2.connect(host=config.host,database=config.database, user=config.user, password=config.password)
        cursor = db.cursor()
        cursor.execute("""SELECT items_purchased FROM nuggies WHERE playerid = '%s'"""% ctx.message.author.id)
        found = cursor.fetchone()
        roles_available = ""
        keys = ""
        passes = ""
        custom = ""
        emotes = {}
        buyables = {}
        x = 0
        em = False
        embed = discord.Embed(title = "Store")
        embed.set_footer(text = "When purchasing, use the EXACT name provided ^.^")
        if found[0] != None:
            itemlist = found[0].split("|")
            user_roles = [r.name for r in ctx.message.author.roles]
            if not "Doki Doki" in user_roles:
                x += 1
                roles_available += str(x)+". Doki Doki :heart:\n"
                buyables.update({"doki doki", 200})
                emotes.update({x:"doki doki"})
            # if not "Protagonist" in user_roles:
            #     x += 1
            #     roles_available += str(x)+". Protagonist :chibidanjump:\n"
            #     buyables.update({"protagonist", 5000})
            #     emotes.update({x:"protagonist"})
            if not "Miyuki" in user_roles:
                x += 1
                roles_available += str(x)+""". Miyuki - "An exclusive role, this one is me!!! The colour of my eyes! :slight_smile: Once purchased, it will be unlocked in your #role-requests flags\n."""
                buyables.update({"miyuki", 10000})
                emotes.update({x:"miyuki"})
            if not "$PLAYER$" in user_roles:
                x += 1
                roles_available += str(x)+""". $PLAYER$ - "An exclusive role, this one is you!!! The faint colour emitting from the other side of your monitor. :eyes:\n"""
                buyables.update({"$player$", 5151})
                emotes.update({x:"$player$"})
            if not "Princess' Bedroom" in user_roles:
                x += 1
                keys += str(x)+""". Princess Key - "Grants access to Marissa's bedroom. Not sure why you'd want this, but if you're into that sort of thing...\n"""
                buyables.update({"princess' bedroom", 900})
                emotes.update({x:"princess' bedroom"})
            if not "N word pass" in itemlist:
                x += 1
                passes += str(x)+""". N Card - "I knew a guy who knew a guy who knew an African American, and with this, you can say it all you want! (Just don't go too overboard.)\n"""
                buyables.update({"n word pass", 200})
                emotes.update({x:"n word pass"})
            x += 1
            roles_available += str(x)+""". Custom Role - "Your very own role, fit with a separate listing above Gold Member, and a colour of your choice! :confetti_ball:\n""""
            buyables.update({"custom role", 100000})
            emotes.update({x:"custom role"})
            x += 1
            custom += str(x)+""". Custom Pictures Command - "Get your own little pictures command, like >os.rolo!\n"""""
            buyables.update({"custom pic", 100000})
            emotes.update({x:"custom pic"})
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
                await self.bot.send_message(ctx.message.channel, embed = embed)
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
                    checker = await self.bot.wait_for_reaction(user = ctx.message.author, message = ctx.message, timeout = 60)
                    if checker == None:
                        await self.bot.say("Come again soon!")
                        cancelled = True

                    if checker.reaction in reactions:
                        reacted = reactioncheck(checker.reaction)
                        item = emotes[reacted]
                        cost = buyables[item]
                        cursor.execute("""SELECT nuggies FROM nuggies WHERE playerid = '%s'"""% ctx.message.author.id)
                        balance = cursor.fetchone()
                        balance = balance[0]
                        if balance >= cost:
                            balance = balance - cost
                            chck(ctx.message.server, item, ctx.message.author)
                            # ser nam mem
                            cursor.execute("""UPDATE nuggies SET nuggies = %s WHERE playerid = %s""", (balance, ctx.message.author.id))
                            await bot.say(f"You have successfully bought: `{item}`!")
                        else:
                            t = await self.bot.say("I'm sorry, but you can't buy that, chief.")
                            await asyncio.sleep(3)
                            await self.bot.remove_message(t)
                    else:
                        t = await self.bot.say("That's not in the store, chief, did you use the exact name :/")
                        await asyncio.sleep(3)
                        await self.bot.remove_message(t)
        db.commit()
        db.close()
def setup(bot):
    bot.add_cog(NuggiesCommands(bot))