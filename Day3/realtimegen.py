def printer():
    while True:
        data = yield
        print("Processing", data)


def printer_wrapper(gen):
    # Below code to avoid TypeError: can't send non-None value to a just-started generator
    gen.send(None)
    while True:
        x = yield
        gen.send(x)


pr = printer_wrapper(printer())

# Below code to avoid TypeError: can't send non-None value to a just-started generator
pr.send(None)

for x in range(1, 5):
    pr.send(x)