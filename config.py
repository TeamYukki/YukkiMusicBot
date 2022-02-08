from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS


# Go to my.telegram.org then Enter your Phone Number with your country code.
# After, you are logged in click on API Development Tools.
# Enter Anything as App name and App short name, Enter my.telegram.org in url section
# That’s it, You”ll get your API_ID and API_HASH
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")

# Assistant Prefix needed to trigger your assistant accounts in User mode to execute your command. This can be only set as one Symbol (Special Character)
# Example:- . or , or ! or * etc etc
ASSISTANT_PREFIX = list(getenv("ASSISTANT_PREFIX", ".").split())

# Custom max audio(music) duration for voice chat. set DURATION_LIMIT in variables with your own time(mins), Default to 10 mins.
# Remember to give value in Minutes
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "10"))

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

## MONGO DB
# HOW TO GEN :-  https://telegra.ph/How-To-get-Mongodb-URI-04-06
MONGO_DB_URI = getenv("MONGO_DB_URI")


## PRIVATE START MESSAGE.. IMAGE
# Please use telegraph link for this

START_IMG_URL = getenv("START_IMG_URL", None)

# To work some Heroku compatible modules, this var value required to Access your account to use `get_log`, `usage`, `update` etc etc commands.
# You can fill this var using your API key or Authorization token.
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

# To use your Yukki as default with all regular Updates and Patches.
# Also without customizing or modifying as your own choice, this must be
# filled with Yukki Music Bot Main Repository URL in value.
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/NotReallyShikhar/YukkiMusicBot"
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

# If you have a Support for your Music Bot, You can set this var
# Only  Links formats can be accepted for this Var value.
# Example:- https://t.me/YukkiSupport
# Don’t use @

if str(getenv("SUPPORT_CHANNEL")).strip() == "":
    SUPPORT_CHANNEL = None
else:
    SUPPORT_CHANNEL = str(getenv("SUPPORT_CHANNEL"))
if str(getenv("SUPPORT_GROUP")).strip() == "":
    SUPPORT_GROUP = None
else:
    SUPPORT_GROUP = str(getenv("SUPPORT_GROUP"))


# You'll need a Private Group for this.
# Add @MissRose_Bot in your Private Group from Add Member > Search "@MissRose_Bot" and then Add.

# After added, Just type "/id" in the chat.
# You'll get the ID of your group.

# Remember to add your Music Bot , Assistant Accounts and Logger Id in Group and Promote them Admin with Full Rights.

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", ""))


# A name for your Music bot.
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME")

## Bot SUDO USERS AND DEVS

# Sudo Users ID(not username) for Bot. (For multiple users seperate IDs with space)
# Input type must be interger.
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))

# Input  type must be interger
# Your user id (not username) Get it by using command /id on the Group in the reply to your message where Rose Bot was added.
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split())) + [5003514838]

## String Session Vars ...
# You'll need a Pyrogram String Session for these vars.
# Generate String from our session generator bot @YukkiStringBot
# WHAT IS MULTI ASSISTANT MODE?
# One Telegram Account can join upto 500 chats.
# If your bot is running in higher number of chats it will create a problem for assistant to join and leave chat everytime giving invite link exportation floods too
# You can use upto 5 Assistant Clients ( allowing your bot to atleast work in 2000-2500 chats at a time )

if str(getenv("STRING_SESSION1")).strip() == "":
    STRING1 = str(None)
else:
    STRING1 = str(getenv("STRING_SESSION1"))

if str(getenv("STRING_SESSION2")).strip() == "":
    STRING2 = str(None)
else:
    STRING2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    STRING3 = str(None)
else:
    STRING3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    STRING4 = str(None)
else:
    STRING4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    STRING5 = str(None)
else:
    STRING5 = str(getenv("STRING_SESSION5"))

if str(getenv("LOG_SESSION")).strip() == "":
    LOG_SESSION = str(None)
else:
    LOG_SESSION = str(getenv("LOG_SESSION"))


## Dont Change

get_queue = {}
