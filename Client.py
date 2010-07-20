#!/usr/bin/env python

import sys, traceback, Ice

Ice.loadSlice('BFAS.ice')
import Noblis

class Client(Ice.Application):
    def run(self, args):

        proxy = Noblis.BFASPrx.checkedCast(\
            self.communicator().propertyToProxy('BFAS.Proxy').ice_twoway().ice_timeout(-1).ice_secure(False))
        if not proxy:
            print args[0] + ": invalid proxy"
            return 1

        try:
            infile = open("file.mtgl","r")
            proxy.analyzeFile(infile.read())
            infile.close()

        except Ice.Exception, ex:
            print ex

        return 0

app = Client()
sys.exit(app.main(sys.argv, "config.client"))
