from ollama import generate

def summarize_reel():
    with open("bucket/reel.txt", "r") as f:
        reel_text = f.read()

    response = generate(
        model = "granite4",
        prompt = "Summarize this Instagram reel: " + reel_text
    )

    with open("bucket/summary.txt", "w") as f:
        f.write(response.get("response"))

    return True