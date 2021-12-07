from config import LOG_GROUP_ID as _channel_id_

from Yukki.Core.Clients.cli import app, userbot

failure = "Make sure your bot is in your log channel and is promoted as an admin with full rights!"


async def log(_message_):
    try:
        await app.send_message(_channel_id_, f"<b>#LOGGER\n\n{_message_}</b>")
        return bool(1)
    except:
        print(failure)
        return


async def startup_send_new(_message_):
    try:
        entities = await app.send_message(
            _channel_id_, f"<code>{_message_}</code>"
        )
        return entities
    except:
        print(failure)
        return


async def startup_edit_last(_message_id, _message_):
    try:
        entities = await app.edit_message_text(
            _channel_id_, _message_id.message_id, f"<code>{_message_}</code>"
        )
        return entities
    except:
        entities = await startup_send_new(_message_)
        return entities


async def startup_delete_last(_message_id):
    try:
        await app.delete_messages(_channel_id_, _message_id.message_id)
        return bool(1)
    except:
        pass
