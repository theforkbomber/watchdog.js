# import sys
# import re
# import configparser
# import urllib.parse
# import urllib.request
# import discord
# from discord.ext import commands
# from cogs.lol import *
# import asyncio
# from subprocess import Popen

# voice_client = None
# text_channel = None
# player = Player
# # p_dl = None
# q_file = "queue.dat"
# yt_url_pattern = re.compile("^http(s)?:/\/(?:www\.)?youtube.com\/watch\?(?=.*v=\w+)(?:\S+)?$")
# yt_color = 0xc4302b
# yt_icon = "https://www.youtube.com/yt/brand/media/image/YouTube-icon-full_color.png"
# text_channel_id = '427450243253272600'

# def get_song_embed(song):
#     if len(song.description) > 200:
#         em = discord.Embed(title=" ", description=song.description[:200] + "...", colour=yt_color, url=song.url)
#     else:
#         em = discord.Embed(title=" ", description=song.description, colour=yt_color, url=song.url)
#     em.set_author(name=song.title, url=song.url)
#     em.add_field(name="Duration", value=song.duration_string, inline=True)
#     em.set_thumbnail(url=song.thumbnail)
#     em.add_field(name="Views", value=song.views, inline=True)
#     em.add_field(name="Likes", value=song.likes, inline=True)
#     em.add_field(name="Dislikes", value=song.dislikes, inline=True)
#     em.set_footer(text=song.source, icon_url=yt_icon)
#     return em


# def get_queue_embed(playlist):
#     em = discord.Embed(title=playlist[0].title,
#                     description="*Duration: " + playlist[0].duration_string + " | Requested by " + playlist[0].requester.display_name + "*",
#                     colour=0x87CEEB,
#                     url=playlist[0].url)
#     em.set_thumbnail(url=playlist[0].thumbnail)
#     em.set_author(name="Playing now:")

#     if len(playlist) > 1:
#         q_list = ""
#         for index, song in enumerate(playlist):
#             if index > 0:
#                 q_list += str(index) + ". " + song.title + " *[" + song.duration_string + " | " + song.requester.display_name + "]*\n\n"
#             if index >= 10:
#                 if len(playlist) > 10:
#                     q_list += "*[" + str(len(playlist) - 10) + " more songs...]*"
#                 break
#         em.add_field(name="Queued:", value=q_list, inline=False)
#     else:
#         em.add_field(name="Queued:", value=" - ", inline=False)
#     return em


# def has_mod_access(user):
#     has_access = False
#     if user.id == '275312272975462411':
#         has_access = True
#     else:
#         for role in user.roles:
#             if role.name == "Minor Literature Club!":
#                 has_access = True
#     return has_access

# if not discord.opus.is_loaded():
#     # the 'opus' library here is opus.dll on windows
#     # or libopus.so on linux in the current directory
#     # you should replace this with the location the
#     # opus library is located in and with the proper filename.
#     # note that on windows this DLL is automatically provided for you
#     discord.opus.load_opus('opus')

# class Music:
#     """Voice related commands.
#     Works in multiple servers at once.
#     """
#     def __init__(self, bot):
#         self.bot = bot
#         player = Player(self.bot, voice_client=voice_client)

    

#     # Initialize opus
#     if not discord.opus.is_loaded():
#         discord.opus.load_opus('opus')

#     # Initialize some global variables

#     # create and start player
   

#     p_dl = Popen(["python", "yt_downloader.py"])

#     @commands.command(pass_context=True, no_pm=True, help="Add a song to the queue. Either the song name or the youtube link.")
#     async def play(self, ctx, *, search_term: str):
#         if ctx.message.channel.id == text_channel_id:
#             await self.bot.send_typing(ctx.message.channel)
#             song_url = None
#             summoned_channel = ctx.message.author.voice_channel
#             await self.bot.join_voice_channel(summoned_channel)
#             # If its a youtube link, search in youtube and get the link of the best match
#             if yt_url_pattern.match(search_term):
#                 song_url = search_term
#             else:
#                 query_string = urllib.parse.urlencode({"search_query": search_term})
#                 html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
#                 search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
#                 if search_results:
#                     song_url = "http://www.youtube.com/watch?v=" + search_results[0]
#                 else:
#                     await self.bot.say(ctx.message.author.mention + " sorry, couldn't find this song on youtube :( Try to give me the link.")

#             if song_url:
#                 # Get all needed information from the song url
#                 try:
#                     this_song = fetch_song(song_url)
#                 except Exception as e:
#                     await self.bot.say(ctx.message.author.mention + " sorry, I can't open this video :( ")
#                     print("Error: " + e)
#                     return

#                 if not this_song:
#                     await self.bot.say(ctx.message.author.mention + " couldn't fetch this song :( ")
#                     return
#                 this_song.requester = ctx.message.author

#                 # Create song embed
#                 em = get_song_embed(this_song)

#                 # Reject song if it's too long
                
#                 player.queue(this_song)
#                 await self.bot.say(ctx.message.author.mention + ' your song was added to the queue!', embed=em)
#             else:
#                 await self.bot.say(ctx.message.author.mention + " sorry, couldn't find a matching song.\nTry to call !play with your desired youtube link.")
#         else:
#             return


#     @commands.command(pass_context=True, no_pm=True, help="Shows the current queue.")
#     async def queue(self, ctx):
#         if ctx.message.channel.id == text_channel_id:
#             await self.bot.send_typing(ctx.message.channel)

#             playlist = player.queue
#             if player and playlist:
#                 em = get_queue_embed(playlist)
#                 await self.bot.say("Here's the current queue: ", embed=em)
#             else:
#                 await self.bot.say(ctx.message.author.mention + " Nothing is playing right now.")


#     @commands.command(pass_context=True, no_pm=True, help="Skip the current song.")
#     async def skip(self, ctx):
#         if ctx.message.channel.id == text_channel_id:
#             await self.bot.send_typing(ctx.message.channel)

#             playlist = player.queue
#             if playlist and len(playlist) > 0:
#                 if ctx.message.author.id == playlist[0].requester.id or has_mod_access(ctx.message.author):
#                     player.skip()
#                     await self.bot.say("Song was skipped by " + ctx.message.author.mention)
#                 else:
#                     await self.bot.say(ctx.message.author.mention + " only the requester can skip this song.")
#             else:
#                 await self.bot.say(ctx.message.author.mention + " nothing is playing right now.")


#     @commands.command(pass_context=True, no_pm=True, help="Remove all queued songs (mod only).")
#     async def clearqueue(self, ctx):
#         if ctx.message.channel.id == text_channel_id:
#             await self.bot.send_typing(ctx.message.channel)

#             if has_mod_access(ctx.message.author):
#                 player.clear_queue()
#                 await self.bot.say(ctx.message.author.mention + " the queue was wiped!")


#     @commands.command(pass_context=True, no_pm=True, help="Show the currently playing song.")
#     async def song(self, ctx):
#         if ctx.message.channel.id == text_channel_id:
#             await self.bot.send_typing(ctx.message.channel)

#             playlist = player.playlist
#             if playlist and len(playlist) > 0:
#                 em = get_song_embed(playlist[0])
#                 await self.bot.say(
#                     ctx.message.author.mention + " this song was requested by " + playlist[0].requester.display_name + " and is playing right now",
#                     embed=em)
#             else:
#                 await self.bot.say(ctx.message.author.mention + " nothing is playing right now")


#     @commands.command(pass_context=True, no_pm=True, help="Restart the music bot (mod only).")
#     async def restart(self, ctx):
#         if ctx.message.channel.id == text_channel_id:
#             if has_mod_access(ctx.message.author):
#                 await self.bot.say("Restarting...")
#                 p_dl.kill()
#                 await self.bot.logout()
#                 t_pending = asyncio.Task.all_tasks(loop=self.bot.loop)
#                 t_gathered = asyncio.gather(*t_pending, loop=self.bot.loop)
#                 t_gathered.cancel()
#                 sys.exit(1)


#     @commands.command(pass_context=True, no_pm=True, help="Remove all queued songs from the mentioned user/yourself.")
#     async def removeall(self, ctx):
#         if ctx.message.channel.id == text_channel_id:
#             await self.bot.send_typing(ctx.message.channel)

#             msg = ""
#             playlist = player.playlist
#             if len(ctx.message.mentions) == 1:
#                 user_mention = ctx.message.mentions[0]
#                 if ctx.message.author.id == user_mention.id or has_mod_access(ctx.message.author):
#                     if playlist and len(playlist) > 1:
#                         for index, song in enumerate(playlist):
#                             if song.requester.id == user_mention.id:
#                                 if not index == 0:
#                                     player.remove(index)
#                                     msg = 'Removed all songs requested by ' + user_mention.mention + ' from the queue.'
#                         if not msg:
#                             msg = ctx.message.author.mention + ' there are no songs from ' + user_mention.mention + ' in the queue.'
#                     else:
#                         msg = ctx.message.author.mention + "the queue is empty, nothing to remove."
#                 else:
#                     msg = ctx.message.author.mention + " you can't remove songs requested by other people."
#             # If command is without mention
#             else:
#                 msg = ctx.message.author.mention + " please mention one person to execute this command."
#             await self.bot.say(msg)


#     @commands.command(pass_context=True, no_pm=True, help="Remove the last added song from the mentioned user/yourself.")
#     async def deltrack(self, ctx):
#         if ctx.message.channel.id == text_channel_id:
#             await self.bot.send_typing(ctx.message.channel)

#             msg = ""
#             playlist = player.playlist
#             # If command is !remove <mention>
#             if len(ctx.message.mentions) > 0:
#                 user_mention = ctx.message.mentions[0]
#                 if ctx.message.author.id == user_mention.id or has_mod_access(ctx.message.author):
#                     if playlist and len(playlist) > 1:
#                         removed_one = False
#                         r_playlist = list(reversed(playlist))
#                         for index, song in enumerate(r_playlist):
#                             # the last song is the first, so the one currently playing
#                             if not index == len(r_playlist) - 1:
#                                 if song.requester.id == user_mention.id:
#                                     if not removed_one:
#                                         player.remove(len(playlist) - index)
#                                         removed_one = True
#                                         msg = 'Removed "' + song.title + '" requested by: ' + song.requester.mention + ' from the queue.'
#                         if not msg:
#                             msg = ctx.message.author.mention + " Could not find any songs from " + user_mention.mention + " in the queue."
#                     else:
#                         msg = ctx.message.author.mention + " Queue is empty, nothing to remove."
#                 else:
#                     msg = ctx.message.author.mention + " You are not allowed to use this command."
#             # If command is without mention
#             else:
#                 if playlist and len(playlist) > 1:
#                     removed_one = False
#                     r_playlist = list(reversed(playlist))
#                     for index, song in enumerate(r_playlist):
#                         if not index == len(r_playlist) - 1:
#                             if song.requester.id == ctx.message.author.id:
#                                 if not removed_one:
#                                     player.remove(len(playlist) - (index + 1))
#                                     removed_one = True
#                                     msg = 'Removed "' + song.title + '" requested by ' + song.requester.mention + ' from the queue.'
#                     if not msg:
#                         msg = ctx.message.author.mention + " Could not find any song that was requested by you in queue."
#                 else:
#                     msg = ctx.message.author.mention + " Queue is empty, nothing to remove."
#             await self.bot.say(msg)


    


#     # # Start the bot in multiprocess compatible manner
#     # if __name__ == "__main__":
#     #     try:
#     #        self.bot.loop.run_until_complete(self.bot.start(login_token))
#     #     except KeyboardInterrupt:
#     #         p_dl.kill()
#     #         self.bot.loop.run_until_complete(self.bot.logout())
#     #         pending = asyncio.Task.all_tasks(loop=bot.loop)
#     #         gathered = asyncio.gather(*pending, loop=bot.loop)
#     #         try:
#     #             gathered.cancel()
#     #             self.bot.loop.run_until_complete(gathered)

#     #             # we want to retrieve any exceptions to make sure that
#     #             # they don't nag us about it being un-retrieved.
#     #             gathered.exception()
#     #         except:
#     #             pass
#     #     finally:
#     #        self.bot.loop.close()
# def setup(bot):
#    bot.add_cog(Music(bot))