from yt_dlp import YoutubeDL
from moviepy import VideoFileClip
from speech_recognition import AudioData, Recognizer
from json import dump
def download_reel(reel_url):
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
    except Exception:
        return False
    return True
    
    
def convert_reel_to_audio():
    try:
        reel = VideoFileClip("bucket/reel.mp4")
        reel_audio = reel.audio
        reel_audio.write_audiofile("bucket/reel.wav", logger = None)
    except Exception:
        return False
    return True


def convert_audio_to_text():
    try:
        reel_audio_data = AudioData.from_file("bucket/reel.wav")
        r = Recognizer()
        reel_text = r.recognize_google(reel_audio_data)
        with open("bucket/reel.txt", "w") as f:
            f.write(reel_text)
    except Exception:
        return False
    return True

    

def get_reel_info(reel_url):
    ydl_opts = {
        "quiet": True,
        "noplaylist": True,
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            reel_info = ydl.extract_info(reel_url, download = False)

            with open("bucket/reel.txt", "r") as f:
                reel_text = f.read()
            
            with open("bucket/summary.txt", "r") as f:
                reel_summary = f.read()

            reel_info_json = {
                "id": reel_info.get("id"),
                "url": reel_url,
                "extractor_key": reel_info.get("extractor_key"),
                "duration": reel_info.get("duration"),
                "thumbnail": reel_info.get("thumbnail"),
                "transcript": reel_text,
                "summary": reel_summary
            }

        with open("bucket/info.json", "w") as f:
            dump(reel_info_json, f, indent = 4)
    except Exception:
        return False

    return True