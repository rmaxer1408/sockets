import socketserver


class ThreadTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class EchoTCPHandler(socketserver.BaseRequestHandler):

    def handle(self) -> None:
        data = self.request.recv(2 ** 10).strip()
        print('Address: {}'.format(self.client_address[0]))
        print('Data: {}'.format(data.decode()))
        self.request.sendall(data)


if __name__ == '__main__':
    with ThreadTCPServer(('', 8888), EchoTCPHandler) as server:
        server.serve_forever()
