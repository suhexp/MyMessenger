import json
import time


# actions: authenticate, presence, quit, msg, join, leave, probe (server)
# fields: action, time, user (account_name, status), type, to, from, encoding, message, room
class JIMMsg:
    def __init__(self, action):
        self.action = action
        self.time = time.ctime(time.time())

    @property
    def json(self):
        fields = self.__dict__
        j = {c: fields[c] for c in fields if fields[c] is not None}
        return json.dumps(j)

    def from_dict(self, values):
        for k, v in values.items():
            setattr(self, k, v)
        return self

    @property
    def utf8(self):
        return self.json.encode('utf-8')


class JIMAuthMsg(JIMMsg):
    def __init__(self, account_name='', password=''):
        super().__init__('authenticate')
        self.user = {'account_name': account_name, 'password': password}


class JIMPresenceMsg(JIMMsg):
    def __init__(self, account_name='', status='', msgtype=None):
        super().__init__('presence')
        self.user = {'account_name': account_name, 'status': status}
        self.type = msgtype


class JIMProbeMsg(JIMMsg):
    def __init__(self):
        super().__init__('probe')


class JIMQuitMsg(JIMMsg):
    def __init__(self):
        super().__init__('quit')


class JIMUserMsg(JIMMsg):
    def __init__(self, to='', acc_name='', message='', encoding='utf-8'):
        super().__init__('msg')
        self.to = to
        self.account = acc_name  # from - служебное слово
        self.encoding = encoding
        self.message = message


class JIMChatMsg(JIMMsg):
    def __init__(self, to='', acc_name='', message=''):
        super().__init__('msg')
        self.to = '#' + to
        self.account = acc_name  # from - служебное слово
        self.message = message


class JIMJoinChatMsg(JIMMsg):
    def __init__(self, room_name=''):
        super().__init__('join')
        self.room = '#' + room_name


class JIMLeaveChatMsg(JIMMsg):
    def __init__(self, room_name=''):
        super().__init__('leave')
        self.room = '#' + room_name


class JIMMessageBuilder:
    msg_classes = {'authenticate': 'JIMAuthMsg', 'presence': 'JIMPresenceMsg',
                   'quit': 'JIMQuitMsg', 'msg': ('JIMUserMsg', 'JIMChatMsg'),
                   'join': 'JIMJoinChatMsg', 'leave': 'JIMLeaveChatMsg',
                   'probe': 'JIMProbeMsg'}

    @staticmethod
    def get_msg_from_json(json_msg):
        # Возвращает объект соответствующего класса сообщения в зависимости от action
        try:
            parsed_msg = json.loads(json_msg)  # Получить словарь атрибутов
        except ValueError:
            return None
        action = parsed_msg['action']
        if action == 'msg':  # сообщение пользователю или в чат
            if parsed_msg['to'][0] == '#':
                class_ = globals()[JIMMessageBuilder.msg_classes[action][1]]
            else:
                class_ = globals()[JIMMessageBuilder.msg_classes[action][0]]
        else:
            class_ = globals()[JIMMessageBuilder.msg_classes[action]]
        return class_().from_dict(parsed_msg)

if __name__ == '__main__':
    msg = JIMUserMsg('admin', 'user', 'hey man')
    js = msg.json
    print(js)
    msg = JIMMessageBuilder.get_msg_from_json(js)
    print(msg)
    print(msg.json)
    print(msg.utf8)