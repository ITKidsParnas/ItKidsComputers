import os
import time
import random
from win10toast import ToastNotifier

toaster = ToastNotifier()
toaster.show_toast("Nofication", "Это уведомление", duration=5)