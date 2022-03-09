#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import platform
from sys import version as pyver
from typing import Union

import psutil
from pyrogram import __version__ as pyrover
from pyrogram import filters, types
from pyrogram.errors import MessageIdInvalid
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto)

import config
from config import BANNED_USERS, MUSIC_BOT_NAME
from strings import get_command, get_string
from YukkiMusic import YouTube, app
from YukkiMusic.core.userbot import assistants
from YukkiMusic.misc import SUDOERS, pymongodb
from YukkiMusic.utils.database import (get_global_tops, get_lang,
                                       get_particulars, get_queries,
                                       get_served_chats,
                                       get_served_users, get_sudoers,
                                       get_top_chats, get_topp_users,
                                       is_commanddelete_on)
from YukkiMusic.utils.decorators.language import languageCB
from YukkiMusic.utils.inline.stats import (back_stats_markup,
                                           overallback_stats_markup,
                                           top_ten_stats_markup)

# Commands
STATS_COMMAND = get_command("STATS_COMMAND")


@app.on_message(
    filters.command(STATS_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@app.on_callback_query(filters.regex("GlobalStats") & ~BANNED_USERS)
async def stats_global(
    client: app, update: Union[types.Message, types.CallbackQuery]
):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except:
            pass
        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        mystic = await update.edit_message_text(_["set_cb_8"])
    else:
        chat_id = update.chat.id
        if await is_commanddelete_on(update.chat.id):
            try:
                await update.delete()
            except:
                pass
        language = await get_lang(chat_id)
        _ = get_string(language)
        mystic = await update.reply_text(_["gstats_1"])
    stats = await get_global_tops()
    if not stats:
        return await mystic.edit(_["gstats_2"])
    results = {}
    for i in stats:
        top_list = stats[i]["spot"]
        results[str(i)] = top_list
        list_arranged = dict(
            sorted(
                results.items(),
                key=lambda item: item[1],
                reverse=True,
            )
        )
    if not results:
        return await mystic.edit(_["gstats_2"])
    videoid = None
    co = None
    for vidid, count in list_arranged.items():
        if vidid == "telegram":
            continue
        else:
            videoid = vidid
            co = count
        break
    (
        title,
        duration_min,
        duration_sec,
        thumbnail,
        vidid,
    ) = await YouTube.details(videoid, True)
    title = title.title()
    final = f"Top Most Played Track on {MUSIC_BOT_NAME}\n\n**Title:** {title}\n\nPlayed** {co} **times"
    not_sudo = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"],
            callback_data="close",
        )
    ]
    sudo = [
        InlineKeyboardButton(
            text=_["SA_B_8"],
            callback_data="bot_stats_sudo",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"],
            callback_data="close",
        ),
    ]
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["SA_B_7"],
                    callback_data="TOPMARKUPGET",
                )
            ],
            [
                InlineKeyboardButton(
                    text=_["SA_B_6"],
                    url=f"https://t.me/{app.username}?start=stats",
                ),
                InlineKeyboardButton(
                    text=_["SA_B_5"],
                    callback_data="TopOverall",
                ),
            ],
            sudo if update.from_user.id in SUDOERS else not_sudo,
        ]
    )
    if is_callback:
        med = InputMediaPhoto(media=thumbnail, caption=final)
        try:
            await update.edit_message_media(
                media=med, reply_markup=upl
            )
        except:
            await update.message.reply_photo(
                photo=thumbnail, caption=final, reply_markup=upl
            )
    else:
        await app.send_photo(
            chat_id, photo=thumbnail, caption=final, reply_markup=upl
        )
        await mystic.delete()


@app.on_callback_query(filters.regex("TOPMARKUPGET") & ~BANNED_USERS)
@languageCB
async def too_ten_reply(client, CallbackQuery, _):
    try:
        await CallbackQuery.answer()
    except:
        pass
    upl = top_ten_stats_markup(_)
    med = InputMediaPhoto(
        media=config.GLOBAL_IMG_URL,
        caption=_["tops_10"],
    )
    try:
        await CallbackQuery.edit_message_media(
            media=med, reply_markup=upl
        )
    except MessageIdInvalid:
        await CallbackQuery.message.reply_photo(
            photo=config.GLOBAL_IMG_URL,
            caption=_["tops_10"],
            reply_markup=upl,
        )


@app.on_callback_query(filters.regex("TopOverall") & ~BANNED_USERS)
@languageCB
async def overall_stats(client, CallbackQuery, _):
    upl = overallback_stats_markup(_)
    try:
        await CallbackQuery.answer()
    except:
        pass
    await CallbackQuery.edit_message_text(_["tops_9"])
    served_chats = len(await get_served_chats())
    served_users = len(await get_served_users())
    total_queries = await get_queries()
    blocked = len(BANNED_USERS)
    sudoers = len(SUDOERS)
    assistant = len(assistants)
    playlist_limit = config.SERVER_PLAYLIST_LIMIT
    fetch_playlist = config.PLAYLIST_FETCH_LIMIT
    song = config.SONG_DOWNLOAD_DURATION
    play_duration = config.DURATION_LIMIT_MIN
    if config.AUTO_LEAVING_ASSISTANT == str(True):
        ass = "Yes"
    else:
        ass = "No"
    cm = config.CLEANMODE_DELETE_MINS
    text = f"""**Bot's Stats and Information:**

**Served Chats:** {served_chats} 
**Served Users:** {served_users} 
**Blocked Users:** {blocked} 
**Sudo Users:** {sudoers} 
    
**Total Queries:** {total_queries} 
**Total Assistants:** {assistant}
**Auto Leaving Assistant:** {ass}
**Cleanmode duration:** {cm} Mins

**Play Duration Limit:** {play_duration} Mins
**Song Download Limit:** {song} Mins
**Bot's Server Playlist Limit:** {playlist_limit}
**Playlist Play Limit:** {fetch_playlist}"""
    med = InputMediaPhoto(media=config.STATS_IMG_URL, caption=text)
    try:
        await CallbackQuery.edit_message_media(
            media=med, reply_markup=upl
        )
    except MessageIdInvalid:
        await CallbackQuery.message.reply_photo(
            photo=config.STATS_IMG_URL, caption=text, reply_markup=upl
        )


@app.on_callback_query(filters.regex("TopUsers") & ~BANNED_USERS)
@languageCB
async def top_users_ten(client, CallbackQuery, _):
    upl = back_stats_markup(_)
    try:
        await CallbackQuery.answer()
    except:
        pass
    mystic = await CallbackQuery.edit_message_text(_["tops_4"])
    stats = await get_topp_users()
    if not stats:
        return await mystic.edit(_["tops_2"], reply_markup=upl)
    msg = ""
    limit = 0
    results = {}
    for i in stats:
        top_list = stats[i]
        results[str(i)] = top_list
        list_arranged = dict(
            sorted(
                results.items(),
                key=lambda item: item[1],
                reverse=True,
            )
        )
    if not results:
        return await mystic.edit(_["tops_2"], reply_markup=upl)
    for user, count in list_arranged.items():
        if limit > 9:
            limit += 1
            break
        try:
            user = (await app.get_users(user)).first_name
            if user is None:
                continue
        except:
            continue
        limit += 1
        msg += f"🔗`{user}` played {count} times on bot.\n\n"
    if limit == 0:
        return await mystic.edit(_["tops_2"], reply_markup=upl)
    msg = _["tops_5"].format(limit, MUSIC_BOT_NAME) + msg
    med = InputMediaPhoto(media=config.GLOBAL_IMG_URL, caption=msg)
    try:
        await CallbackQuery.edit_message_media(
            media=med, reply_markup=upl
        )
    except MessageIdInvalid:
        await CallbackQuery.message.reply_photo(
            photo=config.GLOBAL_IMG_URL, caption=msg, reply_markup=upl
        )


@app.on_callback_query(filters.regex("TopChats") & ~BANNED_USERS)
@languageCB
async def top_ten_chats(client, CallbackQuery, _):
    upl = back_stats_markup(_)
    try:
        await CallbackQuery.answer()
    except:
        pass
    mystic = await CallbackQuery.edit_message_text(_["tops_1"])
    stats = await get_top_chats()
    if not stats:
        return await mystic.edit(_["tops_2"], reply_markup=upl)
    msg = ""
    limit = 0
    results = {}
    for i in stats:
        top_list = stats[i]
        results[str(i)] = top_list
        list_arranged = dict(
            sorted(
                results.items(),
                key=lambda item: item[1],
                reverse=True,
            )
        )
    if not results:
        return await mystic.edit(_["tops_2"], reply_markup=upl)
    for chat, count in list_arranged.items():
        if limit > 9:
            limit += 1
            break
        try:
            title = (await app.get_chat(chat)).title
            if title is None:
                continue
        except:
            continue
        limit += 1
        msg += f"🔗`{title}` played {count} times on bot.\n\n"
    if limit == 0:
        return await mystic.edit(_["tops_2"], reply_markup=upl)
    if limit <= 10:
        limit = 10
    msg = _["tops_3"].format(limit, MUSIC_BOT_NAME) + msg
    med = InputMediaPhoto(media=config.GLOBAL_IMG_URL, caption=msg)
    try:
        await CallbackQuery.edit_message_media(
            media=med, reply_markup=upl
        )
    except MessageIdInvalid:
        await CallbackQuery.message.reply_photo(
            photo=config.GLOBAL_IMG_URL, caption=msg, reply_markup=upl
        )


@app.on_callback_query(filters.regex("TopStats") & ~BANNED_USERS)
@languageCB
async def top_fif_stats(client, CallbackQuery, _):
    upl = back_stats_markup(_)
    try:
        await CallbackQuery.answer()
    except:
        pass
    mystic = await CallbackQuery.edit_message_text(_["tops_7"])
    stats = await get_global_tops()
    tot = len(stats)
    if tot > 10:
        tracks = 10
    else:
        tracks = tot
    queries = await get_queries()
    if not stats:
        return await mystic.edit(_["tops_2"], reply_markup=upl)
    msg = ""
    limit = 0
    results = {}
    for i in stats:
        top_list = stats[i]["spot"]
        results[str(i)] = top_list
        list_arranged = dict(
            sorted(
                results.items(),
                key=lambda item: item[1],
                reverse=True,
            )
        )
    if not results:
        return await mystic.edit(_["tops_2"], reply_markup=upl)
    total_count = 0
    for vidid, count in list_arranged.items():
        total_count += count
        if limit > 9:
            continue
        limit += 1
        details = stats.get(vidid)
        title = (details["title"][:35]).title()
        if vidid == "telegram":
            msg += f"🔗[Telegram Files and Audios](https://t.me/telegram) ** played {count} times**\n\n"
        else:
            msg += f"🔗 [{title}](https://www.youtube.com/watch?v={vidid}) ** played {count} times**\n\n"
    final = (
        _["gstats_3"].format(
            queries, config.MUSIC_BOT_NAME, tot, total_count, tracks
        )
        + msg
    )
    med = InputMediaPhoto(media=config.GLOBAL_IMG_URL, caption=final)
    try:
        await CallbackQuery.edit_message_media(
            media=med, reply_markup=upl
        )
    except MessageIdInvalid:
        await CallbackQuery.message.reply_photo(
            photo=config.GLOBAL_IMG_URL,
            caption=final,
            reply_markup=upl,
        )


@app.on_callback_query(filters.regex("TopHere") & ~BANNED_USERS)
@languageCB
async def top_here(client, CallbackQuery, _):
    chat_id = CallbackQuery.message.chat.id
    upl = back_stats_markup(_)
    try:
        await CallbackQuery.answer()
    except:
        pass
    mystic = await CallbackQuery.edit_message_text(_["tops_6"])
    stats = await get_particulars(chat_id)
    tot = len(stats)
    if tot > 10:
        tracks = 10
    else:
        tracks = tot
    if not stats:
        return await mystic.edit(_["tops_2"], reply_markup=upl)
    msg = ""
    limit = 0
    results = {}
    for i in stats:
        top_list = stats[i]["spot"]
        results[str(i)] = top_list
        list_arranged = dict(
            sorted(
                results.items(),
                key=lambda item: item[1],
                reverse=True,
            )
        )
    if not results:
        return await mystic.edit(_["tops_2"], reply_markup=upl)
    total_count = 0
    for vidid, count in list_arranged.items():
        total_count += count
        if limit > 9:
            continue
        limit += 1
        details = stats.get(vidid)
        title = (details["title"][:35]).title()
        if vidid == "telegram":
            msg += f"🔗[Telegram Files and Audios](https://t.me/telegram) ** played {count} times**\n\n"
        else:
            msg += f"🔗 [{title}](https://www.youtube.com/watch?v={vidid}) ** played {count} times**\n\n"
    msg = _["tops_8"].format(tot, total_count, tracks) + msg
    med = InputMediaPhoto(media=config.GLOBAL_IMG_URL, caption=msg)
    try:
        await CallbackQuery.edit_message_media(
            media=med, reply_markup=upl
        )
    except MessageIdInvalid:
        await CallbackQuery.message.reply_photo(
            photo=config.GLOBAL_IMG_URL, caption=msg, reply_markup=upl
        )


@app.on_callback_query(filters.regex("bot_stats_sudo") & SUDOERS)
@languageCB
async def overall_stats(client, CallbackQuery, _):
    upl = overallback_stats_markup(_)
    try:
        await CallbackQuery.answer(
            "Getting Bot's Stats Master..\n\nPlease Hold on!"
        )
    except:
        pass
    await CallbackQuery.edit_message_text(_["tops_9"])
    sc = platform.system()
    p_core = psutil.cpu_count(logical=False)
    t_core = psutil.cpu_count(logical=True)
    ram = (
        str(round(psutil.virtual_memory().total / (1024.0**3)))
        + " GB"
    )
    try:
        cpu_freq = psutil.cpu_freq().current
        if cpu_freq >= 1000:
            cpu_freq = f"{round(cpu_freq / 1000, 2)}GHz"
        else:
            cpu_freq = f"{round(cpu_freq, 2)}MHz"
    except:
        cpu_freq = "Unable to Fetch"
    hdd = psutil.disk_usage("/")
    total = hdd.total / (1024.0**3)
    total = str(total)
    used = hdd.used / (1024.0**3)
    used = str(used)
    free = hdd.free / (1024.0**3)
    free = str(free)
    db = pymongodb
    call = db.command("dbstats")
    datasize = call["dataSize"] / 1024
    datasize = str(datasize)
    storage = call["storageSize"] / 1024
    objects = call["objects"]
    collections = call["collections"]
    status = db.command("serverStatus")
    query = status["opcounters"]["query"]
    mongouptime = status["uptime"] / 86400
    mongouptime = str(mongouptime)
    served_chats = len(await get_served_chats())
    served_users = len(await get_served_users())
    total_queries = await get_queries()
    blocked = len(BANNED_USERS)
    sudoers = len(await get_sudoers())
    text = f""" **Bot's Stats and Information:**

**Platform:** {sc}
**Ram:** {ram}
**Physical Cores:** {p_core}
**Total Cores:** {t_core}
**Cpu Frequency:** {cpu_freq}

**Python Version:** {pyver.split()[0]}
**Pyrogram Version :** {pyrover}

**Storage Avail:** {total[:4]} GiB
**Storage Used:** {used[:4]} GiB
**Storage Left:** {free[:4]} GiB

**Served Chats:** {served_chats} 
**Served Users:** {served_users} 
**Blocked Users:** {blocked} 
**Sudo Users:** {sudoers} 

**Mongo Uptime:** {mongouptime[:4]} Days
**Total DB Size:** {datasize[:6]} Mb
**Total DB Storage:** {storage} Mb
**Total DB Collections:** {collections}
**Total DB Keys:** {objects}
**Total DB Queries:** `{query}`
**Total Bot Queries:** `{total_queries} `
    """
    med = InputMediaPhoto(media=config.STATS_IMG_URL, caption=text)
    try:
        await CallbackQuery.edit_message_media(
            media=med, reply_markup=upl
        )
    except MessageIdInvalid:
        await CallbackQuery.message.reply_photo(
            photo=config.STATS_IMG_URL, caption=text, reply_markup=upl
        )
