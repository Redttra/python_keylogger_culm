import sys
import listener as ls
from PyQt6.QtWidgets import *
import threading
import globals

sys.argv += ['-platform', 'windows:darkmode=2']

global thread_running
thread_running = False
    
def threadFunct():
     ls.start_listener()

class DisplayWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.label = QLabel("log file:")
        layout.addWidget(self.label)
        self.setWindowTitle("display log")
        self.text_edit = None

        if self.text_edit is None:
            self.text_edit = QTextEdit()
            text_file = open("keylog.txt")
            text = text_file.read()
            self.text_edit.setPlainText(text)
            layout.addWidget(self.text_edit)
        else:
            self.text_edit()  # Close window.
            self.text_edit = None
     

        self.setLayout(layout)

class PyQtLayout(QWidget):

    def __init__(self):
        super().__init__()
        self.disp_status = None
        #self.worker = Worker()
        #self.t = QThread()
        #self.worker.moveToThread(self.t)
        self.UI()
        #self.t.start()
        self.listener_thread = threading.Thread(target=threadFunct, args=())
        

    def UI(self):
        Button1 = QPushButton('start')
        Button1.clicked.connect(self.start_op)
        Button2 = QPushButton('stop')
        Button2.clicked.connect(self.end_op)
        Button3 = QPushButton('display')
        Button3.clicked.connect(self.show_new_window)

        vbox = QVBoxLayout()
        vbox.addWidget(Button1)
        vbox.addWidget(Button2)
        vbox.addWidget(Button3)
 
        self.setLayout(vbox)
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('PyLogger')
        self.show()

    def show_new_window(self, checked):
        if self.disp_status is None:
            self.disp_status= DisplayWindow()
            self.disp_status.show()

        else:
            self.disp_status.close()  # Close window.
            self.disp_status = None 

    def start_op(self):
        globals.end_thread = False
        if thread_running == False:
            thread_running = True
            self.listener_thread.start()

    def end_op(self):
        globals.end_thread = True

def start_gui():
    app = QApplication(sys.argv)
    window = PyQtLayout() 
    sys.exit(app.exec())

start_gui()

shawn 
haliday
zeren
neykov