import asyncio
import discord
from discord.ext import commands
import psycopg2
from datetime import datetime
import config
from discord.ext.commands import HelpFormatter
import re
import platform
import os
import sys
_mentions_transforms = {
    '@everyone': '@\u200beveryone',
    '@here': '@\u200bhere'
}
_mention_pattern = re.compile('|'.join(_mentions_transforms.keys()))
class ServerInfo:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def botstats(self, ctx):
        def linux_distribution():
            try:
                return platform.linux_distribution()
            except:
                return "N/A"

        await self.bot.say("""```py
Python version: %s
dist: %s
linux_distribution: %s
system: %s
machine: %s
platform: %s
version: %s
```""" % (
sys.version.split('\n'),
str(platform.dist()),
linux_distribution(),
platform.system(),
platform.machine(),
platform.platform(),
platform.version(),
))

    @commands.command(pass_context=True, brief="pings mods online, if possible. Misuse this and you will get a strike.")
    async def pingmods(self, ctx, *, reason):
        if ctx.message.channel.name == "detention":
            return
        else:
            server = ctx.message.server
            member = ctx.message.author
            mod = []
            role =  discord.utils.get(server.roles, server = server, name = "Detention")
            for x in server.members:
                for y in x.roles:
                    if y.name == "Minor Literature Club!":
                        mod.append(x)
                        break
            online = []
            offline = []
            away = []
            dnd = []
            on = []
            aw = []
            off = []
            dn = []
            for x in mod:
                if x.status == discord.Status.online:
                    online.append(x.name)
                    on.append(x)
                elif x.status == discord.Status.idle:
                    away.append(x.name)
                    aw.append(x)
                elif x.status == discord.Status.offline:
                    offline.append(x.name)
                    off.append(x)
                elif x.status == discord.Status.dnd:
                    dnd.append(x.name)
                    dn.append(x)
            a = ""
            o = ""
            roler = []
            d = ""
            of = ""
            def check(react):
                return react.user in tocontact
            if len(online) is not 0:
                for i in online:
                    o = o+"<:Online:498506339203416064> "+i+"\n"
                tocontact = on
                await self.bot.say("Available mods:\n"+o)
                for x in tocontact:
                    msg = await self.bot.send_message(x,str(ctx.message.author.name)+" has pinged you because:\n`"+reason+"`\nReact with the 🚫 emote to give "+str(ctx.message.author.name)+" a detention.")
                    await self.bot.add_reaction(emoji="🚫", message=msg)
                    await self.bot.wait_for_reaction(emoji="🚫",user=x,message=msg)
                    for role in server.roles:
                        if role.name == "Detention":
                            det = role
                            await self.bot.add_roles(member, det)
                            print("hm?")
                            break
                    for role in member.roles:
                        if role.name == "Detention":
                            pass
                        else:
                            roler.append(role)
                    await self.bot.remove_roles(member, *roler)

            elif len(away) is not 0:
                for i in away:
                    a = a+"<:Away:498506339052552242> "+i+"\n"
                tocontact = aw
                await self.bot.say("Available mods:\n"+a)
                for x in tocontact:
                    msg = await self.bot.send_message(x,str(ctx.message.author.name)+" has pinged you because:\n`"+reason+"`\nReact with the 🚫 emote to give "+str(ctx.message.author.name)+" a detention.")
                    await self.bot.add_reaction(emoji="🚫", message=msg)
                    await self.bot.wait_for_reaction(emoji="🚫",user=x,message=msg)
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
                        
            elif len(dnd) is not 0:
                for i in dnd:
                    d = d+"<:DnD:498506339052421163> "+i+"\n"
                tocontact = dn
                await self.bot.say("Available mods:\n"+d)
                for x in tocontact:
                    msg = await self.bot.send_message(x,str(ctx.message.author.name)+" has pinged you because:\n`"+reason+"`\nReact with the 🚫 emote to give "+str(ctx.message.author.name)+" a detention.")
                    await self.bot.add_reaction(emoji="🚫", message=msg)
                    await self.bot.wait_for_reaction(emoji="🚫",user=x,message=msg)
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
            elif len(offline) is not 0:
                for i in offline:
                    of = of+"<:Offline:498506339287564293> "+i+"\n"
                tocontact = off
                await self.bot.say("Available mods:\n"+of)
                for x in tocontact:
                    msg = await self.bot.send_message(x,str(ctx.message.author.name)+" has pinged you because:\n`"+reason+"`\nReact with the 🚫 emote to give "+str(ctx.message.author.name)+" a detention.")
                    await self.bot.add_reaction(emoji="🚫", message=msg)
                    await self.bot.wait_for_reaction(emoji="🚫",user=x,message=msg)
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

    @commands.command(pass_context=True, brief="displays info about the server")
    async def info(self, ctx):
        online = 0
        for i in ctx.message.server.members:
            if str(i.status) == 'online' or str(i.status) == 'idle' or str(i.status) == 'dnd':
                online += 1
        all_users = []
        for user in ctx.message.server.members:
            all_users.append('{}#{}'.format(user.name, user.discriminator))
        all_users.sort()
        all = '\n'.join(all_users)
        textchans = [x for x in ctx.message.server.channels if x.type == discord.ChannelType.text]
        voicechans = [x for x in ctx.message.server.channels if x.type == discord.ChannelType.voice]
        channel_count = len(textchans)
        voices = len(voicechans)
        role_count = len(ctx.message.server.roles)
        emoji_count = len(ctx.message.server.emojis)
        em = discord.Embed(color=0xea7938)
        em.add_field(name='Name', value=ctx.message.server.name)
        em.add_field(name='Owner', value=ctx.message.server.owner, inline=False)
        em.add_field(name='Members', value=ctx.message.server.member_count)
        em.add_field(name='Currently Online', value=online)
        em.add_field(name='Text Channels', value=str(channel_count))
        em.add_field(name='Voice Channels', value=str(voices))
        em.add_field(name='Region', value=ctx.message.server.region)
        em.add_field(name='Verification Level', value=str(ctx.message.server.verification_level))
        em.add_field(name='Highest role', value=ctx.message.server.role_hierarchy[0])
        em.add_field(name='Number of roles', value=str(role_count))
        em.add_field(name='Number of emotes', value=str(emoji_count), inline=True)
        em.add_field(name='Created At', value=ctx.message.server.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
        em.set_thumbnail(url=ctx.message.server.icon_url)
        em.set_author(name='Server Info', icon_url='https://i.imgur.com/RHagTDg.png')
        em.set_footer(text='Server ID: %s' % ctx.message.server.id)
        await self.bot.say(embed=em)

    @commands.command(pass_context=True, brief="Returns caught message.")
    async def snipe(self, ctx):
        db = psycopg2.connect(host=config.host,database=config.database, user=config.user, password=config.password)
        server = ctx.message.server
        cursor = db.cursor()
        cursortwo = db.cursor()
        cursor.execute('''SELECT * FROM deleted''')
        cursortwo.execute('''SELECT * FROM edited''')
        chan = cursor.fetchall()
        chane = cursortwo.fetchall()
        notFound = True
        for x in range(0,len(chan)):
            if chan[x][1] == ctx.message.channel.id:
                notFound = False
                meme = x
                msgde = chan[meme][2]

        for x in range(0,len(chane)):
            if chane[x][1] == ctx.message.channel.id:
                memes = x
                msge = chane[memes][2]
                aftermsg = chane[memes][3]
                notFound = False
        if notFound == True:
            em = discord.Embed(description="There are no sniped messages in this channel")
            em.set_author(name="Whoops!")
            await self.bot.send_message(ctx.message.channel, embed=em)
            return
        elif notFound == False:
            try:
                deletetime = chan[meme][3]
                deleted = True
            except:
                deleted = None
                pass
            try:
                edittime = chane[memes][4]
                edited = True
            except:
                edited = None
                pass
            # deletetime = datetime.strptime(deletetime, '%Y-%m-%d %H:%M:%S.%f')
            # edittime = datetime.strptime(edittime, '%Y-%m-%d %H:%M:%S.%f')
            if edited != None and deleted != None:
                if edittime < deletetime:
                    author = chan[meme][4]
                    membername = server.get_member(author)
                    em = discord.Embed(description=msgde)
                    em.set_author(name=membername.name+" said...")
                    em.set_footer(text=str(deletetime))
                    await self.bot.send_message(ctx.message.channel, embed=em)
                elif edittime > deletetime:
                    author = chane[memes][5]
                    membername = server.get_member(author)
                    if membername.bot == True:
                        return
                    else:
                        em = discord.Embed(description="Before: "+msge+"\nAfter: "+aftermsg)
                        em.set_author(name=membername.name+" said...")
                        em.set_footer(text=str(edittime))
                        await self.bot.send_message(ctx.message.channel, embed=em)
            elif edited == None:
                author = chan[meme][4]
                membername = server.get_member(author)
                em = discord.Embed(description=msgde)
                em.set_author(name=membername.name+" said...")
                em.set_footer(text=str(deletetime))
                await self.bot.send_message(ctx.message.channel, embed=em)
            elif deleted == None:
                author = chane[memes][5]
                membername = server.get_member(author)
                if membername.bot == True:
                    return
                else:
                    em = discord.Embed(description="Before: "+msge+"\nAfter: "+aftermsg)
                    em.set_author(name=membername.name+" said...")
                    em.set_footer(text=str(edittime))
                    await self.bot.send_message(ctx.message.channel, embed=em)
        db.close()
    
    @commands.command(no_pm=True, pass_context=True)
    @commands.has_permissions(send_messages=True)
    async def roles(self, ctx):
        """This command can be used to modify the roles on the server.
        Pass no subcommands and this will print the roles currently available on this server

        EXAMPLE: !role
        RESULT: A list of all your roles"""
        # Simply get a list of all roles in this server and send them
        server_roles = []
        for x in ctx.message.server.role_hierarchy:
            server_roles.append(x.name)
        await self.bot.say("Your server's roles are: ```\n{}```".format("\n".join(server_roles)))


def setup(bot):
    bot.add_cog(ServerInfo(bot))