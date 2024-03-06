from pyrogram import Client, filters
import asyncio 
# Ganti dengan token bot Anda
API_ID = 21445722
API_HASH = "710f18f90849255dd85837d00d5fe85f"
BOT_TOKEN = "6976707406:AAE5RJn-W-H1NKGvkiu0EG3zH88LBiQYsN8"

app = Client("video_forward_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Fungsi untuk meneruskan video dari satu grup ke grup lainnya


# Handler untuk menerima pesan video dan meneruskannya 80

data = [12342, 12092, 12090, 12089, 12088, 12087, 12039, 12038, 12037, 12036, 12035, 12034, 12033, 11966, 11963, 11919, 11861, 11860, 11859, 11858, 11857, 11380, 11369, 11368, 11367, 11366, 11335, 11334, 11327, 11175, 10867, 10789, 10633, 10619, 10618, 10575, 10330, 10226, 10190, 10175, 10170, 10154, 10139, 10135, 10101, 10100, 9452, 9439, 9438, 9437, 9436, 9435, 9434, 9433, 9432, 9431, 9430, 9429, 9428, 9427, 9426, 9425, 9424, 9423, 9422, 9421, 9420, 9419, 9418, 9417, 9416, 9415, 9414, 9413, 9412, 9411, 9410, 9409, 9408, 9407, 9406, 9405, 9404, 9403, 9402, 9401, 9400, 9399, 9398, 9397, 9396, 9395, 9394, 9393, 9392, 9391, 9390, 9389, 9388, 9387, 9386, 9385, 9384, 9383, 9382, 9381, 9380, 9379, 9378, 9377, 9376, 9375, 9374, 9373, 9372, 9371, 9370, 9369, 9368, 9367, 9366, 9365, 9364, 9363, 9362, 9361, 9360, 9359, 9358, 9357, 9339, 9338, 9337, 9336, 9335, 9334, 9333, 9332, 9331, 9326, 9325, 9324, 9323, 9322, 9321, 9320, 9319, 9318, 9317, 9316, 9306, 9305, 9304, 9303, 9302, 9301, 9300, 9299, 9298, 9297, 9296, 9295, 9294, 9293, 9292, 9291, 9290, 9289, 9076, 9075, 9050, 9049, 9048, 9037, 9010, 9009, 9008, 8702, 8626, 8464, 7822, 7639, 7638, 7601, 7582, 7546, 7356, 7355, 7354, 7353, 7352, 7351, 7350, 7349, 7348, 7347, 7346, 7345, 7344, 7343, 7342, 7341, 7340, 7339, 7338, 7337, 7336, 7335, 7334, 7333, 7332, 7331, 7330, 7329, 7328, 7327, 7326, 7325, 7324, 7323, 7322, 7310, 7220, 7219, 7218, 7217, 7216, 7215, 7214, 7213, 7212, 7211, 7210, 7209, 7208, 7207, 7205, 7204, 7203, 7202, 7201, 7200, 7199, 7198, 7197, 7196, 7195, 7194, 7193, 7192, 7191, 7190, 7189, 7188, 7187, 7186, 7185, 7184, 7183, 7182, 7181, 7180, 7179, 7178, 7177, 7176, 7175, 7174, 7173, 7172, 7171, 7170, 7169, 7168, 7167, 7166, 7165, 7164, 7163, 7162, 6965, 6964, 6866, 6863, 6743, 6639, 6553, 6552, 6530, 6529, 6528, 6527, 6526, 6525, 6524, 6523, 6521, 6520, 6519, 6518, 6517, 6516, 6515, 6514, 6513, 6512, 6511, 6510, 6509, 6508, 6507, 6506, 6505, 6504, 6503, 6502, 6501, 6500, 6499, 6498, 6497, 6496, 6495, 6494, 6356, 6351, 6349, 6348, 6347, 6346, 6084, 5695, 5694, 5693, 5692, 5691, 5690, 5689, 5688, 5687, 5686, 5162, 5161, 5090, 5089, 5088, 5087, 5085, 5084, 5083, 5082, 5081, 5080, 5079, 5078, 5077, 5076, 5075, 5074, 5073, 5072, 5071, 5070, 5069, 5067, 5066, 5065, 5064, 5063, 5059, 5057, 5056, 5055, 5054, 5053, 5052, 5051, 5050, 5049, 5047, 5046, 4765, 4651, 4585, 4556, 4527, 4502, 4229, 4177, 4176, 4175, 4174, 4173, 4172, 4171, 4170, 4152, 4151, 4150, 4148, 4147, 4146, 4145, 4144, 4143, 4142, 4141, 4140, 4139, 4138, 4137, 4136, 4135, 4134, 4133, 4132, 4131, 4130, 4129, 4128, 4127, 4126, 4125, 4124, 4121, 4120, 4119, 4118, 4117, 4116, 4098, 4097, 4096, 4095, 4094, 4093, 3670, 3567, 3511, 3510, 3486, 3479, 3478, 3462, 3461, 3460, 3440, 3437, 3436, 3435, 3434, 3433, 3432, 3420, 3418, 3417, 3416, 3415, 3410, 3390, 3389, 3388, 3387, 3386, 3385, 3384, 3383, 3374, 3373, 3372, 3367, 3352, 3320, 3319, 3318, 3084, 3076, 2562, 2561, 2560, 2557, 2215, 2214, 2213, 2212, 2211, 2210, 2209, 2207, 2206, 2205, 2133, 2132, 2131, 2130, 2129, 2128, 2127, 2125, 2124, 2123, 2029, 2028, 2027, 2026, 2025, 2024, 2023, 2022, 2021, 2020, 1999, 1998, 1997, 1996, 1995, 1994, 1993, 1992, 1991, 1990, 1988, 1987, 1986, 1985, 1984, 1983, 1982, 1981, 1980, 1979, 1977, 1976, 1975, 1974, 1973, 1972, 1971, 1970, 1969, 1968, 1967, 1966, 1965, 1964, 1963, 1962, 1961, 1960, 1959, 1958, 1562, 1390, 1365, 1364, 1363, 1287, 1284, 1248, 1069, 1060, 1059, 1044, 843, 697, 696, 695, 694, 693, 692, 691, 690, 689, 688, 359, 335, 258]

@app.on_message(filters.command("gas") )
async def forward_videos(client, message):
    # Ganti "nama_grup_tujuan" dengan nama atau ID grup tujuan
    for id in data:
        await app.forward_messages(-1002089478686, -1001868635501, id)
        await asyncio.sleep(1)
# Menjalankan bot
app.run()
