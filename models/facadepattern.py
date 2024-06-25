class Supplier:

    def isAccessible(self):
        print("Supplier Available")


class Delivery:
    def isAccessible(self):
        print("Delivery System Available")


class Payment:

    def isAccessible(self):
        print("Payment System Ready....")


class AmazonStore:
    def __init__(self):
        self.supplier = Supplier()
        self.delivery = Delivery()
        self.payment = Payment()

    def order(self):
        self.supplier.isAccessible()
        self.delivery.isAccessible()
        self.payment.isAccessible()


amazonStore = AmazonStore()
# facade
amazonStore.order()
