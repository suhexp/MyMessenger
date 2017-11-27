import hashlib

__version__ = 3.0

class User(object):
    def __init__(self, login, email):
        self._login = login
        self._email = email
        self._password = None

    @property
    def login(self):
        return self._login

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not isinstance(value,str):
            raise TypeError('Wrong type email !')

        self._email = value
    @property
    def password(self):
        return self._password

    def set_password(self, password):
        login_bt = self._login.encode('utf-8')

        password_bt = password.encode('utf-8')

        hsh = hashlib.new('md5')

        hsh.update(login_bt)
        hsh.update(password_bt)

        self._password = hsh.hexdigest()

        print(self._password)