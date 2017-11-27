import socket
from message import Message
import datetime
import json


class Client(object):

    def __init__(self, host, port):

        self._host = str(host)

        self._port = int(port)

    def run(self):

        with socket.socket() as sock:

            self.socket = sock

            self.socket.connect((self._host, self._port))

            user = input('user:  ')

            while True:

                fl= input('reed(r)/write(w)?')


                if fl == 'w':

                    text = input('Eenter message: ')


                    if text == 'exit':

                        break

                    date = datetime.datetime.now()

                    message_object = {'text': text, 'user': user, "date": str(date)}
                    message_string = json.dumps(message_object)

                    message_byt = message_string.encode('utf-8')
                    sock.send(message_byt)

                if fl =='r':

                    data = sock.recv(1024)
                    sock.close()
                    message_str = data.decode('utf-8')
                    message_object = json.loads(message_str)
                    print('Ansver {}  {}  : {} '.format(message_object.get('date'), message_object.get('user'), message_object.get('text')) )


if __name__ == '__main__':

    client = Client('localhost', 8002)

    client.run()
    # sock = socket.socket()

    # sock.connect(('localhost', 8005))


    # massage = sock.recv(1024)

    # sock.close()

    # print(massage)
