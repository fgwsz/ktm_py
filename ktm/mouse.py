import pyautogui

class Mouse:
    current_dpixel_=32

    def current_position(self):
        x,y=pyautogui.position()
        return x,y

    def current_dpixel(self):
        return Mouse.current_dpixel_

    def left_click(self):
        pyautogui.click()
        return self

    def right_click(self):
        pyautogui.click(button="right")
        return self

    def left_double_click(self):
        pyautogui.doubleClick()
        return self

    def left_down(self):
        pyautogui.mouseDown(button="left")
        return self

    def right_down(self):
        pyautogui.mouseDown(button="right")
        return self

    def left_up(self):
        pyautogui.mouseUp(button="left")
        return self

    def right_up(self):
        pyautogui.mouseUp(button="right")
        return self

    def _move(self,dx,dy):
        pyautogui.moveRel(dx,dy)
        return self

    def move_up(self):
        self._move(0,-Mouse.current_dpixel_)
        return self

    def move_down(self):
        self._move(0,Mouse.current_dpixel_)
        return self

    def move_left(self):
        self._move(-Mouse.current_dpixel_,0)
        return self

    def move_right(self):
        self._move(Mouse.current_dpixel_,0)
        return self

    def dpixel_double(self):
        Mouse.current_dpixel_=Mouse.current_dpixel_*2
        return self

    def dpixel_halve(self):
        Mouse.current_dpixel_=Mouse.current_dpixel_/2
        return self
