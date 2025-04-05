from openai import OpenAI

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="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",
)


def chat_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()


def chat():
    x = input()
    chat_gpt(x)


chat()
