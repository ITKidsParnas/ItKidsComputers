from g4f.client import Client
import webbrowser
usertext=input("Что показать:")
client=Client()
response=client.images.generate(
    model='dall-e-3',
    prompt=usertext,
    response_format='url'
)
webbrowser.open(response.data[0].url)