import pyautogui

class Mouse:
    current_dpixel_=32

    @staticmethod
    def current_position():
        x,y=pyautogui.position()
        return x,y

    @staticmethod
    def current_dpixel():
        return Mouse.current_dpixel_

    @staticmethod
    def left_click():
        pyautogui.click()

    @staticmethod
    def right_click():
        pyautogui.click(button="right")

    @staticmethod
    def left_double_click():
        pyautogui.doubleClick()

    @staticmethod
    def left_down():
        pyautogui.mouseDown(button="left")

    @staticmethod
    def right_down():
        pyautogui.mouseDown(button="right")

    @staticmethod
    def left_up():
        pyautogui.mouseUp(button="left")

    @staticmethod
    def right_up():
        pyautogui.mouseUp(button="right")

    @staticmethod
    def _move(dx,dy):
        pyautogui.moveRel(dx,dy)

    @staticmethod
    def move_up():
        Mouse._move(0,-Mouse.current_dpixel_)

    @staticmethod
    def move_down():
        Mouse._move(0,Mouse.current_dpixel_)

    @staticmethod
    def move_left():
        Mouse._move(-Mouse.current_dpixel_,0)

    @staticmethod
    def move_right():
        Mouse._move(Mouse.current_dpixel_,0)

    @staticmethod
    def dpixel_double():
        Mouse.current_dpixel_=Mouse.current_dpixel_*2

    @staticmethod
    def dpixel_halve():
        Mouse.current_dpixel_=Mouse.current_dpixel_/2
