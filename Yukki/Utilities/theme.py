import random

from Yukki.Database import get_theme

themes = [
    "blue",
    "black",
    "red",
    "green",
    "grey",
    "orange",
    "pink",
    "yellow",
]


async def check_theme(chat_id: int):
    _theme = await get_theme(chat_id, "theme")
    if not _theme:
        theme = random.choice(themes)
    else:
        theme = _theme["theme"]
        if theme == "Random":
            theme = random.choice(themes)
    return theme
