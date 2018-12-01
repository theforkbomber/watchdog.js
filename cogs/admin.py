import asyncio
import os
import psycopg2
import sys
from io import StringIO
import config
import discord
import inspect
from discord.ext import commands
import traceback
import inspect
import textwrap
from contextlib import redirect_stdout
import io

def admincheck(ctx):
    return ctx.message.author.id == "275312272975462411"


class Admin():
    def __init__(self, bot):
        self.bot = bot
        self._last_result = None
        self.sessions = set()

    def cleanup_code(self, content):
        """Automatically removes code blocks from the code."""
        # remove ```py\n```
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])

        # remove `foo`
        return content.strip('` \n')

    def get_syntax_error(self, e):
        if e.text is None:
            return '```py\n{0.__class__.__name__}: {0}\n```'.format(e)
        return '```py\n{0.text}{1:>{0.offset}}\n{2}: {0}```'.format(e, '^', type(e).__name__)
    @commands.command(pass_context=True, brief="Experimental, don't touch")
    @commands.check(admincheck)
    async def flogs(self, ctx):
        channel = ctx.message.channel
        destination = ctx.message.author
        db = psycopg2.connect(host=config.host,database=config.database, user=config.user, password=config.password)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM logs WHERE channel = '"+str(channel.id)+"';")
        c = cursor.fetchall()
        os.remove("Logs.txt")
        txt = open("Logs.txt","at")
        for x in c:
            todisplay = x[1]
            details = x[3]
            txt.write(details+"\n"+todisplay+"\n\n")
        txt.close()
        await self.bot.send_file(destination=destination, fp=open("Logs.txt","rb"), filename="Logs")

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

    @commands.command(pass_context=True)
    @commands.check(admincheck)
    async def initialise(self, ctx):
        server = ctx.message.server
        role = discord.utils.get(server.roles, name='whoops', server = server)
        await self.bot.say("Learning users' roles...")
        for x in server.members:
            await self.bot.add_roles(x, role)
            await asyncio.sleep(2)
            await self.bot.remove_roles(x, role)
            await asyncio.sleep(2)
        await self.bot.say("Learnt all roles, <@275312272975462411>!")

    # @commands.command(pass_context=True)
    # @commands.check(admincheck)
    # async def opusstart(self, ctx):
    #     if not discord.opus.is_loaded():
    #         for opus_lib in opus_libs:
    #             opus.load_opus(opus_lib)
    #             return


    
def setup(bot):
    bot.add_cog(Admin(bot))
