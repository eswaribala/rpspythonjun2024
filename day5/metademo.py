class HelloMeta(type):  
    # A hello method
    def hello(cls):
        print("greetings from %s, a HelloMeta type class" % (type(cls())))

    # Call the metaclass
    def __call__(self, *args, **kwargs):
        # create the new class as normal
        cls = type.__call__(self, *args)

        # define a new hello method for each of these classes
        setattr(cls, "hello", self.hello)

        # return the class
        return cls





# Try out the metaclass
class TryHello(object, metaclass=HelloMeta):  
    def greet(self):
        self.hello()

# Create an instance of the metaclass. It should automatically have a hello method
# even though one is not defined manually in the class
# in other words, it is added for us by the metaclass
greeter = TryHello()  
greeter.greet()













def display(self, myName):
    print("RAY, " + myName)

MyList = type('MyList', (list,), dict(x=62, key=display))

ml = MyList()
ml.append("Mango")
print("meta list")
print(ml)
print(ml.x)
ml.key("KARLOS")
print(ml.__class__.__class__)


