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

bot = discord.Client()

async def zipper():
    print("zipper")
    while True:
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

while True:
	try:
		bot.loop.run_until_complete(bot.run(config.token))
	except BaseException:
		time.sleep(5)
