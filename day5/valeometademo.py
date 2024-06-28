class Product(type):
    def getprops(cls):
        print("test data %s" %type(cls))

# Call the metaclass
    def __call__(self, *args, **kwargs):
        # create the new class as normal
        cls = type.__call__(self, *args)


        setattr(cls, "getprops", self.getprops)

        # return the class
        return cls

class CustomizedProduct(object,metaclass=Product):
    def get(self):
        self.getprops()


obj = CustomizedProduct()
obj.get()
