from YukkiMusic import app
from YukkiMusic.utils.database import get_chatmode, get_cmode


async def get_channeplayCB(_, command, CallbackQuery):
    if command == "c":
        chat_id = await get_cmode(CallbackQuery.message.chat.id)
        if chat_id is None:
            try:
                return await CallbackQuery.answer(
                    _["setting_12"], show_alert=True
                )
            except:
                return
        try:
            chat = await app.get_chat(chat_id)
            channel = chat.title
        except:
            try:
                return await CallbackQuery.answer(
                    _["cplay_4"], show_alert=True
                )
            except:
                return
    else:
        chatmode = await get_chatmode(CallbackQuery.message.chat.id)
        if chatmode == "Group":
            chat_id = CallbackQuery.message.chat.id
            channel = None
        else:
            chat_id = await get_cmode(CallbackQuery.message.chat.id)
            if chat_id is None:
                try:
                    return await CallbackQuery.answer(
                        _["setting_12"], show_alert=True
                    )
                except:
                    return
            try:
                chat = await app.get_chat(chat_id)
                channel = chat.title
            except:
                try:
                    return await CallbackQuery.answer(
                        _["cplay_4"], show_alert=True
                    )
                except:
                    return
    return chat_id, channel
