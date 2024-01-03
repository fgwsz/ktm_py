from pynput import keyboard
import handle
from key_to_keycode import key_to_keycode

def on_press(key):
    handle.on_press(key_to_keycode(key))

def on_release(key):
    handle.on_release(key_to_keycode(key))

def main_loop():
    listener=keyboard.Listener(on_press=on_press,on_release=on_release)
    listener.start()
    listener.join()