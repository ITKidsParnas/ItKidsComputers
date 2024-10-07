import os
import time
import random

apps = ["notepad", "calc", "mspaint","explorer"]

while True:
 app = random.choice(apps)
 os.system(f"start {app}")
 time.sleep(random.randint(1, 5))