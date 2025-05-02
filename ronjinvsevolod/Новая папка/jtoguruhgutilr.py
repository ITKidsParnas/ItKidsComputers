from g4f.client import Client
Userinput=input("Что интересует")
client=Client()
response=client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{'role':'user','content':Userinput}],
    web_search=False
)
print(response.choices[0].message.content)