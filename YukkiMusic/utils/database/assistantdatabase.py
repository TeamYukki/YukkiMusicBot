#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import random

from YukkiMusic import userbot
from YukkiMusic.core.mongo import mongodb

db = mongodb.assistants

assistantdict = {}


async def get_client(assistant: int):
    if assistant == 1:
        return userbot.one
    elif assistant == 2:
        return userbot.two
    elif assistant == 3:
        return userbot.three
    elif assistant == 4:
        return userbot.four
    elif assistant == 5:
        return userbot.five


async def set_assistant(chat_id):
    from YukkiMusic.core.userbot import assistants

    ran_assistant = random.choice(assistants)
    assistantdict[chat_id] = ran_assistant
    await db.update_one(
        {"chat_id": chat_id},
        {"$set": {"assistant": ran_assistant}},
        upsert=True,
    )
    userbot = await get_client(ran_assistant)
    return userbot


async def get_assistant(chat_id: int) -> str:
    from YukkiMusic.core.userbot import assistants

    if assistant := assistantdict.get(chat_id):
        userbot = (
            await get_client(assistant)
            if assistant in assistants
            else await set_assistant(chat_id)
        )

    else:
        dbassistant = await db.find_one({"chat_id": chat_id})
        if not dbassistant:
            userbot = await set_assistant(chat_id)
        else:
            got_assis = dbassistant["assistant"]
            if got_assis in assistants:
                assistantdict[chat_id] = got_assis
                userbot = await get_client(got_assis)
            else:
                userbot = await set_assistant(chat_id)
    return userbot


async def set_calls_assistant(chat_id):
    from YukkiMusic.core.userbot import assistants

    ran_assistant = random.choice(assistants)
    assistantdict[chat_id] = ran_assistant
    await db.update_one(
        {"chat_id": chat_id},
        {"$set": {"assistant": ran_assistant}},
        upsert=True,
    )
    return ran_assistant


async def group_assistant(self, chat_id: int) -> int:
    from YukkiMusic.core.userbot import assistants

    if assistant := assistantdict.get(chat_id):
        assis = (
            assistant
            if assistant in assistants
            else await set_calls_assistant(chat_id)
        )

    else:
        dbassistant = await db.find_one({"chat_id": chat_id})
        if not dbassistant:
            assis = await set_calls_assistant(chat_id)
        else:
            assis = dbassistant["assistant"]
            if assis in assistants:
                assistantdict[chat_id] = assis
                assis = assis
            else:
                assis = await set_calls_assistant(chat_id)
    if int(assis) == 1:
        return self.one
    elif int(assis) == 2:
        return self.two
    elif int(assis) == 3:
        return self.three
    elif int(assis) == 4:
        return self.four
    elif int(assis) == 5:
        return self.five
