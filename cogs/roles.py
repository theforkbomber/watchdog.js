# from discord.ext import commands
# import discord
# import asyncio

# ###########role###################rolerare###############rolelegacy


# class Roles:
#     def __init__(self, bot):
#         self.bot = bot

#     @commands.command(pass_context=True)
#     async def monika(self, ctx):
#         natsuki = ["369253424124133396","384447386153517056","390191979645894666"]          
#         monika = ["369253075137069057","396333414565019661","390191886108983306"]
#         yuri = ["369254043056472065","396333080886902795","390192874484006914"]
#         sayori = ["369261933343408129","396333588854997002","390191678859902987"]
#         misao = ["486963160201297920","396333868694896640","389540219835121684"]
#         protagonist = ["369254217015099414","460284706877865985","409462716432908299"]
#         norm = False
#         rare = False
#         legacy = False
#         server = ctx.message.server
#         user = server.get_member(ctx.message.author.id)
#         for role in user.roles:
#             while norm == False and rare == False and legacy == False:

#                 if role.id == natsuki[0]:
#                     norm = True
#                 if role.id == natsuki[1]:
#                     rare = True
#                 if role.id == natsuki[2]:
#                     legacy = True

#                 if role.id == sayori[0]:
#                     norm = True
#                 if role.id == sayori[1]:
#                     rare = True
#                 if role.id == sayori[2]:
#                     legacy = True

#                 if role.id == misao[0]:
#                     norm = True
#                 if role.id == misao[1]:
#                     rare = True
#                 if role.id == misao[2]:
#                     legacy = True

#                 if role.id == yuri[0]:
#                     norm = True
#                 if role.id == yuri[1]:
#                     rare = True
#                 if role.id == yuri[2]:
#                     legacy = True

#                 if role.id == protagonist[0]:
#                     norm = True
#                 if role.id == protagonist[1]:
#                     rare = True
#                 if role.id == protagonist[2]:
#                     legacy = True
#                 break
            
#             if norm == True:
#                 moni = None
#                 yuri = None
#                 sayori = None
#                 misao = None
#                 nat = None
#                 protag = None
#                 falsey = False
#                 for role in server.roles:
#                     if role.id == monika[0]:
#                         moni = role
#                     if role.id == natsuki[0]:
#                         nat = role
#                     if role.id == yuri[0]:
#                         yuri = role
#                     if role.id == misao[0]:
#                         misao = role
#                     if role.id == sayori[0]:
#                         sayori = role
#                     if role.id == protagonist[0]:
#                         protag = role
#                 if moni != None:
#                     await self.bot.remove_roles(user, moni)
#                 if nat != None:
#                     await self.bot.remove_roles(user, nat)
#                 if yuri != None:
#                     await self.bot.remove_roles(user, yuri)
#                 if misao != None:
#                     await self.bot.remove_roles(user, misao)
#                 if sayori != None:
#                     await self.bot.remove_roles(user, sayori)
#                 if protag != None:
#                     await self.bot.remove_roles(user, protag)
#                 else:
#                     falsey = True
#                 if falsey == False:
#                     await self.bot.add_roles(user, moni)
#             if rare == True:
#                 moni = None
#                 yuri = None
#                 sayori = None
#                 misao = None
#                 nat = None
#                 protag = None
#                 falsey = False
#                 for role in server.roles:
#                     if role.id == monika[1]:
#                         moni = role
#                     if role.id == natsuki[1]:
#                         nat = role
#                     if role.id == yuri[1]:
#                         yuri = role
#                     if role.id == misao[1]:
#                         misao = role
#                     if role.id == sayori[1]:
#                         sayori = role
#                     if role.id == protagonist[1]:
#                         protag = role
#                 if moni != None:
#                     await self.bot.remove_roles(user, moni)
#                 if nat != None:
#                     await self.bot.remove_roles(user, nat)
#                 if yuri != None:
#                     await self.bot.remove_roles(user, yuri)
#                 if misao != None:
#                     await self.bot.remove_roles(user, misao)
#                 if sayori != None:
#                     await self.bot.remove_roles(user, sayori)
#                 if protag != None:
#                     await self.bot.remove_roles(user, protag)
#                 else:
#                     falsey = True
#                 if falsey == False:
#                     await self.bot.add_roles(user, moni)
#             if legacy == True:
#                 moni = None
#                 yuri = None
#                 sayori = None
#                 misao = None
#                 nat = None
#                 protag = None
#                 falsey = False
#                 for role in server.roles:
#                     if role.id == monika[2]:
#                         moni = role
#                     if role.id == natsuki[2]:
#                         nat = role
#                     if role.id == yuri[2]:
#                         yuri = role
#                     if role.id == misao[2]:
#                         misao = role
#                     if role.id == sayori[2]:
#                         sayori = role
#                     if role.id == protagonist[2]:
#                         protag = role
#                 if moni != None:
#                     await self.bot.remove_roles(user, moni)
#                 if nat != None:
#                     await self.bot.remove_roles(user, nat)
#                 if yuri != None:
#                     await self.bot.remove_roles(user, yuri)
#                 if misao != None:
#                     await self.bot.remove_roles(user, misao)
#                 if sayori != None:
#                     await self.bot.remove_roles(user, sayori)
#                 if protag != None:
#                     await self.bot.remove_roles(user, protag)
#                 else:
#                     falsey = True
#                 if falsey == False:
#                     await self.bot.add_roles(user, moni)
#             else:
#                 await self.bot.say("An error occurred...")
#                 break
    
#     @commands.command(pass_context=True)
#     async def natsuki(self, ctx):
#         natsuki = ["369253424124133396","384447386153517056","390191979645894666"]          
#         monika = ["369253075137069057","396333414565019661","390191886108983306"]
#         yuri = ["369254043056472065","396333080886902795","390192874484006914"]
#         sayori = ["369261933343408129","396333588854997002","390191678859902987"]
#         misao = ["486963160201297920","396333868694896640","389540219835121684"]
#         protagonist = ["369254217015099414","460284706877865985","409462716432908299"]
#         norm = False
#         rare = False
#         legacy = False
#         server = ctx.message.server
#         user = server.get_member(ctx.message.author.id)
#         for role in user.roles:
#             while norm == False and rare == False and legacy == False:

#                 if role.id == monika[0]:
#                     norm = True
#                 if role.id == monika[1]:
#                     rare = True
#                 if role.id == monika[2]:
#                     legacy = True

#                 if role.id == sayori[0]:
#                     norm = True
#                 if role.id == sayori[1]:
#                     rare = True
#                 if role.id == sayori[2]:
#                     legacy = True

#                 if role.id == misao[0]:
#                     norm = True
#                 if role.id == misao[1]:
#                     rare = True
#                 if role.id == misao[2]:
#                     legacy = True

#                 if role.id == yuri[0]:
#                     norm = True
#                 if role.id == yuri[1]:
#                     rare = True
#                 if role.id == yuri[2]:
#                     legacy = True

#                 if role.id == protagonist[0]:
#                     norm = True
#                 if role.id == protagonist[1]:
#                     rare = True
#                 if role.id == protagonist[2]:
#                     legacy = True
#                 break
            
#             if norm == True:
#                 moni = None
#                 yuri = None
#                 sayori = None
#                 misao = None
#                 nat = None
#                 protag = None
#                 falsey = False
#                 for role in server.roles:
#                     if role.id == monika[0]:
#                         moni = role
#                     if role.id == natsuki[0]:
#                         nat = role
#                     if role.id == yuri[0]:
#                         yuri = role
#                     if role.id == misao[0]:
#                         misao = role
#                     if role.id == sayori[0]:
#                         sayori = role
#                     if role.id == protagonist[0]:
#                         protag = role
#                 if moni != None:
#                     await self.bot.remove_roles(user, moni)
#                 if nat != None:
#                     await self.bot.remove_roles(user, nat)
#                 if yuri != None:
#                     await self.bot.remove_roles(user, yuri)
#                 if misao != None:
#                     await self.bot.remove_roles(user, misao)
#                 if sayori != None:
#                     await self.bot.remove_roles(user, sayori)
#                 if protag != None:
#                     await self.bot.remove_roles(user, protag)
#                 else:
#                     falsey = True
#                 if falsey == False:
#                     await self.bot.add_roles(user, moni)
#             if rare == True:
#                 moni = None
#                 yuri = None
#                 sayori = None
#                 misao = None
#                 nat = None
#                 protag = None
#                 falsey = False
#                 for role in server.roles:
#                     if role.id == monika[1]:
#                         moni = role
#                     if role.id == natsuki[1]:
#                         nat = role
#                     if role.id == yuri[1]:
#                         yuri = role
#                     if role.id == misao[1]:
#                         misao = role
#                     if role.id == sayori[1]:
#                         sayori = role
#                     if role.id == protagonist[1]:
#                         protag = role
#                 if moni != None:
#                     await self.bot.remove_roles(user, moni)
#                 if nat != None:
#                     await self.bot.remove_roles(user, nat)
#                 if yuri != None:
#                     await self.bot.remove_roles(user, yuri)
#                 if misao != None:
#                     await self.bot.remove_roles(user, misao)
#                 if sayori != None:
#                     await self.bot.remove_roles(user, sayori)
#                 if protag != None:
#                     await self.bot.remove_roles(user, protag)
#                 else:
#                     falsey = True
#                 if falsey == False:
#                     await self.bot.add_roles(user, moni)
#             if legacy == True:
#                 moni = None
#                 yuri = None
#                 sayori = None
#                 misao = None
#                 nat = None
#                 protag = None
#                 falsey = False
#                 for role in server.roles:
#                     if role.id == monika[2]:
#                         moni = role
#                     if role.id == natsuki[2]:
#                         nat = role
#                     if role.id == yuri[2]:
#                         yuri = role
#                     if role.id == misao[2]:
#                         misao = role
#                     if role.id == sayori[2]:
#                         sayori = role
#                     if role.id == protagonist[2]:
#                         protag = role
#                 if moni != None:
#                     await self.bot.remove_roles(user, moni)
#                 if nat != None:
#                     await self.bot.remove_roles(user, nat)
#                 if yuri != None:
#                     await self.bot.remove_roles(user, yuri)
#                 if misao != None:
#                     await self.bot.remove_roles(user, misao)
#                 if sayori != None:
#                     await self.bot.remove_roles(user, sayori)
#                 if protag != None:
#                     await self.bot.remove_roles(user, protag)
#                 else:
#                     falsey = True
#                 if falsey == False:
#                     await self.bot.add_roles(user, moni)
#             else:
#                 await self.bot.say("An error occurred...")
#                 break

#     @commands.command(pass_context=True)
#     async def yuri(self, ctx):
#         natsuki = ["369253424124133396","384447386153517056","390191979645894666"]          
#         monika = ["369253075137069057","396333414565019661","390191886108983306"]
#         yuri = ["369254043056472065","396333080886902795","390192874484006914"]
#         sayori = ["369261933343408129","396333588854997002","390191678859902987"]
#         misao = ["486963160201297920","396333868694896640","389540219835121684"]
#         protagonist = ["369254217015099414","460284706877865985","409462716432908299"]
#         norm = False
#         rare = False
#         legacy = False
#         server = ctx.message.server
#         user = server.get_member(ctx.message.author.id)
#         for role in user.roles:
#             while norm == False and rare == False and legacy == False:

#                 if role.id == monika[0]:
#                     norm = True
#                 if role.id == monika[1]:
#                     rare = True
#                 if role.id == monika[2]:
#                     legacy = True

#                 if role.id == sayori[0]:
#                     norm = True
#                 if role.id == sayori[1]:
#                     rare = True
#                 if role.id == sayori[2]:
#                     legacy = True

#                 if role.id == misao[0]:
#                     norm = True
#                 if role.id == misao[1]:
#                     rare = True
#                 if role.id == misao[2]:
#                     legacy = True

#                 if role.id == natsuki[0]:
#                     norm = True
#                 if role.id == natsuki[1]:
#                     rare = True
#                 if role.id == natsuki[2]:
#                     legacy = True

#                 if role.id == protagonist[0]:
#                     norm = True
#                 if role.id == protagonist[1]:
#                     rare = True
#                 if role.id == protagonist[2]:
#                     legacy = True
#                 break
            
#             if norm == True:
#                 moni = None
#                 yuri = None
#                 sayori = None
#                 misao = None
#                 nat = None
#                 protag = None
#                 falsey = False
#                 for role in server.roles:
#                     if role.id == monika[0]:
#                         moni = role
#                     if role.id == natsuki[0]:
#                         nat = role
#                     if role.id == yuri[0]:
#                         yuri = role
#                     if role.id == misao[0]:
#                         misao = role
#                     if role.id == sayori[0]:
#                         sayori = role
#                     if role.id == protagonist[0]:
#                         protag = role
#                 if moni != None:
#                     await self.bot.remove_roles(user, moni)
#                 if nat != None:
#                     await self.bot.remove_roles(user, nat)
#                 if yuri != None:
#                     await self.bot.remove_roles(user, yuri)
#                 if misao != None:
#                     await self.bot.remove_roles(user, misao)
#                 if sayori != None:
#                     await self.bot.remove_roles(user, sayori)
#                 if protag != None:
#                     await self.bot.remove_roles(user, protag)
#                 else:
#                     falsey = True
#                 if falsey == False:
#                     await self.bot.add_roles(user, moni)
#             if rare == True:
#                 moni = None
#                 yuri = None
#                 sayori = None
#                 misao = None
#                 nat = None
#                 protag = None
#                 falsey = False
#                 for role in server.roles:
#                     if role.id == monika[1]:
#                         moni = role
#                     if role.id == natsuki[1]:
#                         nat = role
#                     if role.id == yuri[1]:
#                         yuri = role
#                     if role.id == misao[1]:
#                         misao = role
#                     if role.id == sayori[1]:
#                         sayori = role
#                     if role.id == protagonist[1]:
#                         protag = role
#                 if moni != None:
#                     await self.bot.remove_roles(user, moni)
#                 if nat != None:
#                     await self.bot.remove_roles(user, nat)
#                 if yuri != None:
#                     await self.bot.remove_roles(user, yuri)
#                 if misao != None:
#                     await self.bot.remove_roles(user, misao)
#                 if sayori != None:
#                     await self.bot.remove_roles(user, sayori)
#                 if protag != None:
#                     await self.bot.remove_roles(user, protag)
#                 else:
#                     falsey = True
#                 if falsey == False:
#                     await self.bot.add_roles(user, moni)
#             if legacy == True:
#                 moni = None
#                 yuri = None
#                 sayori = None
#                 misao = None
#                 nat = None
#                 protag = None
#                 falsey = False
#                 for role in server.roles:
#                     if role.id == monika[2]:
#                         moni = role
#                     if role.id == natsuki[2]:
#                         nat = role
#                     if role.id == yuri[2]:
#                         yuri = role
#                     if role.id == misao[2]:
#                         misao = role
#                     if role.id == sayori[2]:
#                         sayori = role
#                     if role.id == protagonist[2]:
#                         protag = role
#                 if moni != None:
#                     await self.bot.remove_roles(user, moni)
#                 if nat != None:
#                     await self.bot.remove_roles(user, nat)
#                 if yuri != None:
#                     await self.bot.remove_roles(user, yuri)
#                 if misao != None:
#                     await self.bot.remove_roles(user, misao)
#                 if sayori != None:
#                     await self.bot.remove_roles(user, sayori)
#                 if protag != None:
#                     await self.bot.remove_roles(user, protag)
#                 else:
#                     falsey = True
#                 if falsey == False:
#                     await self.bot.add_roles(user, moni)
#             else:
#                 await self.bot.say("An error occurred...")
#                 break

#     @commands.command(pass_context=True)
#     async def misao(self, ctx):
#         natsuki = ["369253424124133396","384447386153517056","390191979645894666"]          
#         monika = ["369253075137069057","396333414565019661","390191886108983306"]
#         yuri = ["369254043056472065","396333080886902795","390192874484006914"]
#         sayori = ["369261933343408129","396333588854997002","390191678859902987"]
#         misao = ["486963160201297920","396333868694896640","389540219835121684"]
#         protagonist = ["369254217015099414","460284706877865985","409462716432908299"]
#         norm = False
#         rare = False
#         legacy = False
#         server = ctx.message.server
#         user = server.get_member(ctx.message.author.id)
#         for role in user.roles:
#             while norm == False and rare == False and legacy == False:

#                 if role.id == monika[0]:
#                     norm = True
#                 if role.id == monika[1]:
#                     rare = True
#                 if role.id == monika[2]:
#                     legacy = True

#                 if role.id == sayori[0]:
#                     norm = True
#                 if role.id == sayori[1]:
#                     rare = True
#                 if role.id == sayori[2]:
#                     legacy = True

#                 if role.id == natsuki[0]:
#                     norm = True
#                 if role.id == natsuki[1]:
#                     rare = True
#                 if role.id == natsuki[2]:
#                     legacy = True

#                 if role.id == yuri[0]:
#                     norm = True
#                 if role.id == yuri[1]:
#                     rare = True
#                 if role.id == yuri[2]:
#                     legacy = True

#                 if role.id == protagonist[0]:
#                     norm = True
#                 if role.id == protagonist[1]:
#                     rare = True
#                 if role.id == protagonist[2]:
#                     legacy = True
#                 break
            
#             if norm == True:
#                 moni = None
#                 yuri = None
#                 sayori = None
#                 misao = None
#                 nat = None
#                 protag = None
#                 falsey = False
#                 for role in server.roles:
#                     if role.id == monika[0]:
#                         moni = role
#                     if role.id == natsuki[0]:
#                         nat = role
#                     if role.id == yuri[0]:
#                         yuri = role
#                     if role.id == misao[0]:
#                         misao = role
#                     if role.id == sayori[0]:
#                         sayori = role
#                     if role.id == protagonist[0]:
#                         protag = role
#                 if moni != None:
#                     await self.bot.remove_roles(user, moni)
#                 if nat != None:
#                     await self.bot.remove_roles(user, nat)
#                 if yuri != None:
#                     await self.bot.remove_roles(user, yuri)
#                 if misao != None:
#                     await self.bot.remove_roles(user, misao)
#                 if sayori != None:
#                     await self.bot.remove_roles(user, sayori)
#                 if protag != None:
#                     await self.bot.remove_roles(user, protag)
#                 else:
#                     falsey = True
#                 if falsey == False:
#                     await self.bot.add_roles(user, moni)
#             if rare == True:
#                 moni = None
#                 yuri = None
#                 sayori = None
#                 misao = None
#                 nat = None
#                 protag = None
#                 falsey = False
#                 for role in server.roles:
#                     if role.id == monika[1]:
#                         moni = role
#                     if role.id == natsuki[1]:
#                         nat = role
#                     if role.id == yuri[1]:
#                         yuri = role
#                     if role.id == misao[1]:
#                         misao = role
#                     if role.id == sayori[1]:
#                         sayori = role
#                     if role.id == protagonist[1]:
#                         protag = role
#                 if moni != None:
#                     await self.bot.remove_roles(user, moni)
#                 if nat != None:
#                     await self.bot.remove_roles(user, nat)
#                 if yuri != None:
#                     await self.bot.remove_roles(user, yuri)
#                 if misao != None:
#                     await self.bot.remove_roles(user, misao)
#                 if sayori != None:
#                     await self.bot.remove_roles(user, sayori)
#                 if protag != None:
#                     await self.bot.remove_roles(user, protag)
#                 else:
#                     falsey = True
#                 if falsey == False:
#                     await self.bot.add_roles(user, moni)
#             if legacy == True:
#                 moni = None
#                 yuri = None
#                 sayori = None
#                 misao = None
#                 nat = None
#                 protag = None
#                 falsey = False
#                 for role in server.roles:
#                     if role.id == monika[2]:
#                         moni = role
#                     if role.id == natsuki[2]:
#                         nat = role
#                     if role.id == yuri[2]:
#                         yuri = role
#                     if role.id == misao[2]:
#                         misao = role
#                     if role.id == sayori[2]:
#                         sayori = role
#                     if role.id == protagonist[2]:
#                         protag = role
#                 if moni != None:
#                     await self.bot.remove_roles(user, moni)
#                 if nat != None:
#                     await self.bot.remove_roles(user, nat)
#                 if yuri != None:
#                     await self.bot.remove_roles(user, yuri)
#                 if misao != None:
#                     await self.bot.remove_roles(user, misao)
#                 if sayori != None:
#                     await self.bot.remove_roles(user, sayori)
#                 if protag != None:
#                     await self.bot.remove_roles(user, protag)
#                 else:
#                     falsey = True
#                 if falsey == False:
#                     await self.bot.add_roles(user, moni)
#             else:
#                 await self.bot.say("An error occurred...")
#                 break

#     @commands.command(pass_context=True)
#     async def sayori(self, ctx):
#         natsuki = ["369253424124133396","384447386153517056","390191979645894666"]          
#         monika = ["369253075137069057","396333414565019661","390191886108983306"]
#         yuri = ["369254043056472065","396333080886902795","390192874484006914"]
#         sayori = ["369261933343408129","396333588854997002","390191678859902987"]
#         misao = ["486963160201297920","396333868694896640","389540219835121684"]
#         protagonist = ["369254217015099414","460284706877865985","409462716432908299"]
#         norm = False
#         rare = False
#         legacy = False
#         server = ctx.message.server
#         user = server.get_member(ctx.message.author.id)
#         for role in user.roles:
#             while norm == False and rare == False and legacy == False:

#                 if role.id == monika[0]:
#                     norm = True
#                 if role.id == monika[1]:
#                     rare = True
#                 if role.id == monika[2]:
#                     legacy = True

#                 if role.id == natsuki[0]:
#                     norm = True
#                 if role.id == natsuki[1]:
#                     rare = True
#                 if role.id == natsuki[2]:
#                     legacy = True

#                 if role.id == misao[0]:
#                     norm = True
#                 if role.id == misao[1]:
#                     rare = True
#                 if role.id == misao[2]:
#                     legacy = True

#                 if role.id == yuri[0]:
#                     norm = True
#                 if role.id == yuri[1]:
#                     rare = True
#                 if role.id == yuri[2]:
#                     legacy = True

#                 if role.id == protagonist[0]:
#                     norm = True
#                 if role.id == protagonist[1]:
#                     rare = True
#                 if role.id == protagonist[2]:
#                     legacy = True
#                 break
            
#             if norm == True:
#                 moni = None
#                 yuri = None
#                 sayori = None
#                 misao = None
#                 nat = None
#                 protag = None
#                 falsey = False
#                 for role in server.roles:
#                     if role.id == monika[0]:
#                         moni = role
#                     if role.id == natsuki[0]:
#                         nat = role
#                     if role.id == yuri[0]:
#                         yuri = role
#                     if role.id == misao[0]:
#                         misao = role
#                     if role.id == sayori[0]:
#                         sayori = role
#                     if role.id == protagonist[0]:
#                         protag = role
#                 if moni != None:
#                     await self.bot.remove_roles(user, moni)
#                 if nat != None:
#                     await self.bot.remove_roles(user, nat)
#                 if yuri != None:
#                     await self.bot.remove_roles(user, yuri)
#                 if misao != None:
#                     await self.bot.remove_roles(user, misao)
#                 if sayori != None:
#                     await self.bot.remove_roles(user, sayori)
#                 if protag != None:
#                     await self.bot.remove_roles(user, protag)
#                 else:
#                     falsey = True
#                 if falsey == False:
#                     await self.bot.add_roles(user, moni)
#             if rare == True:
#                 moni = None
#                 yuri = None
#                 sayori = None
#                 misao = None
#                 nat = None
#                 protag = None
#                 falsey = False
#                 for role in server.roles:
#                     if role.id == monika[1]:
#                         moni = role
#                     if role.id == natsuki[1]:
#                         nat = role
#                     if role.id == yuri[1]:
#                         yuri = role
#                     if role.id == misao[1]:
#                         misao = role
#                     if role.id == sayori[1]:
#                         sayori = role
#                     if role.id == protagonist[1]:
#                         protag = role
#                 if moni != None:
#                     await self.bot.remove_roles(user, moni)
#                 if nat != None:
#                     await self.bot.remove_roles(user, nat)
#                 if yuri != None:
#                     await self.bot.remove_roles(user, yuri)
#                 if misao != None:
#                     await self.bot.remove_roles(user, misao)
#                 if sayori != None:
#                     await self.bot.remove_roles(user, sayori)
#                 if protag != None:
#                     await self.bot.remove_roles(user, protag)
#                 else:
#                     falsey = True
#                 if falsey == False:
#                     await self.bot.add_roles(user, moni)
#             if legacy == True:
#                 moni = None
#                 yuri = None
#                 sayori = None
#                 misao = None
#                 nat = None
#                 protag = None
#                 falsey = False
#                 for role in server.roles:
#                     if role.id == monika[2]:
#                         moni = role
#                     if role.id == natsuki[2]:
#                         nat = role
#                     if role.id == yuri[2]:
#                         yuri = role
#                     if role.id == misao[2]:
#                         misao = role
#                     if role.id == sayori[2]:
#                         sayori = role
#                     if role.id == protagonist[2]:
#                         protag = role
#                 if moni != None:
#                     await self.bot.remove_roles(user, moni)
#                 if nat != None:
#                     await self.bot.remove_roles(user, nat)
#                 if yuri != None:
#                     await self.bot.remove_roles(user, yuri)
#                 if misao != None:
#                     await self.bot.remove_roles(user, misao)
#                 if sayori != None:
#                     await self.bot.remove_roles(user, sayori)
#                 if protag != None:
#                     await self.bot.remove_roles(user, protag)
#                 else:
#                     falsey = True
#                 if falsey == False:
#                     await self.bot.add_roles(user, moni)
#             else:
#                 await self.bot.say("An error occurred...")
#                 break

#     @commands.command(pass_context=True)
#     async def protag(self, ctx):
#         natsuki = ["369253424124133396","384447386153517056","390191979645894666"]          
#         monika = ["369253075137069057","396333414565019661","390191886108983306"]
#         yuri = ["369254043056472065","396333080886902795","390192874484006914"]
#         sayori = ["369261933343408129","396333588854997002","390191678859902987"]
#         misao = ["486963160201297920","396333868694896640","389540219835121684"]
#         protagonist = ["369254217015099414","460284706877865985","409462716432908299"]
#         norm = False
#         rare = False
#         legacy = False
#         server = ctx.message.server
#         user = server.get_member(ctx.message.author.id)
#         for role in user.roles:
#             while norm == False and rare == False and legacy == False:

#                 if role.id == monika[0]:
#                     norm = True
#                 if role.id == monika[1]:
#                     rare = True
#                 if role.id == monika[2]:
#                     legacy = True

#                 if role.id == sayori[0]:
#                     norm = True
#                 if role.id == sayori[1]:
#                     rare = True
#                 if role.id == sayori[2]:
#                     legacy = True

#                 if role.id == misao[0]:
#                     norm = True
#                 if role.id == misao[1]:
#                     rare = True
#                 if role.id == misao[2]:
#                     legacy = True

#                 if role.id == yuri[0]:
#                     norm = True
#                 if role.id == yuri[1]:
#                     rare = True
#                 if role.id == yuri[2]:
#                     legacy = True

#                 if role.id == natsuki[0]:
#                     norm = True
#                 if role.id == natsuki[1]:
#                     rare = True
#                 if role.id == natsuki[2]:
#                     legacy = True
#                 break
            
#             if norm == True:
#                 moni = None
#                 yuri = None
#                 sayori = None
#                 misao = None
#                 nat = None
#                 protag = None
#                 falsey = False
#                 for role in server.roles:
#                     if role.id == monika[0]:
#                         moni = role
#                     if role.id == natsuki[0]:
#                         nat = role
#                     if role.id == yuri[0]:
#                         yuri = role
#                     if role.id == misao[0]:
#                         misao = role
#                     if role.id == sayori[0]:
#                         sayori = role
#                     if role.id == protagonist[0]:
#                         protag = role
#                 if moni != None:
#                     await self.bot.remove_roles(user, moni)
#                 if nat != None:
#                     await self.bot.remove_roles(user, nat)
#                 if yuri != None:
#                     await self.bot.remove_roles(user, yuri)
#                 if misao != None:
#                     await self.bot.remove_roles(user, misao)
#                 if sayori != None:
#                     await self.bot.remove_roles(user, sayori)
#                 if protag != None:
#                     await self.bot.remove_roles(user, protag)
#                 else:
#                     falsey = True
#                 if falsey == False:
#                     await self.bot.add_roles(user, moni)
#             if rare == True:
#                 moni = None
#                 yuri = None
#                 sayori = None
#                 misao = None
#                 nat = None
#                 protag = None
#                 falsey = False
#                 for role in server.roles:
#                     if role.id == monika[1]:
#                         moni = role
#                     if role.id == natsuki[1]:
#                         nat = role
#                     if role.id == yuri[1]:
#                         yuri = role
#                     if role.id == misao[1]:
#                         misao = role
#                     if role.id == sayori[1]:
#                         sayori = role
#                     if role.id == protagonist[1]:
#                         protag = role
#                 if moni != None:
#                     await self.bot.remove_roles(user, moni)
#                 if nat != None:
#                     await self.bot.remove_roles(user, nat)
#                 if yuri != None:
#                     await self.bot.remove_roles(user, yuri)
#                 if misao != None:
#                     await self.bot.remove_roles(user, misao)
#                 if sayori != None:
#                     await self.bot.remove_roles(user, sayori)
#                 if protag != None:
#                     await self.bot.remove_roles(user, protag)
#                 else:
#                     falsey = True
#                 if falsey == False:
#                     await self.bot.add_roles(user, moni)
#             if legacy == True:
#                 moni = None
#                 yuri = None
#                 sayori = None
#                 misao = None
#                 nat = None
#                 protag = None
#                 falsey = False
#                 for role in server.roles:
#                     if role.id == monika[2]:
#                         moni = role
#                     if role.id == natsuki[2]:
#                         nat = role
#                     if role.id == yuri[2]:
#                         yuri = role
#                     if role.id == misao[2]:
#                         misao = role
#                     if role.id == sayori[2]:
#                         sayori = role
#                     if role.id == protagonist[2]:
#                         protag = role
#                 if moni != None:
#                     await self.bot.remove_roles(user, moni)
#                 if nat != None:
#                     await self.bot.remove_roles(user, nat)
#                 if yuri != None:
#                     await self.bot.remove_roles(user, yuri)
#                 if misao != None:
#                     await self.bot.remove_roles(user, misao)
#                 if sayori != None:
#                     await self.bot.remove_roles(user, sayori)
#                 if protag != None:
#                     await self.bot.remove_roles(user, protag)
#                 else:
#                     falsey = True
#                 if falsey == False:
#                     await self.bot.add_roles(user, moni)
#             else:
#                 await self.bot.say("An error occurred...")
#                 break

# def setup(bot):
#     bot.add_cog(Roles(bot))