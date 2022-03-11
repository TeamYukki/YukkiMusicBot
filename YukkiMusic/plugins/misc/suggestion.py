#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import asyncio
import random
from datetime import datetime, timedelta

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from config import clean
from strings import get_string
from YukkiMusic import app, userbot
from YukkiMusic.utils.database import get_lang, get_served_chats, is_active_chat

LEAVE_TIME = config.AUTO_LEAVE_ASSISTANT_TIME

strings = [
    {
        "markup": True,
        "cb": "SEARCHANSWER",
        "value": 1,
    },
    {
        "markup": True,
        "cb": "PLAYTYPEANSWER",
        "value": 2,
    },
    {
        "markup": True,
        "cb": "PLAYMODEANSWER",
        "value": 3,
    },
    {
        "markup": True,
        "cb": "AUTHANSWER",
        "value": 4,
    },
    {
        "markup": True,
        "cb": "CMANSWER",
        "value": 5,
    },
    {
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 6,
    },
    {
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 7,
    },
    {
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 8,
    },
    {
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 9,
    },
    {
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 10,
    },
    {
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 11,
    },
    {
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 12,
    },
    {
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 13,
    },
    {
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 14,
    },
    {
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 15,
    },
    {
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 16,
    },
    {
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 17,
    },
    {
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 18,
    },
    {
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 19,
    },
    {
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 20,
    },
    {
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 21,
    },
    {
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 22,
    },
    {
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 23,
    },
    {
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 24,
    },
    {
        "markup": True,
        "cb": "COMMANDANSWER",
        "value": 25,
    },
    {
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 26,
    },
]

suggestor = {}


async def dont_do_this():
    while not await asyncio.sleep(LEAVE_TIME):
        try:
            if config.AUTO_LEAVING_ASSISTANT == str(True):
                if config.STRING1:
                    async for i in userbot.one.iter_dialogs():
                        chat_type = i.chat.type
                        if chat_type in [
                            "supergroup",
                            "group",
                            "channel",
                        ]:
                            chat_id = i.chat.id
                            if (
                                chat_id != config.LOG_GROUP_ID
                                and chat_id != -1001190342892
                                and chat_id != -1001733534088
                                and chat_id != -1001443281821
                            ):
                                if not await is_active_chat(chat_id):
                                    try:
                                        await userbot.one.leave_chat(
                                            chat_id
                                        )
                                    except:
                                        continue
                if config.STRING2:
                    async for i in userbot.two.iter_dialogs():
                        chat_type = i.chat.type
                        if chat_type in [
                            "supergroup",
                            "group",
                            "channel",
                        ]:
                            chat_id = i.chat.id
                            if (
                                chat_id != config.LOG_GROUP_ID
                                and chat_id != -1001190342892
                                and chat_id != -1001733534088
                                and chat_id != -1001443281821
                            ):
                                if not await is_active_chat(chat_id):
                                    try:
                                        await userbot.two.leave_chat(
                                            chat_id
                                        )
                                    except:
                                        continue
                if config.STRING3:
                    async for i in userbot.three.iter_dialogs():
                        chat_type = i.chat.type
                        if chat_type in [
                            "supergroup",
                            "group",
                            "channel",
                        ]:
                            chat_id = i.chat.id
                            if (
                                chat_id != config.LOG_GROUP_ID
                                and chat_id != -1001190342892
                                and chat_id != -1001733534088
                                and chat_id != -1001443281821
                            ):
                                if not await is_active_chat(chat_id):
                                    try:
                                        await userbot.three.leave_chat(
                                            chat_id
                                        )
                                    except:
                                        continue
                if config.STRING4:
                    async for i in userbot.four.iter_dialogs():
                        chat_type = i.chat.type
                        if chat_type in [
                            "supergroup",
                            "group",
                            "channel",
                        ]:
                            chat_id = i.chat.id
                            if (
                                chat_id != config.LOG_GROUP_ID
                                and chat_id != -1001190342892
                                and chat_id != -1001733534088
                                and chat_id != -1001443281821
                            ):
                                if not await is_active_chat(chat_id):
                                    try:
                                        await userbot.four.leave_chat(
                                            chat_id
                                        )
                                    except:
                                        continue
                if config.STRING5:
                    async for i in userbot.five.iter_dialogs():
                        chat_type = i.chat.type
                        if chat_type in [
                            "supergroup",
                            "group",
                            "channel",
                        ]:
                            chat_id = i.chat.id
                            if (
                                chat_id != config.LOG_GROUP_ID
                                and chat_id != -1001190342892
                                and chat_id != -1001733534088
                                and chat_id != -1001443281821
                            ):
                                if not await is_active_chat(chat_id):
                                    try:
                                        await userbot.five.leave_chat(
                                            chat_id
                                        )
                                    except:
                                        continue
        except:
            pass
        try:
            if config.AUTO_SUGGESTION_MODE == str(True):
                chats = []
                schats = await get_served_chats()
                for chat in schats:
                    chats.append(int(chat["chat_id"]))
                total = len(chats)
                final = int(total / 10)
                if final < 10:
                    final = int(total)
                send_to = 0
                random.shuffle(chats)
                for x in chats:
                    if send_to == final:
                        break
                    if x == config.LOG_GROUP_ID:
                        continue
                    try:
                        language = await get_lang(x)
                        _ = get_string(language)
                    except:
                        _ = get_string("en")
                    string = random.choice(strings)
                    previous = suggestor.get(x)
                    if previous:
                        while previous == string["value"]:
                            string = random.choice(strings)
                    suggestor[x] = string["value"]
                    if string["markup"] is None:
                        try:
                            the_string = string["value"]
                            msg = _["sug_1"] + _[f"sug_{the_string + 2}"]
                            sent = await app.send_message(
                                x, msg
                            )
                            if x not in clean:
                                clean[x] = []
                            time_now = datetime.now()
                            put = {
                                "msg_id": sent.message_id,
                                "timer_after": time_now
                                + timedelta(
                                    minutes=config.CLEANMODE_DELETE_MINS
                                ),
                            }
                            clean[x].append(put)
                            send_to += 1
                        except:
                            pass
                    else:
                        key = InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton(
                                        text=_["sug_2"],
                                        callback_data=string["cb"],
                                    )
                                ]
                            ]
                        )
                        try:
                            the_string = string["value"]
                            msg = _["sug_1"] + _[f'sug_{the_string + 2}']
                            sent = await app.send_message(
                                x, msg, reply_markup=key
                            )
                            if x not in clean:
                                clean[x] = []
                            time_now = datetime.now()
                            put = {
                                "msg_id": sent.message_id,
                                "timer_after": time_now
                                + timedelta(
                                    minutes=config.CLEANMODE_DELETE_MINS
                                ),
                            }
                            clean[x].append(put)
                            send_to += 1
                        except:
                            pass
        except:
            pass


asyncio.create_task(dont_do_this())
