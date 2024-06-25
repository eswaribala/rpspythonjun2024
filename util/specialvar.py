print("Name = %s" % (__name__))

if __name__ == "__main__":
    print("In main...")
else:
    print("Imported...")


# post underscore
class class_:
    def __init__(self):
        self.id = 0
        # pre underscore
        self._name = "Bala"


# create customer object
customer = class_()
print(customer.id)
print(customer._name)
