import asyncio
import time
from datetime import datetime, timedelta

from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from Yukki import db_mem
from Yukki.Database import is_active_chat, is_music_playing
from Yukki.Inline import audio_timer_markup_start, timer_markup


async def start_timer(
    videoid, duration_min, duration_sec, finaltext, chat_id, user_id, aud
):
    left_time = {}
    db_mem[chat_id]["videoid"] = videoid
    db_mem[chat_id]["left"] = duration_min
    db_mem[chat_id]["total"] = duration_min
    user_input_time = int(duration_sec - 8)
    left_time[videoid] = datetime.now()
    try:
        if 0 < user_input_time <= 7:
            while user_input_time:
                if await is_active_chat(chat_id):
                    if db_mem[chat_id]["videoid"] == videoid:
                        if await is_music_playing(chat_id):
                            if datetime.now() > left_time.get(videoid):
                                s = user_input_time % 60
                                c_t = "00:{:02d}".format(s)
                                if aud == 0:
                                    buttons = timer_markup(
                                        videoid, user_id, c_t, duration_min
                                    )
                                else:
                                    buttons = audio_timer_markup_start(
                                        videoid, user_id, c_t, duration_min
                                    )
                                user_input_time -= 1
                                db_mem[chat_id]["left"] = c_t
                                try:
                                    if db_mem[videoid]["check"] == 2:
                                        await finaltext.edit_reply_markup(
                                            reply_markup=InlineKeyboardMarkup(
                                                buttons
                                            )
                                        )
                                except FloodWait as e:
                                    await asyncio.sleep(e.x)
                                    user_input_time -= e.x
                                left_time[
                                    videoid
                                ] = datetime.now() + timedelta(
                                    milliseconds=550
                                )
                    else:
                        break
                else:
                    break
        elif 7 < user_input_time < 60:
            while user_input_time > 0:
                if await is_active_chat(chat_id):
                    if db_mem[chat_id]["videoid"] == videoid:
                        if await is_music_playing(chat_id):
                            if datetime.now() > left_time.get(videoid):
                                s = user_input_time % 60
                                c_t = "00:{:02d}".format(s)
                                user_input_time -= 4
                                if aud == 0:
                                    buttons = timer_markup(
                                        videoid, user_id, c_t, duration_min
                                    )
                                else:
                                    buttons = audio_timer_markup_start(
                                        videoid, user_id, c_t, duration_min
                                    )
                                db_mem[chat_id]["left"] = c_t
                                try:
                                    if db_mem[videoid]["check"] == 2:
                                        await finaltext.edit_reply_markup(
                                            reply_markup=InlineKeyboardMarkup(
                                                buttons
                                            )
                                        )
                                except FloodWait as e:
                                    await asyncio.sleep(e.x)
                                    user_input_time -= e.x
                                left_time[
                                    videoid
                                ] = datetime.now() + timedelta(
                                    milliseconds=3500
                                )
                    else:
                        break
                else:
                    break
        elif 60 <= user_input_time < 3600:
            while user_input_time > 0:
                if await is_active_chat(chat_id):
                    if db_mem[chat_id]["videoid"] == videoid:
                        if await is_music_playing(chat_id):
                            if datetime.now() > left_time.get(videoid):
                                m = user_input_time % 3600 // 60
                                s = user_input_time % 60
                                c_t = "{:02d}:{:02d}".format(m, s)
                                user_input_time -= 6
                                if aud == 0:
                                    buttons = timer_markup(
                                        videoid, user_id, c_t, duration_min
                                    )
                                else:
                                    buttons = audio_timer_markup_start(
                                        videoid, user_id, c_t, duration_min
                                    )
                                db_mem[chat_id]["left"] = c_t
                                try:
                                    if db_mem[videoid]["check"] == 2:
                                        await finaltext.edit_reply_markup(
                                            reply_markup=InlineKeyboardMarkup(
                                                buttons
                                            )
                                        )
                                except FloodWait as e:
                                    await asyncio.sleep(e.x)
                                    user_input_time -= e.x
                                left_time[
                                    videoid
                                ] = datetime.now() + timedelta(
                                    milliseconds=5300
                                )
                    else:
                        break
                else:
                    break
        elif 3600 <= user_input_time < 86400:
            while user_input_time > 0:
                if await is_active_chat(chat_id):
                    if db_mem[chat_id]["videoid"] == videoid:
                        if await is_music_playing(chat_id):
                            if datetime.now() > left_time.get(videoid):
                                h = user_input_time % (3600 * 24) // 3600
                                m = user_input_time % 3600 // 60
                                s = user_input_time % 60
                                c_t = "{:02d}:{:02d}:{:02d}".format(h, m, s)
                                user_input_time -= 10
                                if aud == 0:
                                    buttons = timer_markup(
                                        videoid, user_id, c_t, duration_min
                                    )
                                else:
                                    buttons = audio_timer_markup_start(
                                        videoid, user_id, c_t, duration_min
                                    )
                                db_mem[chat_id]["left"] = c_t
                                try:
                                    if db_mem[videoid]["check"] == 2:
                                        await finaltext.edit_reply_markup(
                                            reply_markup=InlineKeyboardMarkup(
                                                buttons
                                            )
                                        )
                                except FloodWait as e:
                                    await asyncio.sleep(e.x)
                                    user_input_time -= e.x
                                left_time[
                                    videoid
                                ] = datetime.now() + timedelta(
                                    milliseconds=9100
                                )
                    else:
                        break
                else:
                    break
        else:
            return
    except Exception as e:
        print(e)
        return
