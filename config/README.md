# Yukki Music Bot Configs

Config vars are basically the variables which configure or modify bot to function, which are the basic necessities of plugins or code to work. You have to set the proper mandatory vars to make it functional and to start the basic feature of bot.

### Get to know about all these vars in depth from our Docs. [Read Now from Here](https://notreallyshikhar.gitbook.io/yukkimusicbot/config-vars/available-vars)

## Mandatory Vars

- These are the minimum required vars need to setup to make Yukki Music Bot functional.

1. `API_ID` : Get it from my.telegram.org 
2. `API_HASH`  : Get it from my.telegram.org 
3. `BOT_TOKEN` : Get it from [@Botfather](http://t.me/BotFather) in Telegram
4. `MONGO_DB_URI` : Get mongo db [from here.](https://notreallyshikhar.gitbook.io/yukkimusicbot/deployment/mongodb)
5. `LOG_GROUP_ID` : You'll need a Private Group ID for this. Supergroup Needed with id starting from -100 
6. `MUSIC_BOT_NAME` : A name for your Music bot.
7. `OWNER_ID` : Your Owner ID for managing your bot.
8. `STRING_SESSION` : Pyrogram Session Needed, Generate string from [@YukkiStringBot](http://t.me/YukkiStringBot) in Telegram.


## Non-Mandatory Vars

- These are the extra vars for extra features inside Music Bot. You can leave non mandatory vars for now and can add them later.

1. `DURATION_LIMIT` : Custom max audio(music) duration for voice chat. Default to 60 mins.
2. `SONG_DOWNLOAD_DURATION_LIMIT`  : Duration Limit for downloading Songs in MP3 or MP4 format from bot. Default to 180 mins.
3. `VIDEO_STREAM_LIMIT` : Maximum number of video calls allowed on bot. You can later set it via /set_video_limit on telegram. Default to 3 chats.
4. `SERVER_PLAYLIST_LIMIT` : Maximum Limit Allowed for users to save playlists on bot's server. Default to 30
5. `PLAYLIST_FETCH_LIMIT` :  Maximum limit for fetching playlist's track from youtube, spotify, apple links. Default to 25
6. `CLEANMODE_MINS` : Cleanmode time after which bot will delete its old messages from chats. Default to 5 Mins.
7. `SUPPORT_CHANNEL` : If you've any channel for your music bot , fill it with your channel link
8. `SUPPORT_GROUP` : If you've any group support for your music bot , fill it with your group link

## Play FileSize Limit Vars

- Maximum File size limit for the audio and videos that a user can play from your bot. [Only Bytes Size Accepted]
> You can convert mb into bytes from https://www.gbmb.org/mb-to-bytes and use it here 

1. `TG_AUDIO_FILESIZE_LIMIT` : Maximum file size limit for audio files which can be streamed over vc. Defaults to 104857600 bytes, i.e. 100MB
2. `TG_VIDEO_FILESIZE_LIMIT` : Maximum file size limit for video files which can be played. Defaults to 1073741824 bytes, i.e. 1024MB or 1GB


## Bot Vars

- These all vars are used for setting up bot. You can edit these vars if you want , else leave all of them as it is.

1. `PRIVATE_BOT_MODE` : Set it true if you want your bot to be private only or False for all groups. Default to False
2. `YOUTUBE_EDIT_SLEEP` : Time sleep duration For Youtube Downloader. Default to 3 seconds
3. `TELEGRAM_EDIT_SLEEP` : Time sleep duration For Telegram Downloader. Default to 5 seconds
4. `AUTO_LEAVING_ASSISTANT` : Set it in True if you want to leave your assistant after a certain amount of time.
5. `ASSISTANT_LEAVE_TIME` : Time after which your assistant account will leave served chats automatically. Default to 5400 seconds, i.e 90 Mins
6. `AUTO_DOWNLOADS_CLEAR` : Set it True if you want to delete downloads after the music playout ends. 
7. `AUTO_SUGGESTION_MODE` : Set it True if you want to bot to suggest about bot commands to random chats of your bots. 
9. `AUTO_SUGGESTION_TIME` : Time after which your bot will suggest random 1/10 chats of your served chats about bot commands. Default to 5400 seconds, i.e 90 Mins

## Spotify Vars

- You can play tracks or playlists from spotify from Yukki Music bot
- You'll need these two vars to make spotify play working. This is not essential , you can leave them blank if you want.

### How to get these? [Read from here](https://notreallyshikhar.gitbook.io/yukkimusicbot/deployment/spotify)


1. `SPOTIFY_CLIENT_ID` : Get it from https://developer.spotify.com/dashboard 
2. `SPOTIFY_CLIENT_SECRET` : Get it from https://developer.spotify.com/dashboard 


## Heroku Vars

- To work some Heroku compatible modules, this var value required to Access your account to use `get_log`, `usage`, `update` etc etc commands.
- You can fill this var using your API key or Authorization token.

### How to get these? [Read from here](https://notreallyshikhar.gitbook.io/yukkimusicbot/config-vars/heroku-vars)

1. `HEROKU_API_KEY` : Get it from http://dashboard.heroku.com/account 
2. `HEROKU_APP_NAME` : You have to Enter the app name which you gave to identify your Music Bot in Heroku. 


## Custom Repo Vars

- If you plan to use Yukki Music Bot with your own customized or modified code.

1. `UPSTREAM_REPO` : Your Upstream Repo URL or Forked Repo.
2. `UPSTREAM_BRANCH` : Default Branch of your Upstream Repo URL or Forked Repo. 
3. `GIT_TOKEN` : Your GIT TOKEN if your upstream repo is private
4. `GITHUB_REPO` : Your Github Repo url, that will be shown on /start command



## Images/Thumbnail Vars

- You can change images which are used in Yukki Music Bot.
- You can generate telegaph links from [@YukkiTelegraphBot](http://t.me/YukkiTelegraphBot) and use it here.

1. `START_IMG_URL` : Image which comes on /start command in private messages of bot.
2. `PING_IMG_URL` : Image which comes on /ping command of bot.
3. `PLAYLIST_IMG_URL` : Image which comes on /play command of bot. 
4. `GLOBAL_IMG_URL` : Image which comes on /stats command of bot. 
5. `STATS_IMG_URL` : Image which comes on /stats command of bot. 
6. `TELEGRAM_AUDIO_URL` : This image comes when someone plays audios from telegram. 
7. `TELEGRAM_VIDEO_URL` : This image comes when someone plays videos from telegram. 
8. `STREAM_IMG_URL` : his image comes when someone plays m3u8 or index links.
9. `SOUNCLOUD_IMG_URL` : This image comes when someone plays music from soundcloud. 
10. `YOUTUBE_IMG_URL` : This image comes if thumbnail generator fails to gen thumb anyhow.
11. `SPOTIFY_ARTIST_IMG_URL` : This image comes when someone plays Spotify artist via link in inline mode. 
12. `SPOTIFY_ALBUM_IMG_URL` : This image comes when someone plays Spotify album via link in inline mode. 
13. `SPOTIFY_PLAYLIST_IMG_URL` : This image comes when someone plays Spotify album via link in inline mode. 

## Multi Assistant Mode

- You can use upto 5 Assistant Clients ( allowing your bot to atleast work in 2000-2500 chats at a time )

1. `STRING_SESSION2` : Pyrogram Session Needed, Generate string from [@YukkiStringBot](http://t.me/YukkiStringBot) in Telegram.
2. `STRING_SESSION3` : Pyrogram Session Needed, Generate string from [@YukkiStringBot](http://t.me/YukkiStringBot) in Telegram.
3. `STRING_SESSION4` : Pyrogram Session Needed, Generate string from [@YukkiStringBot](http://t.me/YukkiStringBot) in Telegram.
4. `STRING_SESSION5` : Pyrogram Session Needed, Generate string from [@YukkiStringBot](http://t.me/YukkiStringBot) in Telegram.
