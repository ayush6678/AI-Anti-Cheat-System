from groq import Groq

API_KEY="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"

client = Groq(api_key=API_KEY)

def llamaBLUE(bluetooth):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You can only ouptut a ✅ if they pass the requirements also dont give explanation but if they fail output ❌ along with the explanation."
            },
            {
                "role": "user",
                "content": f"Requirent: Bluetooth should be OFF but {bluetooth}.",
            }
        ],
        temperature=0,
        model="llama-3.1-70b-versatile",
        stream=False,
    )

    return chat_completion.choices[0].message.content