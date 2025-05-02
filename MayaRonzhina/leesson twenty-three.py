from g4f.client import Client
import webbrowser
usertext=input("Что показать:")
client = Client ()
response = client.images.generate(
    model='flux',
    prompt=usertext,
    
)
webbrowser.open(response.data[0].url)
