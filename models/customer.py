import random


class Customer:
    # creating the object
    def __new__(cls, id, name, contactno):
        print("Creating new Customer....")
        instance = super().__new__(cls)
        return instance

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


customer1 = Customer(random.randrange(1000,9999,), "Parameswari", 9952032862)
customer2 = Customer(random.randrange(500,999,), "Vignesh", 8056010299)

customer1()
customer2()
