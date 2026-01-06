from pipeline.extraction import download_audio, recognize_speech, get_reel_id
from pipeline.summarization import generate_summary
from database.insertion import insert_reel

def process_reel(reel_url):
    print("[1/4] Downloading audio...", end = "", flush = True)
    download_status = download_audio(reel_url)
    if (download_status == False):
        return None
    print("\r[2/4] Recognizing speech...", end = "", flush = True)
    reel_text = recognize_speech()
    if (reel_text == None):
        return None
    print("\r[3/4] Generating summary...", end = "", flush = True)
    reel_summary = generate_summary(reel_text)
    if (reel_summary == None):
        return None
    print("\r[4/4] Process complete for <" + reel_url + ">.")

    reel_id = get_reel_id(reel_url)
    if (reel_id == None):
        return None
    insert_reel(reel_id, reel_url, reel_summary)
    
    return reel_summary