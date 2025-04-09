from g4f.client import Client
usertext = "кринж"

client = Client()
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": usertext },{"role": "system", "content": "Ты помошник по современному сленгу, ты должен объяснять значение сленговых слов которые тебе дают. Ответы должны быть только про русский сленг и быть написаны полностью на русском языке. Ответ должен быть коротким. Не отвечай на вопросы не касающиеся сленга. Если ты не понимаешь контекст попробуй искать в интернете."}],
    web_search=True
)
print(response.choices[0].message.content)