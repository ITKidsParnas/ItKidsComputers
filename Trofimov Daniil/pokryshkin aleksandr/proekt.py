import pygame
import os

# Инициализация Pygame
pygame.mixer.init()

def play_audio(file_path):
    if os.path.exists(file_path):
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        print(f'Воспроизведение: {file_path}')
    else:
        print(f'Файл не найден: {file_path}')

def stop_audio():
    pygame.mixer.music.stop()
    print('Воспроизведение остановлено.')

def main():
    while True:
        command = input('Введите "play <путь к файлу>" для воспроизведения, "stop" для остановки, "exit" для выхода: ')
        
        if command.startswith("play "):
            file_path = command[5:]  # Получаем путь к файлу
            play_audio(file_path)
        elif command == "stop":
            stop_audio()
        elif command == "exit":
            break
        else:
            print('Неизвестная команда. Попробуйте снова.')

if __name__ == "__main__":
    main()







































































































