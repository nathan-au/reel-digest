from yt_dlp import YoutubeDL
from core.constants import YDL_OPTS_AUDIO_DOWNLOAD, YDL_OPTS_VIDEO_DOWNLOAD

def download_audio(reel_url):
    try:
        with YoutubeDL(YDL_OPTS_AUDIO_DOWNLOAD) as ydl:
            ydl.download([reel_url])
            return True
    except Exception:
        return False
    
def download_video(reel_url):
    try:
        with YoutubeDL(YDL_OPTS_VIDEO_DOWNLOAD) as ydl:
            ydl.download([reel_url])
        return True
    except Exception:
        return False