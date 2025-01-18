import requests
from PIL import Image
from io import BytesIO

url = "https://api.craiyon.com/generate"

prompt = input("what paint: ")

response = requests.post(
    url,
    json = {'prompt': prompt}
)

if response.status_code == 200:
    image_url = response.json()['images'][0]

    img_response = requests.get(image_url)
    image = Image.open(BytesIO(requests.get(image_url).content))
    image.save("image.png")
else:
    print("error")
