from g4f.client import Client

client = Client()
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "привет"}, {"role": "system", "content": "отвечай только в эмодзи"}],
    web_search=False
)
print(response.choices[0].message.content)