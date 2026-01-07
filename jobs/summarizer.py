from ollama import generate

def generate_summary(reel_transcript, reel_description, screenshot_text):
    try:
        response = generate(
            model = "granite4",
            prompt = (
                f"""
                    You are an expert note-taker and technical explainer. Your job is to carefully process
                    the following video transcript and description to create an organized output that captures everything
                    mentioned.

                    Instructions:
                    - Title: informative phrase 10 words or less to indicate what the video is about.
                    - Key Takeaways: List the top 5 insights from the transcript concisely.
                    - Extra Resources: List any books, papers, tools, or websites the speaker references.
                    - Next Steps: Based strictly on the content of the transcript, infer exactly 3 practical actions a viewer could take to apply the ideas. Present these as a numbered list. Do not introduce new concepts not implied by the transcript.

                    - Do not use markdown-style formatting. 
                    - Plain text only.
                    - Do not reference the video, transcript, or speaker.
                    - NEVER output URLs, hyperlinks, domains, or protocol strings (http, https, www).
                    - If a resource is mentioned as a URL, REMOVE the URL and keep ONLY the resource name.
                    - Output is INVALID if it contains any URL or domain.

                    Transcript: {reel_transcript}\n
                    Description: {reel_description}\n
                    Screenshot Text: {screenshot_text}
                """ 
            )
        )
    except Exception:
        return None
    return response.get("response")