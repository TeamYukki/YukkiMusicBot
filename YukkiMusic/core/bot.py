#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import sys

from pyrogram import Client
from pyrogram.types import BotCommand

import config

from ..logging import LOGGER


class YukkiBot(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot")
        super().__init__(
            "YukkiMusicBot",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        try:
            await self.send_message(
                config.LOG_GROUP_ID, "Bot Started"
            )
        except:
            LOGGER(__name__).error(
                "Bot gagal akses grup, jadiin admin di ch maupun grup blok!"
            )
            sys.exit()
        if config.SET_CMDS == str(True):
            try:
                await self.set_bot_commands(
                    [
                        BotCommand("ping", "Check bot masih hidup apa mati"),
                        BotCommand("play", "Mulai lagu sesuai request lo pada"),
                        BotCommand("skip", "Skip ke lagu berikutnya"),
                        BotCommand("pause", "Menjeda lagu yang lagi diputer"),
                        BotCommand("resume", "Melanjutkan lagu yang dijeda"),
                        BotCommand("end", "Berentiin lagu yang udah mulai dan playlist berikutnya"),
                        BotCommand("shuffle", "Mulai lagu secara acak atau random."),
                        BotCommand("playmode", "Allows you to change the default playmode for your chat"),
                        BotCommand("settings", "Open the settings of the music bot for your chat.")
                        ]
                    )
            except:
                pass
        else:
            pass
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != "administrator":
            LOGGER(__name__).error(
                "⚠️ bot nya jadiin admin dong blok!"
            )
            sys.exit()
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        LOGGER(__name__).info(f"ᴡᴏʀsᴛ ᴘᴀʀᴛʏ ᴍᴜsɪᴄ Started as {self.name}")
