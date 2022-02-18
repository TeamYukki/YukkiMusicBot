from typing import Dict, List, Union

from Yukki import db

pytgdb = db.pytg
admindb = db.admin


## Queue Chats Audio


async def get_active_chats() -> list:
    chats = pytgdb.find({"chat_id": {"$lt": 0}})
    if not chats:
        return []
    chats_list = []
    for chat in await chats.to_list(length=1000000000):
        chats_list.append(chat)
    return chats_list


async def is_active_chat(chat_id: int) -> bool:
    chat = await pytgdb.find_one({"chat_id": chat_id})
    if not chat:
        return False
    return True


async def add_active_chat(chat_id: int):
    is_served = await is_active_chat(chat_id)
    if is_served:
        return
    return await pytgdb.insert_one({"chat_id": chat_id})


async def remove_active_chat(chat_id: int):
    is_served = await is_active_chat(chat_id)
    if not is_served:
        return
    return await pytgdb.delete_one({"chat_id": chat_id})


## Music Playing or Paused


async def is_music_playing(chat_id: int) -> bool:
    chat = await admindb.find_one({"chat_id_toggle": chat_id})
    if not chat:
        return True
    return False


async def music_on(chat_id: int):
    is_on = await is_music_playing(chat_id)
    if is_on:
        return
    return await admindb.delete_one({"chat_id_toggle": chat_id})


async def music_off(chat_id: int):
    is_on = await is_music_playing(chat_id)
    if not is_on:
        return
    return await admindb.insert_one({"chat_id_toggle": chat_id})
