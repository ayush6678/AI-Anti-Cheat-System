from groq import Groq

API_KEY = "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"

client = Groq(api_key=API_KEY)


def llamaCAM(similarity, ppl1, ppl2):
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You can only ouptut a ✅ if they pass the requirements also dont give explanation but if they fail output ❌ along with the explanation."},
            {
                "role": "user",
                "content": f"""You are an AI agent in a proctoring system. You receive the following data for each comparison:
                1. Similarity Score: {similarity}
                2. Number of people in image 1: {ppl1}
                3. Number of people in image 2: {ppl2}

                Requirements:
                1. The number of people in both images should be exactly 1.
                2. The similarity score should be greater than 0.8.""",
            },
        ],
        temperature=0,
        model="llama-3.1-70b-versatile",
        stream=False,
    )

    return chat_completion.choices[0].message.content
