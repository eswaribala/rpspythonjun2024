import random


class Customer:
    # creating the object
    def __new__(cls, id, name, contactno):
        # singleton class
        if not hasattr(cls, 'instance'):
            cls.instance = super(Customer, cls).__new__(cls)
        return cls.instance

    # initialize attributes of the class
    def __init__(self, id, name, contactno):
        print("Initializing new Customer....")
        self.customerid = id
        self.name = name
        self.contactno = contactno

    # def customer(self):
    # print("Customer Id=%s\t Name=%s \t Contact No=%d" %(self.customerid,self.name,self.contactno))
    # automated invocation instance method call
    def __call__(self):
        print("Customer Id=%s\t Name=%s \t Contact No=%d" % (self.customerid, self.name, self.contactno))


customer1 = Customer(random.randrange(1000, 9999, ), "Parameswari", 9952032862)
customer2 = Customer(random.randrange(500, 999, ), "Vignesh", 8056010299)
customer3 = Customer(random.randrange(1500, 1999, ), "Anjanan", 8056010200)
# get object id
print(customer1)
print(customer2)
print(customer3)

# customer1()
# customer2()
