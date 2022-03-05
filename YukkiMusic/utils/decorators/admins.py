#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import adminlist
from strings import get_string
from YukkiMusic import app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.utils.database import (get_authuser_names,
                                       get_chatmode, get_cmode,
                                       get_lang, is_active_chat,
                                       is_commanddelete_on,
                                       is_nonadmin_chat)

from ..formatters import int_to_alpha


def AdminRightsCheck(mystic):
    async def wrapper(client, message):
        if await is_commanddelete_on(message.chat.id):
            try:
                await message.delete()
            except:
                pass
        language = await get_lang(message.chat.id)
        _ = get_string(language)
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
        if "pause" in message.command:
            s = "Pausing Stream"
        elif "resume" in message.command:
            s = "Resuming Stream"
        elif "skip" in message.command:
            s = "Skipping Stream"
        elif "stop" in message.command:
            s = "Stopping Stream"
        elif "end" in message.command:
            s = "Ending Stream"
        elif "loop" in message.command:
            s = "Looping Stream"
        elif "shuffle" in message.command:
            s = "Shuffling Stream"
        elif "mute" in message.command:
            s = "Muting Stream"
        elif "unmute" in message.command:
            s = "Unmute Stream"
        else:
            s = "Processing"
        send = _["admin_17"].format(s)
        chatmode = await get_chatmode(message.chat.id)
        if chatmode == "Group":
            send += "\n**▶️ Play Mode:** Group"
            chat_id = message.chat.id
        else:
            chat_id = await get_cmode(message.chat.id)
            try:
                chat = await app.get_chat(chat_id)
            except:
                return await mys.edit_text(_["cplay_4"])
            send += f"\n**▶️ Play Mode:** Channel[{chat.title}]"
        if not await is_active_chat(chat_id):
            return await message.reply_text(_["general_6"])
        is_non_admin = await is_nonadmin_chat(message.chat.id)
        if not is_non_admin:
            if message.from_user.id not in SUDOERS:
                send += (
                    "\n\n**🧛 Admin Commands:** Admins + Auth Users"
                )
                admins = adminlist.get(message.chat.id)
                if not admins:
                    return await message.reply_text(_["admin_18"])
                else:
                    if message.from_user.id not in admins:
                        return await message.reply_text(_["admin_19"])
        else:
            send += "\n\n**🧛 Admins Command:** Anyone"
        mys = await message.reply_text(send)
        return await mystic(client, message, _, mys, chat_id)

    return wrapper


def AdminActual(mystic):
    async def wrapper(client, message):
        if await is_commanddelete_on(message.chat.id):
            try:
                await message.delete()
            except:
                pass
        language = await get_lang(message.chat.id)
        _ = get_string(language)
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
        if message.from_user.id not in SUDOERS:
            try:
                member = await app.get_chat_member(
                    message.chat.id, message.from_user.id
                )
            except:
                return
            if not member.can_manage_voice_chats:
                return await message.reply(_["general_5"])

        return await mystic(client, message, _)

    return wrapper


def ActualAdminCB(mystic):
    async def wrapper(client, CallbackQuery):
        language = await get_lang(CallbackQuery.message.chat.id)
        _ = get_string(language)
        if CallbackQuery.message.chat.type == "private":
            return await mystic(client, CallbackQuery, _)
        is_non_admin = await is_nonadmin_chat(
            CallbackQuery.message.chat.id
        )
        if not is_non_admin:
            try:
                a = await app.get_chat_member(
                    CallbackQuery.message.chat.id,
                    CallbackQuery.from_user.id,
                )
            except:
                return await CallbackQuery.answer(
                    _["general_5"], show_alert=True
                )
            if not a.can_manage_voice_chats:
                if CallbackQuery.from_user.id not in SUDOERS:
                    token = await int_to_alpha(
                        CallbackQuery.from_user.id
                    )
                    _check = await get_authuser_names(
                        CallbackQuery.from_user.id
                    )
                    if token not in _check:
                        try:
                            return await CallbackQuery.answer(
                                _["general_5"],
                                show_alert=True,
                            )
                        except:
                            return
        return await mystic(client, CallbackQuery, _)

    return wrapper
