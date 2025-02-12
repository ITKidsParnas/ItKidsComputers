import socket
import requests

# Получение локального IP-адреса
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Соединяемся с Google DNS
        ip = s.getsockname()[0]  # Получаем локальный IP-адрес
    finally:
        s.close()
    return ip

# Получение внешнего IP-адреса
def get_external_ip():
    response = requests.get("https://api.ipify.org?format=json")
    return response.json()["ip"]

# Преобразование доменного имени в IP-адрес
def get_ip_from_domain(domain):
    return socket.gethostbyname(domain)

if __name__ == "__main__":
    local_ip = get_local_ip()
    print(f"Ваш локальный IP-адрес: {local_ip}")

    external_ip = get_external_ip()
    print(f"Ваш внешний IP-адрес: {external_ip}")

    domain = "example.com"  # Замените на нужное доменное имя
    ip_address = get_ip_from_domain(domain)
    print(f"IP-адрес для {domain}: {ip_address}")
    