#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import re

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from youtubesearchpython import VideosSearch

import config


class SpotifyAPI:
    def __init__(self):
        self.regex = r"^(https:\/\/open.spotify.com\/)(.*)$"
        self.client_id = config.SPOTIFY_CLIENT_ID
        self.client_secret = config.SPOTIFY_CLIENT_SECRET
        if config.SPOTIFY_CLIENT_ID and config.SPOTIFY_CLIENT_SECRET:
            self.client_credentials_manager = (
                SpotifyClientCredentials(
                    self.client_id, self.client_secret
                )
            )
            self.spotify = spotipy.Spotify(
                client_credentials_manager=self.client_credentials_manager
            )
        else:
            self.spotify = None

    async def valid(self, link: str):
        if re.search(self.regex, link):
            return True
        else:
            return False

    async def track(self, link: str):
        meta = self.spotify.track(link)
        results = VideosSearch(
            f"{meta['name']} {meta['album']['artists'][0]['name']}",
            limit=1,
        )
        for result in results.result()["result"]:
            ytlink = result["link"]
            title = result["title"]
            vidid = result["id"]
            duration_min = result["duration"]
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
        track_details = {
            "title": title,
            "link": ytlink,
            "vidid": vidid,
            "duration_min": duration_min,
            "thumb": thumbnail,
        }
        return track_details, vidid

    async def playlist(self, url):
        playlist = self.spotify.playlist(url)
        playlist_id = playlist["id"]
        thumb = playlist["images"][0]["url"]
        results = []
        for item in playlist["tracks"]["items"]:
            music_track = item["track"]
            shikhar = music_track["id"]
            results.append(shikhar)
        return results, playlist_id, thumb

    async def trackplaylist(self, trackid):
        meta = self.spotify.track(trackid)
        to_search = (
            f"{meta['name']} {meta['album']['artists'][0]['name']}"
        )
        return to_search
