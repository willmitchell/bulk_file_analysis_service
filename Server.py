#!/usr/bin/env python

import sys, traceback, time, Ice

Ice.loadSlice('BFAS.ice')
import Noblis

class BFASImpl(Noblis.BFAS):
    def analyzeFile(self, inFile, current=None):
        print "Received File for analysis: contents: [%s]"%inFile

class Server(Ice.Application):
    def run(self, args):
        adapter = self.communicator().createObjectAdapter("BFAS")
        adapter.add(BFASImpl(), self.communicator().stringToIdentity("bfas"))
        adapter.activate()
        self.communicator().waitForShutdown()
        return 0

sys.stdout.flush()
app = Server()
sys.exit(app.main(sys.argv, "config.server"))
