def accumulator():
    total = 0
    value = None
    while True:
        value = yield total
        if value is None:
            break
        total += value

acc = accumulator()
next(acc)  # Prime the generator

print(acc.send(10))
print(acc.send(20))
print(acc.send(30))