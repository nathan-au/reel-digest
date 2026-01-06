from yt_dlp import YoutubeDL
from core.constants import YDL_OPTS_AUDIO_DOWNLOAD, YDL_OPTS_VIDEO_DOWNLOAD

def download_audio(reel_url):
    ydl_opts = YDL_OPTS_AUDIO_DOWNLOAD

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([reel_url])
            return True
    except Exception:
        return False
    
def download_video(reel_url):
    ydl_opts = YDL_OPTS_VIDEO_DOWNLOAD

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([reel_url])
        return True
    except Exception:
        return False