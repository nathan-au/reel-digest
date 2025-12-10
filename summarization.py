from ollama import generate

def summarize_reel():
    print("\r[3/4] Generating summary... ", end = "", flush = True)
    with open("bucket/reel.txt") as f:
        reel_text = f.read()

    response = generate(
        model = "granite4",
        prompt = "Summarize this Instagram reel: " + reel_text
    )

    return response.get("response")