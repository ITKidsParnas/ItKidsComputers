from g4f.client import Client

client = Client()
response = client.images.generate(
    model="flux-pro",
    prompt="snake",
    response_format="url"
)

print(f"Generated image URL: {response.data[0].url}")