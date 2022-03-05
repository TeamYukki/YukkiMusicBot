#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup

from config import BANNED_USERS
from YukkiMusic import app
from YukkiMusic.utils.database import (get_chatmode, get_cmode,
                                       get_global_tops,
                                       get_particulars, get_userss)
from YukkiMusic.utils.decorators.language import languageCB
from YukkiMusic.utils.inline.playlist import (botplaylist_markup,
                                              failed_top_markup,
                                              top_play_markup)
from YukkiMusic.utils.stream.stream import stream


@app.on_callback_query(
    filters.regex("get_playmarkup") & ~BANNED_USERS
)
@languageCB
async def get_play_markup(client, CallbackQuery, _):
    try:
        await CallbackQuery.answer()
    except:
        pass
    buttons = botplaylist_markup(_)
    return await CallbackQuery.edit_message_reply_markup(
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@app.on_callback_query(
    filters.regex("get_top_playlists") & ~BANNED_USERS
)
@languageCB
async def get_topz_playlists(client, CallbackQuery, _):
    try:
        await CallbackQuery.answer()
    except:
        pass
    buttons = top_play_markup(_)
    return await CallbackQuery.edit_message_reply_markup(
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@app.on_callback_query(filters.regex("SERVERTOP") & ~BANNED_USERS)
@languageCB
async def server_to_play(client, CallbackQuery, _):
    chatmode = await get_chatmode(CallbackQuery.message.chat.id)
    if chatmode == "Group":
        chat_id = CallbackQuery.message.chat.id
        channel = None
    else:
        chat_id = await get_cmode(CallbackQuery.message.chat.id)
        try:
            chat = await app.get_chat(chat_id)
            channel = chat.title
        except:
            try:
                return await CallbackQuery.answer(
                    _["cplay_4"], show_alert=True
                )
            except:
                return
    user_name = CallbackQuery.from_user.first_name
    try:
        await CallbackQuery.answer()
    except:
        pass
    callback_data = CallbackQuery.data.strip()
    what = callback_data.split(None, 1)[1]
    mystic = await CallbackQuery.edit_message_text(
        _["tracks_1"].format(
            what,
            CallbackQuery.from_user.first_name,
            f"Enabled on {channel}" if channel else "Disabled ",
        )
    )
    upl = failed_top_markup(_)
    limit = 0
    results = {}
    if what == "Global":
        stats = await get_global_tops()
    elif what == "Group":
        stats = await get_particulars(chat_id)
    elif what == "Personal":
        stats = await get_userss(CallbackQuery.from_user.id)
    if not stats:
        return await mystic.edit(
            _["tracks_2"].format(what), reply_markup=upl
        )
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
        return await mystic.edit(
            _["tracks_2"].format(what), reply_markup=upl
        )
    details = []
    for vidid, count in list_arranged.items():
        if vidid == "telegram":
            continue
        if limit > 9:
            break
        limit += 1
        details.append(vidid)
    if not details:
        return await mystic.edit(
            _["tracks_2"].format(what), reply_markup=upl
        )
    try:
        await stream(
            _,
            mystic,
            CallbackQuery.from_user.id,
            details,
            chat_id,
            user_name,
            CallbackQuery.message.chat.id,
            video=False,
            streamtype="playlist",
        )
    except Exception as e:
        ex_type = type(e).__name__
        err = (
            e
            if ex_type == "AssistantErr"
            else _["general_3"].format(ex_type)
        )
        return await mystic.edit_text(err)
    return await mystic.delete()
