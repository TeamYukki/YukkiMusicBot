from pyrogram import filters

from Yukki import LOG_GROUP_ID, OWNER_ID, SUDOERS, app
from Yukki.Database import is_on_off


@app.on_message(filters.private & ~filters.user(SUDOERS))
async def bot_forward(client, message):
    if await is_on_off(5):
        if message.text == "/start":
            return
        try:
            await app.forward_messages(
                chat_id=LOG_GROUP_ID,
                from_chat_id=message.from_user.id,
                message_ids=message.message_id,
            )
        except Exception as err:
            print(err)
            return
    else:
        return
