import sys
import time
import socket
from MainWindow import  Ui_MainWindow

from LoginWindow import *
from AddU import Ui_Add
import Client
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt, QObject, QThread, pyqtSignal, pyqtSlot


class AddUser(QtWidgets.QWidget):
    def __init__(self, parent=None):
        #self.parent = parent
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Add()
        self.ui.setupUi(self)
        #user = self.ui.lineEdit.text()
        self.ui.pushButton.clicked.connect(self.Find)



    def Find(self):
        contact_signal = pyqtSignal(str)
        user = self.ui.lineEdit.text()
        contact_signal.emit(user)
        #MyWin.AddCont.parentWidget()
        #self.AddCont.parentWidget()
        #self.parentWidget()



class LoginWin(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        # Form = QtWidgets.QWidget()
        self.ui = Ui_LoginWin()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(MyWin.start_chat)

    def Auto(self):
        name = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        with open("config_path_user.json", "w") as f:
            st = {"host": "localhost", "port": 8002, "name": "Name", "login": name, "password": password}

            f.write(str(st))
        f.close("config_path_user.json")

        cl = Client("config_path_user.json")

        cl.authorise()
        if cl.status == 'on':
            MyWin.ui.textEdit.addItem("% is autoririse" % Client.name)

        return f


class MyWin(QtWidgets.QMainWindow):
    sentData = pyqtSignal(str)

    def __init__(self, parent=None, ip='localhost', port=8002, ):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionLogin.triggered.connect(self.login)
        self.ui.action1.triggered.connect(self.Add)
        sectionObj.contact_signal.connect(self.AddCont)
        # self.ui.listView.setItemDelegate('1')
        self.receiver = None
        self.thread = None
        self.sock = None
        self.ip = ip
        self.port = port
        self.is_active = False
        #self.ui.pushButton.clicked.connect(self.A)

    @pyqtSlot(str)
    def AddCont(self,cont):

       # sectionObj.contact_signal.connect(self.AddCont)

        self.ui.listView.addItem(str(cont))


    def closeEvent(self, e):
        result = QtWidgets.QMessageBox.question(self, "Confirm Dialog", "Really quit?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                QtWidgets.QMessageBox.No)

        if result == QtWidgets.QMessageBox.Yes:
            e.accept()
            self.is_active = False
            self.receiver.stop()
            self.sock.close()
            self.setGuiConnected(False)

        else:
            e.ignore()

    def login(self):

        self.secondObj = LoginWin()
        self.secondObj.show()

    def Add(self):
        self.secondObj = AddUser()
        self.secondObj.show()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
