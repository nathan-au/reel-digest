from yt_dlp import YoutubeDL
from moviepy import VideoFileClip
from speech_recognition import AudioData, Recognizer
def download_reel(reel_url):
    print("[0/4] Downloading reel...", end = "", flush = True)
    ydl_opts = {
        "outtmpl": "bucket/reel.mp4",
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
    
def convert_reel_to_audio():
    print("\r[1/4] Extracting audio...", end = "", flush = True)
    try:
        reel = VideoFileClip("bucket/reel.mp4")
        reel_audio = reel.audio
        reel_audio.write_audiofile("bucket/reel.wav", logger = None)

        return True
    except Exception:
        return False

def convert_audio_to_text():
    print("\r[2/4] Transcribing speech...", end = "", flush = True)
    try:
        reel_audio_data = AudioData.from_file("bucket/reel.wav")
        r = Recognizer()
        reel_text = r.recognize_google(reel_audio_data)
        with open("bucket/reel.txt", "w") as f:
            f.write(reel_text)
        return True
    except Exception:
        return False