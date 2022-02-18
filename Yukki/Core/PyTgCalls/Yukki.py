import asyncio
import os
import time
from asyncio import QueueEmpty

from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, KeyboardButton, Message,
                            ReplyKeyboardMarkup, ReplyKeyboardRemove)
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types import Update
from pytgcalls.types.input_stream import (AudioVideoPiped, InputAudioStream,
                                          InputStream)
from pytgcalls.types.input_stream.quality import (HighQualityAudio,
                                                  HighQualityVideo,
                                                  LowQualityVideo,
                                                  MediumQualityVideo)
from pytgcalls.types.stream import StreamAudioEnded, StreamVideoEnded

from config import STRING1, STRING2, STRING3, STRING4, STRING5, get_queue
from Yukki import (ASS_CLI_1, ASS_CLI_2, ASS_CLI_3, ASS_CLI_4, ASS_CLI_5,
                   MUSIC_BOT_NAME, app, db_mem)
from Yukki.Core.PyTgCalls import Queues
from Yukki.Core.PyTgCalls.Converter import convert
from Yukki.Core.PyTgCalls.Downloader import download
from Yukki.Database import (get_assistant, remove_active_chat,
                            remove_active_video_chat)
from Yukki.Inline import (audio_markup, audio_timer_markup_start,
                          primary_markup, secondary_markup2, timer_markup)
from Yukki.Utilities.changers import time_to_seconds
from Yukki.Utilities.chat import specialfont_to_normal
from Yukki.Utilities.theme import check_theme
from Yukki.Utilities.thumbnails import gen_thumb
from Yukki.Utilities.timer import start_timer
from Yukki.Utilities.youtube import get_m3u8, get_yt_info_id

### Clients
pytgcalls1 = PyTgCalls(ASS_CLI_1)
pytgcalls2 = PyTgCalls(ASS_CLI_2)
pytgcalls3 = PyTgCalls(ASS_CLI_3)
pytgcalls4 = PyTgCalls(ASS_CLI_4)
pytgcalls5 = PyTgCalls(ASS_CLI_5)

### Multi Assistant start


async def join_stream(chat_id: int, file_path: str):
    _assistant = await get_assistant(chat_id, "assistant")
    assistant = _assistant["saveassistant"]
    if int(assistant) == 1:
        try:
            await pytgcalls1.join_group_call(
                chat_id,
                InputStream(
                    InputAudioStream(
                        file_path,
                    ),
                ),
                stream_type=StreamType().local_stream,
            )
            return True
        except:
            return False
    elif int(assistant) == 2:
        try:
            await pytgcalls2.join_group_call(
                chat_id,
                InputStream(
                    InputAudioStream(
                        file_path,
                    ),
                ),
                stream_type=StreamType().local_stream,
            )
            return True
        except:
            return False
    elif int(assistant) == 3:
        try:
            await pytgcalls3.join_group_call(
                chat_id,
                InputStream(
                    InputAudioStream(
                        file_path,
                    ),
                ),
                stream_type=StreamType().local_stream,
            )
            return True
        except:
            return False
    elif int(assistant) == 4:
        try:
            await pytgcalls4.join_group_call(
                chat_id,
                InputStream(
                    InputAudioStream(
                        file_path,
                    ),
                ),
                stream_type=StreamType().local_stream,
            )
            return True
        except:
            return False
    elif int(assistant) == 5:
        try:
            await pytgcalls5.join_group_call(
                chat_id,
                InputStream(
                    InputAudioStream(
                        file_path,
                    ),
                ),
                stream_type=StreamType().local_stream,
            )
            return True
        except:
            return False
    return False


### Join Live Stream


async def join_live_stream(chat_id: int, link: str, quality):
    if int(quality) == 720:
        stream_quality = HighQualityVideo()
    elif int(quality) == 480:
        stream_quality = MediumQualityVideo()
    elif int(quality) == 360:
        stream_quality = LowQualityVideo()
    _assistant = await get_assistant(chat_id, "assistant")
    assistant = _assistant["saveassistant"]
    if int(assistant) == 1:
        try:
            await pytgcalls1.join_group_call(
                chat_id,
                AudioVideoPiped(
                    link,
                    HighQualityAudio(),
                    stream_quality,
                ),
                stream_type=StreamType().live_stream,
            )
            return True
        except:
            return False
    elif int(assistant) == 2:
        try:
            await pytgcalls2.join_group_call(
                chat_id,
                AudioVideoPiped(
                    link,
                    HighQualityAudio(),
                    stream_quality,
                ),
                stream_type=StreamType().live_stream,
            )
            return True
        except:
            return False
    elif int(assistant) == 3:
        try:
            await pytgcalls3.join_group_call(
                chat_id,
                AudioVideoPiped(
                    link,
                    HighQualityAudio(),
                    stream_quality,
                ),
                stream_type=StreamType().live_stream,
            )
            return True
        except:
            return False
    elif int(assistant) == 4:
        try:
            await pytgcalls4.join_group_call(
                chat_id,
                AudioVideoPiped(
                    link,
                    HighQualityAudio(),
                    stream_quality,
                ),
                stream_type=StreamType().live_stream,
            )
            return True
        except:
            return False
    elif int(assistant) == 5:
        try:
            await pytgcalls5.join_group_call(
                chat_id,
                AudioVideoPiped(
                    link,
                    HighQualityAudio(),
                    stream_quality,
                ),
                stream_type=StreamType().live_stream,
            )
            return True
        except:
            return False
    return False


### Join Video Stream


async def join_video_stream(chat_id: int, link: str, quality):
    if int(quality) == 720:
        stream_quality = HighQualityVideo()
    elif int(quality) == 480:
        stream_quality = MediumQualityVideo()
    elif int(quality) == 360:
        stream_quality = LowQualityVideo()
    _assistant = await get_assistant(chat_id, "assistant")
    assistant = _assistant["saveassistant"]
    if int(assistant) == 1:
        try:
            await pytgcalls1.join_group_call(
                chat_id,
                AudioVideoPiped(
                    link,
                    HighQualityAudio(),
                    stream_quality,
                ),
                stream_type=StreamType().local_stream,
            )
            return True
        except Exception as e:
            print(e)
            return False
    elif int(assistant) == 2:
        try:
            await pytgcalls2.join_group_call(
                chat_id,
                AudioVideoPiped(
                    link,
                    HighQualityAudio(),
                    stream_quality,
                ),
                stream_type=StreamType().local_stream,
            )
            return True
        except Exception as e:
            print(e)
            return False
    elif int(assistant) == 3:
        try:
            await pytgcalls3.join_group_call(
                chat_id,
                AudioVideoPiped(
                    link,
                    HighQualityAudio(),
                    stream_quality,
                ),
                stream_type=StreamType().local_stream,
            )
            return True
        except:
            return False
    elif int(assistant) == 4:
        try:
            await pytgcalls4.join_group_call(
                chat_id,
                AudioVideoPiped(
                    link,
                    HighQualityAudio(),
                    stream_quality,
                ),
                stream_type=StreamType().local_stream,
            )
            return True
        except:
            return False
    elif int(assistant) == 5:
        try:
            await pytgcalls5.join_group_call(
                chat_id,
                AudioVideoPiped(
                    link,
                    HighQualityAudio(),
                    stream_quality,
                ),
                stream_type=StreamType().local_stream,
            )
            return True
        except:
            return False
    return False


### Multi Assistant Pause


async def pause_stream(chat_id: int):
    _assistant = await get_assistant(chat_id, "assistant")
    assistant = _assistant["saveassistant"]
    if int(assistant) == 1:
        await pytgcalls1.pause_stream(chat_id)
    elif int(assistant) == 2:
        await pytgcalls2.pause_stream(chat_id)
    elif int(assistant) == 3:
        await pytgcalls3.pause_stream(chat_id)
    elif int(assistant) == 4:
        await pytgcalls4.pause_stream(chat_id)
    elif int(assistant) == 5:
        await pytgcalls5.pause_stream(chat_id)


### Multi Assistant Resume


async def resume_stream(chat_id: int):
    _assistant = await get_assistant(chat_id, "assistant")
    assistant = _assistant["saveassistant"]
    if int(assistant) == 1:
        await pytgcalls1.resume_stream(chat_id)
    elif int(assistant) == 2:
        await pytgcalls2.resume_stream(chat_id)
    elif int(assistant) == 3:
        await pytgcalls3.resume_stream(chat_id)
    elif int(assistant) == 4:
        await pytgcalls4.resume_stream(chat_id)
    elif int(assistant) == 5:
        await pytgcalls5.resume_stream(chat_id)


### Multi Assistant Stop


async def stop_stream(chat_id: int):
    _assistant = await get_assistant(chat_id, "assistant")
    assistant = _assistant["saveassistant"]
    if int(assistant) == 1:
        await pytgcalls1.leave_group_call(chat_id)
        await remove_active_video_chat(chat_id)
    elif int(assistant) == 2:
        await pytgcalls2.leave_group_call(chat_id)
        await remove_active_video_chat(chat_id)
    elif int(assistant) == 3:
        await pytgcalls3.leave_group_call(chat_id)
        await remove_active_video_chat(chat_id)
    elif int(assistant) == 4:
        await pytgcalls4.leave_group_call(chat_id)
        await remove_active_video_chat(chat_id)
    elif int(assistant) == 5:
        await pytgcalls5.leave_group_call(chat_id)
        await remove_active_video_chat(chat_id)


### Multi Assistant Skip


async def skip_stream(chat_id: int, file_path: str):
    _assistant = await get_assistant(chat_id, "assistant")
    assistant = _assistant["saveassistant"]
    if int(assistant) == 1:
        await pytgcalls1.change_stream(
            chat_id,
            InputStream(
                InputAudioStream(
                    file_path,
                ),
            ),
        )
    elif int(assistant) == 2:
        await pytgcalls2.change_stream(
            chat_id,
            InputStream(
                InputAudioStream(
                    file_path,
                ),
            ),
        )
    elif int(assistant) == 3:
        await pytgcalls3.change_stream(
            chat_id,
            InputStream(
                InputAudioStream(
                    file_path,
                ),
            ),
        )
    elif int(assistant) == 4:
        await pytgcalls4.change_stream(
            chat_id,
            InputStream(
                InputAudioStream(
                    file_path,
                ),
            ),
        )
    elif int(assistant) == 5:
        await pytgcalls5.change_stream(
            chat_id,
            InputStream(
                InputAudioStream(
                    file_path,
                ),
            ),
        )


### Multi Assistant Video Skip


async def skip_video_stream(chat_id: int, ytlink: str, quality, mystic):
    if int(quality) == 720:
        stream_quality = HighQualityVideo()
    elif int(quality) == 480:
        stream_quality = MediumQualityVideo()
    elif int(quality) == 360:
        stream_quality = LowQualityVideo()
    _assistant = await get_assistant(chat_id, "assistant")
    assistant = _assistant["saveassistant"]
    if int(assistant) == 1:
        try:
            await pytgcalls1.change_stream(
                chat_id,
                AudioVideoPiped(ytlink, HighQualityAudio(), stream_quality),
            )
        except:
            return await mystic.edit(
                "Failed to Change Video Stream.. Please Skip Again."
            )
    elif int(assistant) == 2:
        try:
            await pytgcalls2.change_stream(
                chat_id,
                AudioVideoPiped(ytlink, HighQualityAudio(), stream_quality),
            )
        except:
            return await mystic.edit(
                "Failed to Change Video Stream.. Please Skip Again."
            )
    elif int(assistant) == 3:
        try:
            await pytgcalls3.change_stream(
                chat_id,
                AudioVideoPiped(ytlink, HighQualityAudio(), stream_quality),
            )
        except:
            return await mystic.edit(
                "Failed to Change Video Stream.. Please Skip Again."
            )
    elif int(assistant) == 4:
        try:
            await pytgcalls4.change_stream(
                chat_id,
                AudioVideoPiped(ytlink, HighQualityAudio(), stream_quality),
            )
        except:
            return await mystic.edit(
                "Failed to Change Video Stream.. Please Skip Again."
            )
    elif int(assistant) == 5:
        try:
            await pytgcalls5.change_stream(
                chat_id,
                AudioVideoPiped(ytlink, HighQualityAudio(), stream_quality),
            )
        except:
            return await mystic.edit(
                "Failed to Change Video Stream.. Please Skip Again."
            )


### Multi Assistant Playout End


async def playout_end(pytgclients, chat_id):
    try:
        Queues.task_done(chat_id)
        if Queues.is_empty(chat_id):
            await remove_active_chat(chat_id)
            await remove_active_video_chat(chat_id)
            await pytgclients.leave_group_call(chat_id)
        else:
            afk = Queues.get(chat_id)["file"]
            finxx = f"{afk[0]}{afk[1]}{afk[2]}"
            got_queue = get_queue.get(chat_id)
            if got_queue:
                got_queue.pop(0)
            aud = 0
            if str(finxx) == "raw":
                videoid = afk
                await pytgclients.change_stream(
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
                    caption=f"🎥<b>__Started Streaming:__</b> {title} \n👤<b>__Requested by:__ </b> {mention}",
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
            elif str(finxx) == "s1s":
                read = (str(afk)).replace("s1s_", "", 1)
                s = read.split("_+_")
                quality = s[0]
                videoid = s[1]
                if int(quality) == 1080:
                    stream_quality = HighQualityVideo()
                    try:
                        await pytgclients.change_stream(
                            chat_id,
                            AudioVideoPiped(
                                videoid, HighQualityAudio(), stream_quality
                            ),
                        )
                    except:
                        return await app.send_message(
                            chat_id,
                            "Some Error occured while switching video stream. Playout is on hold now. Please skip the stream to resume the voice chat.",
                        )
                    c_title = db_mem[afk]["chat_title"]
                    chat_title = await specialfont_to_normal(c_title)
                    buttons = secondary_markup2("Smex1", "283028")
                    mention = db_mem[afk]["username"]
                    finaltext = await app.send_photo(
                        chat_id,
                        photo="Utils/Telegram.JPEG",
                        reply_markup=InlineKeyboardMarkup(buttons),
                        caption=(
                            f"**Video Streaming**\n\n🎥<b>__Started Playing:__ </b>Next Video from Telegram \n👤**__Requested by:__** {mention}"
                        ),
                    )
                else:
                    (
                        title,
                        duration_min,
                        duration_sec,
                        thumbnail,
                    ) = get_yt_info_id(videoid)
                    if int(quality) == 720:
                        stream_quality = HighQualityVideo()
                    elif int(quality) == 480:
                        stream_quality = MediumQualityVideo()
                    elif int(quality) == 360:
                        stream_quality = LowQualityVideo()
                    nrs, ytlink = await get_m3u8(videoid)
                    if nrs == 0:
                        return await app.send_message(
                            chat_id,
                            "Failed to fetch Video Formats for next stream. Please skip the stream to resume the voice chat.",
                        )
                    try:
                        await pytgclients.change_stream(
                            chat_id,
                            AudioVideoPiped(
                                ytlink, HighQualityAudio(), stream_quality
                            ),
                        )
                    except:
                        return await app.send_message(
                            chat_id,
                            "Some Error occured while switching video stream. Playout is on hold now. Please skip the stream to resume the voice chat.",
                        )
                    theme = await check_theme(chat_id)
                    c_title = db_mem[afk]["chat_title"]
                    user_id = db_mem[afk]["user_id"]
                    chat_title = await specialfont_to_normal(c_title)
                    thumb = await gen_thumb(
                        thumbnail, title, user_id, theme, chat_title
                    )
                    buttons = primary_markup(
                        videoid, user_id, duration_min, duration_min
                    )
                    mention = db_mem[afk]["username"]
                    finaltext = await app.send_photo(
                        chat_id,
                        photo=thumb,
                        reply_markup=InlineKeyboardMarkup(buttons),
                        caption=(
                            f"**Video Streaming**\n\n🎥<b>__Started Playing:__ </b>[{title[:25]}](https://www.youtube.com/watch?v={afk}) \n👤**__Requested by:__** {mention}"
                        ),
                    )
                    os.remove(thumb)
                    await start_timer(
                        videoid,
                        duration_min,
                        duration_sec,
                        finaltext,
                        chat_id,
                        "28492",
                        aud,
                    )
            else:
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
                await pytgclients.change_stream(
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


### Multi Assistant Queue Clear


async def clear_queue(chat_id):
    try:
        Queues.clear(chat_id)
    except QueueEmpty:
        pass
    await remove_active_video_chat(chat_id)
    await remove_active_chat(chat_id)


### Playout End For Client 1
@pytgcalls1.on_stream_end()
async def stream_end_handler1(_, update: Update):
    if isinstance(update, StreamAudioEnded):
        pass
    else:
        return
    await playout_end(pytgcalls1, update.chat_id)


### Playout End For Client 2
@pytgcalls2.on_stream_end()
async def stream_end_handler(_, update: Update):
    if isinstance(update, StreamAudioEnded):
        pass
    else:
        return
    await playout_end(pytgcalls2, update.chat_id)


### Playout End For Client 3
@pytgcalls3.on_stream_end()
async def stream_end_handler3(_, update: Update):
    if isinstance(update, StreamAudioEnded):
        pass
    else:
        return
    await playout_end(pytgcalls3, update.chat_id)


### Playout End For Client 4
@pytgcalls4.on_stream_end()
async def stream_end_handler(_, update: Update):
    if isinstance(update, StreamAudioEnded):
        pass
    else:
        return
    await playout_end(pytgcalls4, update.chat_id)


### Playout End For Client 5
@pytgcalls5.on_stream_end()
async def stream_end_handler5(_, update: Update):
    if isinstance(update, StreamAudioEnded):
        pass
    else:
        return
    await playout_end(pytgcalls5, update.chat_id)


### Kicked Handlers


@pytgcalls1.on_kicked()
async def kicked_handler1(_, chat_id: int):
    await clear_queue(chat_id)


@pytgcalls2.on_kicked()
async def kicked_handler2(_, chat_id: int):
    await clear_queue(chat_id)


@pytgcalls3.on_kicked()
async def kicked_handle3(_, chat_id: int):
    await clear_queue(chat_id)


@pytgcalls4.on_kicked()
async def kicked_handler4(_, chat_id: int):
    await clear_queue(chat_id)


@pytgcalls5.on_kicked()
async def kicked_handler5(_, chat_id: int):
    await clear_queue(chat_id)


### Closed Handlers


@pytgcalls1.on_closed_voice_chat()
async def closed_voice_chat_handler1(_, chat_id: int):
    await clear_queue(chat_id)


@pytgcalls2.on_closed_voice_chat()
async def closed_voice_chat_handler2(_, chat_id: int):
    await clear_queue(chat_id)


@pytgcalls3.on_closed_voice_chat()
async def closed_voice_chat_handler3(_, chat_id: int):
    await clear_queue(chat_id)


@pytgcalls4.on_closed_voice_chat()
async def closed_voice_chat_handler4(_, chat_id: int):
    await clear_queue(chat_id)


@pytgcalls5.on_closed_voice_chat()
async def closed_voice_chat_handler5(_, chat_id: int):
    await clear_queue(chat_id)


### Left Handlers


@pytgcalls1.on_left()
async def left_handler1(_, chat_id: int):
    await clear_queue(chat_id)


@pytgcalls2.on_left()
async def left_handler2(_, chat_id: int):
    await clear_queue(chat_id)


@pytgcalls3.on_left()
async def left_handler3(_, chat_id: int):
    await clear_queue(chat_id)


@pytgcalls4.on_left()
async def left_handler4(_, chat_id: int):
    await clear_queue(chat_id)


@pytgcalls5.on_left()
async def left_handler5(_, chat_id: int):
    await clear_queue(chat_id)
