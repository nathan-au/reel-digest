from ollama import generate

def summarize_reel():
    with open("bucket/reel.txt", "r") as f:
        reel_text = f.read()

    # response = generate(
    #     model = "granite4",
    #     prompt = "Summarize this Instagram reel: " + reel_text
    # )

    response = generate(
        model = "granite4",
        prompt = (
            """
                You are an expert note-taker and technical explainer. Your job is to carefully process
                the following video transcript and create an organized output that captures everything
                mentioned, without omitting anything.

                Instructions:
                - Key Takeaways: List the top 5 insights from the transcript.
                - Extra Resources Mentioned: List any books, papers, tools, or websites the speaker references.
                - Next Steps: Based strictly on the content of the transcript, infer exactly 3 practical actions a viewer could take to apply the ideas. Present these as a numbered list. Do not introduce new concepts not implied by the transcript.

                Transcript:\n
            """ + reel_text
        )
    )

    with open("bucket/summary.txt", "w") as f:
        f.write(response.get("response"))

    return True

if __name__ == "__main__":
    summarize_reel()