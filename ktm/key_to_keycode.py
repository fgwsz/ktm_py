from pynput.keyboard import Key
from keycode import KeyCode

_key_to_keycode={
    Key.alt_l:KeyCode._LeftAlt,
    Key.alt_r:KeyCode._RightAlt,
    Key.backspace:KeyCode._Backspace,
    Key.caps_lock:KeyCode._CapsLk,
    Key.cmd_l:KeyCode._LeftWin,
    Key.cmd_r:KeyCode._RightWin,
    Key.ctrl_l:KeyCode._LeftCtrl,
    Key.ctrl_r:KeyCode._RightCtrl,
    Key.delete:KeyCode._Delete,
    Key.down:KeyCode._Down,
    Key.end:KeyCode._End,
    Key.enter:KeyCode._Enter,
    Key.esc:KeyCode._Esc,
    Key.f1:KeyCode._F1,
    Key.f2:KeyCode._F2,
    Key.f3:KeyCode._F3,
    Key.f4:KeyCode._F4,
    Key.f5:KeyCode._F5,
    Key.f6:KeyCode._F6,
    Key.f7:KeyCode._F7,
    Key.f8:KeyCode._F8,
    Key.f9:KeyCode._F9,
    Key.f10:KeyCode._F10,
    Key.f11:KeyCode._F11,
    Key.f12:KeyCode._F12,
    Key.f13:KeyCode._F13,
    Key.f14:KeyCode._F14,
    Key.f15:KeyCode._F15,
    Key.f16:KeyCode._F16,
    Key.f17:KeyCode._F17,
    Key.f18:KeyCode._F18,
    Key.f19:KeyCode._F19,
    Key.f20:KeyCode._F20,
    Key.home:KeyCode._Home,
    Key.left:KeyCode._Left,
    Key.page_down:KeyCode._PageDown,
    Key.page_up:KeyCode._PageUp,
    Key.right:KeyCode._Right,
    Key.shift_l:KeyCode._LeftShift,
    Key.shift_r:KeyCode._RightShfit,
    Key.space:KeyCode._Space,
    Key.tab:KeyCode._Tab,
    Key.up:KeyCode._Up,
    Key.media_play_pause:KeyCode._MediaPlayPause,
    Key.media_volume_mute:KeyCode._MediaVolumeMute,
    Key.media_volume_down:KeyCode._MediaVolumeDown,
    Key.media_volume_up:KeyCode._MediaVolumeUp,
    Key.media_previous:KeyCode._MediaPrevTrack,
    Key.media_next:KeyCode._MediaNextTrack,
    Key.insert:KeyCode._Insert,
    Key.menu:KeyCode._Application,
    Key.num_lock:KeyCode._NumLock,
    Key.pause:KeyCode._PauseBreak,
    Key.print_screen:KeyCode._PrintScreen,
    Key.scroll_lock:KeyCode._ScrollLock,
}

def key_to_keycode(key):
    global _key_to_keycode
    if isinstance(key,Key):
        return _key_to_keycode[key]
    else:
        return key.vk