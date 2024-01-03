from pynput import keyboard
import handle

def on_press(key):
    handle._handle_on_press(key.vk)

def on_release(key):
    handle._handle_on_release(key.vk)

def main_loop():
    listener=keyboard.Listener(on_press=on_press,on_release=on_release)
    listener.start()
    listener.join()

