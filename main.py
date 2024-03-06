from pyrogram import Client, filters
import asyncio 
# Ganti dengan token bot Anda
API_ID = 21445722
API_HASH = "710f18f90849255dd85837d00d5fe85f"
BOT_TOKEN = "6976707406:AAE5RJn-W-H1NKGvkiu0EG3zH88LBiQYsN8"

app = Client("video_forward_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Fungsi untuk meneruskan video dari satu grup ke grup lainnya


# Handler untuk menerima pesan video dan meneruskannya 80


@app.on_message(filters.chat(-1001868635501) & filters.video)
async def forward_videos(client, message):
    # Ganti "nama_grup_tujuan" dengan nama atau ID grup tujuan
    await message.forward(chat_id=-1002089478686)
    await asyncio.sleep(1)
# Menjalankan bot
app.run()
