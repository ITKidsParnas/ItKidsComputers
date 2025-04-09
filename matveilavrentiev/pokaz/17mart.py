from g4f.client import Client
import webbrowser
usertext=input("Что покозать")
Client = Client()
response = Client.images.generate(
    model='dall-e-3',
    prompt=usertext,
    response_format='url'
)
webbrowser.open(response.data[0].url)