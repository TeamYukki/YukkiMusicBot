#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import asyncio

from pyrogram import filters

import config
from strings import get_command
from YukkiMusic import app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.utils.database.memorydatabase import get_video_limit
from YukkiMusic.utils.formatters import convert_bytes

VARS_COMMAND = get_command("VARS_COMMAND")


@app.on_message(filters.command(VARS_COMMAND) & SUDOERS)
async def varsFunc(client, message):
    mystic = await message.reply_text(
        "Please wait.. Getting your config"
    )
    v_limit = await get_video_limit()
    bot_name = config.MUSIC_BOT_NAME
    up_r = f"[Repo]({config.UPSTREAM_REPO})"
    up_b = config.UPSTREAM_BRANCH
    auto_leave = config.AUTO_LEAVE_ASSISTANT_TIME
    yt_sleep = config.YOUTUBE_DOWNLOAD_EDIT_SLEEP
    tg_sleep = config.TELEGRAM_DOWNLOAD_EDIT_SLEEP
    playlist_limit = config.SERVER_PLAYLIST_LIMIT
    fetch_playlist = config.PLAYLIST_FETCH_LIMIT
    song = config.SONG_DOWNLOAD_DURATION
    play_duration = config.DURATION_LIMIT_MIN
    cm = config.CLEANMODE_DELETE_MINS
    auto_sug = config.AUTO_SUGGESTION_TIME
    if config.AUTO_LEAVING_ASSISTANT == str(True):
        ass = "Yes"
    else:
        ass = "No"
    if config.PRIVATE_BOT_MODE == str(True):
        pvt = "Yes"
    else:
        pvt = "No"
    if config.AUTO_SUGGESTION_MODE == str(True):
        a_sug = "Yes"
    else:
        a_sug = "No"
    if config.AUTO_DOWNLOADS_CLEAR == str(True):
        down = "Yes"
    else:
        down = "No"

    if not config.GITHUB_REPO:
        git = "No"
    else:
        git = f"[Repo]({config.GITHUB_REPO})"
    if not config.START_IMG_URL:
        start = "No"
    else:
        start = f"[Image]({config.START_IMG_URL})"
    if not config.SUPPORT_CHANNEL:
        s_c = "No"
    else:
        s_c = f"[Channel]({config.SUPPORT_CHANNEL})"
    if not config.SUPPORT_GROUP:
        s_g = "No"
    else:
        s_g = f"[Group]({config.SUPPORT_GROUP})"
    if not config.GIT_TOKEN:
        token = "No"
    else:
        token = "Yes"
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        sotify = "No"
    else:
        sotify = "Yes"
    owners = [str(ids) for ids in config.OWNER_ID]
    owner_id = " ,".join(owners)
    tg_aud = convert_bytes(config.TG_AUDIO_FILESIZE_LIMIT)
    tg_vid = convert_bytes(config.TG_VIDEO_FILESIZE_LIMIT)
    text = f"""**MUSIC BOT CONFIG:**

**<u>Basic Vars:</u>**
`MUSIC_BOT_NAME` : **{bot_name}**
`DURATION_LIMIT` : **{play_duration} min**
`SONG_DOWNLOAD_DURATION_LIMIT` :** {song} min**
`OWNER_ID` : **{owner_id}**
    
**<u>Custom Repo Vars:</u>**
`UPSTREAM_REPO` : **{up_r}**
`UPSTREAM_BRANCH` : **{up_b}**
`GITHUB_REPO` :** {git}**
`GIT_TOKEN `:** {token}**


**<u>Bot Vars:</u>**
`AUTO_LEAVING_ASSISTANT` : **{ass}**
`ASSISTANT_LEAVE_TIME` : **{auto_leave} seconds**
`AUTO_SUGGESTION_MODE` :** {a_sug}**
`AUTO_SUGGESTION_TIME` : **{auto_sug} seconds**
`AUTO_DOWNLOADS_CLEAR` : **{down}**
`PRIVATE_BOT_MODE` : **{pvt}**
`YOUTUBE_EDIT_SLEEP` : **{yt_sleep} seconds**
`TELEGRAM_EDIT_SLEEP` :** {tg_sleep} seconds**
`CLEANMODE_MINS` : **{cm} mins**
`VIDEO_STREAM_LIMIT` : **{v_limit} chats**
`SERVER_PLAYLIST_LIMIT` :** {playlist_limit}**
`PLAYLIST_FETCH_LIMIT` :** {fetch_playlist}**

**<u>Spotify Vars:</u>**
`SPOTIFY_CLIENT_ID` :** {sotify}**
`SPOTIFY_CLIENT_SECRET` : **{sotify}**

**<u>Playsize Vars:</u>**
`TG_AUDIO_FILESIZE_LIMIT` :** {tg_aud}**
`TG_VIDEO_FILESIZE_LIMIT` :** {tg_vid}**

**<u>URL Vars:</u>**
`SUPPORT_CHANNEL` : **{s_c}**
`SUPPORT_GROUP` : ** {s_g}**
`START_IMG_URL` : ** {start}**
    """
    await asyncio.sleep(1)
    await mystic.edit_text(text)
