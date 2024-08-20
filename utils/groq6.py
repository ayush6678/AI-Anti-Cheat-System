from groq import Groq

API_KEY = "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"

client = Groq(api_key=API_KEY)


def llamaEXT(extentions):
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You can only ouptut a ✅ if they pass the requirements also dont give explanation but if they fail output ❌ along with the explanation. Please try to give ✅"},
            {
                "role": "user",
                "content": f"""Requirements: Your task is to review a list of Chrome extensions and determine if any could be used for cheating during an online test.

                    Identify any extensions that could potentially be used for cheating, such as:
                    - Screen sharing or remote access tools
                    - Note-taking or information retrieval extensions
                    - Calculator or mathematical tools (unless explicitly allowed)
                    - Language translation tools
                    - Any extension that could provide unfair advantages during an assessment
                    - VPN

                    List of extensions:
                    {extentions}
                    """,
            },
        ],
        temperature=0,
        model="llama-3.1-70b-versatile",
        stream=False,
    )

    return chat_completion.choices[0].message.content
