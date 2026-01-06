PATH_TO_DATABASE = "data/storage.db"

YDL_OPTS_INFO = {
    "quiet": True,
    "noplaylist": True,
}

YDL_OPTS_AUDIO_DOWNLOAD = {
    "format": "bestaudio/best",
    "outtmpl": "data/bucket/reel",
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "wav",
    }],
    "overwrites": True,
    "noplaylist": True,
    "quiet": True,
    "noprogress": True,
}

YDL_OPTS_VIDEO_DOWNLOAD = {
    "outtmpl": "data/bucket/reel.mp4",
    "overwrites": True,
    "noplaylist": True,
    "quiet": True,
    "noprogress": True,
}