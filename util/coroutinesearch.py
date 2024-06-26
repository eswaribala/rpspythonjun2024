def contains_search(search_string):
    print("Search String=%s" % (search_string))

    while True:
        recd_data = (yield)
        # print(recd_data)
        if search_string in recd_data:
            print("Recd_Data=%s" % (recd_data))


# creating the coroutine
coroutine = contains_search(input("Enter Search String"))
# coroutine generator
coroutine.__next__()
coroutine.send("Advanced Python Training on")
coroutine.send("Python Training day3")
coroutine.send("Java Training upcoming")
coroutine.send("Design Pattern Training Planned")
coroutine.close()
