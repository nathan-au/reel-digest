from yt_dlp import YoutubeDL
from core.constants import YDL_OPTS_INFO

def get_reel_id(reel_url):
    ydl_opts = YDL_OPTS_INFO

    try:
        with YoutubeDL(ydl_opts) as ydl:
            reel_id = ydl.extract_info(reel_url, download = False).get("id")
        return reel_id
    except Exception:
        return None
    
def get_reel_duration(reel_url):
    ydl_opts = YDL_OPTS_INFO

    try:
        with YoutubeDL(ydl_opts) as ydl:
            reel_duration = ydl.extract_info(reel_url, download = False).get("duration")
        return reel_duration
    except Exception:
        return None

def get_reel_description(reel_url):
    ydl_opts = YDL_OPTS_INFO

    try:
        with YoutubeDL(ydl_opts) as ydl:
            reel_description = ydl.extract_info(reel_url, download = False).get("description")
        return reel_description
    except Exception:
        return None