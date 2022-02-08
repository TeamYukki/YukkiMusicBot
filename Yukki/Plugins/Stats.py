import asyncio
import json
import logging
import multiprocessing
import platform
import re
import socket
import time
import uuid
from datetime import datetime
from sys import version as pyver

import psutil
from pymongo import MongoClient
from pyrogram import Client
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.types import Message
from pytgcalls import __version__ as pytgover

from config import (MONGO_DB_URI, MUSIC_BOT_NAME, STRING1, STRING2, STRING3,
                    STRING4, STRING5)
from Yukki import (ASS_CLI_1, ASS_CLI_2, ASS_CLI_3, ASS_CLI_4, ASS_CLI_5,
                   BOT_ID, MUSIC_BOT_NAME, SUDOERS, app, boottime)
from Yukki.Database import get_gbans_count, get_served_chats, get_sudoers
from Yukki.Inline import stats1, stats2, stats3, stats4, stats5, stats6, stats7
from Yukki.Plugins import ALL_MODULES
from Yukki.Utilities.ping import get_readable_time


async def bot_sys_stats():
    bot_uptime = int(time.time() - boottime)
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    stats = f"""
**Uptime:** {get_readable_time((bot_uptime))}
**CPU:** {cpu}%
**RAM:** {mem}%
**Disk: **{disk}%"""
    return stats


@app.on_message(filters.command("stats") & ~filters.edited)
async def gstats(_, message):
    start = datetime.now()
    try:
        await message.delete()
    except:
        pass
    uptime = await bot_sys_stats()
    response = await message.reply_photo(
        photo="Utils/Query.jpg", caption="Getting Stats!"
    )
    end = datetime.now()
    resp = (end - start).microseconds / 1000
    smex = f"""
[•]<u>**General Stats**</u>

Ping: `⚡{resp} ms`
{uptime}
    """
    await response.edit_text(smex, reply_markup=stats1)
    return


@app.on_callback_query(
    filters.regex(
        pattern=r"^(sys_stats|sto_stats|bot_stats|Dashboard|mongo_stats|gen_stats|assis_stats|wait_stats)$"
    )
)
async def stats_markup(_, CallbackQuery):
    command = CallbackQuery.matches[0].group(1)
    if command == "sys_stats":
        await CallbackQuery.answer("Getting System Stats...", show_alert=True)
        sc = platform.system()
        arch = platform.machine()
        p_core = psutil.cpu_count(logical=False)
        t_core = psutil.cpu_count(logical=True)
        try:
            cpu_freq = psutil.cpu_freq().current
            if cpu_freq >= 1000:
                cpu_freq = f"{round(cpu_freq / 1000, 2)}GHz"
            else:
                cpu_freq = f"{round(cpu_freq, 2)}MHz"
        except:
            cpu_freq = "Unable to Fetch"
        cupc = "**CPU Usage Per Core:**\n"
        for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
            cupc += f"Core {i}  : {percentage}%\n"
        cupc += "**Total CPU Usage:**\n"
        cupc += f"All Cores Usage: {psutil.cpu_percent()}%\n"
        ram = (
            str(round(psutil.virtual_memory().total / (1024.0**3))) + " GB"
        )
        bot_uptime = int(time.time() - boottime)
        uptime = f"{get_readable_time((bot_uptime))}"
        smex = f"""
[•]<u>**System Stats**</u>

**{MUSIC_BOT_NAME} Uptime:** {uptime}
**System Process:** Online
**Platform:** {sc}
**Architecture:** {arch}
**Ram:** {ram}
**Python Version:** {pyver.split()[0]}
**Pyrogram Version:** {pyrover}
**PyTgCalls Version:** {pytgover.__version__}

[•]<u>**CPU Stats**</u>

**Physical Cores:** {p_core}
**Total Cores:** {t_core}
**Cpu Frequency:** {cpu_freq}

{cupc}
"""
        await CallbackQuery.edit_message_text(smex, reply_markup=stats2)
    if command == "sto_stats":
        await CallbackQuery.answer(
            "Getting Storage Stats...", show_alert=True
        )
        hdd = psutil.disk_usage("/")
        total = hdd.total / (1024.0**3)
        total = str(total)
        used = hdd.used / (1024.0**3)
        used = str(used)
        free = hdd.free / (1024.0**3)
        free = str(free)
        smex = f"""
[•]<u>**Storage Stats**</u>

**Storage Available:** {total[:4]} GiB
**Storage Used:** {used[:4]} GiB
**Storage Left:** {free[:4]} GiB"""
        await CallbackQuery.edit_message_text(smex, reply_markup=stats3)
    if command == "bot_stats":
        await CallbackQuery.answer("Getting Bot Stats...", show_alert=True)
        served_chats = []
        chats = await get_served_chats()
        for chat in chats:
            served_chats.append(int(chat["chat_id"]))
        blocked = await get_gbans_count()
        sudoers = await get_sudoers()
        modules_loaded = len(ALL_MODULES)
        j = 0
        for count, user_id in enumerate(sudoers, 0):
            try:
                user = await app.get_users(user_id)
                j += 1
            except Exception:
                continue
        smex = f"""
[•]<u>**Bot Stats**</u>

**Modules Loaded:** {modules_loaded}
**GBanned Users:** {blocked}
**Sudo Users:** {j}
**Served Chats:** {len(served_chats)}"""
        await CallbackQuery.edit_message_text(smex, reply_markup=stats4)
    if command == "mongo_stats":
        await CallbackQuery.answer(
            "Getting MongoDB Stats...", show_alert=True
        )
        try:
            pymongo = MongoClient(MONGO_DB_URI)
        except Exception as e:
            print(e)
            return await CallbackQuery.edit_message_text(
                "Failed to get Mongo DB stats", reply_markup=stats5
            )
        try:
            db = pymongo.Yukki
        except Exception as e:
            print(e)
            return await CallbackQuery.edit_message_text(
                "Failed to get Mongo DB stats", reply_markup=stats5
            )
        call = db.command("dbstats")
        database = call["db"]
        datasize = call["dataSize"] / 1024
        datasize = str(datasize)
        storage = call["storageSize"] / 1024
        objects = call["objects"]
        collections = call["collections"]
        status = db.command("serverStatus")
        query = status["opcounters"]["query"]
        mver = status["version"]
        mongouptime = status["uptime"] / 86400
        mongouptime = str(mongouptime)
        provider = status["repl"]["tags"]["provider"]
        smex = f"""
[•]<u>**MongoDB Stats**</u>

**Mongo Uptime:** {mongouptime[:4]} Days
**Version:** {mver}
**Database:** {database}
**Provider:** {provider}
**DB Size:** {datasize[:6]} Mb
**Storage:** {storage} Mb
**Collections:** {collections}
**Keys:** {objects}
**Total Queries:** `{query}`"""
        await CallbackQuery.edit_message_text(smex, reply_markup=stats5)
    if command == "gen_stats":
        start = datetime.now()
        uptime = await bot_sys_stats()
        await CallbackQuery.answer(
            "Getting General Stats...", show_alert=True
        )
        end = datetime.now()
        resp = (end - start).microseconds / 1000
        smex = f"""
[•]<u>General Stats</u>

**Ping:** `⚡{resp} ms`
{uptime}"""
        await CallbackQuery.edit_message_text(smex, reply_markup=stats1)
    if command == "wait_stats":
        await CallbackQuery.answer()
    if command == "assis_stats":
        await CallbackQuery.answer(
            "Getting Assistant Stats...", show_alert=True
        )
        await CallbackQuery.edit_message_text(
            "Getting Assistant Stats.. Please Wait...", reply_markup=stats7
        )
        groups_ub = channels_ub = bots_ub = privates_ub = total_ub = 0
        groups_ub2 = channels_ub2 = bots_ub2 = privates_ub2 = total_ub2 = 0
        groups_ub3 = channels_ub3 = bots_ub3 = privates_ub3 = total_ub3 = 0
        groups_ub4 = channels_ub4 = bots_ub4 = privates_ub4 = total_ub4 = 0
        groups_ub5 = channels_ub5 = bots_ub5 = privates_ub5 = total_ub5 = 0

        if STRING1 != "None":
            async for i in ASS_CLI_1.iter_dialogs():
                t = i.chat.type
                total_ub += 1
                if t in ["supergroup", "group"]:
                    groups_ub += 1
                elif t == "channel":
                    channels_ub += 1
                elif t == "bot":
                    bots_ub += 1
                elif t == "private":
                    privates_ub += 1

        if STRING2 != "None":
            async for i in ASS_CLI_2.iter_dialogs():
                t = i.chat.type
                total_ub2 += 1
                if t in ["supergroup", "group"]:
                    groups_ub2 += 1
                elif t == "channel":
                    channels_ub2 += 1
                elif t == "bot":
                    bots_ub2 += 1
                elif t == "private":
                    privates_ub2 += 1

        if STRING3 != "None":
            async for i in ASS_CLI_3.iter_dialogs():
                t = i.chat.type
                total_ub3 += 1
                if t in ["supergroup", "group"]:
                    groups_ub3 += 1
                elif t == "channel":
                    channels_ub3 += 1
                elif t == "bot":
                    bots_ub3 += 1
                elif t == "private":
                    privates_ub3 += 1

        if STRING4 != "None":
            async for i in ASS_CLI_4.iter_dialogs():
                t = i.chat.type
                total_ub4 += 1
                if t in ["supergroup", "group"]:
                    groups_ub4 += 1
                elif t == "channel":
                    channels_ub4 += 1
                elif t == "bot":
                    bots_ub4 += 1
                elif t == "private":
                    privates_ub4 += 1

        if STRING5 != "None":
            async for i in ASS_CLI_5.iter_dialogs():
                t = i.chat.type
                total_ub5 += 1
                if t in ["supergroup", "group"]:
                    groups_ub5 += 1
                elif t == "channel":
                    channels_ub5 += 1
                elif t == "bot":
                    bots_ub5 += 1
                elif t == "private":
                    privates_ub5 += 1

        msg = "[•]<u>Assistant Stats</u>"
        if STRING1 != "None":
            msg += "\n\n<u>Assistant One:\n</u>"
            msg += f"""**Dialogs:** {total_ub}
**Groups:** {groups_ub}
**Channels:** {channels_ub}
**Bots:** {bots_ub}
**Users:** {privates_ub}"""

        if STRING2 != "None":
            msg += "\n\n<u>Assistant Two:\n</u>"
            msg += f"""**Dialogs:** {total_ub2}
**Groups:** {groups_ub2}
**Channels:** {channels_ub2}
**Bots:** {bots_ub2}
**Users:** {privates_ub2}"""

        if STRING3 != "None":
            msg += "\n\n<u>Assistant Three:\n</u>"
            msg += f"""**Dialogs:** {total_ub3}
**Groups:** {groups_ub3}
**Channels:** {channels_ub3}
**Bots:** {bots_ub3}
**Users:** {privates_ub3}"""

        if STRING4 != "None":
            msg += "\n\n<u>Assistant Four:\n</u>"
            msg += f"""**Dialogs:** {total_ub4}
**Groups:** {groups_ub4}
**Channels:** {channels_ub4}
**Bots:** {bots_ub4}
**Users:** {privates_ub4}"""

        if STRING5 != "None":
            msg += "\n\n<u>Assistant Five:\n</u>"
            msg += f"""**Dialogs:** {total_ub5}
**Groups:** {groups_ub5}
**Channels:** {channels_ub5}
**Bots:** {bots_ub5}
**Users:** {privates_ub5}"""
        await CallbackQuery.edit_message_text(msg, reply_markup=stats6)
