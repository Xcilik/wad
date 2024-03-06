from pyrogram import Client, filters
import asyncio 
# Ganti dengan token bot Anda
API_ID = 21445722
API_HASH = "710f18f90849255dd85837d00d5fe85f"
BOT_TOKEN = "6976707406:AAE5RJn-W-H1NKGvkiu0EG3zH88LBiQYsN8"

app = Client("video_forward_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Fungsi untuk meneruskan video dari satu grup ke grup lainnya
async def forward_video(client, message):
    if message.video:
        await client.forward_messages(chat_id=-1001868635501, from_chat_id=message.chat.id, message_ids=message.message_id)
        await asyncio.sleep(1)

# Handler untuk menerima pesan video dan meneruskannya
@app.on_message(filters.command("gas") & filters.chat(-1001868635501) & filters.video)
async def handle_video(client, message):
    await forward_video(client, message)

# Menjalankan bot
app.run()
