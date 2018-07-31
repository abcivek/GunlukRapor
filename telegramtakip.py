import threading
import telegram
import os

def gonder():
    threading.Timer(60.0*60, gonder).start()
    os.system("py gunluktakip.py")
    with open("takip.txt") as f:
        metin = f.read()

    mytoken = "telegram api tokenınız"
    mychatid = "chat id'niz"  # Chat id için: https://api.telegram.org/bot<yourtoken>/getUpdates
    bot = telegram.Bot(token=mytoken)
    bot.send_message(chat_id=mychatid, text=metin)


gonder()
