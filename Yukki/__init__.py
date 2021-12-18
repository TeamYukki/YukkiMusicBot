import asyncio
import os
import time
from os import listdir, mkdir

from aiohttp import ClientSession
from motor.motor_asyncio import AsyncIOMotorClient as Bot
from rich.console import Console
from rich.table import Table

from config import ASSISTANT_PREFIX, DURATION_LIMIT_MIN, LOG_GROUP_ID
from config import MONGO_DB_URI as mango
from config import MUSIC_BOT_NAME, OWNER_ID, SUDO_USERS, get_queue
from Yukki.Core.Clients.cli import (ASS_CLI_1, ASS_CLI_2, ASS_CLI_3,
                                    ASS_CLI_4, ASS_CLI_5, app)
from Yukki.Core.Logger.Log import (startup_delete_last, startup_edit_last,
                                   startup_send_new)
from Yukki.Utilities.changers import time_to_seconds

loop = asyncio.get_event_loop()
console = Console()

### Modules
MOD_LOAD = []
MOD_NOLOAD = []

### Mongo DB
MONGODB_CLI = Bot(mango)
db = MONGODB_CLI.Yukki

### Boot Time
boottime = time.time()

### Clients
app = app
ASS_CLI_1 = ASS_CLI_1
ASS_CLI_2 = ASS_CLI_2
ASS_CLI_3 = ASS_CLI_3
ASS_CLI_4 = ASS_CLI_4
ASS_CLI_5 = ASS_CLI_5
aiohttpsession = ClientSession()

### Config
SUDOERS = SUDO_USERS
OWNER_ID = OWNER_ID
LOG_GROUP_ID = LOG_GROUP_ID
MUSIC_BOT_NAME = MUSIC_BOT_NAME
DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
ASSISTANT_PREFIX = ASSISTANT_PREFIX

### Bot Info
BOT_ID = 0
BOT_NAME = ""
BOT_USERNAME = ""

### Assistant Info
ASSID1 = 0
ASSNAME1 = ""
ASSUSERNAME1 = ""
ASSMENTION1 = ""
ASSID2 = 0
ASSNAME2 = ""
ASSUSERNAME2 = ""
ASSMENTION2 = ""
ASSID3 = 0
ASSNAME3 = ""
ASSUSERNAME3 = ""
ASSMENTION3 = ""
ASSID4 = 0
ASSNAME4 = ""
ASSUSERNAME4 = ""
ASSMENTION4 = ""
ASSID5 = 0
ASSNAME5 = ""
ASSUSERNAME5 = ""
ASSMENTION5 = ""


async def initiate_bot():
    global SUDOERS, Imp_Modules, OWNER_ID
    global BOT_ID, BOT_NAME, BOT_USERNAME
    global ASSID1, ASSNAME1, ASSMENTION1, ASSUSERNAME1
    global ASSID2, ASSNAME2, ASSMENTION2, ASSUSERNAME2
    global ASSID3, ASSNAME3, ASSMENTION3, ASSUSERNAME3
    global ASSID4, ASSNAME4, ASSMENTION4, ASSUSERNAME4
    global ASSID5, ASSNAME5, ASSMENTION5, ASSUSERNAME5
    os.system("clear")
    header = Table(show_header=True, header_style="bold yellow")
    header.add_column(
        "\x59\x75\x6b\x6b\x69\x20\x4d\x75\x73\x69\x63\x20\x42\x6f\x74\x20\x3a\x20\x54\x68\x65\x20\x4d\x6f\x73\x74\x20\x41\x64\x76\x61\x6e\x63\x65\x64\x20\x4d\x75\x73\x69\x63\x20\x42\x6f\x74"
    )
    console.print(header)
    with console.status(
        "[magenta] Booting up the Bot...",
    ) as status:
        console.print("┌ [red]Booting Up The Clients...\n")
        await app.start()
        console.print("└ [green]Booted Bot Client")
        console.print("\n┌ [red]Booting Up The Assistant Clients...")
        await ASS_CLI_1.start()
        console.print("├ [yellow]Booted Assistant Client 1")
        await ASS_CLI_2.start()
        console.print("├ [yellow]Booted Assistant Client 2")
        await ASS_CLI_3.start()
        console.print("├ [yellow]Booted Assistant Client 3")
        await ASS_CLI_4.start()
        console.print("├ [yellow]Booted Assistant Client 4")
        await ASS_CLI_5.start()
        console.print("├ [yellow]Booted Assistant Client 5")
        await asyncio.sleep(0.5)
        console.print("└ [green]Assistant Clients Booted Successfully!")
        initial = await startup_send_new("Starting Yukki Music Bot...")
        await asyncio.sleep(0.5)
        all_over = await startup_send_new("Checking Required Directories...")
        console.print(
            "\n┌ [red]Checking the existence of Required Directories..."
        )
        if "raw_files" not in listdir():
            mkdir("raw_files")
        if "downloads" not in listdir():
            mkdir("downloads")
        if "cache" not in listdir():
            mkdir("cache")
        if "search" not in listdir():
            mkdir("search")
        console.print("└ [green]Directories Updated!")
        await asyncio.sleep(0.9)
        ___ = await startup_edit_last(
            all_over, "Refurbishing Necessary Data..."
        )
        console.print("\n┌ [red]Refurbishing Necessities...")
        getme = await app.get_me()
        getme1 = await ASS_CLI_1.get_me()
        getme2 = await ASS_CLI_2.get_me()
        getme3 = await ASS_CLI_3.get_me()
        getme4 = await ASS_CLI_4.get_me()
        getme5 = await ASS_CLI_5.get_me()
        BOT_ID = getme.id
        ASSID1 = getme1.id
        ASSID2 = getme2.id
        ASSID3 = getme3.id
        ASSID4 = getme4.id
        ASSID5 = getme5.id
        if getme.last_name:
            BOT_NAME = getme.first_name + " " + getme.last_name
        else:
            BOT_NAME = getme.first_name
        BOT_USERNAME = getme.username
        ASSNAME1 = (
            f"{getme1.first_name} {getme1.last_name}"
            if getme1.last_name
            else getme1.first_name
        )
        ASSUSERNAME1 = getme1.username
        ASSMENTION1 = getme1.mention
        ASSNAME2 = (
            f"{getme2.first_name} {getme2.last_name}"
            if getme2.last_name
            else getme2.first_name
        )
        ASSUSERNAME2 = getme2.username
        ASSMENTION2 = getme2.mention
        ASSNAME3 = (
            f"{getme3.first_name} {getme3.last_name}"
            if getme3.last_name
            else getme3.first_name
        )
        ASSUSERNAME3 = getme3.username
        ASSMENTION3 = getme3.mention
        ASSNAME4 = (
            f"{getme4.first_name} {getme4.last_name}"
            if getme4.last_name
            else getme4.first_name
        )
        ASSUSERNAME4 = getme4.username
        ASSMENTION4 = getme4.mention
        ASSNAME5 = (
            f"{getme5.first_name} {getme5.last_name}"
            if getme5.last_name
            else getme5.first_name
        )
        ASSUSERNAME5 = getme5.username
        ASSMENTION5 = getme5.mention
        console.print("└ [green]Refurbished Successfully!")
        await asyncio.sleep(0.9)
        ____ok = await startup_edit_last(___, "Loading Sudo Users...")
        console.print("\n┌ [red]Loading Sudo Users...")
        sudoersdb = db.sudoers
        sudoers = await sudoersdb.find_one({"sudo": "sudo"})
        sudoers = [] if not sudoers else sudoers["sudoers"]
        for user_id in SUDOERS:
            if user_id not in sudoers:
                sudoers.append(user_id)
                await sudoersdb.update_one(
                    {"sudo": "sudo"},
                    {"$set": {"sudoers": sudoers}},
                    upsert=True,
                )
        SUDOERS = (SUDOERS + sudoers + OWNER_ID) if sudoers else SUDOERS
        await asyncio.sleep(1)
        console.print("└ [green]Loaded Sudo Users Successfully!\n")
        await startup_delete_last(____ok)
        await startup_delete_last(initial)


loop.run_until_complete(initiate_bot())

ASSIDS = []

if ASSID1 not in ASSIDS:
    ASSIDS.append(ASSID1)
if ASSID2 not in ASSIDS:
    ASSIDS.append(ASSID2)
if ASSID3 not in ASSIDS:
    ASSIDS.append(ASSID3)
if ASSID4 not in ASSIDS:
    ASSIDS.append(ASSID4)
if ASSID5 not in ASSIDS:
    ASSIDS.append(ASSID5)


def init_db():
    global db_mem
    db_mem = {}


init_db()
