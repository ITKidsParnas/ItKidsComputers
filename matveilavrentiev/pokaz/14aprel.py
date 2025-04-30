import random
import time
import winsound

def play_sound(duration):
    sounds = [
        winsound.MB_ICONASTERISK,
        winsound.MB_ICONEXCLAMATION,
        winsound.MB_ICONHAND,
        winsound.MB_ICONQUESTION,
        winsound.MB_OK
    ]

    end_time = time.time() + duration

    while time.time() < end_time:
        sound = random.choice(sounds)
        winsound.MessageBeep(sound)
        time.sleep(0.5)

if __name__ == "__main__":
   play_sound(10)