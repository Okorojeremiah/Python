import threading

import time


def my_thread():
    print("Python is bae")
    time.sleep(3)
    print("I love python")


threads = []

for i in range(5):
    th = threading.Thread(target=my_thread)
    th.start()
    threads.append(th)

for th in threads:
    th.join()
