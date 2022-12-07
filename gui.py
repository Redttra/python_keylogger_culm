from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtCore import Qt
import sys
 


def getSize():
    sc = app.screens()[0]
    screen_dim = sc.size()
    return screen_dim 

app = QApplication(sys.argv)

scrn_dim = getSize()

start_button = QPushButton('start')
start_button.move(250, 250)
start_button.show()


sys.exit(app.exec())

