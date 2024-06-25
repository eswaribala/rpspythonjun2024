import random
from time import sleep


def getnumber():
    for i in range(15):
        yield random.randrange(1,9)
        sleep(1)

for i in range(100):
    for number in getnumber():
        print(number, end="\t")
    print("\n")