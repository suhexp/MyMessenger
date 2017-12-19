import sys

from MainWindow import *

from client.LoginWindow import *


class LoginWin(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

       #Form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #Form.show()




class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionLogin.triggered.connect(self.login)
        #self.ui.listView.setItemDelegate('1')

    def closeEvent(self, e):
        result = QtWidgets.QMessageBox.question(self, "Confirm Dialog", "Really quit?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                QtWidgets.QMessageBox.No)

        if result == QtWidgets.QMessageBox.Yes:
            e.accept()
        else:
            e.ignore()

    def login(self):

        #import sys
        #app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
        #sys.exit(app.exec_())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())



