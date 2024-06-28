# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)


def table(n):
    for i in range(1, 11):
        yield n * i
        i = i + 1


def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


for i in infinite_sequence():
    print(i)




for i in table(15):
    print(i)

