from twisted.internet import protocol,endpoints,reactor
class twisted_server(protocol.Protocol):
    def twisted_echo(self,data):
        self.transport.write(data)
class twisted_server_pro(protocol.Factory):
    def twisted_echo_again(self,addr):
        return twisted_server()

endpoints.serverFromString(reactor,"tcp:8000").listen(twisted_server_pro())
reactor.run()
