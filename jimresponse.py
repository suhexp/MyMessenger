import json
import time


class JIMResponse:
    # на будущее
    response_ids = {'100': 'Basic Notification', '101': 'Important Notification',
                    '200': 'OK', '201': 'Object Created', '202': 'Accepted',
                    '400': 'Malformed JSON', '401': 'Not Authorised', '402': 'Wrong Login/Password',
                    '403': 'Forbidden', '404': 'Not Found', '409': 'Connection Conflict',
                    '410': 'User Gone', '500': 'Server Error',
                    }

    def __init__(self, code, text='', resp_time=None):
        strcode = str(code)  # можно передавать число или строку
        self.response = strcode
        if resp_time is None:  # когда клиент читает ответ сервера, у него уже есть отметка времени
            self.time = time.ctime(time.time())
        else:
            self.time = resp_time
        if strcode[0] == '1' or strcode[0] == '2':
            self.alert = text
        else:
            self.error = text

    @property
    def json(self):
        fields = self.__dict__
        j = {c: fields[c] for c in fields if fields[c] is not None}
        return json.dumps(j)

    @property
    def utf8(self):
        return self.json.encode('utf-8')

    @staticmethod
    def fromjson(json_resp):
        try:
            parsed_resp = json.loads(json_resp)
        except ValueError:
            return None
        text = parsed_resp['alert'] if 'alert' in parsed_resp else parsed_resp['error']
        response = JIMResponse(parsed_resp['response'], text, parsed_resp['time'])
        return response

if __name__ == '__main__':
    resp = JIMResponse(300, 'Hello there')
    print(resp.json)
    time.sleep(5)
    resp2 = JIMResponse.fromjson(resp.json)
    print(resp2.json)
