import sys
from PyQt5.QtWidgets import *
 
class PyQtLayout(QWidget):
 
    def __init__(self):
        super().__init__()
        self.UI()
 
    def UI(self):
        Button1 = QPushButton('PyQt')
        Button2 = QPushButton('Layout')
        Button3 = QPushButton('Management')
         
        vbox = QVBoxLayout()
        vbox.addWidget(Button1)
        vbox.addWidget(Button2)
        vbox.addWidget(Button3)
 
        self.setLayout(vbox)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('PyQt5 Layout')
        self.show()

def main():
    app = QApplication(sys.argv)
    window = PyQtLayout()
    sys.exit(app.exec())

if __name__ == '__main__':
   main()