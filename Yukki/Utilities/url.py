from typing import Union

from pyrogram.types import Message


def get_url(message_1: Message) -> Union[str, None]:
    messages = [message_1]
    if message_1.reply_to_message:
        messages.append(message_1.reply_to_message)
    text = ""
    offset = None
    length = None
    for message in messages:
        if offset:
            break
        if message.entities:
            for entity in message.entities:
                if entity.type == "url":
                    text = message.text or message.caption
                    offset, length = entity.offset, entity.length
                    break
    if offset in (None,):
        return None
    return text[offset : offset + length]
