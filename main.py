import datetime
import sys
from os import system
from time import sleep

import keyboard
import pyperclip

pressed_keys = set()


def on_key_event(event, log_key_pressed=False):

    if event.event_type == 'down':

        if (keyboard.is_pressed('ctrl') and
                keyboard.is_pressed('alt') and
                keyboard.is_pressed('shift')):
            with open('clipboard.txt', 'r') as fd:
                to_copy = fd.read()
                fd.close()

            pyperclip.copy(to_copy)
            print(f'{str(datetime.datetime.now())} - Clipboard updated')





if __name__ == '__main__':
    """ If the first argument is 'log', it will print key pressed state
    """
    try:
        log = sys.argv[1] == 'log'
    except IndexError:
        log = False
    keyboard.hook(lambda event: on_key_event(event, log_key_pressed=log))

    while True:
        sleep(3600)
