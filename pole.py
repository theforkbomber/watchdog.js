import discord
import random

client = discord.Client()
greetfirst = ["Greetings ","Hello there "]
greets = ["! Please read the rules in <#448470389836742656>! Also please check out the <#396008626017271811> for better introduction to the server!","! Please read the server's rules in <#448470389836742656>! Also, please check out <#396008626017271811> for a better introduction to the server show! Most importantly, however, I hope you'll enjoy your stay here!"]



@client.event
async def on_ready():
    print('Successfully logged in.')
    print('Username -> ' + client.user.name)
    print('ID -> ' + str(client.user.id))
    activity = discord.Game(name="games whilst waiting for the real Pole to come back...")
    await client.change_presence(status=discord.Status.idle, game=activity)

@client.event
async def on_member_join(member):
    server = member.server
    mention = "<@"+member.id+">"
    if server.id == "454338814865965099":
        channels = "454338815310430239"
    elif server.id == "369252350927306752":
        channels = "398687305482764289"
    elif server.id == "427450243253272598":
        channels = "487662594312765441"
    channel = server.get_channel(channels)
    randomnum = random.randint(0,len(greetfirst)-1)
    greetchosenfirst = greetfirst[randomnum]
    greetlast = greets[randomnum]
    print(channel)
    if channels == "454338815310430239":
        await client.send_message(channel, "Hello "+mention+", make sure you read the <#470285350166855693>, and if you want a certain role, head over to <#470515234767896597> and ping a mod with a role you want.")
    else:
        await client.send_message(channel, greetchosenfirst+mention+greetlast)

client.run("NTA2MDczNjY1MjUxNTczNzYy.Drc3Vg._3iM6CzLcpBOUelv6piq5Z-AD_o")