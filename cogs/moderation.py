import asyncio
import discord
import re
from discord.ext import commands
import config
import psycopg2

class Moderation:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, brief="'remove @someone --tmp' kicks, 'remove @someone --pm' bans")
    @commands.has_permissions(manage_roles=True)
    async def remove(self, ctx, member, typer=None, *, reason=None):
        if typer == "--pm":
            go = True
            nums = ["1","2","3","4","5","6","7"]
            await self.bot.say("How many days worth of messages do you want to purge? (1-7)")
            while go == True:
                checker = await self.bot.wait_for_message(author = ctx.message.author, channel = ctx.message.channel)
                if checker.content in nums:
                    go = False
                    numchosen = int(checker.content)
                else:
                    go = True
                    await self.bot.say("That was an invalid value, try again...")
            if reason == None:
                for user in ctx.message.mentions:
                    em = discord.Embed(description='No reason given.', colour=0xf44242)
                    em.set_author(name="You have been removed from directory `"+ctx.message.server.name+"` by "+ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
                    await self.bot.send_message(user, embed=em)
                    
                    await self.bot.ban(user, delete_message_days=numchosen)
                    await self.bot.say("*"+user.name+".chr deleted successfully.*")
            else:
                for user in ctx.message.mentions:
                    em = discord.Embed(description='Reason: '+str(reason), colour=0xf44242)
                    em.set_author(name="You have been removed from directory `"+ctx.message.server.name+"` by "+ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
                    await self.bot.send_message(user, embed=em)
                    await self.bot.ban(user, delete_message_days=7)
                    await self.bot.say("*"+user.name+".chr deleted successfully.*")
        elif typer == "--tmp":
            if reason == None:
                for user in ctx.message.mentions:
                    em = discord.Embed(description='No reason given.', colour=0xf44242)
                    em.set_author(name="You have been removed from directory `"+ctx.message.server.name+"` by "+ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
                    await self.bot.send_message(user, embed=em)
                    await self.bot.kick(user)
                    await self.bot.say("*"+user.name+".chr deleted successfully.*")
            else:
                for user in ctx.message.mentions:
                    em = discord.Embed(description='Reason: '+str(reason), colour=0xf44242)
                    em.set_author(name="You have been removed from directory `"+ctx.message.server.name+"` by "+ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
                    await self.bot.send_message(user, embed=em)
                    await self.bot.kick(user)
                    await self.bot.say("*"+user.name+".chr deleted successfully.*")

    @commands.command(pass_context=True, brief="Remove channels", aliases=["rmchan", "removechannel"])
    @commands.has_permissions(manage_roles=True)
    async def rmchannel(self, ctx, channel):
        for x in ctx.message.raw_channel_mentions:
            channel = ctx.message.server.get_channel(x)
            await self.bot.delete_channel(channel)

    @commands.command(pass_context=True, brief="Edits channels.")
    @commands.has_permissions(manage_roles=True)
    async def editchannels(self, ctx, channel, *, name):
        for channels in ctx.message.raw_channel_mentions:
            channels = self.bot.get_channel(channels)
            await self.bot.edit_channel(name=name, channel=channels)

    @commands.command(pass_context="True")
    @commands.has_permissions(manage_roles=True)
    async def addchannel(self, ctx, typer=None, *, name=None):
        server = ctx.message.server  
        if typer == "V":
            await self.bot.create_channel(server, name, type=discord.ChannelType.voice)
        else:
            await self.bot.create_channel(server, typer)

    @commands.command(pass_context=True, aliases = ["detent", "detention"])
    @commands.has_permissions(manage_roles=True)
    async def detain(self, ctx):
        server = ctx.message.server
        roler = []
        detented = False
        for user in ctx.message.mentions:
            member = server.get_member(user.id)
            print("DT")
            undetent = []
            db = psycopg2.connect(host=config.host,database=config.database, user=config.user, password=config.password)
            cursor = db.cursor()
            try:
                username = str(member.id)
                cursor.execute("SELECT * FROM detention WHERE username= %s", (username,))
                results = cursor.fetchall()
                print(results)
                if results[0][1] == "FALSE":
                    print("help")
                    for role in server.roles:
                        if role.name == "Detention":
                            det = role
                            await self.bot.add_roles(member, det)
                            print("hm?")
                            break
                    for role in member.roles:
                        if role.name == "Detention":
                            continue
                        else:
                            roler.append(role)
                    await self.bot.remove_roles(member, *roler)

                elif results[0][1] == "TRUE":
                    cursor.execute("SELECT * FROM roles WHERE username= %s", (username,))
                    c = cursor.fetchall()
                    print(c)
                    rolled = c[0][2]
                    print(rolled)
                    rolled = rolled.split("|")
                    for x in rolled:
                        try:
                            for role in server.roles:
                                if role.name == str(x):
                                    if role.name == "@everyone" or role.name == "Detention":
                                        continue
                                    else:
                                        undetent.append(role)
            
                        except Exception as e:
                            print(e)
                    await self.bot.add_roles(member, *undetent)
                    for role in server.roles:
                        if role.name == "Detention":
                            dete = role
                            break
                    await self.bot.remove_roles(member, dete)
            except Exception as e:
                print(e)
            
            db.close()
        await self.bot.add_reaction(emoji="\u2705", message=ctx.message)

                # db = psycopg2.connect(host=config.host,database=config.database, user=config.user, password=config.password)
                # cursor = db.cursor()
                # cursor.execute("SELECT * FROM detention WHERE username= %s", str(member.id),)
                # c = cursor.fetchall()
                # print(c)
                # roles = c[2]
                # db.close()
                # for x in range (0,len(roles)-1):
                #     for role in server.roles:
                #         if role.name == roles[x]:
                #             teckk = role
                #     await self.bot.add_roles(member, teckk)
                # await self.bot.remove_roles(user, det)

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, user, minutes):
        for user in ctx.message.mentions:
            for c in ctx.message.server.channels:
                overwrite = discord.PermissionOverwrite()
                overwrite.send_messages = False
                await self.bot.edit_channel_permissions(c, user, overwrite)
                print("Before:",user.permissions_in(c).send_messages)
            try:
                time = int(minutes) * 60
            except:
                await self.bot.say("""Invalid parameter [MINUTES]""")
                break
            def check(msg):
                return (msg.author.permissions_in(c).manage_roles == True) and (msg.server == ctx.message.server)
            await self.bot.wait_for_message(content = "unmute <@"+user.id+">", check = check, timeout = time)
            overwrite = discord.PermissionOverwrite()
            overwrite.send_messages = True
            await self.bot.edit_channel_permissions(c, user, overwrite)
            print("After:",user.permissions_in(c).send_messages)

    @commands.command(aliases = ["clearbots"],pass_context=True)
    @commands.has_permissions(manage_roles=True)
    async def cleanbots(self, ctx, num=None):
        channel = ctx.message.channel
        if num == None:
            try:
                def check(message):
                    return message.author.bot == True
                await self.bot.purge_from(channel, limit=20, check = check)
                mess = await self.bot.send_message(ctx.message.channel,"Done!")
                
            except Exception as e:
                getid = ctx.message.server.get_member("506885595470102549")
                if getid.server_permissions.manage_server == False:
                    em = discord.Embed(description="Requirements not met:\n-Manage server\nDETAILS:\n"+e, colour=0xf44242)
                    em.set_author(name="Failed to purge bot messages.", icon_url=ctx.message.author.avatar_url)
                    my_message = await self.bot.send_message(ctx.message.channel, embed=em)  
                else:
                    em = discord.Embed(description="Caught an error!\nDETAILS:\n"+e, colour=0xf44242)
                    em.set_author(name="Failed to purge bot messages.", icon_url=ctx.message.author.avatar_url)
                    my_message = await self.bot.send_message(ctx.message.channel, embed=em) 
        else:
            try:
                todelet = int(num)
                def check(message):
                    return message.author.bot == True
                await self.bot.purge_from(channel, limit=todelet, check = check)
                mess = await self.bot.send_message(ctx.message.channel,"Done!")
                
            except Exception as e:
                e = str(e)
                getid = ctx.message.server.get_member("506885595470102549")
                if getid.server_permissions.manage_server == False:
                    em = discord.Embed(description="Requirements not met:\n-Manage server\nDETAILS:\n"+e, colour=0xf44242)
                    em.set_author(name="Failed to purge bot messages.", icon_url=ctx.message.author.avatar_url)
                    my_message = await self.bot.send_message(ctx.message.channel, embed=em)  
                else:
                    em = discord.Embed(description="Caught an error!\nDETAILS:\n"+e, colour=0xf44242)
                    em.set_author(name="Failed to purge bot messages.", icon_url=ctx.message.author.avatar_url)
                    my_message = await self.bot.send_message(ctx.message.channel, embed=em)

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_roles=True)
    async def userpurge(self, ctx, user, num=None):
        channel = ctx.message.channel
        for x in ctx.message.mentions:          
            if num == None:
                try:
                    def check(message):
                        return message.author == x
                    await self.bot.purge_from(channel, limit=20, check = check)
                    mess = await self.bot.send_message(ctx.message.channel,"Done!")
                    
                except Exception as e:
                    getid = ctx.message.server.get_member("506885595470102549")
                    if getid.server_permissions.manage_server == False:
                        em = discord.Embed(description="Requirements not met:\n-Manage server\nDETAILS:\n"+e, colour=0xf44242)
                        em.set_author(name="Failed to purge bot messages.", icon_url=ctx.message.author.avatar_url)
                        my_message = await self.bot.send_message(ctx.message.channel, embed=em)  
                    else:
                        em = discord.Embed(description="Caught an error!\nDETAILS:\n"+e, colour=0xf44242)
                        em.set_author(name="Failed to purge bot messages.", icon_url=ctx.message.author.avatar_url)
                        my_message = await self.bot.send_message(ctx.message.channel, embed=em) 
            else:
                try:
                    todelet = int(num)
                    def check(message):
                        return message.author == x
                    await self.bot.purge_from(channel, limit=todelet, check = check)
                    mess = await self.bot.send_message(ctx.message.channel,"Done!")
                    
                except Exception as e:
                    e = str(e)
                    getid = ctx.message.server.get_member("506885595470102549")
                    if getid.server_permissions.manage_server == False:
                        em = discord.Embed(description="Requirements not met:\n-Manage server\nDETAILS:\n"+e, colour=0xf44242)
                        em.set_author(name="Failed to purge bot messages.", icon_url=ctx.message.author.avatar_url)
                        my_message = await self.bot.send_message(ctx.message.channel, embed=em)  
                    else:
                        em = discord.Embed(description="Caught an error!\nDETAILS:\n"+e, colour=0xf44242)
                        em.set_author(name="Failed to purge bot messages.", icon_url=ctx.message.author.avatar_url)
                        my_message = await self.bot.send_message(ctx.message.channel, embed=em)

    @commands.command(aliases = ["exterminatus","clean","clear"], pass_context=True)
    @commands.has_permissions(manage_roles=True)
    async def purge(self, ctx, num=None):
        channel = ctx.message.channel
        if num == None:
            try:
                await self.bot.purge_from(channel, limit=20)
                if ctx.message.content.startswith(">os.exterminatus"):
                    mess = await self.bot.send_file(ctx.message.channel,open("exterminatus.gif","rb"))
                else:
                    await self.bot.send_message(ctx.message.channel, "Done!")
                
            except Exception as e:
                getid = ctx.message.server.get_member("506885595470102549")
                if getid.server_permissions.manage_server == False:
                    em = discord.Embed(description="Requirements not met:\n-Manage server\nDETAILS:\n"+e, colour=0xf44242)
                    em.set_author(name="Failed to purge bot messages.", icon_url=ctx.message.author.avatar_url)
                    my_message = await self.bot.send_message(ctx.message.channel, embed=em)  
                else:
                    em = discord.Embed(description="Caught an error!\nDETAILS:\n"+e, colour=0xf44242)
                    em.set_author(name="Failed to purge bot messages.", icon_url=ctx.message.author.avatar_url)
                    my_message = await self.bot.send_message(ctx.message.channel, embed=em) 
        else:
            try:
                todelet = int(num)
                await self.bot.purge_from(channel, limit=20)
                if ctx.message.content.startswith(">os.exterminatus"):
                    mess = await self.bot.send_file(ctx.message.channel,open("exterminatus.gif","rb"))
                else:
                    await self.bot.send_message(ctx.message.channel, "Done!")
                
            except Exception as e:
                e = str(e)
                getid = ctx.message.server.get_member("506885595470102549")
                if getid.server_permissions.manage_server == False:
                    em = discord.Embed(description="Requirements not met:\n-Manage server\nDETAILS:\n"+e, colour=0xf44242)
                    em.set_author(name="Failed to purge bot messages.", icon_url=ctx.message.author.avatar_url)
                    my_message = await self.bot.send_message(ctx.message.channel, embed=em)  
                else:
                    em = discord.Embed(description="Caught an error!\nDETAILS:\n"+e, colour=0xf44242)
                    em.set_author(name="Failed to purge bot messages.", icon_url=ctx.message.author.avatar_url)
                    my_message = await self.bot.send_message(ctx.message.channel, embed=em) 

    @commands.command(pass_context=True, no_pm=True)
    @commands.has_permissions(manage_roles=True)
    async def remove_role(self, ctx):
        """Use this to remove roles from a number of members

        EXAMPLE: !role remove @Jim @Bot @Joe
        RESULT: A follow-along to remove the role(s) you want to, from these 3 members"""
        # No use in running through everything if the bot cannot manage roles
        if not ctx.message.server.me.permissions_in(ctx.message.channel).manage_roles:
            await self.bot.say("I can't manage roles in this server, do you not trust  me? :c")
            return

        server_roles = [role for role in ctx.message.server.roles if not role.is_everyone]
        # First get the list of all mentioned users
        members = ctx.message.mentions
        # If no users are mentioned, ask the author for a list of the members they want to remove the role from
        if len(members) == 0:
            await self.bot.say("Please provide the list of members you want to remove a role from")
            msg = await self.bot.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            if msg is None:
                await self.bot.say("You took too long. I'm impatient, don't make me wait")
                return
            if len(msg.mentions) == 0:
                await self.bot.say("I cannot remove a role from someone if you don't provide someone...")
                return
            # Override members if everything has gone alright, and then continue
            members = msg.mentions

        # This allows the user to remove multiple roles from the list of users, if they want.
        await self.bot.say("Alright, please provide the roles you would like to remove from this member. "
                           "Make sure the roles, if more than one is provided, are separate by commas. "
                           "Here is a list of this server's roles:"
                           "```\n{}```".format("\n".join([r.name for r in server_roles])))
        msg = await self.bot.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
        if msg is None:
            await self.bot.say("You took too long. I'm impatient, don't make me wait")
            return

        # Split the content based on commas, using regex so we can split if a space was not provided or if it was
        role_names = re.split(', ?', msg.content)
        roles = []
        # This loop is just to get the actual role objects based on the name
        for role in role_names:
            _role = discord.utils.get(server_roles, name=role)
            if _role is not None:
                roles.append(_role)

        # If no valid roles were given, let them know that and return
        if len(roles) == 0:
            await self.bot.say("Please provide a valid role next time!")
            return

        # Otherwise, remove the roles from each member given
        for member in members:
            await self.bot.remove_roles(member, *roles)
        await self.bot.say("I have just removed the following roles:```\n{}``` from the following members:"
                           "```\n{}```".format("\n".join(role_names), "\n".join([m.display_name for m in members])))

    @commands.command(name='addrole', pass_context=True, no_pm=True)
    @commands.has_permissions(manage_roles=True)
    async def add_role(self, ctx):
        """Use this to add a role to multiple members.
        Provide the list of members, and I'll ask for the role
        If no members are provided, I'll first ask for them

        EXAMPLE: >os.addrole @Bob @Joe @jim
        RESULT: A follow along to add the roles you want to these 3"""
        # No use in running through everything if the bot cannot manage roles
        if not ctx.message.server.me.permissions_in(ctx.message.channel).manage_roles:
            await self.bot.say("I can't manage roles in this server, do you not trust  me? :c")
            return

        # This is exactly the same as removing roles, except we call add_roles instead.
        server_roles = [role for role in ctx.mesage.server.roles if not role.is_everyone]
        members = ctx.message.mentions
        if len(members) == 0:
            await self.bot.say("Please provide the list of members you want to add a role to")
            msg = await self.bot.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            if msg is None:
                await self.bot.say("You took too long. I'm impatient, don't make me wait")
                return
            if len(msg.mentions) == 0:
                await self.bot.say("I cannot add a role to someone if you don't provide someone...")
                return
            members = msg.mentions

        await self.bot.say("Alright, please provide the roles you would like to add to this member. "
                           "Make sure the roles, if more than one is provided, are separate by commas. "
                           "Here is a list of this server's roles:"
                           "```\n{}```".format("\n".join([r.name for r in server_roles])))

        msg = await self.bot.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
        if msg is None:
            await self.bot.say("You took too long. I'm impatient, don't make me wait")
            return
        role_names = re.split(', ?', msg.content)
        roles = []
        for role in role_names:
            _role = discord.utils.get(server_roles, name=role)
            if _role is not None:
                roles.append(_role)

        if len(roles) == 0:
            await self.bot.say("Please provide a valid role next time!")
            return

        for member in members:
            await self.bot.add_roles(member, *roles)
        await self.bot.say("I have just added the following roles:```\n{}``` to the following members:"
                           "```\n{}```".format("\n".join(role_names), "\n".join([m.display_name for m in members])))

    @commands.command(name='deleterole', pass_context=True, no_pm=True)
    @commands.has_permissions(manage_roles=True)
    async def delete_role(self, ctx, *, role: discord.Role = None):
        """This command can be used to delete one of the roles from the server

        EXAMPLE: >os.deleterole StupidRole
        RESULT: No more role called StupidRole"""
        # No use in running through everything if the bot cannot manage roles
        if not ctx.message.server.me.permissions_in(ctx.message.channel).manage_roles:
            await self.bot.say("I can't delete roles in this server, do you not trust  me? :c")
            return

        # If no role was given, get the current roles on the server and ask which ones they'd like to remove
        if role is None:
            server_roles = [role for role in ctx.message.server.roles if not role.is_everyone]

            await self.bot.say(
                "Which role would you like to remove from the server? Here is a list of this server's roles:"
                "```\n{}```".format("\n".join([r.name for r in server_roles])))

            # For this method we're only going to delete one role at a time
            # This check attempts to find a role based on the content provided, if it can't find one it returns None
            # We can use that fact to simply use just that as our check
            check = lambda m: discord.utils.get(server_roles, name=m.content)
            msg = await self.bot.wait_for_message(author=ctx.message.author, channel=ctx.message.channel, check=check)
            if msg is None:
                await self.bot.say("You took too long. I'm impatient, don't make me wait")
                return
            # If we have gotten here, based on our previous check, we know that the content provided is a valid role.
            # Due to that, no need for any error checking here
            role = discord.utils.get(server_roles, name=msg.content)

        await self.bot.delete_role(ctx.message.server, role)
        await self.bot.say("I have just removed the role {} from this server".format(role.name))

    @commands.command(name='createrole', pass_context=True, no_pm=True)
    @commands.has_permissions(manage_roles=True)
    async def create_role(self, ctx):
        """This command can be used to create a new role for this server
        A prompt will follow asking what settings you would like for this new role
        I'll then ask if you'd like to set anyone to use this role

        EXAMPLE: !role create
        RESULT: A follow along in order to create a new role"""
        # No use in running through everything if the bot cannot create the role
        if not ctx.message.server.me.permissions_in(ctx.message.channel).manage_roles:
            await self.bot.say("I can't create roles in this server, do you not trust  me? :c")
            return

        # Save a couple variables that will be used repeatedly
        author = ctx.message.author
        server = ctx.message.server
        channel = ctx.message.channel

        # A couple checks that will be used in the wait_for_message's
        num_separated_check = lambda m: re.search("(\d(, ?| )?|[nN]one)", m.content) is not None
        yes_no_check = lambda m: re.search("(yes|no)", m.content.lower()) is not None
        members_check = lambda m: len(m.mentions) > 0

        # Start the checks for the role, get the name of the role first
        await self.bot.say(
            "Alright! I'm ready to create a new role, please respond with the name of the role you want to create")
        msg = await self.bot.wait_for_message(timeout=60.0, author=author, channel=channel)
        if msg is None:
            await self.bot.say("You took too long. I'm impatient, don't make me wait")
            return
        name = msg.content

        # Print a list of all the permissions available, then ask for which ones need to be active on this new role
        all_perms = [p for p in dir(discord.Permissions) if isinstance(getattr(discord.Permissions, p), property)]
        fmt = "\n".join("{}) {}".format(i, perm) for i, perm in enumerate(all_perms))
        await self.bot.say("Sounds fancy! Here is a list of all the permissions available. Please respond with just "
                           "the numbers, seperated by commas, of the permissions you want this role to have.\n"
                           "```\n{}```".format(fmt))
        # For this we're going to give a couple extra minutes before we timeout
        # as it might take a bit to figure out which permissions they want
        msg = await self.bot.wait_for_message(timeout=180.0, author=author, channel=channel, check=num_separated_check)
        if msg is None:
            await self.bot.say("You took too long. I'm impatient, don't make me wait")
            return

        # Check if any integer's were provided that are within the length of the list of permissions
        num_permissions = [int(i) for i in re.split(' ?,?', msg.content) if i.isdigit() and int(i) < len(all_perms)]

        # Check if this role should be in a separate section on the sidebard, i.e. hoisted
        await self.bot.say("Do you want this role to be in a separate section on the sidebar? (yes or no)")
        msg = await self.bot.wait_for_message(timeout=60.0, author=author, channel=channel, check=yes_no_check)
        if msg is None:
            await self.bot.say("You took too long. I'm impatient, don't make me wait")
            return
        hoist = True if msg.content.lower() == "yes" else False

        # Check if this role should be able to be mentioned
        await self.bot.say("Do you want this role to be mentionable? (yes or no)")
        msg = await self.bot.wait_for_message(timeout=60.0, author=author, channel=channel, check=yes_no_check)
        if msg is None:
            await self.bot.say("You took too long. I'm impatient, don't make me wait")
            return
        mentionable = True if msg.content.lower() == "yes" else False

        # Ready to actually create the role
        # First create a permissions object based on the numbers provided
        perms = discord.Permissions.none()
        for index in num_permissions:
            setattr(perms, all_perms[index], True)

        payload = {
            'name': name,
            'permissions': perms,
            'hoist': hoist,
            'mentionable': mentionable
        }
        # Create the role, and wait a second, sometimes it goes too quickly and we get a role with 'new role' to print
        role = await self.bot.create_role(server, **payload)
        await asyncio.sleep(1)
        await self.bot.say("We did it! You just created the new role {}\nIf you want to add this role"
                           " to some people, mention them now".format(role.name))
        msg = await self.bot.wait_for_message(timeout=60.0, author=author, channel=channel, check=members_check)
        # There's no need to mention the users, so don't send a failure message if they didn't, just return
        if msg is None:
            return

        # Otherwise members were mentioned, add the new role to them now
        for member in msg.mentions:
            await self.bot.add_roles(member, role)

        fmt = "\n".join(m.display_name for m in msg.mentions)
        await self.bot.say("I have just added the role {} to: ```\n{}```".format(name, fmt))

    
def setup(bot):
    bot.add_cog(Moderation(bot))