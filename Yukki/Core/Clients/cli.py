from pyrogram import Client

from config import (API_HASH, API_ID, BOT_TOKEN, LOG_SESSION, STRING1, STRING2,
                    STRING3, STRING4, STRING5)

app = Client(
    "YukkiMusicBot",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
)


if not STRING1:
    ASS_CLI_1 = None
else:
    ASS_CLI_1 = Client(
        api_id=API_ID,
        api_hash=API_HASH,
        session_name=STRING1,
        plugins=dict(root="Yukki.Plugins.Multi-Assistant"),
    )


if not STRING2:
    ASS_CLI_2 = None
else:
    ASS_CLI_2 = Client(
        api_id=API_ID,
        api_hash=API_HASH,
        session_name=STRING2,
        plugins=dict(root="Yukki.Plugins.Multi-Assistant"),
    )


if not STRING3:
    ASS_CLI_3 = None
else:
    ASS_CLI_3 = Client(
        api_id=API_ID,
        api_hash=API_HASH,
        session_name=STRING3,
        plugins=dict(root="Yukki.Plugins.Multi-Assistant"),
    )


if not STRING4:
    ASS_CLI_4 = None
else:
    ASS_CLI_4 = Client(
        api_id=API_ID,
        api_hash=API_HASH,
        session_name=STRING4,
        plugins=dict(root="Yukki.Plugins.Multi-Assistant"),
    )


if not STRING5:
    ASS_CLI_5 = None
else:
    ASS_CLI_5 = Client(
        api_id=API_ID,
        api_hash=API_HASH,
        session_name=STRING5,
        plugins=dict(root="Yukki.Plugins.Multi-Assistant"),
    )


if not LOG_SESSION:
    LOG_CLIENT = None
else:
    LOG_CLIENT = Client(LOG_SESSION, API_ID, API_HASH)
