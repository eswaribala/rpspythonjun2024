from memory_profiler import profile
import random
import pickle

def random_string():
    return "".join([chr(64 + random.randint(0, 25)) for _ in range(20)])

@profile
def create_file():
    x = [(random.random(),
          random_string(),
          random.randint(0, 2 ** 64))
         for _ in range(10000) ]

    f = open('machin.flat', 'w')
    for xx in x:
        print (f, xx)
    f.close()

@profile
def load_file():
    y = []
    f = open('machin.flat', 'r')
    for line in f:
        y.append(eval(line))
    f.close()
    return y

if __name__== "__main__":
    create_file()
    load_file()

#python -m memory_profiler