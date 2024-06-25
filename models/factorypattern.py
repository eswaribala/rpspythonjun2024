import random
from abc import ABCMeta, abstractmethod


# abstract class
class Customer(metaclass=ABCMeta):
    @abstractmethod
    def deposit(self, amount):
        pass


class Individual(Customer):

    def __init__(self):
        self.amount = None

    def deposit(self, amount):
        self.amount = amount + amount * 0.06
        print(self.amount)


class Corporate(Customer):

    def __init__(self):
        self.amount = None

    def deposit(self, amount):
        self.amount = amount + amount * 0.17
        print(self.amount)


class FactoryClass(object):

    def choosedeposit(self, object_type):
        return eval(object_type)().deposit(random.randrange(100000))


# abstract class cannot create instance and it can only be inherited
# customer = Customer()
factoryclass = FactoryClass()
type = input("Choose Either Individual or Corporate")
factoryclass.choosedeposit(type)
