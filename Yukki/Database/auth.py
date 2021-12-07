from typing import Dict, List, Union

from Yukki import db

authdb = db.adminauth


async def is_nonadmin_chat(user_id: int) -> bool:
    user = await authdb.find_one({"user_id": user_id})
    if not user:
        return False
    return True


async def add_nonadmin_chat(user_id: int):
    is_gbanned = await is_nonadmin_chat(user_id)
    if is_gbanned:
        return
    return await authdb.insert_one({"user_id": user_id})


async def remove_nonadmin_chat(user_id: int):
    is_gbanned = await is_nonadmin_chat(user_id)
    if not is_gbanned:
        return
    return await authdb.delete_one({"user_id": user_id})


## Save Auth User

authuserdb = db.authuser


async def get_authuser_count() -> dict:
    chats = authuserdb.find({"chat_id": {"$lt": 0}})
    if not chats:
        return {}
    chats_count = 0
    notes_count = 0
    for chat in await chats.to_list(length=1000000000):
        notes_name = await get_authuser_names(chat["chat_id"])
        notes_count += len(notes_name)
        chats_count += 1
    return {"chats_count": chats_count, "notes_count": notes_count}


async def _get_authusers(chat_id: int) -> Dict[str, int]:
    _notes = await authuserdb.find_one({"chat_id": chat_id})
    if not _notes:
        return {}
    return _notes["notes"]


async def get_authuser_names(chat_id: int) -> List[str]:
    _notes = []
    for note in await _get_authusers(chat_id):
        _notes.append(note)
    return _notes


async def get_authuser(chat_id: int, name: str) -> Union[bool, dict]:
    name = name
    _notes = await _get_authusers(chat_id)
    if name in _notes:
        return _notes[name]
    else:
        return False


async def save_authuser(chat_id: int, name: str, note: dict):
    name = name
    _notes = await _get_authusers(chat_id)
    _notes[name] = note

    await authuserdb.update_one(
        {"chat_id": chat_id}, {"$set": {"notes": _notes}}, upsert=True
    )


async def delete_authuser(chat_id: int, name: str) -> bool:
    notesd = await _get_authusers(chat_id)
    name = name
    if name in notesd:
        del notesd[name]
        await authuserdb.update_one(
            {"chat_id": chat_id}, {"$set": {"notes": notesd}}, upsert=True
        )
        return True
    return False
