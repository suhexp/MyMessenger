import unittest

import hashlib

import users

LOGIN = 'TestLogin'

EMAIL = 'some@inbox.ru'

ANITHER_EMAIL = 'another@inbox.ru'

PASSWORD = 'qwerty'

class UserInitTest(unittest.TestCase):
    def setUp(self):
        self.user = users.User(LOGIN, EMAIL)

        self.user.set_password(PASSWORD)

    def test_set_password(self):
        login_bt = LOGIN.encode('utf-8')

        password_bt = PASSWORD.encode('utf-8')

        hsh = hashlib.new('md5')

        hsh.update(login_bt)
        hsh.update(password_bt)

        self.assertEqual(hsh.hexdigest(), self.user.password)


    def test_set_wrong_password(self):
        login_bt = LOGIN.encode('utf-8')

        password_bt = PASSWORD.encode('utf-8')

        email_bt = EMAIL.encode('utf-8')

        hsh = hashlib.new('md5')

        hsh.update(login_bt)
        hsh.update(password_bt)
        hsh.update(email_bt)

        self.assertNotEqual(hsh.hexdigest(), self.user.password)

    def test_set_email(self):
        self.user.email = ANITHER_EMAIL

        self.assertEqual(self.user.email, ANITHER_EMAIL)

    def test_set_wrong_email(self):
        with self.assertRaises(TypeError):
            self.user.email = 123

if __name__ == '__main__':
    unittest.main()

