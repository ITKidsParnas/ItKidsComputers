import requests 
from bs4 import BeautifulSoup
city= input("какой город вам нужен ")
link = f"https://www.google.com/search?q=погода+в+{city}"

headers = {
       "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
        }
responce = requests.get(link, headers=headers)
print(responce)
soup = BeautifulSoup(responce.text, "html.parser")

temperature = soup.select("wob_tm")[0].getText()
humidity = soup.select("wob_hm")[0].getText()
time = soup.select("wob_dts")[0].getText()
wind = soup.select("wob_ws")[0].getText()
osadki = soup.select("wob_pp")[0].getText()
print(time)
print(f"Ветер:{wind}")
print(f"Температура:{temperature}")
print(f"Влажность:{humidity}")
print(f"Осадки:{osadki}")