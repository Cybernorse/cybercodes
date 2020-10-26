from twisted.internet import protocol, reactor
class echoclient(protocol.Protocol):
    def connectionmade(self):
        self.transport.write("Hello server i am data")
    def datarecieved(self,data):
        print(data)
        self.transport.loseconnection()
class echofactory(protocol.ClientFactory):
    def buildprotocol(self,addr):
        return echoclient()
    def clientconnectionfailed(self,connector,reason):
        print("Connection failed")
        reactor.stop()
    def clientconnectionlost(self,connector,reason):
        print("Connection Lost")
        reactor.stop()
reactor.connectTCP('localhost',8000,echofactory())
reactor.run()
