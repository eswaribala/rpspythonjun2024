class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
             cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
s = Singleton()
print("Object created", s)
s1 = Singleton()
print("Object created", s1) #returns same instance











#singleton with meta

class MyInt(type):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __call__(cls, *args, **kwds):
        print("***** Here's My int *****", args)
        print("Now do whatever you want with these objects...")
        return type.__call__(cls, *args, **kwds)
class int(metaclass=MyInt):
   pass
i = int(4,5)