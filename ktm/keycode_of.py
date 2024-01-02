from enum import Enum
from keycode import KeyCode

# 快捷键设置
class KeyCodeOf(Enum):
    leader                 =KeyCode.KeyCode_LeftAlt.value
    mouse_move_up          =KeyCode.KeyCode_K      .value# Vim K
    mouse_move_down        =KeyCode.KeyCode_J      .value# Vim J
    mouse_move_left        =KeyCode.KeyCode_H      .value# Vim H
    mouse_move_right       =KeyCode.KeyCode_L      .value# Vim L
    mouse_wheel_up         =KeyCode.KeyCode_B      .value# Back
    mouse_wheel_down       =KeyCode.KeyCode_N      .value# Next
    mouse_left_click       =KeyCode.KeyCode_O      .value# GameBoy O
    mouse_left_double_click=KeyCode.KeyCode_A      .value# GameBoy A
    mouse_right_click      =KeyCode.KeyCode_X      .value# GameBoy X
    mouse_key_up           =KeyCode.KeyCode_U      .value# Up or Undo
    mouse_left_down        =KeyCode.KeyCode_G      .value# Get
    mouse_right_down       =KeyCode.KeyCode_I      .value# Invert
    mouse_dpixel_double    =KeyCode.KeyCode_2      .value# * 2
    mouse_dpixel_halve     =KeyCode.KeyCode_Hyphen .value# - Decrease
    app_quit               =KeyCode.KeyCode_Q      .value# Quit
