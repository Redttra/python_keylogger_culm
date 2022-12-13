import sys
import listener as ls
from PyQt5.QtWidgets import *
 
class PyQtLayout(QWidget):
 
    def __init__(self):
        super().__init__()
        self.UI()
 
    def UI(self):
        Button1 = QPushButton('start')
        Button1.clicked.connect(ls.proxy_start)
        Button2 = QPushButton('stop')
        Button2.clicked.connect(ls.stop_listener)
        Button3 = QPushButton('display')
    
        vbox = QVBoxLayout()
        vbox.addWidget(Button1)
        vbox.addWidget(Button2)
        vbox.addWidget(Button3)
 
        self.setLayout(vbox)
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('PyLogger')
        self.show()


def start_gui():
    app = QApplication(sys.argv)
    window = PyQtLayout()
    sys.exit(app.exec())

start_gui()
