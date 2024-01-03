from logger import Logger
from mouse import Mouse
from keycode_to_name import keycode_to_name
import keycode_of

is_leader_down     =False
is_mouse_left_down =False
is_mouse_right_down=False

mouse_logger   =Logger("[MOU] ")
cursor_logger  =Logger("[CUR] ")
keyboard_logger=Logger("[KEY] ")
pixel_logger   =Logger("[PIX] ")
wheel_logger   =Logger("[WHE] ")
app_logger     =Logger("[APP] ")

key_down_set=set([])

def mouse_move_up():
    Mouse.move_up()
    cursor_logger.println_with_head(
        "↑ Pix{",
        Mouse.current_dpixel(),
        "} => ",
        Mouse.current_position()
    )

def mouse_move_down():
    Mouse.move_down()
    cursor_logger.println_with_head(
        "↓ Pix{",
        Mouse.current_dpixel(),
        "} => ",
        Mouse.current_position()
    )

def mouse_move_left():
    Mouse.move_left()
    cursor_logger.println_with_head(
        "← Pix{",
        Mouse.current_dpixel(),
        "} => ",
        Mouse.current_position()
    )

def mouse_move_right():
    Mouse.move_right()
    cursor_logger.println_with_head(
        "→ Pix{",
        Mouse.current_dpixel(),
        "} => ",
        Mouse.current_position()
    )

def mouse_wheel_up():
    Mouse.wheel_up()
    wheel_logger.println_with_head(
        "↑ Pix{",
        Mouse.current_dpixel(),
        "}"
    )

def mouse_wheel_down():
    Mouse.wheel_down()
    wheel_logger.println_with_head(
        "↓ Pix{",
        Mouse.current_dpixel(),
        "}"
    )

def _mouse_key_auto_up():
    if is_mouse_left_down:
        Mouse.left_up()
        is_mouse_left_down=False
        mouse_logger.println_with_head("Left Up")
    elif is_mouse_right_down:
        Mouse.right_up()
        is_mouse_right_down=False
        mouse_logger.println_with_head("Right Up")

def mouse_left_click():
    _mouse_key_auto_up()
    Mouse.left_click()
    mouse_logger.println_with_head("Left Click")

def mouse_left_double_click():
    _mouse_key_auto_up()
    Mouse.left_double_click()
    mouse_logger.println_with_head("Left Double Click")

def mouse_right_click():
    _mouse_key_auto_up()
    Mouse.right_click()
    mouse_logger.println_with_head("Right Click")

def mouse_key_up():
    _mouse_key_auto_up()

def mouse_left_down():
    _mouse_key_auto_up()
    Mouse.left_down()
    is_mouse_left_down=True
    mouse_logger.println_with_head("Left Down")

def mouse_right_down():
    _mouse_key_auto_up()
    Mouse.right_down()
    is_mouse_right_down=True
    mouse_logger.println_with_head("Right Down")

def mouse_dpixel_double():
    Mouse.dpixel_double()
    pixel_logger.println_with_head(
        "D_Pixel * 2 => ",
        Mouse.current_dpixel()
    )

def mouse_dpixel_halve():
    Mouse.dpixel_halve()
    pixel_logger.println_with_head(
        "D_Pixel / 2 => ",
        Mouse.current_dpixel()
    )

def app_quit():
    app_logger.println_with_head("Quit")
    exit(0)

key_down_handle_list={
    keycode_of.KeyCodeOf_mouse_move_up          :mouse_move_up,
    keycode_of.KeyCodeOf_mouse_move_down        :mouse_move_down,
    keycode_of.KeyCodeOf_mouse_move_left        :mouse_move_left,
    keycode_of.KeyCodeOf_mouse_move_right       :mouse_move_right,
    keycode_of.KeyCodeOf_mouse_wheel_up         :mouse_wheel_up,
    keycode_of.KeyCodeOf_mouse_wheel_down       :mouse_wheel_down,
    keycode_of.KeyCodeOf_mouse_left_click       :mouse_left_click,
    keycode_of.KeyCodeOf_mouse_left_double_click:mouse_left_double_click,
    keycode_of.KeyCodeOf_mouse_right_click      :mouse_right_click,
    keycode_of.KeyCodeOf_mouse_key_up           :mouse_key_up,
    keycode_of.KeyCodeOf_mouse_left_down        :mouse_left_down,
    keycode_of.KeyCodeOf_mouse_right_down       :mouse_right_down,
    keycode_of.KeyCodeOf_mouse_dpixel_double    :mouse_dpixel_double,
    keycode_of.KeyCodeOf_mouse_dpixel_halve     :mouse_dpixel_halve,
}

def _println_key_down():
    keyboard_logger.print_with_head()
    for element in key_down_set:
        keyboard_logger.print("<",keycode_to_name(element),">")
    keyboard_logger.println(" Down")

def _println_key_up(keycode):
    keyboard_logger.println_with_head(
        "<",
        keycode_to_name(keycode),
        "> Up"
    )

def _handle_on_press(keycode):
    if not keycode in key_down_set:
        key_down_set.add(keycode)
        _println_key_down()

    if keycode==keycode_of.KeyCodeOf_leader:
        is_leader_down=True

    elif is_leader_down and keycode in key_down_handle_list:
        key_down_handle_list[keycode]()

def _handle_on_release(keycode):
    key_down_set.remove(keycode)
    if keycode==keycode_of.KeyCodeOf_leader:
        is_leader_down=False

    _println_key_up(keycode)

