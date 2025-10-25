# bot.py
import asyncio
from telethon import TelegramClient, events
from config import API_ID, API_HASH, SESSION_NAME, AUTO_REPLY_MESSAGE

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

@client.on(events.NewMessage(incoming=True, private=True))
async def handler_new_message(event):
    sender = await event.get_sender()
    if sender and not sender.bot:
        await asyncio.sleep(1) 
        await event.respond(AUTO_REPLY_MESSAGE)

if __name__ == '__main__':
    with client:
        client.run_until_disconnected()
