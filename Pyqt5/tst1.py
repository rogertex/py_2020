import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
from Ui_first import Ui_MainWindow
from Ui_sec import Ui_Form

if __name__ == "__main__":
    app = QApplication(sys.argv)
    qw = QMainWindow()
    qw2 = QMainWindow()
    sui = Ui_Form()
    fui = Ui_MainWindow()
    sui.setupUi(qw2)
    fui.setupUi(qw)
    btn = fui.pushButton
    btn.clicked.connect(qw2.show)
     
    
    qw.show()
    
    
           
    sys.exit(app.exec_())
