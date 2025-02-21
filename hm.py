import openai

openai.api_key = "API_KEY شما"

def chat_with_gpt(user_input):
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=user_input,
      max_tokens=150
    )
    return response.choices[0].text.strip()
