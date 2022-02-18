from typing import Dict, List, Union

from Yukki import db

videodb = db.yukkivideocalls


## limit


async def get_video_limit(chat_id: int) -> str:
    limit = await videodb.find_one({"chat_id": chat_id})
    if not limit:
        return ""
    return limit["limit"]


async def set_video_limit(chat_id: int, limit: str):
    return await videodb.update_one(
        {"chat_id": chat_id}, {"$set": {"limit": limit}}, upsert=True
    )


## Queue Chats Video


async def get_active_video_chats() -> list:
    chats = videodb.find({"chat_id": {"$lt": 0}})
    if not chats:
        return []
    chats_list = []
    for chat in await chats.to_list(length=1000000000):
        chats_list.append(chat)
    return chats_list


async def is_active_video_chat(chat_id: int) -> bool:
    chat = await videodb.find_one({"chat_id": chat_id})
    if not chat:
        return False
    return True


async def add_active_video_chat(chat_id: int):
    is_served = await is_active_video_chat(chat_id)
    if is_served:
        return
    return await videodb.insert_one({"chat_id": chat_id})


async def remove_active_video_chat(chat_id: int):
    is_served = await is_active_video_chat(chat_id)
    if not is_served:
        return
    return await videodb.delete_one({"chat_id": chat_id})
