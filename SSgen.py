  
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
print.white.italic ("")
print.bold.blue ("")
print.red.italic (""" Wyline String Alıcıya Hoşgeldiniz SupportGroup:@wylinesupport""")

API_KEY = '1754367'
API_HASH = "231b8cc6cca12ee51a85cf543321f476"
while True:
  try:
   with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
      print("")
      session = client.session.save()
      client.send_message("me", f"**TELEGRAM STRING SESSION**👇\n(tap to copy) \n\n `{session}`\n\n\n ** Join to Win! >> @wylinesupport**")
      print("You Telegram String session Telegram Kayitli Mesajlariniza Gelmiştir Oraya Bakin  ")
      print("Store it safe!!")
  except:
   print ("")
   print ("Wrong telefon numaraniz \n Gelen Kodu Buraya Atınız...")
   print ("")
   continue
  break
