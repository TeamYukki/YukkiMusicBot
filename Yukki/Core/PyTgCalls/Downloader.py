from os import path

from yt_dlp import YoutubeDL

from Yukki import MUSIC_BOT_NAME

ytdl = YoutubeDL(
    {
        "outtmpl": "downloads/%(id)s.%(ext)s",
        "format": "bestaudio/best",
        "geo_bypass": True,
        "nocheckcertificate": True,
        "quiet": True,
        "no_warnings": True,
    }
)


def download(videoid: str, mystic, title) -> str:
    flex = {}
    url = f"https://www.youtube.com/watch?v={videoid}"

    def my_hook(d):
        if d.get("status") == "downloading":
            percentage = d.get("_percent_str")
            per = (str(percentage)).replace(".", "", 1).replace("%", "", 1)
            per = int(per)
            eta = d.get("eta")
            speed = d.get("_speed_str")
            size = d.get("_total_bytes_str")
            bytesx = d.get("total_bytes")
            if str(bytesx) in flex:
                pass
            else:
                flex.get(str(bytesx)) = 1
            if flex.get(str(bytesx)) == 1:
                flex.get(str(bytesx)) += 1
                try:
                    if eta > 2:
                        mystic.edit(
                            f"**{MUSIC_BOT_NAME} Downloader**\n\n**Title:** {title[:50]}:\n**FileSize:** {size}\n\n**<u>Downloaded:</u>**\n**Speed:** {speed}\n**ETA:** {eta} Seconds\n\n\n{percentage} ▓▓▓▓▓▓▓▓▓▓▓▓ 100%"
                        )
                except Exception as e:
                    pass
            if per > 250:
                if flex.get(str(bytesx)) == 2:
                    flex.get(str(bytesx)) += 1
                    if eta > 2:
                        mystic.edit(
                            f"**{MUSIC_BOT_NAME}Downloader**\n\n**Title:** {title[:50]}:\n**FileSize:** {size}\n\n**<u>Downloaded:</u>**\n**Speed:** {speed}\n**ETA:** {eta} Seconds\n\n\n{percentage} ███▓▓▓▓▓▓▓▓▓ 100%"
                        )
            if per > 500:
                if flex.get(str(bytesx)) == 3:
                    flex.get(str(bytesx)) += 1
                    if eta > 2:
                        mystic.edit(
                            f"**{MUSIC_BOT_NAME} Downloader**\n\n**Title:** {title[:50]}:\n**FileSize:** {size}\n\n**<u>Downloaded:</u>**\n**Speed:** {speed}\n**ETA:** {eta} Seconds\n\n\n{percentage} ██████▓▓▓▓▓▓ 100%"
                        )
            if per > 800:
                if flex.get(str(bytesx)) == 4:
                    flex.get(str(bytesx)) += 1
                    if eta > 2:
                        mystic.edit(
                            f"**{MUSIC_BOT_NAME} Downloader**\n\n**Title:** {title[:50]}:\n**FileSize:** {size}\n\n**<u>Downloaded:</u>**\n**Speed:** {speed}\n**ETA:** {eta} Seconds\n\n\n{percentage} ██████████▓▓ 100%"
                        )
        if d["status"] == "finished":
            try:
                taken = d.get("_elapsed_str")
            except Exception as e:
                taken = "00:00"
            size = d.get("_total_bytes_str")
            mystic.edit(
                f"**{MUSIC_BOT_NAME} Downloader**\n\n**Title:** {title[:50]}:\n\n100% ████████████100%\n\n**Time Taken:** {taken} Seconds\n\nConverting Audio[FFmpeg Process]"
            )

    ydl_optssx = {
        "format": "bestaudio/best",
        "outtmpl": "downloads/%(id)s.%(ext)s",
        "geo_bypass": True,
        "nocheckcertificate": True,
        "quiet": True,
        "no_warnings": True,
    }
    try:
        x = YoutubeDL(ydl_optssx)
        x.add_progress_hook(my_hook)
        dloader = x.download([url])
    except Exception as y_e:
        return print(y_e)
    else:
        dloader
    info = x.extract_info(url, False)
    xyz = path.join("downloads", f"{info['id']}.{info['ext']}")
    return xyz
