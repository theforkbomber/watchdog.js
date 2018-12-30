import discord
import asyncio
import random
from discord.ext import commands
import time
import os
import psycopg2
import zipfile
import config
from os import listdir
from os.path import isfile, join
import io
import shutil
from datetime import datetime
bot = commands.Bot(command_prefix=">os.")

async def serverpfp():
    print("serverpfp")
    try:
        await bot.wait_until_ready()
        await asyncio.sleep(60*60*6)
        server = bot.get_server('369252350927306752')
        channel = bot.get_channel("418556524785303563")
        randomnum = random.randint(1,405)
        if randomnum <= 10:
            with open("ThePassword.png","rb") as f:
                p = f.read()
                f.close()
            await bot.edit_server(server, icon=p)
            await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: Kyo Takara (ERROR)")
        elif 10 < randomnum <= 30:
            with open("JMAF_Marissa.png","rb") as f:
                p = f.read()
                f.close()
            await bot.edit_server(server, icon=p)
            await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: Marissa")
        elif 30 < randomnum <= 60:
            with open("jmafseason3hype.png","rb") as f:
                p = f.read()
                f.close()
            await bot.edit_server(server, icon=p)
            await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: JMAF Season 3 Banner")
        elif 60 < randomnum <= 100:
            with open("jmafDAN.png","rb") as f:
                p = f.read()
                f.close()
            await bot.edit_server(server, icon=p)
            await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: Dan")
        elif 100 < randomnum <= 150:
            with open("jmafmonika.png","rb") as f:
                p = f.read()
                f.close()
            await bot.edit_server(server, icon=p)
            await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: Monika")
        elif 150 < randomnum <= 205:
            with open("jmafsayori2.png","rb") as f:
                p = f.read()
                f.close()
            await bot.edit_server(server, icon=p)
            await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: Sayori (Variant)")
        elif 205 < randomnum <= 265:
            with open("monikajmaf.png","rb") as f:
                p = f.read()
                f.close()
            await bot.edit_server(server, icon=p)
            await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: Monika (Season 4)")
        elif 265 < randomnum <= 355:
            randomnum2 = random.randint(1,6)
            if randomnum2 == 1:
                with open("JMAF_ICON_2.png","rb") as f:
                    p = f.read()
                    f.close()
                await bot.edit_server(server, icon=p)
                await bot.send_message(channel)
                await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: Natsuki")
            elif randomnum2 == 2:
                with open("JMAF_ICON_3.png","rb") as f:
                    p = f.read()
                    f.close()
                await bot.edit_server(server, icon=p)
                await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: Sayori")
            elif randomnum2 == 3:
                with open("JMAF_ICON_4.png","rb") as f:
                    p = f.read()
                    f.close()
                await bot.edit_server(server, icon=p)
                await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: Yuri")
            elif randomnum2 == 4:
                with open("Misao_JMAF.png","rb") as f:
                    p = f.read()
                    f.close()
                await bot.edit_server(server, icon=p)
                await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: Misao")
            elif randomnum2 == 5:
                with open("jmafmonika2.png","rb") as f:
                    p = f.read()
                    f.close()
                await bot.edit_server(server, icon=p)
                await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: Monika (Season 1-2)")
            elif randomnum2 == 6:
                with open("jmafyuricon3.png","rb") as f:
                    p = f.read()
                    f.close()
                await bot.edit_server(server, icon=p)
                await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: Yuri (Variant)")
        
    except Exception as e:
        print(str(e))

async def zipper():
    print("zipper")
    try:
        await bot.wait_until_ready()
        channel = bot.get_channel('526179743616466955')
        server = bot.get_server('369252350927306752')
        db = psycopg2.connect(host=config.host,database=config.database, user=config.user, password=config.password)
        cursor = db.cursor()
        for x in server.channels:
            if str(x.type) == "text":
                try:
                    cursor.execute("SELECT * FROM logs WHERE channel = '"+str(x.id)+"' ORDER BY time;")
                    c = cursor.fetchall()
                    path = "Just Monika (And Friends) #DAENATAKEOVER/"
                    if not os.path.exists(path):
                        os.makedirs(path)
                    try:
                        os.remove("Just Monika (And Friends) #DAENATAKEOVER/"+x.name+".txt")
                    except:
                        pass
                    txt = open("Just Monika (And Friends) #DAENATAKEOVER/"+x.name+".txt","at")
                    for x in c:
                        todisplay = x[1]
                        details = x[3]
                        txt.write(details+"\n"+todisplay+"\n\n")
                    txt.close()
                except Exception as e:
                    print(e)
        await bot.wait_until_ready()
        def zipdir(path, ziph):
            # ziph is zipfile handle
            for root, dirs, files in os.walk(path):
                for file in files:
                    ziph.write(os.path.join(root, file))
        b = io.BytesIO()
        zipf = zipfile.ZipFile(b, mode="w")
        zipdir('Just Monika (And Friends) #DAENATAKEOVER/', zipf)
        zipf.close()
        b.seek(0)
        await bot.send_file(channel, fp=b, filename=str(datetime.now().day)+"/"+str(datetime.now().month)+"/"+str(datetime.now().year)+"JMAFLogs.zip")
        shutil.rmtree("Just Monika (And Friends) #DAENATAKEOVER/")
        cursor.execute("truncate logs;")
        db.commit()
        db.close()
        await asyncio.sleep(60*60*24)
    except Exception as e:
        print(str(e))
        
bot.loop.create_task(zipper())
bot.loop.create_task(serverpfp())

while True:
	try:
		bot.loop.run_until_complete(bot.run(config.token))
	except BaseException:
		time.sleep(5)
