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
from YukkiMusic import app
from YukkiMusic.utils.database import get_lang, get_served_chats
from YukkiMusic.utils.database.mongodatabase import \
    get_private_served_chats

LEAVE_TIME = config.AUTO_SUGGESTION_TIME

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
        "markup": None,
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
        "value": 6,
    },
    {
        "markup": None,
        "value": 7,
    },
    {
        "markup": None,
        "value": 8,
    },
    {
        "markup": None,
        "value": 9,
    },
    {
        "markup": None,
        "value": 10,
    },
    {
        "markup": None,
        "value": 11,
    },
    {
        "markup": None,
        "value": 12,
    },
    {
        "markup": None,
        "value": 13,
    },
    {
        "markup": None,
        "value": 14,
    },
    {
        "markup": None,
        "value": 15,
    },
    {
        "markup": None,
        "value": 16,
    },
    {
        "markup": None,
        "value": 17,
    },
    {
        "markup": None,
        "value": 18,
    },
    {
        "markup": None,
        "value": 19,
    },
    {
        "markup": None,
        "value": 20,
    },
    {
        "markup": None,
        "value": 21,
    },
    {
        "markup": None,
        "value": 22,
    },
    {
        "markup": None,
        "value": 23,
    },
    {
        "markup": None,
        "value": 24,
    },
    {
        "markup": True,
        "cb": "COMMANDANSWER",
        "value": 25,
    },
    {
        "markup": None,
        "value": 26,
    },
    {
        "markup": None,
        "value": 27,
    },
]

suggestor = {}


async def dont_do_this():
    if config.AUTO_SUGGESTION_MODE == str(True):
        while not await asyncio.sleep(LEAVE_TIME):
            try:
                chats = []
                if config.PRIVATE_BOT_MODE == str(True):
                    schats = await get_private_served_chats()
                else:
                    schats = await get_served_chats()
                for chat in schats:
                    chats.append(int(chat["chat_id"]))
                total = len(chats)
                if total >= 100:
                    total //= 10
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
