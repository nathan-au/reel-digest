DATABASE_PATH = "database/storage.db"
YDL_OPTS_INFO = {
    "quiet": True,
    "noplaylist": True,
}

YDL_OPTS_DOWNLOAD = {
        "format": "bestaudio/best",
        "outtmpl": "bucket/reel",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "wav",
        }],
        "overwrites": True,
        "noplaylist": True,
        "quiet": True,
        "noprogress": True,
    }