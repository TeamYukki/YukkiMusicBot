import random

from pyrogram import filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup

from config import (AUTO_DOWNLOADS_CLEAR, BANNED_USERS,
                    SOUNCLOUD_IMG_URL, STREAM_IMG_URL,
                    TELEGRAM_AUDIO_URL, TELEGRAM_VIDEO_URL, adminlist)
from YukkiMusic import YouTube, app
from YukkiMusic.core.call import Yukki
from YukkiMusic.misc import SUDOERS, db
from YukkiMusic.utils.database import (is_active_chat,
                                       is_music_playing, is_muted,
                                       is_nonadmin_chat, music_off,
                                       music_on, mute_off, mute_on,
                                       set_loop)
from YukkiMusic.utils.decorators.language import languageCB
from YukkiMusic.utils.formatters import seconds_to_min
from YukkiMusic.utils.inline.play import (panel_markup_1,
                                          panel_markup_2,
                                          panel_markup_3,
                                          stream_markup,
                                          telegram_markup)
from YukkiMusic.utils.stream.autoclear import auto_clean
from YukkiMusic.utils.thumbnails import gen_thumb

wrong = {}


@app.on_callback_query(filters.regex("PanelMarkup") & ~BANNED_USERS)
@languageCB
async def markup_panel(client, CallbackQuery: CallbackQuery, _):
    await CallbackQuery.answer()
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    videoid, chat_id = callback_request.split("|")
    chat_id = CallbackQuery.message.chat.id
    buttons = panel_markup_1(_, videoid, chat_id)
    try:
        await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except:
        return
    if chat_id not in wrong:
        wrong[chat_id] = {}
    wrong[chat_id][CallbackQuery.message.id] = False


@app.on_callback_query(filters.regex("MainMarkup") & ~BANNED_USERS)
@languageCB
async def del_back_playlist(client, CallbackQuery, _):
    await CallbackQuery.answer()
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    videoid, chat_id = callback_request.split("|")
    if videoid == str(None):
        buttons = telegram_markup(_, chat_id)
    else:
        buttons = stream_markup(_, videoid, chat_id)
    chat_id = CallbackQuery.message.chat.id
    try:
        await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except:
        return
    if chat_id not in wrong:
        wrong[chat_id] = {}
    wrong[chat_id][CallbackQuery.message.id] = True


@app.on_callback_query(filters.regex("Pages") & ~BANNED_USERS)
@languageCB
async def del_back_playlist(client, CallbackQuery, _):
    await CallbackQuery.answer()
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    state, pages, videoid, chat = callback_request.split("|")
    chat_id = int(chat)
    pages = int(pages)
    if state == "Forw":
        if pages == 0:
            buttons = panel_markup_2(_, videoid, chat_id)
        if pages == 2:
            buttons = panel_markup_1(_, videoid, chat_id)
        if pages == 1:
            buttons = panel_markup_3(_, videoid, chat_id)
    if state == "Back":
        if pages == 2:
            buttons = panel_markup_2(_, videoid, chat_id)
        if pages == 1:
            buttons = panel_markup_1(_, videoid, chat_id)
        if pages == 0:
            buttons = panel_markup_3(_, videoid, chat_id)
    try:
        await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except:
        return


downvote = {}
downvoters = {}


@app.on_callback_query(filters.regex("ADMIN") & ~BANNED_USERS)
@languageCB
async def del_back_playlist(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    command, chat = callback_request.split("|")
    chat_id = int(chat)
    if not await is_active_chat(chat_id):
        return await CallbackQuery.answer(
            _["general_6"], show_alert=True
        )
    mention = CallbackQuery.from_user.mention
    is_non_admin = await is_nonadmin_chat(
        CallbackQuery.message.chat.id
    )
    if not is_non_admin:
        if CallbackQuery.from_user.id not in SUDOERS:
            admins = adminlist.get(CallbackQuery.message.chat.id)
            if not admins:
                return await CallbackQuery.answer(
                    _["admin_18"], show_alert=True
                )
            else:
                if CallbackQuery.from_user.id not in admins:
                    return await CallbackQuery.answer(
                        _["admin_19"], show_alert=True
                    )
    if command == "Pause":
        if not await is_music_playing(chat_id):
            return await CallbackQuery.answer(
                _["admin_1"], show_alert=True
            )
        await CallbackQuery.answer()
        await music_off(chat_id)
        await Yukki.pause_stream(chat_id)
        await CallbackQuery.message.reply_text(
            _["admin_2"].format(mention)
        )
    elif command == "Resume":
        if await is_music_playing(chat_id):
            return await CallbackQuery.answer(
                _["admin_3"], show_alert=True
            )
        await CallbackQuery.answer()
        await music_on(chat_id)
        await Yukki.resume_stream(chat_id)
        await CallbackQuery.message.reply_text(
            _["admin_4"].format(mention)
        )
    elif command == "Stop" or command == "End":
        await CallbackQuery.answer()
        await Yukki.stop_stream(chat_id)
        await set_loop(chat_id, 0)
        await CallbackQuery.message.reply_text(
            _["admin_9"].format(mention)
        )
    elif command == "Mute":
        if await is_muted(chat_id):
            return await CallbackQuery.answer(
                _["admin_5"], show_alert=True
            )
        await CallbackQuery.answer()
        await mute_on(chat_id)
        await Yukki.mute_stream(chat_id)
        await CallbackQuery.message.reply_text(
            _["admin_6"].format(mention)
        )
    elif command == "Unmute":
        if not await is_muted(chat_id):
            return await CallbackQuery.answer(
                _["admin_7"], show_alert=True
            )
        await CallbackQuery.answer()
        await mute_off(chat_id)
        await Yukki.unmute_stream(chat_id)
        await CallbackQuery.message.reply_text(
            _["admin_8"].format(mention)
        )
    elif command == "Loop":
        await CallbackQuery.answer()
        await set_loop(chat_id, 3)
        await CallbackQuery.message.reply_text(
            _["admin_25"].format(mention, 3)
        )
    elif command == "Shuffle":
        check = db.get(chat_id)
        if not check:
            return await CallbackQuery.answer(
                _["admin_21"], show_alert=True
            )
        try:
            popped = check.pop(0)
        except:
            return await CallbackQuery.answer(
                _["admin_22"], show_alert=True
            )
        check = db.get(chat_id)
        if not check:
            check.insert(0, popped)
            return await CallbackQuery.answer(
                _["admin_22"], show_alert=True
            )
        await CallbackQuery.answer()
        random.shuffle(check)
        check.insert(0, popped)
        await CallbackQuery.message.reply_text(
            _["admin_23"].format(mention)
        )
    elif command == "Skip":
        check = db.get(chat_id)
        txt = f"Skipped by {mention}"
        popped = None
        try:
            popped = check.pop(0)
            if popped:
                if AUTO_DOWNLOADS_CLEAR == str(True):
                    await auto_clean(popped)
            if not check:
                await CallbackQuery.edit_message_text(
                    f"Skipped by {mention}"
                )
                await CallbackQuery.message.reply_text(
                    _["admin_10"].format(mention)
                )
                try:
                    return await Yukki.stop_stream(chat_id)
                except:
                    return
        except:
            try:
                await CallbackQuery.edit_message_text(
                    f"Skipped by {mention}"
                )
                await CallbackQuery.message.reply_text(
                    _["admin_10"].format(mention)
                )
                return await Yukki.stop_stream(chat_id)
            except:
                return
        await CallbackQuery.answer()
        queued = check[0]["file"]
        title = (check[0]["title"]).title()
        user = check[0]["by"]
        streamtype = check[0]["streamtype"]
        videoid = check[0]["vidid"]
        status = True if str(streamtype) == "video" else None
        db[chat_id][0]["played"] = 0
        if "live_" in queued:
            n, link = await YouTube.video(videoid, True)
            if n == 0:
                return await CallbackQuery.message.reply_text(
                    _["admin_11"].format(title)
                )
            try:
                await Yukki.skip_stream(chat_id, link, video=status)
            except Exception:
                return await CallbackQuery.message.reply_text(
                    _["call_9"]
                )
            button = telegram_markup(_, chat_id)
            img = await gen_thumb(videoid)
            run = await CallbackQuery.message.reply_photo(
                photo=img,
                caption=_["stream_1"].format(
                    user,
                    f"https://t.me/{app.username}?start=info_{videoid}",
                ),
                reply_markup=InlineKeyboardMarkup(button),
            )
            db[chat_id][0]["mystic"] = run
            db[chat_id][0]["markup"] = "tg"
            await CallbackQuery.edit_message_text(txt)
        elif "vid_" in queued:
            mystic = await CallbackQuery.message.reply_text(
                _["call_10"], disable_web_page_preview=True
            )
            try:
                file_path, direct = await YouTube.download(
                    videoid,
                    mystic,
                    videoid=True,
                    video=status,
                )
            except:
                return await mystic.edit_text(_["call_9"])
            try:
                await Yukki.skip_stream(
                    chat_id, file_path, video=status
                )
            except Exception:
                return await mystic.edit_text(_["call_9"])
            button = stream_markup(_, videoid, chat_id)
            img = await gen_thumb(videoid)
            run = await CallbackQuery.message.reply_photo(
                photo=img,
                caption=_["stream_1"].format(
                    user,
                    f"https://t.me/{app.username}?start=info_{videoid}",
                ),
                reply_markup=InlineKeyboardMarkup(button),
            )
            db[chat_id][0]["mystic"] = run
            db[chat_id][0]["markup"] = "stream"
            await CallbackQuery.edit_message_text(txt)
            await mystic.delete()
        elif "index_" in queued:
            try:
                await Yukki.skip_stream(
                    chat_id, videoid, video=status
                )
            except Exception:
                return await CallbackQuery.message.reply_text(
                    _["call_9"]
                )
            button = telegram_markup(_, chat_id)
            run = await CallbackQuery.message.reply_photo(
                photo=STREAM_IMG_URL,
                caption=_["stream_2"].format(user),
                reply_markup=InlineKeyboardMarkup(button),
            )
            db[chat_id][0]["mystic"] = run
            db[chat_id][0]["markup"] = "tg"
            await CallbackQuery.edit_message_text(txt)
        else:
            try:
                await Yukki.skip_stream(chat_id, queued, video=status)
            except Exception:
                return await CallbackQuery.message.reply_text(
                    _["call_9"]
                )
            if videoid == "telegram":
                button = telegram_markup(_, chat_id)
                run = await CallbackQuery.message.reply_photo(
                    photo=TELEGRAM_AUDIO_URL
                    if str(streamtype) == "audio"
                    else TELEGRAM_VIDEO_URL,
                    caption=_["stream_3"].format(
                        title, check[0]["dur"], user
                    ),
                    reply_markup=InlineKeyboardMarkup(button),
                )
                db[chat_id][0]["mystic"] = run
                db[chat_id][0]["markup"] = "tg"
            elif videoid == "soundcloud":
                button = telegram_markup(_, chat_id)
                run = await CallbackQuery.message.reply_photo(
                    photo=SOUNCLOUD_IMG_URL
                    if str(streamtype) == "audio"
                    else TELEGRAM_VIDEO_URL,
                    caption=_["stream_3"].format(
                        title, check[0]["dur"], user
                    ),
                    reply_markup=InlineKeyboardMarkup(button),
                )
                db[chat_id][0]["mystic"] = run
                db[chat_id][0]["markup"] = "tg"
            else:
                button = stream_markup(_, videoid, chat_id)
                img = await gen_thumb(videoid)
                run = await CallbackQuery.message.reply_photo(
                    photo=img,
                    caption=_["stream_1"].format(
                        user,
                        f"https://t.me/{app.username}?start=info_{videoid}",
                    ),
                    reply_markup=InlineKeyboardMarkup(button),
                )
                db[chat_id][0]["mystic"] = run
                db[chat_id][0]["markup"] = "stream"
            await CallbackQuery.edit_message_text(txt)
    else:
        playing = db.get(chat_id)
        if not playing:
            return await CallbackQuery.answer(
                _["queue_2"], show_alert=True
            )
        duration_seconds = int(playing[0]["seconds"])
        if duration_seconds == 0:
            return await CallbackQuery.answer(
                _["admin_30"], show_alert=True
            )
        file_path = playing[0]["file"]
        if "index_" in file_path or "live_" in file_path:
            return await CallbackQuery.answer(
                _["admin_30"], show_alert=True
            )
        duration_played = int(playing[0]["played"])
        if int(command) in [1, 2]:
            duration_to_skip = 10
        else:
            duration_to_skip = 30
        duration = playing[0]["dur"]
        if int(command) in [1, 3]:
            if (duration_played - duration_to_skip) <= 10:
                bet = seconds_to_min(duration_played)
                return await CallbackQuery.answer(
                    f"Bot is not able to seek due to total duration has been exceeded.\n\nCurrently played** {bet}** mins out of **{duration}** mins",
                    show_alert=True,
                )
            to_seek = duration_played - duration_to_skip + 1
        else:
            if (
                duration_seconds
                - (duration_played + duration_to_skip)
            ) <= 10:
                bet = seconds_to_min(duration_played)
                return await CallbackQuery.answer(
                    f"Bot is not able to seek due to total duration has been exceeded.\n\nCurrently played** {bet}** mins out of **{duration}** mins",
                    show_alert=True,
                )
            to_seek = duration_played + duration_to_skip + 1
        await CallbackQuery.answer()
        mystic = await CallbackQuery.message.reply_text(_["admin_32"])
        if "vid_" in file_path:
            n, file_path = await YouTube.video(
                playing[0]["vidid"], True
            )
            if n == 0:
                return await mystic.edit_text(_["admin_30"])
        try:
            await Yukki.seek_stream(
                chat_id,
                file_path,
                seconds_to_min(to_seek),
                duration,
                playing[0]["streamtype"],
            )
        except:
            return await mystic.edit_text(_["admin_34"])
        if int(command) in [1, 3]:
            db[chat_id][0]["played"] -= duration_to_skip
        else:
            db[chat_id][0]["played"] += duration_to_skip
        string = _["admin_33"].format(seconds_to_min(to_seek))
        await mystic.edit_text(
            f"{string}\n\nChanges done by: {mention}"
        )
