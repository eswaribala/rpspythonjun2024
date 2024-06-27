import threading
from threading import *

rlock = RLock()


# recursive function
def countdown(n):
    rlock.acquire()
    print(n)
    # critical section
    if n > 0:
        countdown(n - 1)
    rlock.release()


def invoke_countdown(count):
    print("Count Down Started", countdown(count))


countdown1 = threading.Thread(name="countdown1", target=invoke_countdown, args=(50,))
countdown2 = threading.Thread(name="countdown1", target=invoke_countdown, args=(100,))
countdown1.start()
countdown2.start()
