from yt_dlp import YoutubeDL
from core.constants import YDL_OPTS_INFO

def is_valid_platform(message_text):
    if ("instagram.com" in message_text or "tiktok.com" in message_text or "youtube.com" in message_text):
        return True
    return False

def extract_url(message_text):
    reel_url = message_text.split("?")[0].rstrip('/')
    return reel_url

def is_reel(reel_url):
    try:
        with YoutubeDL(YDL_OPTS_INFO) as ydl:
            post_info = ydl.extract_info(reel_url, download = False)
            post_type = post_info.get("_type")
            post_duration = post_info.get("duration")
        if (not post_type and post_duration):
            return True
        return False
    except Exception:
        return False