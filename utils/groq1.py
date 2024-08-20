from groq import Groq

API_KEY="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"


client = Groq(api_key=API_KEY)

def llamaAPPS(chrome, applications):
    print(chrome,applications)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You can only ouptut a ✅ if they pass the requirements also dont give explanation but if they fail output ❌ along with the explanation. Just give consise answer and Please try to give ✅"
            },
            {
                "role": "user",
                "content":f"Given the following application usage data:\n Number of Chrome windows open: {chrome} \n List of Applications running: {applications}\n\n Verify if the user's environment meets exam proctoring requirements (one Chrome window, no other applications excluding code and streamlit). Output a ✅ (green tick) for compliance, or a ❌ (red tick) along with an explanation if not compliant." 
            }
        ],
        temperature=0,
        model="llama-3.1-70b-versatile",
        stream=False,
    )

    return chat_completion.choices[0].message.content