import threading
from threading import *

lock = Lock()


def withdraw(amount):
    global balance
    lock.acquire()
    if (balance > amount):
        print("You Transaction initiated and available balance %d" % (balance))
        # critical section
        balance = balance - amount
        print("Collect the cash %d" % (amount))
        print("You Transaction completed and available balance %d" % (balance))
    else:
        print("You Transaction could not be continued due to insufficient balance %d" % (balance))
    lock.release()


balance = 10000
customer1 = threading.Thread(name="Customer1", target=withdraw, args=(5000,))
customer2 = threading.Thread(name="Customer1", target=withdraw, args=(7000,))
customer1.start()
customer2.start()
