import openai
from api_secret import API_KEY_OPENAI


def ask_computer(prompt):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        max_tokens=100
    )
    return response["choices"][0]["text"]
