import psutil
import ctypes
import time
import pygetwindow as gw 


def close_window(title):
    for window in gw.getWindowsWithTitle(title):
        try:
            if window.title==title:
                hwnd=window._hWnd
                ctypes.windll.user32.PostMessageW(hwnd,0x0010,0,0)
        except Exception as e:
            print("Ошибка закрытия")
excluded_titles=["Visual Studio Code," "Code"]
def monitor_and_close():
    active_window_title=""
    start_time=0

    while True:
        try:
            windows=gw.getActiveWindowTitle("")
            active_window=next((w for w in windows if w.isActive),None)
            if active_window:
                current_title=active_window.title

                if current_title != active_window_title:
                    active_window_title=current_title
                    start_time=time.time()
                elif time.time()-start_time>=2:
                    if not any(excluded in active_window_title for excluded in excluded_titles):
                        print(f"Закрываю:{active_window_title}")
                        active_window_title=""
            time.sleep(0.1)
        except Exception as e:
            print(f"Ошибка:{e}")
            break
if __name__=="__main__":
    monitor_and_close()