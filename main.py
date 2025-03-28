from pyrogram import Client, filters, idle
import asyncio 
from config import *
from pyrogram.errors import FloodWait
# Ganti dengan token bot Anda

app = Client("video_forward_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Fungsi untuk meneruskan video dari satu grup ke grup lainnya

loop = asyncio.get_event_loop()
# Handler untuk menerima pesan video dan meneruskannya 80


async def init():
    await app.start()


    @app.on_message(filters.command("gundul") )
    async def forward_videos(client, message):
        await message.reply("proses")
    # Ganti "nama_grup_tujuan" dengan nama atau ID grup tujuan
        for id in DATA:
            try:
                await app.copy_message(TO, FROM, id, caption="")
                await asyncio.sleep(3)
            except FloodWait as e:
               flood_time = e.value
               if flood_time > 200:
                  continue
               await asyncio.sleep(flood_time)
        
# Menjalankan bot
    print("[Bot Copy] - Started")
    await idle()



if __name__ == "__main__":
    loop.run_until_complete(init())
