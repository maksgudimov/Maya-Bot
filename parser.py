from telethon.sync import TelegramClient, events
from telethon.tl.types import Channel
import asyncio
api_id      = 123
api_hash    = "apikey"
 
mychan        = 'maya_test' # куда пересылать
channels     = ["maya_test", "artretail", "DigitalNorsoyan", "fcgretail", "fcgmedia", "PROfashionChannel", "DaniyaTkacheva", "fashionbusinessblog", "ROSTOVSHCHIKOV", "fashionprokachka", "frontfashion", "galina_krav", "fashionsoyuz", "rbcstyle", "minpromtorg_ru", "artretail", "legprom_review", "techfashiontech", "intertkan", "metodologiafashion", "profashion_rabota", "buyertimetoact", "fashion_shtab", "Hackingfashion", "matu_academy"] # откуда пересылать
 
BADTEXT = {} # исключения
 
client = TelegramClient('myApp15', api_id, api_hash)
print("[+] activate")
 
def to_lower(word: str):
    return word.lower()
   
@client.on(events.NewMessage(chats=channels))
async def my_event_handler(event: events.newmessage.NewMessage.Event):
    global BADTEXT
    message_text = event.raw_text
    message_text_lowered = event.raw_text.lower()  
    if not [element for element in BADTEXT if message_text_lowered.__contains__(element)]:
        await asyncio.sleep(0.5) #задержка
        await client.send_message(mychan, event.message)
           
with client:
    client.run_until_disconnected()
