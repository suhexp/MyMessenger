import datetime
import json

class Message(object):
    def __init__(self,text, user):
        self.text = text
        self.user = user
        self.date=datetime.datetime.now()

    def send(self):
        message_object = {'text': self.text, 'user': self.user, "date": self.date}
        message_string = json.dumps(message_object)

        message_bytes = message_string.encode('utf-8')
        return message_bytes

    def get(self,message_byt):
        message_string = message_byt.decode('utf-8')
        message_object = json.loads(message_string)
        self.text = message_object.get('text')
        self.user = message_object.get('user')
        self.date = message_object.get('date')

    def print(self):
        print('{}   {} : {}'.format(self.date, self.user, self.text))


