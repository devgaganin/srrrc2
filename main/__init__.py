#Github.com/devgaganin

from pyrogram import Client, filters
from pyrogram.types import Message

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging
import time
import sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = "26075120"
API_HASH = "1fda88a5d1de46058a4791c78bce198e"
BOT_TOKEN = "6468925244:AAHFq2wDZtw3Jc9YoL3D3ESiAMvB0lQbA6o"
SESSION = "BAA62LZMclzNoSFGROSO_FGKFEIcEH4cBqWV0wFpwxR2xX0lRtYCXwTTueKvFgbLUqAlSDBNnbuUnnH53QS9AD_QEQZ4iUID9tc8bL4xwA89nzuFfFdCwXY8d-xL0NYh-puvjaX_hvG55IzXaDO56P1aglxkN_ZRiNK6hFvP8yNRQAKTuxdgC8NCqhOD3jO54_lUZVtknY8plntxuf3P9E5LgvPXCJLk-SShqDS1iNsX5F91XlqPDy9SooxDiXr1Gk7iBhAWMkBwu6egW3fz5nzkn6aonG3KoMoShvLiRBaalE2KSH7iDSWjS_0niAZomJRbUWj_8UjwtZPWgh12GlGoAAAAAYSLfM0A"
FORCESUB = "dev_gagan"
AUTH = "6876018655"
SUDO_USERS = []
if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

#userbot = Client(
#    session_name=SESSION, 
#    api_hash=API_HASH, 
#    api_id=API_ID)
userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
