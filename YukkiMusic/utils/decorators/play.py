#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import PLAYLIST_IMG_URL, PRIVATE_BOT_MODE, adminlist
from strings import get_string
from YukkiMusic import YouTube, app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.utils.database import (get_chatmode, get_cmode,
                                       get_lang, get_loop,
                                       get_playmode, get_playtype,
                                       is_commanddelete_on,
                                       is_served_private_chat)
from YukkiMusic.utils.inline.playlist import botplaylist_markup


def PlayWrapper(command):
    async def wrapper(client, message):
        if PRIVATE_BOT_MODE:
            if not await is_served_private_chat(message.chat.id):
                await message.reply_text(
                    "**Private Music Bot**\n\nOnly for authorized chats from the owner. Ask my owner to allow your chat first."
                )
                return await app.leave_chat(message.chat.id)
        if await is_commanddelete_on(message.chat.id):
            try:
                await message.delete()
            except:
                pass
        language = await get_lang(message.chat.id)
        _ = get_string(language)
        audio_telegram = (
            (
                message.reply_to_message.audio
                or message.reply_to_message.voice
            )
            if message.reply_to_message
            else None
        )
        video_telegram = (
            (
                message.reply_to_message.video
                or message.reply_to_message.document
            )
            if message.reply_to_message
            else None
        )
        url = await YouTube.url(message)
        if (
            audio_telegram is None
            and video_telegram is None
            and url is None
        ):
            if len(message.command) < 2:
                if "stream" in message.command:
                    return await message.reply_text(_["str_1"])
                buttons = botplaylist_markup(_)
                return await message.reply_photo(
                    photo=PLAYLIST_IMG_URL,
                    caption=_["playlist_1"],
                    reply_markup=InlineKeyboardMarkup(buttons),
                )
        if message.sender_chat:
            upl = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="How to Fix this? ",
                            callback_data="AnonymousAdmin",
                        ),
                    ]
                ]
            )
            return await message.reply_text(
                _["general_4"], reply_markup=upl
            )
        sms = _["play_1"]
        chatmode = await get_chatmode(message.chat.id)
        if chatmode == "Group":
            sms += "\n\n**▶️ Play Mode:** Group"
            chat_id = message.chat.id
            channel = None
        else:
            chat_id = await get_cmode(message.chat.id)
            try:
                chat = await app.get_chat(chat_id)
            except:
                return await message.reply_text(_["cplay_4"])
            channel = chat.title
            sms += f"\n\n**▶️ Play Mode:** Channel[{channel}]"
        playmode = await get_playmode(message.chat.id)
        if str(playmode) == "Direct":
            sms += "\n**🔎 Search Mode:** Direct"
        else:
            sms += "\n**🔎 Search Mode:** Inline"
        playty = await get_playtype(message.chat.id)
        if playty != "Everyone":
            if message.from_user.id not in SUDOERS:
                sms += "\n**🧛 Play Type:** Admins Only"
                admins = adminlist.get(message.chat.id)
                if not admins:
                    return await message.reply_text(_["admin_18"])
                else:
                    if message.from_user.id not in admins:
                        return await message.reply_text(_["play_4"])
        if "vplay" in message.command:
            video = True
        else:
            if "-v" in message.text:
                video = True
            else:
                video = None
        loop = await get_loop(chat_id)
        if loop != 0:
            sms += f"\n**🔄 Loop Play:** Enabled for {loop} times"
        else:
            sms += "\n**🔄 Loop Play:** Disabled"
        sms += "\n\nChange modes via /playmode"
        mystic = await message.reply_text(sms)
        return await command(
            client,
            message,
            _,
            chat_id,
            video,
            channel,
            playmode,
            mystic,
            url,
        )

    return wrapper
