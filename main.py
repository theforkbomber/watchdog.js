
import asyncio
import importlib
import inspect
import os
import re
import sys
import time
import traceback
from datetime import datetime, timedelta
import sqlite3
from os import listdir
from os.path import isfile, join
import random

import discord
import psutil
import psycopg2
from discord.ext import commands
from discord.ext.commands.context import Context
from discord.ext.commands.core import Command, GroupMixin, command
from discord.ext.commands.errors import CommandError, CommandNotFound
from discord.ext.commands.view import StringView
from googletrans import Translator
from PyDictionary import PyDictionary

import config
from opus_loader import load_opus_lib

load_opus_lib()
then = datetime.now()
bot = commands.Bot(command_prefix=">os.")
cogs_dir = "cogs"
# bot.remove_command("help")
uk = discord.Reaction(emoji="\U0001f1ec\U0001f1e7")
us = discord.Reaction(emoji="\U0001f1fa\U0001f1f8")
jp = discord.Reaction(emoji="\U0001f1ef\U0001f1f5")
ind = discord.Reaction(emoji="\U0001f1ee\U0001f1f3")
es = discord.Reaction(emoji="\U0001f1ea\U0001f1f8")
de = discord.Reaction(emoji="\U0001f1ea\U0001f1f8")
fr = discord.Reaction(emoji="\U0001f1eb\U0001f1f7")
pt = discord.Reaction(emoji="\U0001f1f5\U0001f1f9")
cn = discord.Reaction(emoji="\U0001f1e8\U0001f1f3")
pole = discord.Reaction(emoji="\U0001f1f5\U0001f1f1")

initial_extensions = (
    'cogs.moderation',
    'cogs.serverinfo',
    'cogs.admin',
    'cogs.roles',
    'cogs.fun',
    'cogs.music',
)


def translate(payload, lang):
    translating = Translator()
    translated = translating.translate(payload, dest=lang)
    translatedtext = translated.text
    return translatedtext



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
        server = bot.get_server('427450243253272598')
        me = discord.utils.get(server.members, id = '275312272975462411')
        mystatus = me.status
        if me.status != discord.Status.offline:
            pass
        else:
            mystatus = discord.Status.dnd
        activity = discord.Game(name="CPU: "+str(psutil.cpu_percent())+"%\nRAM: "+str(m.percent)+"%\nUptime: "+str(uptime))
        # await bot.change_presence(status=discord.Status.dnd, game=discord.Game(name="Under maintenance..."))
        await bot.change_presence(status=mystatus, game=activity)
        await asyncio.sleep(15)
        await bot.change_presence(status=mystatus, game=discord.Game(name = "over JMAF", type = 3))
        await asyncio.sleep(15)
        await bot.change_presence(status=mystatus, game=discord.Game(name = "#suggestions", type = 2))
        await asyncio.sleep(15)

@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.CommandOnCooldown):
        my_time = (datetime(1970,1,1) + timedelta(seconds=int(error.retry_after))).time() 
        await bot.send_message(ctx.message.channel, content=str(my_time)+' left on the cooldown.')
    raise error  # re-raise the error so all the errors will still show up in console

@bot.event
async def on_message_edit(before, after):
    db = psycopg2.connect(host=config.host,database=config.database, user=config.user, password=config.password)
    cursor = db.cursor()
    # cursor.execute('''DROP TABLE edited''')
    # db.commit()
    # cursor.execute('''CREATE TABLE edited(id SERIAL PRIMARY KEY, channel TEXT, messagebefore TEXT, messageafter TEXT, timestamp TIME, author TEXT)''')
    # db.commit()
    aftermsg = after.content
    beforemsg = before.content
    ts = str(after.timestamp)
    ch = str(after.channel.id)
    author = after.author.id
    server = after.server
    mem = server.get_member(author)
    if mem.bot == True:
        db.close()
        return
    else:
        cursor.execute('''DELETE FROM edited WHERE channel ='%s';'''% str(ch),)
        cursor.execute('''INSERT INTO edited(channel, messagebefore, messageafter, timestamp, author)VALUES(%s,%s,%s,%s,%s) RETURNING id;''', (ch, beforemsg, aftermsg, ts, author))
        db.commit()
        db.close()
    db.close()

@bot.event
async def on_message_delete(message):
    db = psycopg2.connect(host=config.host,database=config.database, user=config.user, password=config.password)
    cursor = db.cursor()
    if message.edited_timestamp != None:
        db.close()
        pass
    # cursor.execute('''DROP TABLE deleted''')
    # db.commit()
    # cursor.execute('''CREATE TABLE deleted(id SERIAL PRIMARY KEY, channel TEXT, message TEXT, timestamp TIME, author TEXT)''')
    # db.commit()
    else:
        msg = message.content
        ts = message.timestamp
        ch = str(message.channel.id)
        author = message.author.id
        cursor.execute('''DELETE FROM deleted WHERE channel ='%s';'''% str(ch),)
        cursor.execute('''INSERT INTO deleted(channel, message, timestamp, author)VALUES(%s,%s,%s,%s) RETURNING id;''', (ch, msg, ts, author))
        db.commit()
        db.close()
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
    server = member.server
    dokis = ["Monika", "Misao", "Sayori", "Natsuki", "Protagonist", "Yuri"]
    Doki = False
    wb = []
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
    if nickcheck != None:
        await bot.change_nickname(member, "Not"+nickcheck)
    db = psycopg2.connect(host=config.host,database=config.database, user=config.user, password=config.password)
    cursor = db.cursor()
    try:
        username = str(member.id)
        cursor.execute("SELECT * FROM detention WHERE username= %s", (username,))
        results = cursor.fetchone()
        print(results)
        if results[1] == "TRUE":
            for role in server.roles:
                if role.name == "Detention":
                    det = role
                    Doki = True
                    break
            await bot.add_roles(member, det)

        elif results[1] == "FALSE":
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
    else:
        pass

@bot.event
async def on_member_update(before, after):
    server = after.server
    roles = ""
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
        nickcheck = nicknamecheck(name)
        if nickcheck != None:
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

    if message.author.bot == True:
        return
    
    if message.channel.is_private == True:
        return

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
        d = message.content.replace(">os.silly sausage", ">os.detent")
        print(d)
        message.content = d
    if message.content.startswith(">os."):
        await bot.process_commands(message)
    # try:
    
    # else:
    #     waitforreact = await bot.wait_for_reaction(message=message, timeout=500)
    #     if waitforreact != None:
    #         if waitforreact.reaction == uk or waitforreact.reaction == us:
    #             lang = "en"
    #             payload = message.content
    #             await bot.send_typing(message.channel)
    #             em = discord.Embed(description=translate(payload, lang), colour=0x53bceb)
    #             await bot.send_message(message.channel, embed=em)

    #         elif waitforreact.reaction == cn:
    #             lang = "zh-tw"
    #             payload = message.content
    #             await bot.send_typing(message.channel)
    #             em = discord.Embed(description=translate(payload, lang), colour=0x53bceb)
    #             await bot.send_message(message.channel, embed=em)

    #         elif waitforreact.reaction == fr:
    #             lang = "fr"
    #             payload = message.content
    #             await bot.send_typing(message.channel)
    #             em = discord.Embed(description=translate(payload, lang), colour=0x53bceb)
    #             await bot.send_message(message.channel, embed=em)

    #         elif waitforreact.reaction == es:
    #             lang = "es"
    #             payload = message.content
    #             await bot.send_typing(message.channel)
    #             em = discord.Embed(description=translate(payload, lang), colour=0x53bceb)
    #             await bot.send_message(message.channel, embed=em)

    #         elif waitforreact.reaction == pt:
    #             lang = "pt"
    #             payload = message.content
    #             await bot.send_typing(message.channel)
    #             em = discord.Embed(description=translate(payload, lang), colour=0x53bceb)
    #             await bot.send_message(message.channel, embed=em)

    #         elif waitforreact.reaction == jp:
    #             lang = "ja"
    #             payload = message.content
    #             await bot.send_typing(message.channel)
    #             em = discord.Embed(description=translate(payload, lang), colour=0x53bceb)
    #             await bot.send_message(message.channel, embed=em)

    #         elif waitforreact.reaction == de:
    #             lang = "de"
    #             payload = message.content
    #             await bot.send_typing(message.channel)
    #             em = discord.Embed(description=translate(payload, lang), colour=0x53bceb)
    #             await bot.send_message(message.channel, embed=em)

    #         elif waitforreact.reaction == ind:
    #             lang = "in"
    #             payload = message.content
    #             await bot.send_typing(message.channel)
    #             em = discord.Embed(description=translate(payload, lang), colour=0x53bceb)
    #             await bot.send_message(message.channel, embed=em)

    #         elif waitforreact.reaction == pole:
    #             lang = "pl"
    #             payload = message.content
    #             await bot.send_typing(message.channel)
    #             em = discord.Embed(description=translate(payload, lang), colour=0x53bceb)
    #             await bot.send_message(message.channel, embed=em)

    if message.content.startswith(">os.") == False:
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
                            for role in message.server.roles:
                                if role.name == "Detention":
                                    det = role
                                    await bot.add_roles(message.author, det)
                            for role in message.author.roles:
                                if role.name == "Detention":
                                    continue
                                else:
                                    roler.append(role)
                            print(roler)
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




for extension in initial_extensions:
    bot.load_extension(extension)

bot.run(config.token)