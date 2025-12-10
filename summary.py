from ollama import generate

def summarize_reel(reel_text):
    print("Summarizing reel...")
    response = generate(
        model = "granite4",
        prompt = "Summarize this Instagram reel: " + reel_text
    )
    print(response.get("response"))
    print("Reel summarized successfully.")
    return response.get("response")