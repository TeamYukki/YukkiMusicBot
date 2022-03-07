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
from YukkiMusic import app, userbot
from YukkiMusic.utils.database import get_served_chats, is_active_chat

LEAVE_TIME = config.AUTO_LEAVE_ASSISTANT_TIME

BASE = "❓**Do You Know?**\n\n✅"
strings = [
    {
        "msg": f"{BASE} You can play music in two **search modes** i.e. Direct Mode and Inline Mode.\nChange modes via /playmode",
        "markup": "💡 More Information",
        "cb": "SEARCHANSWER",
        "value": 1,
    },
    {
        "msg": f"{BASE} You can play music in two **play types** i.e. Everyone Mode and Admins Mode.\nChange modes via /playmode",
        "markup": "💡 More Information",
        "cb": "PLAYTYPEANSWER",
        "value": 2,
    },
    {
        "msg": f"{BASE} You can play music in **channels** too.Set channel_id via /channelplay and change playing modes via /playmode",
        "markup": "💡 More Information",
        "cb": "PLAYMODEANSWER",
        "value": 3,
    },
    {
        "msg": f"{BASE} Non Admins can use admin commands too by adding them to** AUTH USERS LIST**. Add any user to auth list by /auth , remove with /unauth and check auth users via /authusers",
        "markup": "💡 More Information",
        "cb": "AUTHANSWER",
        "value": 4,
    },
    {
        "msg": f"{BASE} Bot has a feature called **Clean Mode**.\nIt deletes the bot's messages after {config.CLEANMODE_DELETE_MINS} Mins and ensures that  your chat remains clean.\nEnable or disable cleanmode from /settings [__Enabled by default__]",
        "markup": "💡 More Information",
        "cb": "CMANSWER",
        "value": 5,
    },
    {
        "msg": f"{BASE} You can play **Spotify** tracks and playlists too.\n\nStart playing now with /play [Spotify Link]",
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 6,
    },
    {
        "msg": f"{BASE} You can play **Apple Music** tracks and playlists too.\n\nStart playing now with /play [Apple Link]",
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 7,
    },
    {
        "msg": f"{BASE} You can play **Resso Music** tracks and playlists too.\n\nStart playing now with /play [Resso Link]",
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 8,
    },
    {
        "msg": f"{BASE} You can play **Sound Cloud** tracks and playlists too.\n\nStart playing now with /play [SoundCloud Link]",
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 9,
    },
    {
        "msg": f"{BASE} You can play **Videos** in voice chat via /vplay [Video Name] or /play -v [Video Name]",
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 10,
    },
    {
        "msg": f"{BASE} You can set **Audio Quality** of voice chat to Low, Medium or High.\n\nSet quality via /settings",
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 11,
    },
    {
        "msg": f"{BASE} You can set **Video Quality** of voice chat to Low, Medium or High.\n\nSet quality via /settings",
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 12,
    },
    {
        "msg": f"{BASE} You can check your **Statistics** on bot like Top 10 Played Tracks.\n\nGet Stats: /stats ",
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 13,
    },
    {
        "msg": f"{BASE} You can check **Group's Stats** on bot like Top 10 Played Tracks.\n\nGet Stats: /stats ",
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 14,
    },
    {
        "msg": f"{BASE} You can check bot's **Global Stats** like top 10 users, top 10 chats, top 10 tracks etc etc.\n\nCheck Stats: /stats ",
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 15,
    },
    {
        "msg": f"{BASE} You can now mute the music which is playing on voice chat.\n\nCommand: /mute",
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 16,
    },
    {
        "msg": f"{BASE} You can now unmute and mute the music which is playing on voice chat.\n\nCommand: /mute and /unmute",
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 17,
    },
    {
        "msg": f"{BASE} You can search the lyrics of musics with us too..\n\nCommand: /lyrics [Music Name]",
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 18,
    },
    {
        "msg": f"{BASE} You can download the music or video from the bot through Youtube.\n\nCommand: /song [Music Name]",
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 19,
    },
    {
        "msg": f"{BASE} You can get a complete list of my commands that i accept.\n\nCommand: /help",
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 20,
    },
    {
        "msg": f"{BASE} Bot has server-sided playlist option.\nYou can add music in your playlist and play them all together via /play",
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 21,
    },
    {
        "msg": f"{BASE} You can now shuffle the queued musics on the bot.\n\nCommand: /shuffle",
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 22,
    },
    {
        "msg": f"{BASE} You can check the queue of the musics.\n\nCommand: /queue",
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 23,
    },
    {
        "msg": f"{BASE} You can check my owner and sudo users who manage me.\n\nCommand: /sudolist",
        "markup": None,
        "cb": "SEARCHANSWER",
        "value": 24,
    },
    {
        "msg": f"{BASE} Bot has a feature called **Commands Delete Mode**. It deletes its executed commands automatically.\nEnable or disable deletemode from /settings [__Enabled by default__]",
        "markup": "💡 More Information",
        "cb": "COMMANDANSWER",
        "value": 25,
    },
    {
        "msg": f"{BASE} You can change language of the bot to available languages for easy understanding.\n\nCommand: /language",
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
                    string = random.choice(strings)
                    previous = suggestor.get(x)
                    if previous:
                        if previous == string["value"]:
                            string = random.choice(strings)
                            if previous == string["value"]:
                                string = random.choice(strings)
                    suggestor[x] = string["value"]
                    if string["markup"] is None:
                        try:
                            sent = await app.send_message(
                                x, string["msg"]
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
                                        text=string["markup"],
                                        callback_data=string["cb"],
                                    )
                                ]
                            ]
                        )
                        try:
                            sent = await app.send_message(
                                x, string["msg"], reply_markup=key
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
