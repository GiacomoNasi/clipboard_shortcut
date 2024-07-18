import datetime
from time import sleep

import keyboard
import pyperclip

pressed_keys = set()


def on_key_event(event):
    global pressed_keys
    if event.event_type == 'down':
        pressed_keys.add(event.name)
    if event.event_type == 'up':
        pressed_keys.discard(event.name)

    if pressed_keys == {'ctrl', 'alt gr', 'alt'}:
        with open('clipboard.txt', 'r') as fd:
            to_copy = fd.read()
            fd.close()

        pyperclip.copy(to_copy)
        print(f'{str(datetime.datetime.now())} - Clipboard updated')


keyboard.hook(on_key_event)

while True:
    sleep(3600)
