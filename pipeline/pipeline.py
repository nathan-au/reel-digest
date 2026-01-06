from pipeline.extraction import download_audio, recognize_speech, get_reel_id, get_reel_duration, get_reel_description
from pipeline.summarization import generate_summary
from database.insertion import insert_reel
from database.selection import select_saved_summary

def process_reel(reel_url):

    reel_id = get_reel_id(reel_url)
    if (reel_id != None):
        saved_reel_summary = select_saved_summary(reel_id)
        if (saved_reel_summary != None):
            print("[cached] Process complete for <" + reel_url + ">.")
            return saved_reel_summary[0]

    print("[1/4] Downloading audio...", end = "", flush = True)
    download_status = download_audio(reel_url)
    if (download_status == False):
        return None
    
    print("\r[2/4] Extracting content...", end = "", flush = True)
    reel_transcript = recognize_speech()
    if (reel_transcript == None):
        reel_transcript = ""
    reel_description = get_reel_description(reel_url)
    if (reel_description == None):
        reel_description = ""
    if (reel_transcript == "" and reel_description == ""):
        return None
    
    print("\r[3/4] Generating summary...", end = "", flush = True)
    reel_summary = generate_summary(reel_transcript, reel_description)
    if (reel_summary == None):
        return None
    
    print("\r[4/4] Process complete for <" + reel_url + ">.")

    reel_id = get_reel_id(reel_url)
    if (reel_id != None):
        reel_duration = get_reel_duration(reel_url)
        if (reel_duration == None):
            reel_duration = 0
        insert_reel(reel_id, reel_url, reel_summary, reel_duration)
    else:
        print("Reel could not be saved.")
    
    return reel_summary