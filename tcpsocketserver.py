from socketserver import TCPServer, ThreadingMixIn
from socketserver import StreamRequestHandler
from socketserver import BaseRequestHandler
import jimserver
from sys import argv
import socket
import time


class ThreadingJIMServer(ThreadingMixIn, TCPServer):
    def __init__(self, server_address, request_handler):
        super().__init__(server_address, request_handler, True)
        self.clients = set()

    def add_client(self, client):
        self.clients.add(client)

    def remove_client(self, client):
        self.clients.remove(client)

    allow_reuse_address = True
    max_children = 100


class JIMRequestHandler(BaseRequestHandler):
    def setup(self):
        self.server.add_client(self)

    def handle(self):
        if isinstance(self.request, socket.socket):
            # работа с потоком
            try:
                while True:
                    data = self.request.recv(1024)
                    if not data:
                        print('{0} disconnected'.format(self.client_address[0]))
                        break
                    print(data.decode('ascii'))
                    response, action = jimserver.parse_client_message(data.decode('ascii'))
                    if action:
                        # self.request.sendall(action.encode('ascii'))
                        for client in tuple(self.server.clients):
                            client.request.sendall(action.encode('ascii'))
                    else:
                        self.request.sendall(response.encode('ascii'))
            except Exception as e:
                print('{0} suddenly disconnected'.format(self.client_address[0]))

    def finish(self):
        self.server.remove_client(self)


def checkcmdargs():
    args = ['localhost', 7777]
    args[0] = argv[1] if len(argv) > 1 else 'localhost'
    args[1] = int(argv[2]) if len(argv) > 2 else 7777
    return args


def mainloop():
    address, port = checkcmdargs()
    serv = ThreadingJIMServer((address, port), JIMRequestHandler)
    print('Сервер запущен в {0}'.format(time.ctime(time.time())))
    serv.serve_forever()


mainloop()
