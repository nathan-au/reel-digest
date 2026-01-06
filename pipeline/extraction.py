from yt_dlp import YoutubeDL
from speech_recognition import AudioData, Recognizer
from core.constants import YDL_OPTS_INFO, YDL_OPTS_DOWNLOAD

def download_audio(reel_url):
    ydl_opts = YDL_OPTS_DOWNLOAD

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([reel_url])
            return True
    except Exception:
        return False
    
def recognize_speech():
    try:
        reel_audio_data = AudioData.from_file("bucket/reel.wav")
        reel_transcript = Recognizer().recognize_google(reel_audio_data)
        return reel_transcript
    except Exception:
        return None

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