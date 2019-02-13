import asyncio
import importlib
import inspect
import os
import re
import sys
import zipfile
import time
import traceback
from datetime import datetime, timedelta
import sqlite3
from os import listdir
from os.path import isfile, join
import random
import io
import shutil
import discord
import psutil
import psycopg2
from discord.ext import commands
from discord.ext.commands.context import Context
from discord.ext.commands.core import Command, GroupMixin, command
from discord.ext.commands.errors import CommandError, CommandNotFound
from discord.ext.commands.view import StringView
from googletrans import Translator
from googletrans import LANGUAGES
from PyDictionary import PyDictionary

import config
from opus_loader import load_opus_lib

load_opus_lib()
then = datetime.now()
bot = commands.Bot(command_prefix=">os.")
cogs_dir = "cogs"
# bot.remove_command("help")
listoflangs = {
    discord.Reaction(emoji="\U0001f1ec\U0001f1e7"):"en", #uk
    discord.Reaction(emoji="\U0001f1fa\U0001f1f8"):"en", #us
    discord.Reaction(emoji="\U0001f1ef\U0001f1f5"):"ja", #japan
    discord.Reaction(emoji="\U0001f1ee\U0001f1f3"):"hi", #india
    discord.Reaction(emoji="\U0001f1ea\U0001f1f8"):"es", #spain
    discord.Reaction(emoji="\U0001f1e9\U0001f1ea"):"de", #germany
    discord.Reaction(emoji="\U0001f1eb\U0001f1f7"):"fr", #france
    discord.Reaction(emoji="\U0001f1f5\U0001f1f9"):"pt", #portugal
    discord.Reaction(emoji="\U0001f1e7\U0001f1f7"):"pt", #brazil
    discord.Reaction(emoji="\U0001f1f3\U0001f1e6"):"af", #namibia
    discord.Reaction(emoji="\U0001f1ff\U0001f1e6"):"af", #southafrica
    discord.Reaction(emoji="\U0001f1f1\U0001f1fe"):"ar", #libya
    discord.Reaction(emoji="\U0001f1f8\U0001f1e6"):"ar", #saudi
    discord.Reaction(emoji="\U0001f1ea\U0001f1ec"):"ar", #egypt
    discord.Reaction(emoji="\U0001f1e7\U0001f1ed"):"ar", #bahrain
    discord.Reaction(emoji="\U0001f1e9\U0001f1ff"):"ar", #algeria
    discord.Reaction(emoji="\U0001f1ee\U0001f1f6"):"ar", #iraq
    discord.Reaction(emoji="\U0001f1ef\U0001f1f4"):"ar", #jordan
    discord.Reaction(emoji="\U0001f1f0\U0001f1fc"):"ar", #kuwait
    discord.Reaction(emoji="\U0001f1f1\U0001f1e7"):"ar", #lebanon
    discord.Reaction(emoji="\U0001f1f2\U0001f1f7"):"ar", #mauritania
    discord.Reaction(emoji="\U0001f1f2\U0001f1e6"):"ar", #morocco
    discord.Reaction(emoji="\U0001f1f4\U0001f1f2"):"ar", #oman
    discord.Reaction(emoji="\U0001f1f5\U0001f1f8"):"ar", #palestine
    discord.Reaction(emoji="\U0001f1f6\U0001f1e6"):"ar", #qatar
    discord.Reaction(emoji="\U0001f1f8\U0001f1e9"):"ar", #sudan
    discord.Reaction(emoji="\U0001f1f8\U0001f1fe"):"ar", #syria
    discord.Reaction(emoji="\U0001f1f9\U0001f1f3"):"ar", #tunisia
    discord.Reaction(emoji="\U0001f1e6\U0001f1ea"):"ar", #uae
    discord.Reaction(emoji="\U0001f1fe\U0001f1ea"):"ar", #yemen
    discord.Reaction(emoji="\U0001f1e6\U0001f1f2"):"hy", #armenia
    discord.Reaction(emoji="\U0001f1e6\U0001f1ff"):"az", #azer.....?
    discord.Reaction(emoji="\U0001f1e7\U0001f1fe"):"be", #belarus
    discord.Reaction(emoji="\U0001f1ed\U0001f1f7"):"hr", #croatia
    discord.Reaction(emoji="\U0001f1f2\U0001f1fd"):"es", #mexico
    discord.Reaction(emoji="\U0001f1e8\U0001f1ff"):"cs", #czech republic
    discord.Reaction(emoji="\U0001f1e9\U0001f1f0"):"da", #denmark
    discord.Reaction(emoji="\U0001f1ea\U0001f1ea"):"et", #estonia
    discord.Reaction(emoji="\U0001f1f5\U0001f1ed"):"tl", #phillipines
    discord.Reaction(emoji="\U0001f1eb\U0001f1ee"):"fi", #finland
    discord.Reaction(emoji="\U0001f1f3\U0001f1f1"):"nl", #netherlands
    discord.Reaction(emoji="\U0001f1ec\U0001f1ea"):"ka", #georgia
    discord.Reaction(emoji="\U0001f1ec\U0001f1f7"):"el", #greece
    discord.Reaction(emoji="\U0001f1ed\U0001f1f9"):"ht", #haiti
    discord.Reaction(emoji="\U0001f1f3\U0001f1ec"):"ha", #nigeria
    discord.Reaction(emoji="\U0001f1f3\U0001f1ea"):"ha", #niger
    discord.Reaction(emoji="\U0001f1ec\U0001f1ed"):"ha", #ghana
    discord.Reaction(emoji="\U0001f1ee\U0001f1f1"):"iw", #israel
    discord.Reaction(emoji="\U0001f1f1\U0001f1e6"):"lo", #laos
    discord.Reaction(emoji="\U0001f1ed\U0001f1fa"):"hu", #hungarian
    discord.Reaction(emoji="\U0001f1ee\U0001f1f8"):"is", #iceland
    discord.Reaction(emoji="\U0001f1ee\U0001f1e9"):"id", #indonesia
    discord.Reaction(emoji="\U0001f1ee\U0001f1ea"):"ga", #ireland
    discord.Reaction(emoji="\U0001f1ee\U0001f1f9"):"it", #italy
    discord.Reaction(emoji="\U0001f1f0\U0001f1ff"):"kk", #kazakhstan
    discord.Reaction(emoji="\U0001f1f0\U0001f1ed"):"km", #cambodia
    discord.Reaction(emoji="\U0001f1f0\U0001f1f7"):"ko", #south korea
    discord.Reaction(emoji="\U0001f1f0\U0001f1f5"):"ko", #north korea
    discord.Reaction(emoji="\U0001f1f0\U0001f1ec"):"ky", #kyrgyzstan
    discord.Reaction(emoji="\U0001f1f1\U0001f1fb"):"lv", #latvia
    discord.Reaction(emoji="\U0001f1f1\U0001f1f9"):"lt", #lithuania
    discord.Reaction(emoji="\U0001f1f1\U0001f1fa"):"lb", #luxembourg
    discord.Reaction(emoji="\U0001f1f2\U0001f1f0"):"mk", #macedonia
    discord.Reaction(emoji="\U0001f1f2\U0001f1ec"):"mg", #madagascar
    discord.Reaction(emoji="\U0001f1f8\U0001f1ec"):"ms", #singapore
    discord.Reaction(emoji="\U0001f1e7\U0001f1f3"):"ms", #brunei
    discord.Reaction(emoji="\U0001f1f2\U0001f1fe"):"ms", #malaysia
    discord.Reaction(emoji="\U0001f1f2\U0001f1f9"):"mt", #malta
    discord.Reaction(emoji="\U0001f1f3\U0001f1ff"):"mi", #new zealand
    discord.Reaction(emoji="\U0001f1f2\U0001f1f3"):"mn", #mongolia
    discord.Reaction(emoji="\U0001f1f2\U0001f1f2"):"my", #myanmar/burma
    discord.Reaction(emoji="\U0001f1f3\U0001f1f5"):"ne", #nepali
    discord.Reaction(emoji="\U0001f1f3\U0001f1f4"):"no", #norway
    discord.Reaction(emoji="\U0001f1ee\U0001f1f7"):"fa", #iran
    discord.Reaction(emoji="\U0001f1f7\U0001f1f4"):"ro", #romania
    discord.Reaction(emoji="\U0001f1f7\U0001f1fa"):"ru", #russia
    discord.Reaction(emoji="\U0001f1fc\U0001f1f8"):"sm", #samoa
    discord.Reaction(emoji="\U0001f1f7\U0001f1f8"):"sr", #serbia
    discord.Reaction(emoji="\U0001f1ff\U0001f1fc"):"sn", #zimbabwe
    discord.Reaction(emoji="\U0001f1f8\U0001f1f0"):"sk", #slovakia
    discord.Reaction(emoji="\U0001f1f8\U0001f1ee"):"sl", #slovenia
    discord.Reaction(emoji="\U0001f1f8\U0001f1f4"):"so", #somalia
    discord.Reaction(emoji="\U0001f1f0\U0001f1ea"):"sw", #kenya
    discord.Reaction(emoji="\U0001f1f8\U0001f1ea"):"sv", #sweden
    discord.Reaction(emoji="\U0001f1f9\U0001f1ef"):"tg", #tajikistan
    discord.Reaction(emoji="\U0001f1f5\U0001f1f0"):"sd", #pakistan
    discord.Reaction(emoji="\U0001f1f9\U0001f1ed"):"th", #thailand
    discord.Reaction(emoji="\U0001f1f9\U0001f1f7"):"tr", #turkish
    discord.Reaction(emoji="\U0001f1fa\U0001f1e6"):"uk", #ukraine
    discord.Reaction(emoji="\U0001f1fa\U0001f1ff"):"uz", #uzbekistan
    discord.Reaction(emoji="\U0001f1fb\U0001f1f3"):"vi", #vietnam
    discord.Reaction(emoji="\U0001f1e8\U0001f1f3"):"zh-tw", #china
    discord.Reaction(emoji="\U0001f1f5\U0001f1f1"):"pl", #poland
}
initial_extensions = (
    'cogs.moderation',
    'cogs.serverinfo',
    'cogs.admin',
    'cogs.roles',
    'cogs.fun',
    'cogs.music',
    'cogs.nuggies'
)


def translateerrr(payload, lang):
    translating = Translator()
    translated = translating.translate(payload, dest=lang)
    translatedtext = translated.text
    return translatedtext

def statusmaker():
    server = bot.get_server('427450243253272598')
    me = discord.utils.get(server.members, id = '275312272975462411')
    mystatus = me.status
    if me.status != discord.Status.offline:
        pass
    else:
        mystatus = discord.Status.dnd
    return mystatus

@bot.event
async def on_ready():
    print('Successfully logged in.')
    print('Username -> ' + bot.user.name)
    print('ID -> ' + str(bot.user.id))
    while True:
        now = datetime.now()
        d = datetime.now()
        m = psutil.virtual_memory()
        uptime = now-then
        activity = discord.Game(name="CPU: "+str(psutil.cpu_percent())+"%\nRAM: "+str(m.percent)+"%\nUptime: "+str(uptime))
        # await bot.change_presence(status=discord.Status.dnd, game=discord.Game(name="Under maintenance..."))
        await bot.change_presence(status=statusmaker(), game=activity)
        await asyncio.sleep(15)
        await bot.change_presence(status=statusmaker(), game=discord.Game(name = "over JMAF", type = 3))
        await asyncio.sleep(15)
        await bot.change_presence(status=statusmaker(), game=discord.Game(name = "#suggestions", type = 2))
        await asyncio.sleep(15)

@bot.event
async def on_reaction_add(reaction, user):
    rvsn = bot.get_server("427450243253272598")
    thingy = discord.utils.get(rvsn.emojis, id = "539932839102119979")
    print(str(reaction.emoji))
    if reaction.emoji == thingy and (reaction.message.channel.id == "418556524785303563" or reaction.message.channel.id == "539966436290986014"):
        #print("Come on")
    
        await bot.remove_roles(bot.get_server(reaction.message.server.id).get_member(user.id), discord.utils.get(reaction.message.server.roles, name = "Audience"))
    if str(reaction.emoji) == ":susie":
        await bot.add_roles(bot.get_server(reaction.message.server.id).get_member(user.id), discord.utils.get(reaction.message.server.roles, name = "Minecraft"))
    try:
        #if reaction == thingy and (reaction.message.channel.id == "418556524785303563" or reaction.message.channel.id == "539966436290986014"):
            #await bot.remove_roles(bot.get_server(reaction.message.server.id).get_member(user.id), discord.utils.get(message.server.roles, name = "Audience"))
        if reaction == discord.Reaction(emoji="🛑") and user.id == "275312272975462411":
            await bot.delete_message(reaction.message)
        elif len(reaction.message.embeds) != 0:
            payload = reaction.message.embeds[0]['description']
        else:
            payload = reaction.message.content
        if reaction in listoflangs and reaction.message.channel.id != "418556524785303563":
            lang = listoflangs[reaction]
            #print(lang, reaction)
            await bot.send_typing(reaction.message.channel)
            em = discord.Embed(description=translateerrr(payload, lang), colour=0x53bceb)
            await bot.send_message(reaction.message.channel, embed=em)
    except:
        pass

@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.CommandOnCooldown):
        my_time = (datetime(1970,1,1) + timedelta(seconds=int(error.retry_after))).time() 
        await bot.send_message(ctx.message.channel, content=str(my_time)+' left on the cooldown.')
    raise error  # re-raise the error so all the errors will still show up in console

@bot.event
async def on_message_edit(before, after):
    if "nigger" in after.content.lower() and not "N-Word Pass" in [r.name for r in after.author.roles]:
        await bot.delete_message(after)
    prog = re.compile(r'(https?:\/\/)?(www.)?((discord).(gg|io|me|li|link)|discordapp.com\/invite|invite.(gg|io|me|li|link))\/.+[a-zA-Z0-9]')
    line = str(after.content)
    if prog.search(line) and not after.author.server_permissions.manage_roles:
        m = prog.search(line)
        print(f"MATCHED\nUser: {after.author.name}\nInvite: {after.content}")
        result = m.group(0) if m else ""
        if result:
            try:
                c = await bot.get_invite(str(result))
                if c.server.id in ["369252350927306752", "372766620977725441"]:
                    return
            except:
                print("Skirted invite detected")
        await bot.delete_message(after)
        await bot.send_message(after.author, "You aren't permitted to advertise in this server.")
        return
    try:
        if str(before.channel.type) == "private":
            return
        else:
            db = psycopg2.connect(host=config.host,database=config.database, user=config.user, password=config.password)
            cursor = db.cursor()
            # cursor.execute('''DROP TABLE edited''')
            # db.commit()
            # cursor.execute('''CREATE TABLE edited(id SERIAL PRIMARY KEY, channel TEXT, messagebefore TEXT, messageafter TEXT, timestamp TIME, author TEXT)''')
            # db.commit()
            aftermsg = after.content
            if len(after.attachments) > 0:
                try:
                    aftermsg = aftermsg+"\n"+after.attachments[0]["proxy_url"]
                except:
                    pass
            if len(after.embeds) > 0:
                try:
                    aftermsg = aftermsg+"\n"+after.embeds[0]["author"]["name"]
                except:
                    pass
                try:
                    aftermsg = aftermsg +"\n"+after.embeds[0]["description"]
                except:
                    pass
                try:
                    aftermsg = aftermsg +"\n"+after.embeds[0]["footer"]["text"]
                except:
                    pass
            beforemsg = before.content
            if len(before.attachments) > 0:
                try:
                    beforemsg = beforemsg +"\n"+before.attachments[0]["proxy_url"]
                except:
                    pass
            if len(before.embeds) > 0:
                try:
                    beforemsg = beforemsg+"\n"+before.embeds[0]["author"]["name"]
                except:
                    pass
                try:
                    beforemsg = beforemsg +"\n"+before.embeds[0]["description"]
                except:
                    pass
                try:
                    beforemsg = beforemsg +"\n"+before.embeds[0]["footer"]["text"]
                except:
                    pass
            ts = str(after.timestamp)
            ch = str(after.channel.id)
            author = after.author.id
            server = after.server
            mem = server.get_member(author)
            if mem == bot.user:
                db.close()
                return
            else:
                cursor.execute("SELECT todisplay FROM logs WHERE id = '%s'"% str(before.id))
                r = cursor.fetchone()
                r = r[0]
                todisplay = r+"\n(EDITED)"+str(ts)+" UTC"+"\n"+aftermsg
                cursor.execute('''UPDATE logs SET todisplay = %s WHERE id = %s;''', (todisplay, str(before.id)))
                if not mem.bot:
                    cursor.execute('''DELETE FROM edited WHERE channel ='%s';'''% str(ch),)
                    cursor.execute('''INSERT INTO edited(channel, messagebefore, messageafter, timestamp, author)VALUES(%s,%s,%s,%s,%s) RETURNING id;''', (ch, beforemsg, aftermsg, ts, author))
                db.commit()
                db.close()
            db.close()
    except:
        print("EDIT error lol")

@bot.event
async def on_message_delete(message):
    if ">os.logs" in message.content or ">os.flogs" in message.content:
        return
    db = psycopg2.connect(host=config.host,database=config.database, user=config.user, password=config.password)
    cursor = db.cursor()
    prog = re.compile(r'(https?://)?(www.)?(discord.(gg|io|me|li|link)|discordapp.com/invite)/.+[a-z]')
    line = str(message.content)
    if prog.search(line) and not message.author.server_permissions.manage_roles:
        return
    # cursor.execute('''DROP TABLE deleted''')
    # db.commit()
    # cursor.execute('''CREATE TABLE deleted(id SERIAL PRIMARY KEY, channel TEXT, message TEXT, timestamp TIME, author TEXT)''')
    # db.commit()
    msg = message.content
    if len(message.attachments) > 0:
        try:
            msg = message.attachments[0]["proxy_url"]
        except:
            pass
        try:
            msg = message.embeds[0]["author"]["name"]
        except:
            pass
        try:
            msg = msg +"\n"+message.embeds[0]["description"]
        except:
            pass
        try:
            msg = msg +"\n"+message.embeds[0]["footer"]["text"]
        except:
            pass
    ts = message.timestamp
    ch = str(message.channel.id)
    author = message.author.id
    mem = message.server.get_member(author)
    #print("niggerfilter: "+str((("nigger" in message.content.lower() and message.author.id == "418828859069300742") == False) ^ (mem.bot == False)))
    #print(mem.bot)
    #print("asda"+str((("nigger" in message.content.lower() and message.author.id == "418828859069300742") == False) == (mem.bot == False)))
    if message.edited_timestamp != None:
        #print("it has been edited")
        cursor.execute("SELECT todisplay FROM logs WHERE id = '%s'"% str(message.id))
        r = cursor.fetchone()
        r = r[0]
        todisplay = r+"(DELETED)"+str(ts)+" UTC"+"\n"
        cursor.execute('''UPDATE logs SET todisplay = %s WHERE id = %s;''', (todisplay, str(message.id)))
        ts = message.edited_timestamp
    elif message.edited_timestamp == None:
        #print("it hasn't been edited")
        todisplay = "(DELETED)"+str(ts)+" UTC"+"\n"+msg
        cursor.execute('''UPDATE logs SET todisplay = %s WHERE id = %s;''', (todisplay, str(message.id)))
    if not (("nigger" in message.content.lower() and message.author.id == "418828859069300742") == False) ^ (mem.bot == False):
        if mem.bot == True:
            db.commit()
            db.close()
            return
        cursor.execute('''DELETE FROM deleted WHERE channel ='%s';'''% str(ch),)
        cursor.execute('''INSERT INTO deleted(channel, message, timestamp, author)VALUES(%s,%s,%s,%s) RETURNING id;''', (ch, msg, str(ts), author))
    db.commit()
    db.close()

@bot.event
async def on_server_join(server):
    if server.id == '369252350927306752' or server.id == '427450243253272598' or server.id == '454338814865965099':
        pass
    else:
        try:
            await bot.send_message(server.default_channel, "Currently, Watchdog can't join other servers for security purposes, sorry.")
            await bot.leave_server(server)
        except:
            await bot.leave_server(server)

@bot.event
async def on_member_join(member):
    # if not ("everyone" in member.nick or "here" in member.nick):
    #     pass
    # elif "everyone" in member.nick or "here" in member.nick:
    server = member.server
    dokis = ["Monika", "Misao", "Sayori", "Natsuki", "Protagonist", "Yuri"]
    Doki = False
    wb = []
    wb.append(discord.utils.get(server.roles, name = "Audience"))
    def nicknamecheck(a):
        names = ["Monika", "Natsuki", "Yuri", "Dan", "Misao", "Sayori"]
        for x in range(0,len(names)):
            if a == names[x]:
                nick = names[x]
                return nick
    if member.nick == None:
        name = member.name
    else:
        name = member.nick
    nickcheck = nicknamecheck(name)
    if nickcheck != None and member.id != '487029456397926420':
        await bot.change_nickname(member, "Not"+nickcheck)
    db = psycopg2.connect(host=config.host,database=config.database, user=config.user, password=config.password)
    cursor = db.cursor()
    try:
        username = str(member.id)
        cursor.execute("SELECT * FROM detention WHERE username= %s", (username,))
        results = cursor.fetchone()
        #print(results)
        # await bot.add_roles(member, discord.utils.get(server.roles, name = "Audience"))
        if results[1] == "TRUE":
            for role in server.roles:
                if role.name == "Detention":
                    rolee = False
                    while rolee == False:
                        det = role
                        Doki = True
                        await bot.add_roles(member, det)
                        #print("hm?")
                        if det in member.roles:
                            rolee = True
                    break
            await bot.add_roles(member, det)

        elif results[1] == "FALSE":
            cursor.execute("SELECT * FROM roles WHERE username= %s", (username,))
            c = cursor.fetchall()
            await bot.add_roles(member, discord.utils.get(server.roles, name = "Audience"))
            #print(c)
            rolled = c[0][2]
            #print(rolled)
            rolled = rolled.split("|")
            for x in rolled:
                try:
                    for role in server.roles:
                        if role.name == str(x):
                            if role.name == "@everyone":
                                continue
                            else:
                                wb.append(role)
                    for role in wb:
                        if role.name in dokis:
                            Doki = True
                            break
                except:
                    pass
    except Exception as e:
        print(e)
    await bot.add_roles(member, *wb)
    db.close()
    if Doki == False:
        randomnum = random.randint(0,5)
        if randomnum == 0:
            for role in server.roles:
                if role.name == "Monika":
                    moni = role
            await bot.add_roles(member, moni)
            randomnume = random.randint(0,6000000)
            if randomnume == 0:
                for role in server.roles:
                    if role.name == "Monika (Rare)":
                        moni = role
                await asyncio.sleep(2)
                await bot.add_roles(member, moni)
                
        if randomnum == 1:
            for role in server.roles:
                if role.name == "Natsuki":
                    moni = role
            await bot.add_roles(member, moni)
            randomnume = random.randint(0,6000000)
            if randomnume == 0:
                for role in server.roles:
                    if role.name == "Natsuki (Rare)":
                        moni = role
                await asyncio.sleep(2)
                await bot.add_roles(member, moni)
                
        if randomnum == 2:
            for role in server.roles:
                if role.name == "Yuri":
                    moni = role
            await bot.add_roles(member, moni)
            randomnume = random.randint(0,6000000)
            if randomnume == 0:
                for role in server.roles:
                    if role.name == "Yuri (Rare)":
                        moni = role
                await asyncio.sleep(2)
                await bot.add_roles(member, moni)

        if randomnum == 3:
            for role in server.roles:
                if role.name == "Misao":
                    moni = role
            await bot.add_roles(member, moni)
            randomnume = random.randint(0,6000000)
            if randomnume == 0:
                for role in server.roles:
                    if role.name == "Misao (Rare)":
                        moni = role
                await asyncio.sleep(2)
                await bot.add_roles(member, moni)
        if randomnum == 4:
            for role in server.roles:
                if role.name == "Protagonist":
                    moni = role
            await bot.add_roles(member, moni)
            randomnume = random.randint(0,6000000)
            if randomnume == 0:
                for role in server.roles:
                    if role.name == "Protagonist (Rare)":
                        moni = role
                await asyncio.sleep(2)
                await bot.add_roles(member, moni)
        if randomnum == 5:
            for role in server.roles:
                if role.name == "Sayori":
                    moni = role
            await bot.add_roles(member, moni)
            randomnume = random.randint(0,6000000)
            if randomnume == 0:
                for role in server.roles:
                    if role.name == "Sayori (Rare)":
                        moni = role
                await asyncio.sleep(2)
                await bot.add_roles(member, moni)
        checker = random.randint(0,1000000000)
        if checker == 0:
            for role in server.roles:
                if role.name == "Dog":
                    moni = role
            await asyncio.sleep(2)
            await bot.add_roles(member, moni)
        if checker == 1:
            for role in server.roles:
                if role.name == "Cat":
                    moni = role
            await asyncio.sleep(2)
            await bot.add_roles(member, moni)
        if checker == 2:
            for role in server.roles:
                if role.name == "$PLAYER$":
                    moni = role
            await asyncio.sleep(2)
            await bot.add_roles(member, moni)
        if checker == 3:
            for role in server.roles:
                if role.name == "Piano Pass":
                    moni = role
            await asyncio.sleep(2)
            await bot.add_roles(member, moni)

    greetfirst = ["Greetings ","Hello there ","Henlo, ","Hiya and welcome to the server ","Hiya "]
    greets = ["! Please read the rules in <#448470389836742656>! Also please check out the <#396008626017271811> for better introduction to the server!","! Please read the server's rules in <#448470389836742656>! Also, please check out <#396008626017271811> for a better introduction to the server show! Most importantly, however, I hope you'll enjoy your stay here!", ". Make sure to read <#448470389836742656> if you haven’t already to get a sense of the rules here. Most importantly however, enjoy your time on the server! If you have any questions feel free to ask!","! Be sure to read <#448470389836742656> and also read <#396008626017271811> if you’re looking for more information on the show that occurs weekly here. Most importantly, enjoy your time here and if you have any questions feel free to ask!",", and welcome to the server! Make sure to read <#448470389836742656> to get a sense of the rules and read <#396008626017271811> if you’d like to know more about the show and the going ons around here. Most importantly, enjoy your time here and feel free to ask if you have any questions!","Pwease wead the sewvew's wuwes in <#448470389836742656> owo  Awso, pwease check out <#396008626017271811> fow a bettew intwoduction to the sewvew show owo  Most impowtantwy, howevew, I hope you'ww enjoy youw stay hewe owo"]
    server = member.server
    mention = "<@"+member.id+">"
    if server.id == "454338814865965099":
        channels = "454338815310430239"
    elif server.id == "369252350927306752":
        channels = "390221854830362624"
    elif server.id == "427450243253272598":
        channels = "487662594312765441"
    channel = server.get_channel(channels)
    mnum = random.randint(0,100)
    if mnum == 1:
        greetchosenfirst = "Hewwo thewe "
        greetlast = "Pwease wead the sewvew's wuwes in <#448470389836742656> owo  Awso, pwease check out <#396008626017271811> fow a bettew intwoduction to the sewvew show owo  Most impowtantwy, howevew, I hope you'ww enjoy youw stay hewe owo"
        await bot.send_message(channel, greetchosenfirst+mention+greetlast)
        return
    randomnum = random.randint(0,len(greetfirst)-1)
    greetchosenfirst = greetfirst[randomnum]
    greetlast = greets[randomnum]
    await bot.send_message(channel, greetchosenfirst+mention+greetlast)
@bot.event
async def on_member_update(before, after):
    server = after.server
    roles = ""
    if (before.id == "408077627908161556" and server.id == "427450243253272598") or server.id == "369252350927306752":
        try:
            def nicknamecheck(a):
                names = ["Monika", "Natsuki", "Yuri", "Dan", "Misao", "Sayori"]
                for x in range(0,len(names)):
                    if a == names[x]:
                        nick = names[x]
                        return nick
            if after.nick == None:
                name = after.name
            else:
                name = after.nick
                named = True
            nickcheck = nicknamecheck(name)
            if nickcheck != None and after.id != '419293764528635905':
                await bot.change_nickname(after, "Not"+nickcheck)
            for role in after.roles:
                roles = roles + str(role.name)+"|"
            if after.roles == before.roles:
                pass
            else:
                for role in server.roles:
                    if role.name == "Detention":
                        det = role
                        status = "FALSE"
                        for role in after.roles:
                            if role == det:
                                status = "TRUE"
                                username = str(after.id)
                                db = psycopg2.connect(host=config.host,database=config.database, user=config.user, password=config.password)
                                cursor = db.cursor()
                                cursor.execute('''DELETE FROM detention WHERE username ='%s';'''% str(username),)
                                cursor.execute('''INSERT INTO detention(status, username)VALUES(%s,%s) RETURNING id;''', (status, username))
                                db.commit()
                                db.close()
                                break
                                
                if status == "FALSE":
                    username = str(after.id)
                    db = psycopg2.connect(host=config.host,database=config.database, user=config.user, password=config.password)
                    cursor = db.cursor()
                    cursor.execute('''DELETE FROM detention WHERE username = '%s';'''% str(username),)
                    cursor.execute('''DELETE FROM roles WHERE username = '%s';'''% str(username),)
                    cursor.execute('''INSERT INTO detention(status, username)VALUES(%s,%s) RETURNING id;''', (status, username))
                    cursor.execute('''INSERT INTO roles(username, roles)VALUES(%s,%s) RETURNING id;''', (username, roles))
                    db.commit()
                    db.close()
        except:
            pass
                        
            


@bot.event
async def on_message(message):
    if "<@&541323335930347532>" in message.content and message.channel.id == "418556524785303563":
        rvsn = bot.get_server("427450243253272598")
        react = discord.utils.get(rvsn.emojis, id = "539932839102119979")
        await bot.add_reaction(message, react)
    #     rvsn = bot.get_server("427450243253272598")
    #     react = discord.utils.get(rvsn.emojis, id = "539932839102119979")
    #     await bot.add_reaction(message, react)
    #     cancelled = False
    #     while cancelled == False:
    #         t = await bot.wait_for_reaction(message = message, timeout = 60*60)
    #         if t == None:
    #             cancelled = True
    #         await bot.remove_roles(t.user, discord.utils.get(message.server.roles, name = "Audience"))


    db = psycopg2.connect(host=config.host,database=config.database, user=config.user, password=config.password)
    cursor = db.cursor()
    # if message.server.id != "369252350927306752":
    cursor.execute("""SELECT last_message_sent FROM nuggies WHERE playerid = '%s'"""% message.author.id)
    last_sent = cursor.fetchone()
    cursor.execute("""SELECT last_gn FROM nuggies WHERE playerid = '%s'"""% message.author.id)
    last_gn = cursor.fetchone()
    if last_sent == None:
        if message.channel.id == "384536425023930379":
            cursor.execute("""INSERT INTO nuggies(playerid, nuggies, last_message_sent, last_gn, messages)VALUES(%s, %s, %s, %s, %s) RETURNING id;""", (message.author.id, 100, message.timestamp, message.timestamp, 1))
            db.commit()
            db.close()
            return
        else:
            cursor.execute("""INSERT INTO nuggies(playerid, nuggies, last_message_sent, messages)VALUES(%s, %s, %s, %s) RETURNING id;""", (message.author.id, 100, message.timestamp, 1))
            db.commit()
            db.close()
            return

    cursor.execute("""SELECT messages FROM nuggies WHERE playerid = '%s'"""% message.author.id)
    messages = cursor.fetchone()
    if message.channel.id != "395690294659776532" and (message.channel.id != "417756656684761118" and message.channel.id != "395690294659776532"):
        try:
            cursor.execute('''UPDATE nuggies SET messages = %s WHERE playerid = %s;''', (messages[0]+1, str(message.author.id)))
        except Exception as e:
            #print(str(e))
            cursor.execute('''UPDATE nuggies SET messages = %s WHERE playerid = %s;''', (1, str(message.author.id)))
            db.commit()
            db.close()
            return
    if message.channel.id == "398333869327122432" and not "nonugs" in message.content:
        cursor.execute("""SELECT nuggies FROM nuggies WHERE playerid = '%s'"""% message.author.id)
        nuggies = cursor.fetchone()
        cursor.execute('''UPDATE nuggies SET nuggies = %s WHERE playerid = %s;''', (nuggies[0]+515, str(message.author.id)))
        print("Literature "+str(message.timestamp), message.content, message.author.name)
        db.commit()
    if (messages[0] % 100)== 0:
        cursor.execute("""SELECT nuggies FROM nuggies WHERE playerid = '%s'"""% message.author.id)
        nuggies = cursor.fetchone()
        cursor.execute('''UPDATE nuggies SET nuggies = %s WHERE playerid = %s;''', (nuggies[0]+100, str(message.author.id)))
        print("% 100 "+str(message.timestamp), message.content, message.author.name, str(messages[0]))
        db.commit()
    if last_sent != None:
        if last_sent[0] >= (datetime.now() - timedelta(days=1)):
            pass
        if last_gn[0] == None and message.channel.id == "384536425023930379":
            cursor.execute("""SELECT nuggies FROM nuggies WHERE playerid = '%s'"""% message.author.id)
            nuggies = cursor.fetchone()
            cursor.execute('''UPDATE nuggies SET last_gn = %s WHERE playerid = %s;''', (message.timestamp, str(message.author.id)))
            cursor.execute('''UPDATE nuggies SET nuggies = %s WHERE playerid = %s;''', (nuggies[0]+100, str(message.author.id)))
            print("Last goodnight one "+str(message.timestamp), message.content, message.author.name)
            db.commit()
        if last_gn[0] != None:
            if last_gn[0] < (datetime.now() - timedelta(days=1)) and message.channel.id == "384536425023930379":
                cursor.execute("""SELECT nuggies FROM nuggies WHERE playerid = '%s'"""% message.author.id)
                nuggies = cursor.fetchone()
                cursor.execute('''UPDATE nuggies SET last_gn = %s WHERE playerid = %s;''', (message.timestamp, str(message.author.id)))
                cursor.execute('''UPDATE nuggies SET nuggies = %s WHERE playerid = %s;''', (nuggies[0]+100, str(message.author.id)))
                print("Last goodnight two "+str(message.timestamp), message.content, message.author.name)
                db.commit()
        if last_sent[0] < (datetime.now() - timedelta(days=1)):
            cursor.execute("""SELECT nuggies FROM nuggies WHERE playerid = '%s'"""% message.author.id)
            nuggies = cursor.fetchone()
            cursor.execute('''UPDATE nuggies SET last_message_sent = %s WHERE playerid = %s;''', (message.timestamp, str(message.author.id)))
            cursor.execute('''UPDATE nuggies SET nuggies = %s WHERE playerid = %s;''', (nuggies[0]+100, str(message.author.id)))
            print("Dailies "+str(message.timestamp), message.content, message.author.name)
            db.commit()
    if "nigger" in message.content.lower() and not "N-Word Pass" in [r.name for r in message.author.roles]:
        await bot.delete_message(message)
    details = "Sent by "+message.author.name+" @"+str(message.timestamp)+"UTC"
    msg = message.content
    if len(message.attachments) > 0:
        try:
            msg = msg+"\n"+message.attachments[0]["proxy_url"]
        except:
            pass
    if len(message.embeds) > 0:
        try:
            msg = msg +"\n"+message.embeds[0]["author"]["name"]
        except:
            pass
        try:
            msg = msg +"\n"+message.embeds[0]["description"]
        except:
            pass
        try:
            msg = msg +"\n"+message.embeds[0]["footer"]["text"]
        except:
            pass
    cursor.execute("INSERT INTO logs (todisplay, id, details, time, channel)VALUES(%s,%s,%s,%s,%s) RETURNING id;", (str(msg), str(message.id), str(details), message.timestamp, str(message.channel.id)))
    db.commit()
    db.close()
    if message.author.bot == True:
        return
    
    if message.channel.is_private == True:
        return

    prog = re.compile(r'(https?:\/\/)?(www.)?((discord).(gg|io|me|li|link)|discordapp.com\/invite|invite.(gg|io|me|li|link))\/.+[a-zA-Z0-9]')
    line = str(message.content)
    if prog.search(line) and not message.author.server_permissions.manage_roles:
        m = prog.search(line)
        print(f"MATCHED\nUser: {message.author.name}\nInvite: {message.content}")
        result = m.group(0) if m else ""
        if result:
            try:
                c = await bot.get_invite(str(result))
                if c.server.id in ["369252350927306752", "372766620977725441"]:
                    return
            except:
                print("Skirted invite detected")
        await bot.delete_message(message)
        await bot.send_message(message.author, "You aren't permitted to advertise in this server.")
        return
    else:
        pass

    if message.content.startswith(">os.help"):
        
        payload = """This is still a work in progess, but have *you* got any suggestions or ideas? Ping me in <#466802471876952095>!"""
        em = discord.Embed(description=payload, colour=0x53bceb)
        await bot.send_message(message.channel, embed=em)



#     if message.content == ">os.help epdesign":
#         arg = """Here lies the abandoned remains of a project that had potential, no extra work has been done on this since the 6th of the 6th 2018, and there will be no more work done for it. You may mess around with the commands at your pleasure.\n```>os.epdesign

# Commands:
#   make   
#   start  
#   list   
#   remove 

# Type >os.help command for more info on a command.
# You can also type >os.help category for more info on a category.```"""
#         await bot.send_message(message.channel, arg)

#     elif message.content == ">os.help EpDesign":
#         arg = """Here lies the abandoned remains of a project that had potential, no extra work has been done on this since the 6th of the 6th 2018, and there will be no more work done for it. You may mess around with the commands at your pleasure.\n```Commands:
#   epdesign     

# Type >os.help command for more info on a command.
# You can also type >os.help category for more info on a category.```"""
#         await bot.send_message(message.channel, arg)
    if message.content.startswith(">os.silly sausage"):
        ##await bot.wait_until_ready()
        d = message.content.replace(">os.silly sausage", ">os.detent")
        #print(d)
        message.content = d
    if message.content.startswith(">os.prune"):
        #await bot.wait_until_ready()
        server = bot.get_server("369252350927306752")
        user = server.get_member("120560856701468676")
        await bot.send_message(user, str(message.channel.name))
        return
    if message.content.startswith(">os.roleme "):
        ##await bot.wait_until_ready()
        t = message.content.replace(">os.roleme ","")
        test = t.split(" ")
        if t in ["Cinnamon bun", "Cinnamon Bun", "cinnamon bun", "cinnamon Bun"]:
            message.content = ">os.roleme sayori"
            await bot.process_commands(message)
            return
        elif len(test) > 1:
            try:
                ##await bot.wait_until_ready()
                #print(message.channel)
                await bot.send_message(message.channel, "Command expected 1 argument, received "+str(len(test)))
                return
            except Exception as e:
                print(e)
        elif test[0] in ["Nat", "destined", "natsuki", "Natsuki", "nat", "tsundere", "Misao", "misao", "Dan","Protag", "yuri", "Yuri", "monika", "Monika", "moni","Moni", "sayori", "Sayori", "sayo", "Sayo"]:
            ##await bot.wait_until_ready()
            await bot.process_commands(message)
            return
        elif test[0] not in ["Nat", "natsuki", "Natsuki", "nat", "tsundere", "Misao", "misao", "yuri", "Yuri", "monika", "Monika", "moni","Moni", "sayori", "Sayori", "sayo", "Sayo"]:
            ##await bot.wait_until_ready()
            try:
                #print(message.channel)
                await bot.send_message(message.channel,"Unknown or invalid role name, try again.")
            except Exception as e:
                print(e)
            return



    if message.content.startswith(">os."):
        await bot.process_commands(message)

    # try:
    
    # # else:
    # if message.content == "HASHIRE SORI YO" and message.channel.id != "398687305482764289":
    #     await bot.wait_until_ready()
    #     await bot.send_message(message.channel, "KAZE NO YOU NI")
    
    # if message.content == "TSUKIMIHARA WO" and message.channel.id != "398687305482764289":
    #     await bot.wait_until_ready()
    #     if message.author.id == "343302587899969538":
    #         await bot.send_file(message.channel,open("HashiresoriyokazenoyounitsukimiharawoPadoruPadoru.mp4","rb"), content="***P A D O R U    P A D O R U***")
    #     else:
    #         await bot.send_file(message.channel,open("MerryChristmas.mp4","rb"), content="***P A D O R U    P A D O R U***")
    
    if message.content.startswith(">os.") == False:
        logs_channel = bot.get_channel("526179783994900491")
        if str(message.type) != "MessageType.default":
            return
        if message.author.permissions_in(message.channel).manage_roles == True or message.author.id == '275312272975462411':
            return
        else:
            db = sqlite3.connect("audits.db")
            cursor = db.cursor()
            roler = []
            server = message.server
            authormsg = str(message.author.id)
            warned = False
            if len(message.attachments) > 0:
                record = message.attachments[0]["url"]
            else:
                record = message.content
            description = ""
            desc = ""
            strikes = "0"
            getbot = server.get_member(message.author.id)
            checker = await bot.wait_for_message(author = message.author, channel = message.channel, timeout = 60)
            if checker == None:
                message = "nothing"
                cursor.execute('''DELETE FROM audit_list WHERE username = (?)''', (authormsg,))
                db.commit()
                db.close()
            elif checker.content == message.content:
                if message.channel.id == "493528500892991492" or message.channel.id == "417756656684761118" or message.channel.id == "395690294659776532":
                    db.close()
                    pass
                else:
                    if getbot.bot == False:
                        cursor.execute("SELECT * FROM audit_list WHERE username=(?)", (authormsg,))
                        results = cursor.fetchone()
                        if results == None:
                            cursor.execute('''INSERT INTO audit_list(username, warned, record, recstrike, description)VALUES(?,?,?,?,?)''', (authormsg, warned, record, strikes, description,))
                            db.commit()
                            db.close()
                        else:
                            if message.content == results[3] and 6 > int(results[4]) >= 3:
                                warned = True
                                steps = int(results[4])+1
                                steps = str(steps)
                                await bot.send_message(message.author, "Warning, you've posted the same message "+steps+" times, carry on and you will be placed in detention.")
                                strikes = str(int(results[4])+1)
                            elif message.content == results[3] and int(results[4]) == 6:
                                embed = discord.Embed(colour = 0xff0000, title = "Detention", description = f"Watchdog has detained {message.author.name}")
                                embed.set_footer(text=str(message.timestamp))
                                if message.server.id == "369252350927306752":
                                    await bot.send_message(logs_channel, embed = embed)
                
                                for role in message.server.roles:
                                    if role.name == "Detention":
                                        rolee = False
                                        while rolee == False:
                                            det = role
                                            #print("hm?")
                                            await bot.add_roles(message.author, det)
                                            if det in message.author.roles:
                                                rolee = True
                                        break
                                for role in message.author.roles:
                                    if role.name == "Detention":
                                        continue
                                    else:
                                        roler.append(role)
                                #print(roler)
                                await bot.remove_roles(message.author, *roler)
                                desc = "Spammed the same message 6 times."
                            elif message.content == results[3]:
                                strikes = str(int(results[4])+1)
                            
                            else:
                                pass
                            if results[1] == True:
                                warned = True
                            description = results[5]+desc
                            cursor.execute('''DELETE FROM audit_list WHERE username = (?)''', (authormsg,))
                            cursor.execute('''INSERT INTO audit_list(username, warned, record, recstrike, description)VALUES(?,?,?,?,?)''', (authormsg, warned, record, strikes, description,))
                            db.commit()
                            db.close()
    # except Exception as e:
    #     print(e)
    #     pass


@bot.command(pass_context=True)
async def translate(ctx):
    lol = ctx.message.author.name
    em = discord.Embed(description="Translation successful!", colour=0x53bceb)
    async for message in bot.logs_from(ctx.message.channel, limit=2, reverse=True):
        if message.id == ctx.message.id:
            continue
        translator = Translator()
        totranslate = message.content
        orig = message.content
        lang = translator.detect(totranslate)
        newlang = lang.lang
        translated = translator.translate(totranslate, dest='en')
        translatedd = translated.text
        await bot.send_typing(ctx.message.channel)
        # a.append(orig)
        # b.append(translatedd)
        # c.append(message.author)
        em.add_field(name=ctx.message.author.name+", "+LANGUAGES[newlang]+' -> english', value=orig+"\n"+translatedd, inline=True)
        await bot.send_message(ctx.message.channel, embed=em)

for extension in initial_extensions:
    bot.load_extension(extension)

# async def serverpfp():
#     print("serverpfp")
#     try:
#         await bot.wait_until_ready()
#         server = bot.get_server('369252350927306752')
#         channel = bot.get_channel("418556524785303563")
#         randomnum = random.randint(1,405)
#         if randomnum <= 10:
#             with open("ThePassword.png","rb") as f:
#                 p = f.read()
#                 f.close()
#             await bot.edit_server(server, icon=p)
#             await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: Kyo Takara (ERROR)")
#         elif 10 < randomnum <= 30:
#             with open("JMAF_Marissa.png","rb") as f:
#                 p = f.read()
#                 f.close()
#             await bot.edit_server(server, icon=p)
#             await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: Marissa")
#         elif 30 < randomnum <= 60:
#             with open("jmafseason3hype.png","rb") as f:
#                 p = f.read()
#                 f.close()
#             await bot.edit_server(server, icon=p)
#             await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: JMAF Season 3 Banner")
#         elif 60 < randomnum <= 100:
#             with open("jmafDAN.png","rb") as f:
#                 p = f.read()
#                 f.close()
#             await bot.edit_server(server, icon=p)
#             await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: Dan")
#         elif 100 < randomnum <= 150:
#             with open("jmafmonika.png","rb") as f:
#                 p = f.read()
#                 f.close()
#             await bot.edit_server(server, icon=p)
#             await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: Monika")
#         elif 150 < randomnum <= 205:
#             with open("jmafsayori2.png","rb") as f:
#                 p = f.read()
#                 f.close()
#             await bot.edit_server(server, icon=p)
#             await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: Sayori (Variant)")
#         elif 205 < randomnum <= 265:
#             with open("monikajmaf.png","rb") as f:
#                 p = f.read()
#                 f.close()
#             await bot.edit_server(server, icon=p)
#             await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: Monika (Season 4)")
#         elif 265 < randomnum <= 355:
#             randomnum2 = random.randint(1,6)
#             if randomnum2 == 1:
#                 with open("JMAF_ICON_2.png","rb") as f:
#                     p = f.read()
#                     f.close()
#                 await bot.edit_server(server, icon=p)
#                 await bot.send_message(channel)
#                 await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: Natsuki")
#             elif randomnum2 == 2:
#                 with open("JMAF_ICON_3.png","rb") as f:
#                     p = f.read()
#                     f.close()
#                 await bot.edit_server(server, icon=p)
#                 await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: Sayori")
#             elif randomnum2 == 3:
#                 with open("JMAF_ICON_4.png","rb") as f:
#                     p = f.read()
#                     f.close()
#                 await bot.edit_server(server, icon=p)
#                 await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: Yuri")
#             elif randomnum2 == 4:
#                 with open("Misao_JMAF.png","rb") as f:
#                     p = f.read()
#                     f.close()
#                 await bot.edit_server(server, icon=p)
#                 await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: Misao")
#             elif randomnum2 == 5:
#                 with open("jmafmonika2.png","rb") as f:
#                     p = f.read()
#                     f.close()
#                 await bot.edit_server(server, icon=p)
#                 await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: Monika (Season 1-2)")
#             elif randomnum2 == 6:
#                 with open("jmafyuricon3.png","rb") as f:
#                     p = f.read()
#                     f.close()
#                 await bot.edit_server(server, icon=p)
#                 await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: Yuri (Variant)")
#         await asyncio.sleep(60*60*6)
#     except Exception as e:
#         print(str(e))

# async def zipper():
#     print("zipper")
#     try:
#         await bot.wait_until_ready()
#         channel = bot.get_channel('526179743616466955')
#         server = bot.get_server('369252350927306752')
#         db = psycopg2.connect(host=config.host,database=config.database, user=config.user, password=config.password)
#         cursor = db.cursor()
#         for x in server.channels:
#             if str(x.type) == "text":
#                 try:
#                     cursor.execute("SELECT * FROM logs WHERE channel = '"+str(x.id)+"' ORDER BY time;")
#                     c = cursor.fetchall()
#                     path = "Just Monika (And Friends) #DAENATAKEOVER/"
#                     if not os.path.exists(path):
#                         os.makedirs(path)
#                     try:
#                         os.remove("Just Monika (And Friends) #DAENATAKEOVER/"+x.name+".txt")
#                     except:
#                         pass
#                     txt = open("Just Monika (And Friends) #DAENATAKEOVER/"+x.name+".txt","at")
#                     for x in c:
#                         todisplay = x[1]
#                         details = x[3]
#                         txt.write(details+"\n"+todisplay+"\n\n")
#                     txt.close()
#                 except Exception as e:
#                     print(e)
#         await bot.wait_until_ready()
#         def zipdir(path, ziph):
#             # ziph is zipfile handle
#             for root, dirs, files in os.walk(path):
#                 for file in files:
#                     ziph.write(os.path.join(root, file))
#         b = io.BytesIO()
#         zipf = zipfile.ZipFile(b, mode="w")
#         zipdir('Just Monika (And Friends) #DAENATAKEOVER/', zipf)
#         zipf.close()
#         b.seek(0)
#         await bot.send_file(channel, fp=b, filename=str(datetime.now().day)+"/"+str(datetime.now().month)+"/"+str(datetime.now().year)+"JMAFLogs.zip")
#         shutil.rmtree("Just Monika (And Friends) #DAENATAKEOVER/")
#         cursor.execute("truncate logs;")
#         db.commit()
#         db.close()
#         await asyncio.sleep(60*60*24)
#     except:
#         print("lolno")
        
# bot.loop.create_task(zipper())
# bot.loop.create_task(serverpfp())
while True:
	try:
		bot.loop.run_until_complete(bot.run(config.token))
	except BaseException:
		time.sleep(5)

