#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import asyncio
from datetime import datetime, timedelta

from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.raw import types

import config
from config import adminlist, chatstats, clean, userstats
from strings import get_command
from YukkiMusic import app, userbot
from YukkiMusic.misc import SUDOERS
from YukkiMusic.utils.database import (get_active_chats,
                                       get_authuser_names,
                                       get_particular_top,
                                       get_queries, get_served_chats,
                                       get_served_users, get_user_top,
                                       is_cleanmode_on, set_queries,
                                       update_particular_top,
                                       update_user_top)
from YukkiMusic.utils.decorators.language import language
from YukkiMusic.utils.formatters import alpha_to_int

BROADCAST_COMMAND = get_command("BROADCAST_COMMAND")
AUTO_DELETE = config.CLEANMODE_DELETE_MINS
AUTO_SLEEP = 5
IS_BROADCASTING = False
cleanmode_group = 15


@app.on_raw_update(group=cleanmode_group)
async def clean_mode(client, update, users, chats):
    global IS_BROADCASTING
    if IS_BROADCASTING:
        return
    try:
        if not isinstance(update, types.UpdateReadChannelOutbox):
            return
    except:
        return
    message_id = update.max_id
    chat_id = int(f"-100{update.channel_id}")
    if not await is_cleanmode_on(chat_id):
        return
    if chat_id not in clean:
        clean[chat_id] = []
    time_now = datetime.now()
    put = {
        "msg_id": message_id,
        "timer_after": time_now + timedelta(minutes=AUTO_DELETE),
    }
    clean[chat_id].append(put)
    await get_queries()
    await set_queries(1)


@app.on_message(filters.command(BROADCAST_COMMAND) & SUDOERS)
@language
async def braodcast_message(client, message, _):
    global IS_BROADCASTING
    if message.reply_to_message:
        x = message.reply_to_message.message_id
        y = message.chat.id
        sent = 0
        pin = 0
        chats = []
        schats = await get_served_chats()
        for chat in schats:
            chats.append(int(chat["chat_id"]))
        IS_BROADCASTING = True
        if "-nobot" not in message.text:
            for i in chats:
                try:
                    m = await app.forward_messages(i, y, x)
                    if "-pin" in message.text:
                        try:
                            await m.pin(disable_notification=True)
                            pin += 1
                        except Exception:
                            pass
                    elif "-pinloud" in message.text:
                        try:
                            await m.pin(disable_notification=False)
                            pin += 1
                        except Exception:
                            pass
                    sent += 1
                except FloodWait as e:
                    await asyncio.sleep(e.x)
                except Exception:
                    pass
            try:
                await message.reply_text(
                    _["broad_1"].format(sent, pin)
                )
            except:
                pass
        if "-user" in message.text:
            susr = 0
            served_users = []
            susers = await get_served_users()
            for user in susers:
                served_users.append(int(user["user_id"]))
            for i in served_users:
                try:
                    m = await app.forward_messages(i, y, x)
                    susr += 1
                except FloodWait as e:
                    await asyncio.sleep(e.x)
                except Exception:
                    pass
            try:
                await message.reply_text(_["broad_11"].format(susr))
            except:
                pass
        if "-assistant" in message.text:
            aw = await message.reply_text(_["broad_2"])
            s1 = 0
            s2 = 0
            s3 = 0
            s4 = 0
            s5 = 0
            text = _["broad_3"]
            if config.STRING1:
                async for dialog in userbot.one.iter_dialogs():
                    try:
                        m = await userbot.one.forward_messages(
                            dialog.chat.id, y, x
                        )
                        s1 += 1
                    except FloodWait as e:
                        await asyncio.sleep(e.x)
                    except Exception:
                        continue
                text += _["broad_4"].format(s1)
            if config.STRING2:
                async for dialog in userbot.two.iter_dialogs():
                    try:
                        m = await userbot.two.forward_messages(
                            dialog.chat.id, y, x
                        )
                        s2 += 1
                    except FloodWait as e:
                        await asyncio.sleep(e.x)
                    except Exception:
                        continue
                text += _["broad_5"].format(s2)
            if config.STRING3:
                async for dialog in userbot.three.iter_dialogs():
                    try:
                        m = await userbot.three.forward_messages(
                            dialog.chat.id, y, x
                        )
                        s3 += 1
                    except FloodWait as e:
                        await asyncio.sleep(e.x)
                    except Exception:
                        continue
                text += _["broad_6"].format(s3)
            if config.STRING4:
                async for dialog in userbot.four.iter_dialogs():
                    try:
                        m = await userbot.four.forward_messages(
                            dialog.chat.id, y, x
                        )
                        s4 += 1
                    except FloodWait as e:
                        await asyncio.sleep(e.x)
                    except Exception:
                        continue
                text += _["broad_7"].format(s4)
            if config.STRING5:
                async for dialog in userbot.five.iter_dialogs():
                    try:
                        m = await userbot.five.forward_messages(
                            dialog.chat.id, y, x
                        )
                        s5 += 1
                    except FloodWait as e:
                        await asyncio.sleep(e.x)
                    except Exception:
                        continue
                text += _["broad_8"].format(s5)
            try:
                await aw.edit_text(text)
            except:
                pass
        IS_BROADCASTING = False
    else:
        if len(message.command) < 2:
            return await message.reply_text(_["broad_9"])
        query = message.text.split(None, 1)[1]
        if "-pin" in query:
            query = query.replace("-pin", "")
        if "-nobot" in query:
            query = query.replace("-nobot", "")
        if "-pinloud" in query:
            query = query.replace("-pinloud", "")
        if "-assistant" in query:
            query = query.replace("-assistant", "")
        if "-user" in query:
            query = query.replace("-user", "")
        if query == "":
            return await message.reply_text(_["broad_10"])
        sent = 0
        pin = 0
        chats = []
        schats = await get_served_chats()
        for chat in schats:
            chats.append(int(chat["chat_id"]))
        IS_BROADCASTING = True
        if "-nobot" not in message.text:
            for i in chats:
                try:
                    m = await app.send_message(i, text=query)
                    if "-pin" in message.text:
                        try:
                            await m.pin(disable_notification=True)
                            pin += 1
                        except Exception:
                            pass
                    elif "-pinloud" in message.text:
                        try:
                            await m.pin(disable_notification=False)
                            pin += 1
                        except Exception:
                            pass
                    sent += 1
                except FloodWait as e:
                    await asyncio.sleep(e.x)
                except Exception:
                    pass
            try:
                await message.reply_text(
                    _["broad_1"].format(sent, pin)
                )
            except:
                pass
        if "-user" in message.text:
            susr = 0
            served_users = []
            susers = await get_served_users()
            for user in susers:
                served_users.append(int(user["user_id"]))
            for i in served_users:
                try:
                    m = await app.send_message(i, text=query)
                    susr += 1
                except FloodWait as e:
                    await asyncio.sleep(e.x)
                except Exception:
                    pass
            try:
                await message.reply_text(_["broad_11"].format(susr))
            except:
                pass
        if "-assistant" in message.text:
            aw = await message.reply_text(_["broad_2"])
            s1 = 0
            s2 = 0
            s3 = 0
            s4 = 0
            s5 = 0
            text = _["broad_3"]
            if config.STRING1:
                async for dialog in userbot.one.iter_dialogs():
                    try:
                        m = await userbot.one.send_message(
                            dialog.chat.id, text=query
                        )
                        s1 += 1
                    except FloodWait as e:
                        await asyncio.sleep(e.x)
                    except Exception:
                        continue
                text += _["broad_4"].format(s1)
            if config.STRING2:
                async for dialog in userbot.two.iter_dialogs():
                    try:
                        m = await userbot.two.send_message(
                            dialog.chat.id, text=query
                        )
                        s2 += 1
                    except FloodWait as e:
                        await asyncio.sleep(e.x)
                    except Exception:
                        continue
                text += _["broad_5"].format(s2)
            if config.STRING3:
                async for dialog in userbot.three.iter_dialogs():
                    try:
                        m = await userbot.three.send_message(
                            dialog.chat.id, text=query
                        )
                        s3 += 1
                    except FloodWait as e:
                        await asyncio.sleep(e.x)
                    except Exception:
                        continue
                text += _["broad_6"].format(s3)
            if config.STRING4:
                async for dialog in userbot.four.iter_dialogs():
                    try:
                        m = await userbot.four.send_message(
                            dialog.chat.id, text=query
                        )
                        s4 += 1
                    except FloodWait as e:
                        await asyncio.sleep(e.x)
                    except Exception:
                        continue
                text += _["broad_7"].format(s4)
            if config.STRING5:
                async for dialog in userbot.five.iter_dialogs():
                    try:
                        m = await userbot.five.send_message(
                            dialog.chat.id, text=query
                        )
                        s5 += 1
                    except FloodWait as e:
                        await asyncio.sleep(e.x)
                    except Exception:
                        continue
                text += _["broad_8"].format(s5)
            try:
                await aw.edit_text(text)
            except:
                pass
        IS_BROADCASTING = False


async def auto_clean():
    while not await asyncio.sleep(AUTO_SLEEP):
        try:
            for chat_id in chatstats:
                for dic in chatstats[chat_id]:
                    vidid = dic["vidid"]
                    title = dic["title"]
                    chatstats[chat_id].pop(0)
                    spot = await get_particular_top(chat_id, vidid)
                    if spot:
                        spot = spot["spot"]
                        next_spot = spot + 1
                        new_spot = {"spot": next_spot, "title": title}
                        await update_particular_top(
                            chat_id, vidid, new_spot
                        )
                    else:
                        next_spot = 1
                        new_spot = {"spot": next_spot, "title": title}
                        await update_particular_top(
                            chat_id, vidid, new_spot
                        )
            for user_id in userstats:
                for dic in userstats[user_id]:
                    vidid = dic["vidid"]
                    title = dic["title"]
                    userstats[user_id].pop(0)
                    spot = await get_user_top(user_id, vidid)
                    if spot:
                        spot = spot["spot"]
                        next_spot = spot + 1
                        new_spot = {"spot": next_spot, "title": title}
                        await update_user_top(
                            user_id, vidid, new_spot
                        )
                    else:
                        next_spot = 1
                        new_spot = {"spot": next_spot, "title": title}
                        await update_user_top(
                            user_id, vidid, new_spot
                        )
        except:
            pass
        try:
            for chat_id in clean:
                if chat_id == config.LOG_GROUP_ID:
                    continue
                for x in clean[chat_id]:
                    if datetime.now() > x["timer_after"]:
                        try:
                            await app.delete_messages(
                                chat_id, x["msg_id"]
                            )
                        except FloodWait as e:
                            await asyncio.sleep(e.x)
                        except:
                            pass
                    else:
                        continue
        except:
            pass
        try:
            served_chats = await get_active_chats()
            for chat_id in served_chats:
                if chat_id not in adminlist:
                    adminlist[chat_id] = []
                    admins = await app.get_chat_members(
                        chat_id, filter="administrators"
                    )
                    for user in admins:
                        if user.can_manage_voice_chats:
                            adminlist[chat_id].append(user.user.id)
                    authusers = await get_authuser_names(chat_id)
                    for user in authusers:
                        user_id = await alpha_to_int(user)
                        adminlist[chat_id].append(user_id)
        except:
            pass


asyncio.create_task(auto_clean())
