import os
import time
import random

apps = ['notepad', 'calc', 'mspaint']

while True:
    app = random.choice(apps)
    os.system(f"start {app}")
    time.sleep(1)