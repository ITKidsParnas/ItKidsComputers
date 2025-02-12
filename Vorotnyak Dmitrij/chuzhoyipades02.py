import requests

def get_location(ip_address):
    # Используем сервис ipinfo.io для получения информации о местоположении
    response = requests.get(f'https://ipinfo.io/{ip_address}/json')
    data = response.json()
    
    # Проверяем, успешно ли получены данные
    if 'error' not in data:
        return {
            'IP': data.get('ip'),
            'City': data.get('city'),
            'Region': data.get('region'),
            'Country': data.get('country'),
            'Location': data.get('loc'),
            'Organization': data.get('org'),
        }
    else:
        return f"Ошибка: {data['error']['message']}"

# Пример использования функции
ip = '178.178.249.136'  # Замените на интересующий вас IP
location_info = get_location(ip)
print(location_info)