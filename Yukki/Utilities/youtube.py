from youtubesearchpython import VideosSearch

from Yukki.Utilities.changers import time_to_seconds


def get_yt_info_id(videoid):
    url = f"https://www.youtube.com/watch?v={videoid}"
    results = VideosSearch(url, limit=1)
    for result in results.result()["result"]:
        title = result["title"]
        duration_min = result["duration"]
        thumbnail = result["thumbnails"][0]["url"].split("?")[0]
        if str(duration_min) == "None":
            duration_sec = 0
        else:
            duration_sec = int(time_to_seconds(duration_min))
    return title, duration_min, duration_sec, thumbnail


def get_yt_info_query(query: str):
    results = VideosSearch(query, limit=1)
    for result in results.result()["result"]:
        title = result["title"]
        duration_min = result["duration"]
        thumbnail = result["thumbnails"][0]["url"].split("?")[0]
        videoid = result["id"]
        if str(duration_min) == "None":
            duration_sec = 0
        else:
            duration_sec = int(time_to_seconds(duration_min))
    return title, duration_min, duration_sec, thumbnail, videoid


def get_yt_info_query_slider(query: str, query_type: int):
    a = VideosSearch(query, limit=10)
    result = (a.result()).get("result")
    title = result[query_type]["title"]
    duration_min = result[query_type]["duration"]
    videoid = result[query_type]["id"]
    thumbnail = result[query_type]["thumbnails"][0]["url"].split("?")[0]
    if str(duration_min) == "None":
        duration_sec = 0
    else:
        duration_sec = int(time_to_seconds(duration_min))
    return title, duration_min, duration_sec, thumbnail, videoid
