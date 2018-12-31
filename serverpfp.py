import discord
import asyncio
import config
import time
import random

bot = discord.Client()

async def serverpfp():
    print("serverpfp")
    try:
        await bot.wait_until_ready()
        server = bot.get_server('369252350927306752')
        channel = bot.get_channel("398687305482764289")
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
        # elif 205 < randomnum <= 265:
        #     with open("monikajmaf.png","rb") as f:
        #         p = f.read()
        #         f.close()
        #     await bot.edit_server(server, icon=p)
        #     await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: Monika (Season 4)")
        elif 205 < randomnum <= 355:
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
        await asyncio.sleep(60*60*6)        
    except Exception as e:
        print(str(e))

bot.loop.create_task(serverpfp())

while True:
	try:
		bot.loop.run_until_complete(bot.run(config.token))
	except BaseException:
		time.sleep(5)

