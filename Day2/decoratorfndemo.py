#defining decorator function
def decorator_func(func):
   def inner_func():
      print ('I am decorated Harry')
      return func
   return inner_func()

@decorator_func
def display():
   print ('Harry')

display()





def perfect_square(str_param):
  def middle_decorator(func):
    def inner(x):
      print (str_param,' of ',x)
      print ('The sqaure of', x ,' is ')
      return func(x)
    return inner
  return middle_decorator

@perfect_square('Find the square')
def display_square(a):
  return a*a

display_square(5)





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