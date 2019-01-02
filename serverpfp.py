import discord
import asyncio
import config
import time
import random

bot = discord.Client()

async def serverpfp():
    kyo = 0
    mari = 0
    season3 = 0
    dan = 0
    monikaseason3 = 0
    sayoriv = 0
    moniseason4 = 0
    nat = 0
    sayori = 0
    yuri = 0
    misao = 0
    moniseason12 = 0
    yuriv = 0
    while True:
        changed = False
        print("serverpfp")
        try:
            await bot.wait_until_ready()
            server = bot.get_server('369252350927306752')
            channel = bot.get_channel("398687305482764289")
            randomnum = random.randint(1,405)
            if randomnum <= 10 and kyo == 0:
                if kyo == 0 and randomnum <= 10:
                    with open("ThePassword.png","rb") as f:
                        p = f.read()
                        f.close()
                    await bot.edit_server(server, icon=p)
                    await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: Kyo Takara (ERROR)")
                    kyo += 1
                    # kyo = 0
                    mari = 0
                    season3 = 0
                    dan = 0
                    monikaseason3 = 0
                    sayoriv = 0
                    moniseason4 = 0
                    nat = 0
                    sayori = 0
                    yuri = 0
                    misao = 0
                    moniseason12 = 0
                    yuriv = 0
                    changed = True
                else:
                    kyo = 0
                    changes = False
                    while changes == False:
                        randomnum = random.randint(1,405)
                        if randomnum <= 10:
                            pass
                        else:
                            changes = True
            elif 10 < randomnum <= 30 and mari == 0:
                if mari == 0 and 10 < randomnum <= 30:
                    with open("JMAF_Marissa.png","rb") as f:
                        p = f.read()
                        f.close()
                    await bot.edit_server(server, icon=p)
                    await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: Marissa")
                    kyo = 0
                    mari = 0
                    season3 = 0
                    dan = 0
                    monikaseason3 = 0
                    sayoriv = 0
                    moniseason4 = 0
                    nat = 0
                    sayori = 0
                    yuri = 0
                    misao = 0
                    moniseason12 = 0
                    yuriv = 0
                    mari += 1
                    changed = True
                else:
                    mari = 0
                    changes = False
                    while changes == False:
                        randomnum = random.randint(1,405)
                        if 10 < randomnum <= 30:
                            pass
                        else:
                            changes = True
            elif 30 < randomnum <= 60 and season3 == 0:
                if season3 == 0 and 30 < randomnum <= 60:
                    with open("jmafseason3hype.png","rb") as f:
                        p = f.read()
                        f.close()
                    await bot.edit_server(server, icon=p)
                    await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: America Arc Banner")
                    kyo = 0
                    mari = 0
                    season3 = 0
                    dan = 0
                    monikaseason3 = 0
                    sayoriv = 0
                    moniseason4 = 0
                    nat = 0
                    sayori = 0
                    yuri = 0
                    misao = 0
                    moniseason12 = 0
                    yuriv = 0
                    season3 += 1
                    changed = True
                else:
                    season3 = 0
                    changes = False
                    while changes == False:
                        randomnum = random.randint(1,405)
                        if 30 < randomnum <= 60:
                            pass
                        else:
                            changes = True
            elif 60 < randomnum <= 100 and dan == 0:
                if dan == 0 and 60 < randomnum <= 100:
                    with open("jMAFDAN.png","rb") as f:
                        p = f.read()
                        f.close()
                    await bot.edit_server(server, icon=p)
                    await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: Dan")
                    kyo = 0
                    mari = 0
                    season3 = 0
                    dan = 0
                    monikaseason3 = 0
                    sayoriv = 0
                    moniseason4 = 0
                    nat = 0
                    sayori = 0
                    yuri = 0
                    misao = 0
                    moniseason12 = 0
                    yuriv = 0
                    dan += 1
                    changed = True
                else:
                    dan = 0
                    changes = False
                    while changes == False:
                        randomnum = random.randint(1,405)
                        if 60 < randomnum <= 100:
                            pass
                        else:
                            changes = True
            elif 100 < randomnum <= 150 and monikaseason3 == 0:
                if monikaseason3 == 0 and 100 < randomnum <= 150:
                    with open("jmafmonika.png","rb") as f:
                        p = f.read()
                        f.close()
                    await bot.edit_server(server, icon=p)
                    await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: Monika (Season 3)")
                    kyo = 0
                    mari = 0
                    season3 = 0
                    dan = 0
                    monikaseason3 = 0
                    sayoriv = 0
                    moniseason4 = 0
                    nat = 0
                    sayori = 0
                    yuri = 0
                    misao = 0
                    moniseason12 = 0
                    yuriv = 0
                    monikaseason3 += 1
                    changed = True
                else:
                    monikaseason3 = 0
                    changes = False
                    while changes == False:
                        randomnum = random.randint(1,405)
                        if 100 < randomnum <= 150:
                            pass
                        else:
                            changes = True
            elif 150 < randomnum <= 205 and sayoriv == 0:
                if sayoriv == 0 and 150 < randomnum <= 205:
                    with open("jmafsayori2.png","rb") as f:
                        p = f.read()
                        f.close()
                    await bot.edit_server(server, icon=p)
                    await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: Sayori (Variant)")
                    kyo = 0
                    mari = 0
                    season3 = 0
                    dan = 0
                    monikaseason3 = 0
                    sayoriv = 0
                    moniseason4 = 0
                    nat = 0
                    sayori = 0
                    yuri = 0
                    misao = 0
                    moniseason12 = 0
                    yuriv = 0
                    sayoriv += 1
                    changed = True
                else:
                    sayoriv = 0
                    changes = False
                    while changes == False:
                        randomnum = random.randint(1,405)
                        if 150 < randomnum <= 205:
                            pass
                        else:
                            changes = True
            elif 205 < randomnum <= 265 and moniseason4 == 0:
                if moniseason4 == 0 and 205 < randomnum <= 265:
                    with open("monikajmaf.png","rb") as f:
                        p = f.read()
                        f.close()
                    await bot.edit_server(server, icon=p)
                    await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: Monika (Season 4)")
                    kyo = 0
                    mari = 0
                    season3 = 0
                    dan = 0
                    monikaseason3 = 0
                    sayoriv = 0
                    moniseason4 = 0
                    nat = 0
                    sayori = 0
                    yuri = 0
                    misao = 0
                    moniseason12 = 0
                    yuriv = 0
                    moniseason4 += 1
                    changed = True
                else:
                    moniseason4 = 0
                    changes = False
                    while changes == False:
                        randomnum = random.randint(1,405)
                        if 205 < randomnum <= 265:
                            pass
                        else:
                            changes = True
            elif 265 < randomnum <= 355:
                randomnum2 = random.randint(1,6)
                if randomnum2 == 1 and nat == 0:
                    if nat == 0 and randomnum2 == 1:
                        with open("JMAF_ICON_2.png","rb") as f:
                            p = f.read()
                            f.close()
                        await bot.edit_server(server, icon=p)
                        await bot.send_message(channel)
                        await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: Natsuki")
                        kyo = 0
                        mari = 0
                        season3 = 0
                        dan = 0
                        monikaseason3 = 0
                        sayoriv = 0
                        moniseason4 = 0
                        nat = 0
                        sayori = 0
                        yuri = 0
                        misao = 0
                        moniseason12 = 0
                        yuriv = 0
                        nat += 1
                        changed = True
                    else:
                        nat = 0
                        changes = False
                        while changes == False:
                            randomnum = random.randint(1,405)
                            if 265 < randomnum <= 355:
                                randomnum2 = random.randint(1,6)
                                if randomnum2 == 1:
                                    pass
                                else:
                                    changes = True
                            else:
                                changes = True
                elif randomnum2 == 2 and sayori == 0:
                    if sayori == 0 and randomnum2 == 2:
                        with open("JMAF_ICON_3.png","rb") as f:
                            p = f.read()
                            f.close()
                        await bot.edit_server(server, icon=p)
                        await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: Sayori")
                        kyo = 0
                        mari = 0
                        season3 = 0
                        dan = 0
                        monikaseason3 = 0
                        sayoriv = 0
                        moniseason4 = 0
                        nat = 0
                        sayori = 0
                        yuri = 0
                        misao = 0
                        moniseason12 = 0
                        yuriv = 0
                        sayori += 1
                        changed = True
                    else:
                        sayori = 0
                        changes = False
                        while changes == False:
                            randomnum = random.randint(1,405)
                            if 265 < randomnum <= 355:
                                randomnum2 = random.randint(1,6)
                                if randomnum2 == 2:
                                    pass
                                else:
                                    changes = True
                            else:
                                changes = True
                elif randomnum2 == 3 and yuri == 0:
                    if yuri == 0 and randomnum2 == 3:
                        with open("jmaf_icon_4.png","rb") as f:
                            p = f.read()
                            f.close()
                        await bot.edit_server(server, icon=p)
                        await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: Yuri")
                        kyo = 0
                        mari = 0
                        season3 = 0
                        dan = 0
                        monikaseason3 = 0
                        sayoriv = 0
                        moniseason4 = 0
                        nat = 0
                        sayori = 0
                        yuri = 0
                        misao = 0
                        moniseason12 = 0
                        yuriv = 0
                        yuri += 1
                        changed = True
                    else:
                        yuri = 0
                        changes = False
                        while changes == False:
                            randomnum = random.randint(1,405)
                            if 265 < randomnum <= 355:
                                randomnum2 = random.randint(1,6)
                                if randomnum2 == 3:
                                    pass
                                else:
                                    changes = True
                            else:
                                changes = True
                elif randomnum2 == 4 and misao == 0:
                    if misao == 0 and randomnum2 == 4:
                        with open("Misao_JMAF.png","rb") as f:
                            p = f.read()
                            f.close()
                        await bot.edit_server(server, icon=p)
                        await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: Misao")
                        kyo = 0
                        mari = 0
                        season3 = 0
                        dan = 0
                        monikaseason3 = 0
                        sayoriv = 0
                        moniseason4 = 0
                        nat = 0
                        sayori = 0
                        yuri = 0
                        misao = 0
                        moniseason12 = 0
                        yuriv = 0
                        misao += 1
                        changed = True
                    else:
                        misao = 0
                        changes = False
                        while changes == False:
                            randomnum = random.randint(1,405)
                            if 265 < randomnum <= 355:
                                randomnum2 = random.randint(1,6)
                                if randomnum2 == 4:
                                    pass
                                else:
                                    changes = True
                            else:
                                changes = True

                elif randomnum2 == 5 and moniseason12 == 0:
                    if moniseason12 == 0 and randomnum2 == 5:
                        with open("jmafmonika2.png","rb") as f:
                            p = f.read()
                            f.close()
                        await bot.edit_server(server, icon=p)
                        await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: Monika (Season 1-2)")
                        kyo = 0
                        mari = 0
                        season3 = 0
                        dan = 0
                        monikaseason3 = 0
                        sayoriv = 0
                        moniseason4 = 0
                        nat = 0
                        sayori = 0
                        yuri = 0
                        misao = 0
                        moniseason12 = 0
                        yuriv = 0
                        moniseason12 += 1
                        changed = True
                    else:
                        moniseason12 = 0
                        changes = False
                        while changes == False:
                            randomnum = random.randint(1,405)
                            if 265 < randomnum <= 355:
                                randomnum2 = random.randint(1,6)
                                if randomnum2 == 5:
                                    pass
                                else:
                                    changes = True
                            else:
                                changes = True
                elif randomnum2 == 6 and yuriv == 0:
                    if yuriv == 0 and randomnum2 == 6:
                        with open("jmafyuricon3.png","rb") as f:
                            p = f.read()
                            f.close()
                        await bot.edit_server(server, icon=p)
                        await bot.send_message(channel, "The server image has changed! CURRENT ARTWORK: Yuri (Variant)")
                        kyo = 0
                        mari = 0
                        season3 = 0
                        dan = 0
                        monikaseason3 = 0
                        sayoriv = 0
                        moniseason4 = 0
                        nat = 0
                        sayori = 0
                        yuri = 0
                        misao = 0
                        moniseason12 = 0
                        yuriv = 0
                        yuriv += 1
                        changed = True
                    else:
                        yuriv = 0
                        changes = False
                        while changes == False:
                            randomnum = random.randint(1,405)
                            if 265 < randomnum <= 355:
                                randomnum2 = random.randint(1,6)
                                if randomnum2 == 6:
                                    pass
                                else:
                                    changes = True
                            else:
                                changes = True
            if changed == True:
                await asyncio.sleep(60*60*6)
            else:
                pass
        except Exception as e:
            print(str(e))

bot.loop.create_task(serverpfp())

while True:
	try:
		bot.loop.run_until_complete(bot.run(config.token))
	except BaseException:
		time.sleep(5)

