from yt_dlp import YoutubeDL
from speech_recognition import AudioData, Recognizer

def download_audio(reel_url):
    ydl_opts = {
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
    
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([reel_url])
            return True
    except Exception:
        return False
    
def recognize_speech():
    try:
        reel_audio_data = AudioData.from_file("bucket/reel.wav")
        reel_text = Recognizer().recognize_google(reel_audio_data)
        return reel_text
    except Exception:
        return None

def get_reel_id(reel_url):
    ydl_opts = {
        "quiet": True,
        "noplaylist": True,
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            reel_id = ydl.extract_info(reel_url, download = False).get("id")
        return reel_id
    except Exception:
        return None