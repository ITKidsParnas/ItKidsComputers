import requests

# Параметры для запроса
params = {
    "lang": "ru",
    "lat": 53,  # Широта
    "lon": 30,  # Долгота
    "appid": "84061a2a5ff54b490d63bd38d557b06d",  # Ваш API ключ
    "units": "metric"  # Единицы измерения
}

print("Соединение с сервером...")

# Запрос текущей погоды
response_current = requests.get('http://api.openweathermap.org/data/2.5/weather', params=params)
# Запрос прогноза погоды
response_forecast = requests.get('http://api.openweathermap.org/data/2.5/forecast', params=params)

# Проверка успешности запросов
if response_current.status_code == 200 and response_forecast.status_code == 200:
    # Обработка текущей погоды
    print("-------------------Погода сейчас-------------------")
    data_current = response_current.json()
    
    description = data_current.get("weather")[0].get("description")
    print('***********', end='')
    print(description, end='')
    print('***********')
    
    temp = data_current.get("main").get("temp")
    print("Температура (*C):", temp)
    
    humidity = data_current.get("main").get("humidity")
    print("Влажность:", humidity, "%")
    
    wind_speed = data_current.get("wind").get("speed")
    print('Скорость ветра:', wind_speed, "м/с")

    # Обработка прогноза погоды
    print("-------------------На ближайшее время-------------------")
    forecast = response_forecast.json().get('list')[:5]
    
    for i in forecast:
        dt = i.get('dt_txt')
        print(dt, ':')
        print("Будет {}".format(i.get("weather")[0].get("description")))
        print("Подробно:")
        print("    Температура:", i.get("main").get("temp"), "*C")
        print("    Влажность:", i.get("main").get("humidity"), "%")
        
        pressure = int(i.get("main").get("pressure"))
        print("    Давление (мм.рт.ст):", pressure / 133.322)  # Преобразуем давление в мм рт. ст.
        print("-----------------------------------------------------------------------------")
    
    print("Данные от openweathermap.org")

else:
    print("Ошибка при получении данных. Код статуса:", response_current.status_code, response_forecast.status_code)
