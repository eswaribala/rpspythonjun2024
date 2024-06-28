def coroutine_name(name):
    print("Searching prefix:{}".format(name))
    while True:
        C_name = (yield)
        if name in C_name:
            print(C_name)


# search python and return only matching rows
co_routine = coroutine_name("Python")
co_routine.__next__()
co_routine.send("Python is a powerful programming language.")
co_routine.send("Java is the great one!")
co_routine.send("Kotlin is evergreen.")
co_routine.send("Python has a lot of fields for building applications.")
co_routine.send("Python is vastly used in data science.")
co_routine.close()
