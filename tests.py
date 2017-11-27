from unittest import mock, TestCase, main

import socket

from server import Server

from client import Client


HOST = 'localhost'

PORT = '8001'

class SocketTest(TestCase):
    def test_connect(self):

        with mock.patch('socket.socket') as mock_socket:

            c = Server(HOST, PORT)

            c.tcp_socket.bind.assert_called_with((HOST, PORT))

class ClientTestCase(TestCase):

    def test_connect(self):
        
        with mock.patch('socket.socket') as mock_socket:

            c = Client(HOST, PORT)

            c.run()

            c.socket.connect.assert_called_with((HOST, PORT))

if __name__ == '__main__':

    main()