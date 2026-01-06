from speech_recognition import AudioData, Recognizer

def recognize_speech():
    try:
        reel_audio_data = AudioData.from_file("bucket/reel.wav")
        reel_transcript = Recognizer().recognize_google(reel_audio_data)
        return reel_transcript
    except Exception:
        return None
    
