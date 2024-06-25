import random


# step1
def otp(name):
    # step 2
    def guess(func):
        # step 3
        def compute(rangevalue):
            print(name, ' of ', rangevalue)
            print('Coined Value', rangevalue, ' is ')
            return func(rangevalue)

        return compute

    return guess

#decorator
@otp('Generate OTP')
def invokeotpgen(range):
    #step 4
    print(random.randrange(range))


invokeotpgen(int(input("Enter the range")))
