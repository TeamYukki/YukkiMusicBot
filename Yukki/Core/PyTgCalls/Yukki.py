import asyncio
import os
import time
from asyncio import QueueEmpty

from config import get_queue
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, KeyboardButton, Message,
                            ReplyKeyboardMarkup, ReplyKeyboardRemove)
from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from pytgcalls.types.input_stream import InputAudioStream, InputStream

from Yukki import MUSIC_BOT_NAME, app, db_mem, userbot
from Yukki.Core.PyTgCalls import Queues
from Yukki.Core.PyTgCalls.Converter import convert
from Yukki.Core.PyTgCalls.Downloader import download
from Yukki.Database import remove_active_chat
from Yukki.Inline import (audio_markup, audio_timer_markup_start,
                          primary_markup, timer_markup)
from Yukki.Utilities.changers import time_to_seconds
from Yukki.Utilities.chat import specialfont_to_normal
from Yukki.Utilities.theme import check_theme
from Yukki.Utilities.thumbnails import gen_thumb
from Yukki.Utilities.timer import start_timer
from Yukki.Utilities.youtube import get_yt_info_id

pytgcalls = PyTgCalls(userbot)


@pytgcalls.on_kicked()
async def kicked_handler(_, chat_id: int):
    try:
        Queues.clear(chat_id)
    except QueueEmpty:
        pass
    await remove_active_chat(chat_id)


@pytgcalls.on_closed_voice_chat()
async def closed_voice_chat_handler(_, chat_id: int):
    try:
        Queues.clear(chat_id)
    except QueueEmpty:
        pass
    await remove_active_chat(chat_id)


@pytgcalls.on_left()
async def left_handler(_, chat_id: int):
    try:
        Queues.clear(chat_id)
    except QueueEmpty:
        pass
    await remove_active_chat(chat_id)


@pytgcalls.on_stream_end()
async def stream_end_handler(_, update: Update):
    chat_id = update.chat_id
    try:
        Queues.task_done(chat_id)
        if Queues.is_empty(chat_id):
            await remove_active_chat(chat_id)
            await pytgcalls.leave_group_call(chat_id)
        else:
            afk = Queues.get(chat_id)["file"]
            finxx = f"{afk[0]}{afk[1]}{afk[2]}"
            got_queue = get_queue.get(chat_id)
            if got_queue:
                got_queue.pop(0)
            aud = 0
            if str(finxx) != "raw":
                mystic = await app.send_message(
                    chat_id,
                    "**Playlist Function**\n\n__Downloading Next Music From Playlist....__",
                )
                (
                    title,
                    duration_min,
                    duration_sec,
                    thumbnail,
                ) = get_yt_info_id(afk)
                mystic = await mystic.edit(
                    f"**{MUSIC_BOT_NAME} Downloader**\n\n**Title:** {title[:50]}\n\n0% ▓▓▓▓▓▓▓▓▓▓▓▓ 100%"
                )
                loop = asyncio.get_event_loop()
                downloaded_file = await loop.run_in_executor(
                    None, download, afk, mystic, title
                )
                raw_path = await convert(downloaded_file)
                await pytgcalls.change_stream(
                    chat_id,
                    InputStream(
                        InputAudioStream(
                            raw_path,
                        ),
                    ),
                )
                theme = await check_theme(chat_id)
                c_title = db_mem[afk]["chat_title"]
                user_id = db_mem[afk]["user_id"]
                chat_title = await specialfont_to_normal(c_title)
                thumb = await gen_thumb(
                    thumbnail, title, user_id, theme, chat_title
                )
                buttons = primary_markup(
                    afk, user_id, duration_min, duration_min
                )
                await mystic.delete()
                mention = db_mem[afk]["username"]
                finaltext = await app.send_photo(
                    chat_id,
                    photo=thumb,
                    reply_markup=InlineKeyboardMarkup(buttons),
                    caption=(
                        f"🎥<b>__Started Playing:__ </b>[{title[:25]}](https://www.youtube.com/watch?v={afk}) \n👤**__Requested by:__** {mention}"
                    ),
                )
                os.remove(thumb)
                videoid = afk
            else:
                videoid = afk
                await pytgcalls.change_stream(
                    chat_id,
                    InputStream(
                        InputAudioStream(
                            afk,
                        ),
                    ),
                )
                title = db_mem[videoid]["title"]
                duration_min = db_mem[videoid]["duration"]
                duration_sec = int(time_to_seconds(duration_min))
                mention = db_mem[videoid]["username"]
                videoid = db_mem[videoid]["videoid"]
                if str(videoid) == "smex1":
                    buttons = buttons = audio_markup(
                        videoid, "283402", duration_min, duration_min
                    )
                    thumb = "Utils/Telegram.JPEG"
                    aud = 1
                else:
                    _path_ = _path_ = (
                        (str(afk))
                        .replace("_", "", 1)
                        .replace("/", "", 1)
                        .replace(".", "", 1)
                    )
                    thumb = f"cache/{_path_}final.png"
                    buttons = primary_markup(
                        videoid, "283402", duration_min, duration_min
                    )
                finaltext = await app.send_photo(
                    chat_id,
                    photo=thumb,
                    reply_markup=InlineKeyboardMarkup(buttons),
                    caption=f"🎥<b>__Started Playing:__</b> {title} \n👤<b>__Requested by:__ </b> {mention}",
                )
            await start_timer(
                videoid,
                duration_min,
                duration_sec,
                finaltext,
                chat_id,
                "28492",
                aud,
            )
    except Exception as e:
        print(e)


run = pytgcalls.run
