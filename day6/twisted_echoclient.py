# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 19:38:23 2019

@author: Balasubramaniam
"""

from twisted.internet import reactor, protocol

class EchoClient(protocol.Protocol):
    def connectionMade(self):
        self.transport.write(u"Hello, world!".encode('utf-8'))

    def dataReceived(self, data):
        print("Server said:", data)
        self.transport.loseConnection()

class EchoFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return EchoClient()

    def clientConnectionFailed(self, connector, reason):
        print("Connection failed.")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Connection lost.")
        reactor.stop()

reactor.connectTCP("localhost", 7070, EchoFactory())
reactor.run()