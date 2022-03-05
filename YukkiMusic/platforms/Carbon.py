#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import random
from os.path import realpath

import aiohttp
from aiohttp import client_exceptions


class UnableToFetchCarbon(Exception):
    pass


themes = [
    "3024-night",
    "a11y-dark",
    "blackboard",
    "base16-dark",
    "base16-light",
    "cobalt",
    "duotone-dark",
    "dracula-pro",
    "hopscotch",
    "lucario",
    "material",
    "monokai",
    "nightowl",
    "nord",
    "oceanic-next",
    "one-light",
    "one-dark",
    "panda-syntax",
    "parasio-dark",
    "seti",
    "shades-of-purple",
    "solarized+dark",
    "solarized+light",
    "synthwave-84",
    "twilight",
    "verminal",
    "vscode",
    "yeti",
    "zenburn",
]

colour = [
    "#FF0000",
    "#FF5733",
    "#FFFF00",
    "#008000",
    "#0000FF",
    "#800080",
    "#A52A2A",
    "#FF00FF",
    "#D2B48C",
    "#00FFFF",
    "#808000",
    "#800000",
    "#00FFFF",
    "#30D5C8",
    "#00FF00",
    "#008080",
    "#4B0082",
    "#EE82EE",
    "#FFC0CB",
    "#000000",
    "#FFFFFF",
    "#808080",
]


class CarbonAPI:
    def __init__(self):
        self.language = "auto"
        self.drop_shadow = True
        self.drop_shadow_blur = "68px"
        self.drop_shadow_offset = "20px"
        self.font_family = "JetBrains Mono"
        self.width_adjustment = True
        self.watermark = False

    async def generate(self, text: str, user_id):
        async with aiohttp.ClientSession(
            headers={"Content-Type": "application/json"},
        ) as ses:
            params = {
                "code": text,
            }
            params["backgroundColor"] = random.choice(colour)
            params["theme"] = random.choice(themes)
            params["dropShadow"] = self.drop_shadow
            params["dropShadowOffsetY"] = self.drop_shadow_offset
            params["dropShadowBlurRadius"] = self.drop_shadow_blur
            params["fontFamily"] = self.font_family
            params["language"] = self.language
            params["watermark"] = self.watermark
            params["widthAdjustment"] = self.width_adjustment
            try:
                request = await ses.post(
                    "https://carbonara.vercel.app/api/cook",
                    json=params,
                )
            except client_exceptions.ClientConnectorError:
                raise UnableToFetchCarbon("Can not reach the Host!")
            resp = await request.read()
            with open(f"cache/carbon{user_id}.jpg", "wb") as f:
                f.write(resp)
            return realpath(f.name)
