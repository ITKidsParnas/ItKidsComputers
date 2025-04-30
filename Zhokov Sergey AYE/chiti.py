import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super().__init__()
        self.delay = delay
        self.button = button
        self.is_clicking = False
        self.is_running = True

    def start_clicking(self):
        self.is_clicking = True

    def stop_clicking(self):
        self.is_clicking = False

    def exit(self):
        self.stop_clicking()
        self.is_running = False

    def run(self):
        mouse = Controller()
        while self.is_running:
            while self.is_clicking:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


def on_press(key):
    if key == start_stop_key:
        if click_thread.is_clicking:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()  # Gracefully exit the thread
        listener.stop()


if __name__ == "__main__":
    delay = float(input("Введите задержку между кликами (например, 0.001): ") or 0.001)
    button_input = input("Введите 'left' для левой кнопки или 'right' для правой: ").strip().lower()
    button = Button.left if button_input == 'left' else Button.right

    start_stop_key = KeyCode(char='r')  # Клавиша для запуска/остановки кликов
    exit_key = KeyCode(char='e')  # Клавиша для выхода

    click_thread = ClickMouse(delay, button)
    click_thread.start()

    with Listener(on_press=on_press) as listener:
        listener.join()
