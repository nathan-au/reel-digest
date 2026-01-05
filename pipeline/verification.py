def verify_message(message_text):
    if ("instagram.com" not in message_text):
        return False
    return True

def clean_url(reel_url):
    clean_reel_url = reel_url.split("?")[0]
    clean_reel_url = clean_reel_url.rstrip('/')

    return clean_reel_url