from speech_recognition import AudioData, Recognizer
from cv2 import VideoCapture, CAP_PROP_POS_MSEC, imwrite
from PIL import Image
from pytesseract import image_to_string

def recognize_speech():
    try:
        reel_audio_data = AudioData.from_file("data/bucket/reel.wav")
        reel_transcript = Recognizer().recognize_google(reel_audio_data)
        return reel_transcript
    except Exception:
        return None

def capture_screenshot():
    try:
        cap = VideoCapture("data/bucket/video.mp4")
        if (not cap.isOpened()):
            return False

        cap.set(CAP_PROP_POS_MSEC, 1000) 
        status, screenshot = cap.read()
        if (not status):
            return False
        
        imwrite("data/bucket/screenshot.png", screenshot)
        return True
    except Exception:
        return False
    finally:
        cap.release()

def recognize_text():
    try:
        with Image.open("data/bucket/screenshot.png") as screenshot:
            screenshot = screenshot.convert("L")
            screenshot_text = image_to_string(screenshot)
        return screenshot_text
    except Exception:
        return None
