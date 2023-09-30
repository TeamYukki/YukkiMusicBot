#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="Masky Capek",
            description=f"Pause the current playout on group call.",
            thumb_url="https://telegra.ph//file/1bbd14dc24ad0ac0b5d01.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="Udh gk capek",
            description=f"Resume the ongoing playout on group call.",
            thumb_url="https://telegra.ph//file/1bbd14dc24ad0ac0b5d01.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="Cipok Masky",
            description=f"Mute the ongoing playout on group call.",
            thumb_url="https://telegra.ph//file/1bbd14dc24ad0ac0b5d01.jpg",
            input_message_content=InputTextMessageContent("/mute"),
        ),
        InlineQueryResultArticle(
            title="Udh Cipoknya",
            description=f"Unmute the ongoing playout on group call.",
            thumb_url="https://telegra.ph//file/1bbd14dc24ad0ac0b5d01.jpg",
            input_message_content=InputTextMessageContent("/unmute"),
        ),
        InlineQueryResultArticle(
            title="Skip Males",
            description=f"Skip to next track. | For Specific track number: /skip [number] ",
            thumb_url="https://telegra.ph//file/1bbd14dc24ad0ac0b5d01.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="kita putus",
            description="Stop the ongoing playout on group call.",
            thumb_url="https://telegra.ph//file/1bbd14dc24ad0ac0b5d01.jpg",
            input_message_content=InputTextMessageContent("/stop"),
        ),
        InlineQueryResultArticle(
            title="Shuffle Stream",
            description="Shuffle the queued tracks list.",
            thumb_url="https://telegra.ph//file/1bbd14dc24ad0ac0b5d01.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="Seek Stream",
            description="Seek the ongoing stream to a specific duration.",
            thumb_url="https://telegra.ph//file/1bbd14dc24ad0ac0b5d01.jpg",
            input_message_content=InputTextMessageContent("/seek 10"),
        ),
        InlineQueryResultArticle(
            title="Loop Stream",
            description="Loop the current playing music. | Usage: /loop [enable|disable]",
            thumb_url="https://telegra.ph//file/1bbd14dc24ad0ac0b5d01.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
