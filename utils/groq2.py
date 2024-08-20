from groq import Groq

API_KEY="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"

client = Groq(api_key=API_KEY)

def llamaUSB(devices):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You can only ouptut a ✅ if they pass the requirements also dont give explanation but if they fail output ❌ along with the explanation. Please try to give ✅"
            },
            {
                "role": "user",
                "content": f"Given the following list of USB and HDMI devices: {devices}. If one HDMI display is connected, then its fine but if more than one is there then the requirement is not met. To check this, you have the exhaustive list of HDMI deivces given in the above list"
            }
        ],
        temperature=0,
        model="llama-3.1-70b-versatile",
        stream=False,
    )

    return chat_completion.choices[0].message.content