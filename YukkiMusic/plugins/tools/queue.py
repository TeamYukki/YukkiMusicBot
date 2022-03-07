#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import os
from random import randint

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from YukkiMusic import Carbon, app
from YukkiMusic.misc import db
from YukkiMusic.utils.database import (get_chatmode, get_cmode,
                                       is_active_chat)
from YukkiMusic.utils.decorators.language import language
from YukkiMusic.utils.pastebin import Yukkibin

###Commands
QUEUE_COMMAND = get_command("QUEUE_COMMAND")


@app.on_message(
    filters.command(QUEUE_COMMAND) & filters.group & ~BANNED_USERS
)
@language
async def ping_com(client, message: Message, _):
    if message.command[0][0] == "c":
        chat_id = await get_cmode(message.chat.id)
        if chat_id is None:
            return await message.reply_text(_["setting_12"])
        try:
            chat = await app.get_chat(chat_id)
        except:
            return await message.reply_text(_["cplay_4"])
        channel = chat.title
    else:
        chatmode = await get_chatmode(message.chat.id)
        if chatmode == "Group":
            chat_id = message.chat.id
            channel = None
        else:
            chat_id = await get_cmode(message.chat.id)
            try:
                chat = await app.get_chat(chat_id)
            except:
                return await message.reply_text(_["cplay_4"])
            channel = chat.title
    send = await message.reply_text(_["queue_1"])
    if await is_active_chat(chat_id):
        got = db.get(chat_id)
        if got:
            j = 0
            msg = ""
            for x in got:
                j += 1
                if j == 1:
                    msg += f'Currently Playing:\n\n🏷Title: {x["title"]}\nDur: {x["dur"]}\nBy: {x["by"]}\n\n'
                elif j == 2:
                    msg += f'Queued:\n\n🏷Title: {x["title"]}\nDur: {x["dur"]}\nBy: {x["by"]}\n\n'
                else:
                    msg += (
                        f'🏷Title: {x["title"]}\nDur: {x["dur"]}\nBy: {x["by"]}\n\n'
                    )
            if "Queued" in msg:
                link = await Yukkibin(msg)
                lines = msg.count("\n")
                if lines >= 23:
                    car = os.linesep.join(msg.split(os.linesep)[:23])
                else:
                    return await send.edit_text(msg)
                if "🏷" in car:
                    car = car.replace("🏷", "")
                carbon = await Carbon.generate(
                    car, randint(100, 10000000)
                )
                await message.reply_photo(
                    photo=carbon, caption=_["queue_3"].format(link)
                )
                await send.delete()
            else:
                await send.edit_text(msg)
        else:
            await send.edit_text(_["queue_2"])
    else:
        await send.edit_text(_["queue_2"])
