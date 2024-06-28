# PythonDecorators/my_decorator.py
class greeting_decorator(object):

    def __init__(self, f):
        print("inside greeting_decorator.__init__()")
        f() # Prove that function definition has completed

    def __call__(self):
        print("inside greeting_decorator.__call__()")

@greeting_decorator
def invoke():
    print("inside invoke()")

print("Finished decorating invoke()")

invoke()

#-------------------------------------------------------------

class entry_exit(object):

    def __init__(self, f):
        self.f = f

    def __call__(self):
        print("Entering", self.f.__name__)
        self.f()
        print("Exited", self.f.__name__)

@entry_exit
def func1():
    print("inside func1()")

@entry_exit
def func2():
    print("inside func2()")

func1()
func2()
#--------------------------------------------------
class decorator_without_arguments(object):

    def __init__(self, f):
        """
        If there are no decorator arguments, the function
        to be decorated is passed to the constructor.
        """
        print("Inside __init__()")
        self.f = f

    def __call__(self, *args):
        """
        The __call__ method is not called until the
        decorated function is called.
        """
        print("Inside __call__()")
        self.f(*args)
        print("After self.f(*args)")

@decorator_without_arguments
def decorate(a1, a2, a3, a4):
    print('decorate arguments:', a1, a2, a3, a4)

print("After decoration")

print("Preparing to call sayHello()")
decorate("check", "log", "argument", "list")
print("After first decorate() call")
decorate("a", "different", "set of", "arguments")
print("After second decorate() call")

#-----------------------------------------------------
class decorator_with_arguments(object):

    def __init__(self, arg1, arg2, arg3):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        print("Inside __init__()")
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """
        print("Inside __call__()")
        def wrapped_f(*args):
            print("Inside wrapped_f()")
            print("Decorator arguments:", self.arg1, self.arg2, self.arg3)
            f(*args)
            print("After f(*args)")
        return wrapped_f

@decorator_with_arguments("BMW", "Q4", 42)
def decorate(a1, a2, a3, a4):
    print('decorate arguments:', a1, a2, a3, a4)

print("After decoration")

print("Preparing to call sayHello()")
decorate("check", "log", "argument", "list")
print("After first decorate() call")
decorate("a", "different", "set of", "arguments")
print("After second decorate() call")