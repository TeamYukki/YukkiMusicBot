## Yukki Music Bot Configs

- `Required` : If true it is a mandatory var, you can't leave it blank
- `Value Type` : Value type of the config var. Example: If integer , you'll need to input number[1-9] only.


# Mandatory Vars
- These are the minimum required vars need to setup to make Yukki Music Bot functional.

| Number | Config Var | Required | Value Type | Info | Example
|-|-------|---|---|-------|---|
| 1 | API_ID | True | Integer | Get it from my.telegram.org | 
| 2 | API_HASH  | True | Hash | Get it from my.telegram.org | 
| 3 | BOT_TOKEN | True | Token | Get it from [@Botfather](http://t.me/BotFather) in Telegram. | 
| 4 | MONGO_DB_URI | True | URL | Get mongo db : https://telegra.ph/How-To-get-Mongodb-URI-04-06 |
| 5 | DURATION_LIMIT | True | Time (Mins) | Custom max audio(music) duration for voice chat. Default to 60 mins. | 60
| 6 | SONG_DOWNLOAD_DURATION | True | Time (Mins) | Duration Limit for downloading Songs in MP3 or MP4 format from bot. Default to 180 mins. | 180
| 7 | LOG_GROUP_ID | True | Integer | You'll need a Private Group ID for this. Supergroup Needed with id starting from -100 | -1001733534088
| 8 | MUSIC_BOT_NAME | True | String | A name for your Music bot. | Yukki Music
| 9 | OWNER_ID | True | Integer | Your Owner ID for managing your bot. | 83022323


# Non-Mandatory Vars
- These are the extra vars for extra features inside Music Bot.

- You can leave non mandatory vars for now and can add them later.

| Number | Config Var | Required | Value Type | Info | Example
|----|-------|---|---|-------|---|
| 1 | VIDEO_STREAM_LIMIT | False | Integer |  Maximum number of video calls allowed on bot. You can later set it via /set_video_limit on telegram | 3
| 2 | SERVER_PLAYLIST_LIMIT | True | Integer | Maximum Limit Allowed for users to save playlists on bot's server | 30
| 3 | PLAYLIST_FETCH_LIMIT | True | Integer |  MaximuM limit for fetching playlist's track from youtube, spotify, apple links. | 25
| 4 | CLEANMODE_MINS | True | Time(Mins) | Cleanmode time after which bot will delete its old messages from chats | 5
| 5 | SUPPORT_CHANNEL | False | URL | If you've any channel for your music bot , fill it with your channel link | https://t.me/TheYukki
| 6 | SUPPORT_GROUP | False | URL | If you've any group support for your music bot , fill it with your channel link | https://t.me/YukkiSupport


# Bot Vars
- These all vars are used for setting up bot.
- You can edit these vars if you want , else leave all of them as it is.

| Number | Config | Required | Value Type | Info |
|----|-------|-----|-----|-------|
| 1 | PRIVATE_BOT_MODE | False | Bool | Set it true if you want your bot to be private only or False for all groups. |
| 2 | YOUTUBE_EDIT_SLEEP | False | Time(Seconds) | Time sleep duration For Youtube Downloader| 
| 3 | TELEGRAM_EDIT_SLEEP | False | Time(Seconds) | Time sleep duration For Telegram Downloader| 
| 4 | AUTO_LEAVING_ASSISTANT | False | Bool | Set it in True if you want to leave your assistant after a certain amount of time. |
| 5 | ASSISTANT_LEAVE_TIME | False | Time(seconds) | Time after which your assistant account will leave served chats automatically. |
| 6 | AUTO_DOWNLOADS_CLEAR | False | Bool | Set it True if you want to delete downloads after the music playout ends. | 
| 6 | AUTO_SUGGESTION_MODE | False | Bool | Set it True if you want to bot to suggest about bot commands to random chats of your bots. | 



# Spotify Vars
- You can play tracks or playlists from spotify from Yukki Music bot

- You'll need these two vars to make spotify play working. This is not essential , you can leave them blank if you want.

| Number | Config | Required | Value Type | Info |
|----|-------|-----|-----|-------|
| 1 | SPOTIFY_CLIENT_ID | False | Token | Get it from https://developer.spotify.com/dashboard | 
| 2 | SPOTIFY_CLIENT_SECRET | False | Token | Get it from https://developer.spotify.com/dashboard | 


# Heroku Vars
- To work some Heroku compatible modules, this var value required to Access your account to use `get_log`, `usage`, `update` etc etc commands.

- You can fill this var using your API key or Authorization token.

| Number | Config | Required | Value Type | Info |
|----|-------|-----|-----|-------|
| 1 | HEROKU_API_KEY | False | Key | Get it from http://dashboard.heroku.com/account |
| 2 | HEROKU_APP_NAME | False | String | You have to Enter the app name which you gave to identify your Music Bot in Heroku. | 


# Custom Repo Vars
- To use your Yukki as default with all regular Updates and Patches. Also without customizing or modifying as your own choice, this must be filled with Yukki Music Bot Main Repository URL in value.

- If you plan to use Yukki Music Bot with your own customized or modified code, you must fill your own Forked YukkiMusicBot Repository URL in `UPSTREAM_REPO` Var value and the branch name in `UPSTREAM_BRANCH` Var value

| Number | Config | Required | Value Type | Info |
|----|-------|-----|-----|-------|
| 1 | UPSTREAM_REPO | False | URL | Your Upstream Repo URL or Forked Repo. | 
| 2 | UPSTREAM_BRANCH | False | BRANCH | Default Branch of your Upstream Repo URL or Forked Repo.  | 
| 3 | GIT_TOKEN | False | Token | Your GIT TOKEN if your upstream repo is private| 
| 4 | GITHUB_REPO | True | URL |  Your Github Repo url, that will be shown on /start command |



# Images/Thumbnail Vars
- You can change images which are used in Yukki Music Bot.

- You can generate telegaph links from [@YukkiTelegraphBot](http://t.me/YukkiTelegraphBot) and use it here.

| Number | Config | Required | Value Type | Info |
|----|-------|-----|-----|-------|
| 1 | START_IMG_URL | False | URL | Image which comes on /start command in private messages of bot. | 
| 2 | PING_IMG_URL | False | URL | Image which comes on /ping command of bot. | 
| 3 | PLAYLIST_IMG_URL | False | URL | Image which comes on /play command of bot. | 
| 4 | GLOBAL_IMG_URL | False | URL | Image which comes on /stats command of bot. | 
| 5 | STATS_IMG_URL | False | URL | Image which comes on /stats command of bot. | 
| 6 | TELEGRAM_AUDIO_URL | False | URL | This image comes when someone plays audios from telegram. | 
| 7 | TELEGRAM_VIDEO_URL | False | URL | This image comes when someone plays videos from telegram. | 
| 8 | STREAM_IMG_URL | False | URL | This image comes when someone plays m3u8 or index links. | 
| 9 | SOUNCLOUD_IMG_URL | False | URL |  This image comes when someone plays music from soundcloud. | 
| 10 | YOUTUBE_IMG_URL | False | URL |  This image comes if thumbnail generator fails to gen thumb anyhow.. | 



# Multi Assistant Mode

### What is Multi-Assistant Mode?
- One Telegram Account can join upto 500 chats. If your bot is running in higher number of chats it will create a problem for assistant to join and leave chat everytime giving invite link exportation floods too
- You can use upto 5 Assistant Clients ( allowing your bot to atleast work in 2000-2500 chats at a time )

> Setting STRING_SESSION is mandatory and for other vars if you want multi-assistant mode you can set else leave blank.

| Number | Config | Required | Value Type | Info |
|----|-------|-----|-----|-------|
| 1| STRING_SESSION | True | Pyrogram Session | Generate string from [@YukkiStringBot](http://t.me/YukkiStringBot) in Telegram. | 
| 2 | STRING_SESSION2 | False | Pyrogram Session |Generate string from [@YukkiStringBot](http://t.me/YukkiStringBot) in Telegram. | 
| 3 | STRING_SESSION2 | False | Pyrogram Session | Generate string from [@YukkiStringBot](http://t.me/YukkiStringBot) in Telegram. | 
| 4 | STRING_SESSION2 | False | Pyrogram Session | Generate string from [@YukkiStringBot](http://t.me/YukkiStringBot) in Telegram. | 
| 5 | STRING_SESSION2 | False | Pyrogram Session | Generate string from [@YukkiStringBot](http://t.me/YukkiStringBot) in Telegram. | 
