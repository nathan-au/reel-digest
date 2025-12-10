from yt_dlp import YoutubeDL
from moviepy import VideoFileClip
from speech_recognition import AudioData, Recognizer
def download_reel(reel_url):
    ydl_opts = {
        "outtmpl": "bucket/reel.mp4",
        "overwrites": True,
        "noplaylist": True
        # "quiet": True
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([reel_url])
            return True
    except Exception:
        return False
    
def convert_reel_to_audio():
    try:
        reel = VideoFileClip("bucket/reel.mp4")
        reel_audio = reel.audio
        reel_audio.write_audiofile("bucket/reel.wav")
        return True
    except Exception:
        return False

def convert_audio_to_text():
    try:
        print("Transcribing audio...")
        reel_audio_data = AudioData.from_file("bucket/reel.wav")
        r = Recognizer()
        reel_text = r.recognize_google(reel_audio_data)
        print(reel_text + "\n")
        return True
    except Exception:
        return False

def extract_reel(reel_url):
    if (download_reel(reel_url) and convert_reel_to_audio() and convert_audio_to_text()):
        return True
    return False