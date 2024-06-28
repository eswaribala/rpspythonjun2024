class ChatRoom(object):
    '''Mediator class.'''

    def displayMessage(self, user, message):
        print("[{} says]: {}".format(user, message))


class User(object):
    '''A class whose instances want to interact with each other.'''

    def __init__(self, name):
        self.name = name
        self.chatRoom = ChatRoom()

    def sendMessage(self, message):
        self.chatRoom.displayMessage(self, message)

    def __str__(self):
        return self.name


mahi = User('Mahi')
sachin = User('Sachin')
ganguly = User('Ganguly')

mahi.sendMessage("Hi Team! Meeting at 3 PM today.")
sachin.sendMessage("Roger that!")
ganguly.sendMessage("Alright.")
