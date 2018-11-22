import discord
from discord.ext import commands
import random
import traceback
import inspect
import sys
from io import StringIO
import textwrap
from contextlib import redirect_stdout
import io

client = discord.Client()
greetfirst = ["Greetings ","Hello there "]
greets = ["! Please read the rules in <#448470389836742656>! Also please check out the <#396008626017271811> for better introduction to the server!","! Please read the server's rules in <#448470389836742656>! Also, please check out <#396008626017271811> for a better introduction to the server show! Most importantly, however, I hope you'll enjoy your stay here!"]

def admincheck(ctx):
    return ctx.message.author.id == "275312272975462411"
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

    @commands.command(pass_context=True)
    @commands.check(admincheck)
    async def run(self, ctx, *, body: str):
        env = {
            'bot': self.bot,
            'ctx': ctx,
            'channel': ctx.message.channel,
            'author': ctx.message.author,
            'server': ctx.message.server,
            'message': ctx.message,
            '_': self._last_result
        }

        env.update(globals())

        body = self.cleanup_code(body)
        stdout = io.StringIO()

        to_compile = 'async def func():\n%s' % textwrap.indent(body, '  ')

        try:
            exec(to_compile, env)
        except SyntaxError as e:
            return await self.bot.say(self.get_syntax_error(e))

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            await self.bot.say('```py\n{}{}\n```'.format(value, traceback.format_exc()))
        else:
            value = stdout.getvalue()
            try:
                await self.bot.add_reaction(ctx.message, '\u2705')
            except:
                pass

            if ret is None:
                if value:
                    await self.bot.say('```py\n%s\n```' % value)
            else:
                self._last_result = ret
                await self.bot.say('```py\n%s%s\n```' % (value, ret))

client.run("NTA2MDczNjY1MjUxNTczNzYy.Drc3Vg._3iM6CzLcpBOUelv6piq5Z-AD_o")