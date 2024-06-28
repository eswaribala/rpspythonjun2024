# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 19:36:19 2019

@author: Balasubramaniam
"""

from twisted.internet import protocol, reactor
import sys
from twisted.python import log
class Echo(protocol.Protocol):
    def dataReceived(self,data):
        self.transport.write(data)

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()

reactor.listenTCP(7070, EchoFactory())
log.startLogging(sys.stdout)
reactor.run()