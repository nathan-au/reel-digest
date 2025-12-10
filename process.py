from extraction import download_reel, convert_reel_to_audio, convert_audio_to_text, get_reel_info
from summarization import summarize_reel
from database import insert_reel
import json

def process_reel(reel_url):
    print("\nReceived: " + reel_url)
    print("[0/4] Downloading reel...", end = "", flush = True)
    if (download_reel(reel_url)):
        print("\r[1/4] Extracting audio...", end = "", flush = True)
        if (convert_reel_to_audio()):
            print("\r[2/4] Transcribing speech...", end = "", flush = True)
            if (convert_audio_to_text()):
                print("\r[3/4] Generating summary... ", end = "", flush = True)
                if (summarize_reel()):
                    print("\r[4/4] Process completed.    ")
                    if (get_reel_info(reel_url)):
                        with open("bucket/info.json", "r") as f:
                            info = json.load(f)

                        insert_reel(info.get("id"), info.get("url"), info.get("extractor_key"), info.get("duration"), info.get("thumbnail"), info.get("transcript"), info.get("summary"))
                        
                        return True
    print("Reel could not be processed.\n")
    return False