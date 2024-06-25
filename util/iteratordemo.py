import random

name = "Parameswari"

# print char by char

# for ch in name:
# print(ch,end=" ")

# equivalent in iterator
iterated_name = iter(name)
print(next(iterated_name))
print(next(iterated_name))
print(next(iterated_name))


class Iterator_:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.data = 100
        return self

    def __next__(self):
        data = self.data
        if data > self.limit:
            raise StopIteration
        self.data = data + random.randrange(10)
        return data


# customized iteration
for i in Iterator_(150):
    print(i)
