from groq import Groq

API_KEY = "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"

client = Groq(api_key=API_KEY)


def llamaRESULT(result):
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You can only ouptut a ✅ if they pass the requirements also dont give explanation but if they fail output ❌ along with the explanation. "},
            {
                "role": "user",
                "content": f"""
                Given response from other agents: {result}
                Requirements: Your task is to check if all the requirements are satisfactory or not. If not, then give the output:
                "❌ All Requirements are not met. Please fix the shortcomings and re-run the system check."
                If the requirements are satisfactory, then give the output:
                "✅ Your System has met all the conditions to start the test. You are Good to Go!"
                    """,
            },
        ],
        temperature=0,
        model="llama-3.1-70b-versatile",
        stream=False,
    )

    return chat_completion.choices[0].message.content
