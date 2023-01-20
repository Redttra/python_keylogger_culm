import sys
import listener as ls
from PyQt6.QtWidgets import *
import threading
import globals

# Changes window theme to darkmode
sys.argv += ['-platform', 'windows:darkmode=2']

global thread_running
thread_running = False

# Simply function used for creation of the listener thread, calls upon the start function from listener.py
def threadFunct():
     ls.start_listener()

# Class for the display log window
class DisplayWindow(QWidget):
    #Defines the layout of the window
    def __init__(self):
        super().__init__()
        # Defines layout
        layout = QVBoxLayout()
        # Changes the widget text
        self.label = QLabel("log file:")
        # Adds the label to the window layout
        layout.addWidget(self.label)
        # Sets window title
        self.setWindowTitle("display log")
        # Variable correlated to the status of the display window (open vs not open), used to make the window toggle open and closed with the same button
        self.text_edit = None

        # If window not open
        if self.text_edit is None:
            #Create text box widget and load the keylog file into it
            self.text_edit = QTextEdit()
            text_file = open(r"C:\Users\Zeren\Desktop\python code\culm\pylogger\keylog.txt")
            text = text_file.read()
            self.text_edit.setPlainText(text)
            layout.addWidget(self.text_edit)
        # If window is already open, close the window and reset the status of the window
        else:
            self.text_edit()  # Close window.
            self.text_edit = None
     
        # Sets the layout of the window to the layout with all the widgets added
        self.setLayout(layout)

# Class for the help text window
class HelpWindow(QWidget):
    # Defines layout
    def __init__(self):
        super().__init__()
        # Creates layout for the window and changes the window text and title
        layout = QVBoxLayout()
        self.label = QLabel("Help File:")
        layout.addWidget(self.label)
        self.setWindowTitle("Help")
        # Window status (open vs closed)
        self.text_help = None

        # If window is not open
        if self.text_help is None:
            # Create the window with the help text loaded into the text box widget
            self.text_help = QTextEdit()
            text_file = open(r'C:\Users\Zeren\Desktop\python code\culm\pylogger\help.txt')
            text = text_file.read()
            self.text_help.setPlainText(text)
            # add the widget to the window
            layout.addWidget(self.text_help)

        # If window is open
        else:
            self.text_help()  # Close window.
            self.text_help = None
     

        self.setLayout(layout)



# Class for the main GUI window
class PyQtLayout(QWidget):
    # defines the layout 
    def __init__(self):
        super().__init__()
        # creates variables used to track the status of the various windows
        self.disp_status = None
        self.disp_status_help = None
        # runs the UI class method, which creates all the widgets and correctly positions them within the fram
        self.UI()
        # Creates the thread used to run the listener
        self.listener_thread = threading.Thread(target=threadFunct, args=())
        

    def UI(self):
        # Creates all the buttons
        Button1 = QPushButton('Start')
        # Defines the styles of the button
        Button1.setStyleSheet("border-radius : 50; border : 1px solid black")
        # Connects the button with clicking functionality
        Button1.clicked.connect(self.start_op)
        Button2 = QPushButton('Stop')
        Button2.setStyleSheet("border-radius : 50; border : 1px solid black")
        Button2.clicked.connect(self.end_op)
        Button3 = QPushButton('Display log')
        Button3.setStyleSheet("border-radius : 50; border : 1px solid black")
        Button3.clicked.connect(self.show_new_window)
        Button4 = QPushButton('Help')
        Button4.setStyleSheet("border-radius : 50; border : 1px solid black")
        Button4.clicked.connect(self.show_new_help_window)

        # Creates a verticle widget layout and adds all the buttons to it
        vbox = QVBoxLayout()
        vbox.addWidget(Button1)
        vbox.addWidget(Button2)
        vbox.addWidget(Button3)
        vbox.addWidget(Button4)
 
        # Sets the layout of the window
        self.setLayout(vbox)
        # Sets the window size and position
        self.setGeometry(500, 500, 500, 500)
        # Sets window title
        self.setWindowTitle('PyLogger')
        # 'blips' the layout
        self.show()

    # Function for the display window button
    def show_new_window(self, checked):
        # Checks the status of the window (open vs closed)

        #If closed, create the window
        if self.disp_status is None:
            self.disp_status= DisplayWindow()
            self.disp_status.show()

        #if window open, close it and reset the status
        else:
            self.disp_status.close()  # Close window.
            self.disp_status = None 
    
    # Function for help window button
    def show_new_help_window(self, checked):
         # Checks the status of the window (open vs closed)

        #If closed, create the window
        if self.disp_status_help is None:
            self.disp_status_help = HelpWindow()
            self.disp_status_help.show()

        #if window open, close it and reset the status
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

# Calls the function to start the GUI
start_gui()