import sqlite3
import platform
from PyQt5 import uic, QtWidgets
from datetime import date
 
def welcome():
    todays=date.today()
    opsys=platform.system()
    opsysv=platform.release()

    print('github.com/muradpontes/noctem' + ' — ' + (str(opsys)+ ' ' + str(opsysv) + ' — ' + str(todays)))

def openSec_win():
    firstWindow.label_5.setText("")
    usernameQt = firstWindow.lineEdit_4.text()
    passwordQt = firstWindow.lineEdit_3.text()
    if usernameQt == "murad" and passwordQt == "12345" :
        firstWindow.close()
        secondWindow.show()
    else:
        firstWindow.label_5.setText("wrong username or password")

def openFirst_win():
    secondWindow.close()
    firstWindow.show()

def backFirst_win():
    thirdWindow.close()
    firstWindow.show()

def openThird_win():
    firstWindow.close()
    thirdWindow.show()

def signup():
    usuarioQt = thirdWindow.lineEdit_4.text()
    senhaQt = thirdWindow.lineEdit_5.text()
    c_senhaQt = thirdWindow.lineEdit_6.text()

    if (senhaQt == c_senhaQt):
        try:
            conn = sqlite3.connect('login.db')
            cursor = conn.cursor()
    
            cursor.execute('''INSERT INTO accounts(userQt, passwordQt) VALUES(? ,?)''', (usuarioQt, senhaQt))
            conn.commit()
        except:
            print("a")

    thirdWindow.label.setText("your account has been created!")
    thirdWindow.lineEdit_4.setText("")
    thirdWindow.lineEdit_5.setText("")
    thirdWindow.lineEdit_6.setText("")




welcome()

app = QtWidgets.QApplication([])

firstWindow = uic.loadUi("window1.ui")
secondWindow = uic.loadUi("window2.ui")
thirdWindow = uic.loadUi("window3.ui")

firstWindow.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
firstWindow.pushButton.clicked.connect(openSec_win)
firstWindow.pushButton_2.clicked.connect(openThird_win)

secondWindow.pushButton.clicked.connect(openFirst_win)

thirdWindow.pushButton_4.clicked.connect(backFirst_win)
thirdWindow.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
thirdWindow.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Password)
#thirdWindow.pushButton_3.clicked.connect(writeDB)



firstWindow.show()
app.exec()

#def home():
#    print(r"""\
#                     __                           
#                    /\ \__                        
#  ___     ___     ___\ \ ,_\    __    ___ ___      
#/' _ `\  / __`\  /'___\ \ \/  /'__`\/' __` __`\      __
#/\ \/\ \/\ \L\ \/\ \__/\ \ \_/\  __//\ \/\ \/\ \   <(o )___            
#\ \_\ \_\ \____/\ \____\\ \__\ \____\ \_\ \_\ \_\   ( ._> / 
# \/_/\/_/\/___/  \/____/ \/__/\/____/\/_/\/_/\/_/    `---'   
#                    """)
