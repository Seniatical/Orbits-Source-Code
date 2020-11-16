'''
    async def on_raw_reaction_add(self, payload):
        if payload.message_id == 746333872546906144 and payload.emoji.name == '✅':
            try:
                await payload.member.add_roles(discord.utils.get(self.get_guild(740523643980873789).roles, name='Supporters'))
            except AttributeError:
                return
        elif payload.message_id == 777184317628743689 and payload.emoji.name == '🔔':
            try:
                await payload.member.add_roles(discord.utils.get(self.get_guild(740523643980873789).roles, name='Ping'))
            except AttributeError:
                return
        elif payload.message_id == 777184317628743689 and payload.emoji.name == '📣':
            try:
                await payload.member.add_roles(discord.utils.get(self.get_guild(740523643980873789).roles, name='Announcements'))
            except AttributeError:
                return
        elif payload.message_id == 777184317628743689 and payload.emoji.name == '💝':
            try:
                await payload.member.add_roles(discord.utils.get(self.get_guild(740523643980873789).roles, name='Giveaways'))
            except AttributeError:
                return
        elif payload.message_id == 777184317628743689 and payload.emoji.name == '<:blobidea:745290075390083102>':
            try:
                await payload.member.add_roles(discord.utils.get(self.get_guild(740523643980873789).roles, name='Miscellaneous'))
            except AttributeError:
                return  
        else:
            return

    async def on_raw_reaction_remove(self, payload):
        if payload.message_id == 746333872546906144 and payload.emoji.name == '✅':
            try:
                for x in self.get_guild(payload.guild_id).members:
                    if x.id == payload.user_id:
                        await x.remove_roles(discord.utils.get(self.get_guild(740523643980873789).roles, name='Supporters'))
                        return
                return
            except AttributeError:
                return
        if payload.message_id == 777208106932240386 and payload.emoji.name == '🔔':
            try:
                for x in self.get_guild(payload.guild_id).members:
                    if x.id == payload.user_id:
                        await x.remove_roles(discord.utils.get(self.get_guild(740523643980873789).roles, name='Ping'))
                        return
                return
            except AttributeError:
                return
        if payload.message_id == 777208106932240386 and payload.emoji.name == '📣':
            try:
                for x in self.get_guild(payload.guild_id).members:
                    if x.id == payload.user_id:
                        await x.remove_roles(discord.utils.get(self.get_guild(740523643980873789).roles, name='Announcements'))
                        return
                return
            except AttributeError:
                return
        if payload.message_id == 777208106932240386 and payload.emoji.name == '💝':
            try:
                for x in self.get_guild(payload.guild_id).members:
                    if x.id == payload.user_id:
                        await x.remove_roles(discord.utils.get(self.get_guild(740523643980873789).roles, name='Giveaways'))
                        return
                return
            except AttributeError:
                return
        if payload.message_id == 777208106932240386 and payload.emoji.name == '<:blobidea:745290075390083102>':
            try:
                for x in self.get_guild(payload.guild_id).members:
                    if x.id == payload.user_id:
                        await x.remove_roles(discord.utils.get(self.get_guild(740523643980873789).roles, name='Miscellaneous'))
                        return
                return
            except AttributeError:
                return
        else:
            return
'''
'''
import  requests
from bs4 import BeautifulSoup

word = "scrape"
r = requests.get("http://www.urbandictionary.com/define.php?term={}".format(word))
soup = BeautifulSoup(r.content, 'html5lib')
print(soup.find("div",attrs={"class":"contributor"}).text)
print(soup.find("div",attrs={"class":"meaning"}).text)
print(soup.find("div",attrs={"class":"example"}).text)
print(soup.find("span",attrs={"class":"count"}).text)
'''
"""
Example:
Detect human faces from a webcam.
"""
'''
import cv2

cap = cv2.VideoCapture("videos/05-1.avi")
if not cap.isOpened():
    raise IOError("Cannot open webcam")
face_cascade = cv2.CascadeClassifier(
    "cascade_files/haarcascade_frontalface_alt.xml")
while True:
    ret, frame = cap.read()
    if not ret:
        break 
    face_rects = face_cascade.detectMultiScale(
        frame, scaleFactor=1.3, minNeighbors=3)
    for (x, y, w, h) in face_rects:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    cv2.imshow("Face Detector", frame)
    c = cv2.waitKey(30)
    if c == 27:
        break
cap.release()
'''
'''
import  requests
from bs4 import BeautifulSoup


r = requests.get("https://www.roblox.com/catalog/20573078/Shaggy")
soup = BeautifulSoup(r.content, 'html5lib')
price = soup.find("span",attrs={"class":"text-robux-lg wait-for-i18n-format-render"}).text
'''
import random
y = ['8','D']
x = random.randint(1, 10)
for i in range(x):
    y.insert(1, '=')
print(''.join(map(str, y)))


















