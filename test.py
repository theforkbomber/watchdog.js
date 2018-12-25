>os.run
def chooser(userid):
    numbered = int(userid[len(userid)-3:len(userid)])
    if numbered < 166:
        return "Y"
    elif 166 <= numbered < 166*2:
        return"N"
    elif 166*2 <= numbered < 166*3:
        return"Mi"
    elif 166*3 <= numbered < 166*4:
        return"S"
    elif 166*4 <= numbered < 166*5:
        return"M"
    elif 166*5 <= numbered < 999:
        return"D"
server = bot.get_server("369252350927306752")
sayori, dan, natsuki, monika, misao, yuri == [],[],[],[],[],[]
for x in server.members:
    c = chooser(x.id)
    if c == "M":
        monika.append(x.name)
    elif c == "N":
        natsuki.append(x.name)
    elif c == "D":
        dan.append(x.name)
    elif c == "Mi":
        misao.append(x.name)
    elif c == "Y":
        yuri.append(x.name)
    elif c == "S":
        sayori.append(x.name)
print(f"Yuris: {len(yuri)}\nMonikas: {len(monika)}\nSayoris: {len(sayori)}\nNatsukis: {len(natsuki)}\nMisaos: {len(misao)}\nDans: {len(dan)}")