from pyparsing import Word, OneOrMore, Optional, Group, Suppress,alphanums
import subprocess
import time
class NotePad:
    def __init__(self):
        self.is_open = False
    def __str__(self):
        return 'open' if self.is_open else 'closed'
    def open(self):
        print('opening the notepad')
        self.open=subprocess.Popen('notepad.exe',
                         shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
        #self.is_open = True
    def close(self):
        print('closing the notepad', self.open.pid)
        self.open.kill(self)
        #self.is_open = False

class Gate:
    def __init__(self):
        self.is_open = False
    def __str__(self):
        return 'open' if self.is_open else 'closed'
    def open(self):
        print('opening the gate')
        self.is_open = True
    def close(self):
        print('closing the gate')
        self.is_open = False

class Garage:
    def __init__(self):
        self.is_open = False
    def __str__(self):
        return 'open' if self.is_open else 'closed'
    def open(self):
        print('opening the garage')
        self.is_open = True
    def close(self):
        print('closing the garage')
        self.is_open = False

class Aircondition:
    def __init__(self):
        self.is_on = False
    def __str__(self):
        return 'on' if self.is_on else 'off'
    def turn_on(self):
        print('turning on the aircondition')
        self.is_on = True
    def turn_off(self):
        print('turning off the aircondition')
        self.is_on = False

class Heating:
    def __init__(self):
        self.is_on = False
    def __str__(self):
        return 'on' if self.is_on else 'off'
    def turn_on(self):
        print('turning on the heating')
        self.is_on = True
    def turn_off(self):
        print('turning off the heating')
        self.is_on = False

class Boiler:
    def __init__(self):
        self.temperature = 83  # in celsius

    def __str__(self):
        return 'boiler temperature: {}'.format(self.temperature)

    def increase_temperature(self, amount):
        print("increasing the boiler's temperature by {} degrees".
              format(amount))
        self.temperature += amount

    def decrease_temperature(self, amount):
        print("decreasing the boiler's temperature by {} degrees".
              format(amount))
        self.temperature -= amount

class Fridge:
    def __init__(self):

        self.temperature = 2  # in celsius

    def __str__(self):
        return 'fridge temperature: {}'.format(self.temperature)

    def increase_temperature(self, amount):
        print("increasing the fridge's temperature by {} degrees".
              format(amount))

        self.temperature += amount

    def decrease_temperature(self, amount):
        print("decreasing the fridge's temperature by {} degrees".
              format(amount))

        self.temperature -= amount

def main():
    word = Word(alphanums)
    command = Group(OneOrMore(word))
    token = Suppress("->")
    device = Group(OneOrMore(word))
    argument = Group(OneOrMore(word))
    event = command + token + device + Optional(token + argument)
    notepad=NotePad()
    gate = Gate()
    garage = Garage()
    airco = Aircondition()
    heating = Heating()
    boiler = Boiler()
    fridge = Fridge()
    tests = ('open->notepad','open -> gate',
    'close -> garage','close -> notepad',
    'turn on -> aircondition',
    'turn off -> heating',
    'increase -> boiler temperature -> 5 degrees',
    'decrease -> fridge temperature -> 2 degrees')

    open_actions = {'notepad':notepad.open,'gate': gate.open, 'garage': garage.open,
                    'aircondition': airco.turn_on,
                    'heating': heating.turn_on, 'boiler\
                        temperature':boiler.increase_temperature,
                                   'fridge temperature': fridge.increase_temperature}
    close_actions = {'notepad': notepad.close,'gate': gate.close, 'garage': garage.close,
                     'aircondition': airco.turn_off,
                     'heating': heating.turn_off, 'boiler\
                         temperature':boiler.decrease_temperature,
                                    'fridge temperature': fridge.decrease_temperature}
    for t in tests:
        if len(event.parseString(t)) == 2:  # no argument
            cmd, dev = event.parseString(t)
            cmd_str, dev_str = ' '.join(cmd), ' '.join(dev)
            if 'open' in cmd_str or 'turn on' in cmd_str:
                open_actions[dev_str]()
                time.sleep(10)

            elif 'close' in cmd_str or 'turn off' in cmd_str:
                close_actions[dev_str]()
        elif len(event.parseString(t)) == 3:  # argument
            cmd, dev, arg = event.parseString(t)
            cmd_str, dev_str, arg_str = ' '.join(cmd), ' '.join(dev),' '.join(arg)
            num_arg = 0
            try:
                num_arg = int(arg_str.split()[0])
            except ValueError as err:
                 print("expected number but got: '{}'".format(arg_str[0]))
            if 'increase' in cmd_str and num_arg > 0:
                open_actions[dev_str](num_arg)
            elif 'decrease' in cmd_str and num_arg > 0:
                 close_actions[dev_str](num_arg)
if __name__ == '__main__':
    main()