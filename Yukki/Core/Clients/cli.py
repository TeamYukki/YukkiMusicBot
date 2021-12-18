from pyrogram import Client

from config import (API_HASH, API_ID, BOT_TOKEN, STRING1, STRING2, STRING3,
                    STRING4, STRING5)

app = Client(
    "YukkiMusicBot",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
)

ASS_CLI_1 = Client(STRING1, API_ID, API_HASH)
ASS_CLI_2 = Client(STRING2, API_ID, API_HASH)
ASS_CLI_3 = Client(STRING3, API_ID, API_HASH)
ASS_CLI_4 = Client(STRING4, API_ID, API_HASH)
ASS_CLI_5 = Client(STRING5, API_ID, API_HASH)
