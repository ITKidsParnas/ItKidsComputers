import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('IP_СЕРВЕРА', 9999))  # Замените на IP-адрес сервера
    
    while True:
        command = input("Введите команду (или 'exit' для выхода): ")
        client.send(command.encode('utf-8'))
        
        if command.lower() == 'exit':
            break
        
        response = client.recv(4096)
        print(response.decode('utf-8'))
    
    client.close()

if __name__ == "__main__":
    start_client()

















































































