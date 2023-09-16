import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import sqlite3

conn = sqlite3.connect('magazinElectroniki')
cursor = conn.cursor()

class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui",self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccbutton.clicked.connect(self.gotocreate)

    def loginfunction(self):
        email=self.email.text()
        password=self.password.text()
        user_check = cursor.execute(f'SELECT password FROM users WHERE email = "{email}"').fetchone()
        if user_check is None:
            return print("This user does not exist!")
        if password != user_check[0]:
            return print('Incorrect password!')
        print("Successfully logged in with email: ", email, "and password:", password)

    def gotocreate(self):
        createacc=CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)

class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc,self).__init__()
        loadUi("createacc.ui",self)
        self.signupbutton.clicked.connect(self.createaccfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)

    def createaccfunction(self):
        email = self.email.text()
        if self.password.text()==self.confirmpass.text():
            password=self.password.text()
            email_check = cursor.execute(f'SELECT * FROM users WHERE email = "{email}"').fetchone()
            if email_check is not None:
                return print("This email is already in use!")
            print("Successfully created acc with email: ", email, "and password: ", password)
            cursor.execute(f'INSERT INTO users VALUES ("{email}", "{password}")')
            conn.commit()
            login=Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)



app=QApplication(sys.argv)
mainwindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(480)
widget.setFixedHeight(620)
widget.show()
app.exec_()
