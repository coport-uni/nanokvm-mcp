"""HID keycodes and constants for NanoKVM WebSocket protocol."""

from enum import IntEnum
from typing import NamedTuple


class KeyboardModifier(IntEnum):
    """Keyboard modifier flags for WebSocket HID protocol."""

    NONE = 0
    CTRL_LEFT = 1
    SHIFT_LEFT = 2
    ALT_LEFT = 4
    META_LEFT = 8
    CTRL_RIGHT = 16
    SHIFT_RIGHT = 32
    ALT_RIGHT = 64
    META_RIGHT = 128


class MouseButton(IntEnum):
    """Mouse button bitmask values (NanoKVM HID report byte 0).

    These are bit flags, not indices: multiple buttons can be combined.
    Matches the official firmware's MouseButtons map (Left=1<<0, Right=1<<1,
    Middle=1<<2).
    """

    NONE = 0
    LEFT = 1    # 1 << 0
    RIGHT = 2   # 1 << 1
    MIDDLE = 4  # 1 << 2


class KeyInfo(NamedTuple):
    """Key information with code and required modifiers."""

    code: int
    shift: bool = False


# USB HID keyboard scancodes
# Reference: https://usb.org/sites/default/files/hut1_22.pdf
KEYCODES: dict[str, int] = {
    # Letters (lowercase - no shift needed)
    "a": 0x04,
    "b": 0x05,
    "c": 0x06,
    "d": 0x07,
    "e": 0x08,
    "f": 0x09,
    "g": 0x0A,
    "h": 0x0B,
    "i": 0x0C,
    "j": 0x0D,
    "k": 0x0E,
    "l": 0x0F,
    "m": 0x10,
    "n": 0x11,
    "o": 0x12,
    "p": 0x13,
    "q": 0x14,
    "r": 0x15,
    "s": 0x16,
    "t": 0x17,
    "u": 0x18,
    "v": 0x19,
    "w": 0x1A,
    "x": 0x1B,
    "y": 0x1C,
    "z": 0x1D,
    # Numbers
    "1": 0x1E,
    "2": 0x1F,
    "3": 0x20,
    "4": 0x21,
    "5": 0x22,
    "6": 0x23,
    "7": 0x24,
    "8": 0x25,
    "9": 0x26,
    "0": 0x27,
    # Special keys
    "enter": 0x28,
    "return": 0x28,
    "escape": 0x29,
    "esc": 0x29,
    "backspace": 0x2A,
    "tab": 0x2B,
    "space": 0x2C,
    # Punctuation (unshifted)
    "-": 0x2D,
    "=": 0x2E,
    "[": 0x2F,
    "]": 0x30,
    "\\": 0x31,
    ";": 0x33,
    "'": 0x34,
    "`": 0x35,
    ",": 0x36,
    ".": 0x37,
    "/": 0x38,
    # Function keys
    "f1": 0x3A,
    "f2": 0x3B,
    "f3": 0x3C,
    "f4": 0x3D,
    "f5": 0x3E,
    "f6": 0x3F,
    "f7": 0x40,
    "f8": 0x41,
    "f9": 0x42,
    "f10": 0x43,
    "f11": 0x44,
    "f12": 0x45,
    # Control keys
    "printscreen": 0x46,
    "scrolllock": 0x47,
    "pause": 0x48,
    "insert": 0x49,
    "home": 0x4A,
    "pageup": 0x4B,
    "delete": 0x4C,
    "end": 0x4D,
    "pagedown": 0x4E,
    # Arrow keys
    "right": 0x4F,
    "left": 0x50,
    "down": 0x51,
    "up": 0x52,
    # Numpad
    "numlock": 0x53,
    "kp_divide": 0x54,
    "kp_multiply": 0x55,
    "kp_minus": 0x56,
    "kp_plus": 0x57,
    "kp_enter": 0x58,
    "kp_1": 0x59,
    "kp_2": 0x5A,
    "kp_3": 0x5B,
    "kp_4": 0x5C,
    "kp_5": 0x5D,
    "kp_6": 0x5E,
    "kp_7": 0x5F,
    "kp_8": 0x60,
    "kp_9": 0x61,
    "kp_0": 0x62,
    "kp_decimal": 0x63,
    # International / IME keys
    "hangul": 0x90,  # LANG1 - Korean Han/Eng toggle
    "haneng": 0x90,
    "hanja": 0x91,  # LANG2
    # Modifiers (for reference, usually handled separately)
    "capslock": 0x39,
    "ctrl": 0xE0,
    "lctrl": 0xE0,
    "rctrl": 0xE4,
    "shift": 0xE1,
    "lshift": 0xE1,
    "rshift": 0xE5,
    "alt": 0xE2,
    "lalt": 0xE2,
    "ralt": 0xE6,
    "meta": 0xE3,
    "lmeta": 0xE3,
    "rmeta": 0xE7,
    "win": 0xE3,
    "cmd": 0xE3,
    "super": 0xE3,
}

# Characters that require shift
SHIFTED_CHARS: dict[str, int] = {
    "A": 0x04,
    "B": 0x05,
    "C": 0x06,
    "D": 0x07,
    "E": 0x08,
    "F": 0x09,
    "G": 0x0A,
    "H": 0x0B,
    "I": 0x0C,
    "J": 0x0D,
    "K": 0x0E,
    "L": 0x0F,
    "M": 0x10,
    "N": 0x11,
    "O": 0x12,
    "P": 0x13,
    "Q": 0x14,
    "R": 0x15,
    "S": 0x16,
    "T": 0x17,
    "U": 0x18,
    "V": 0x19,
    "W": 0x1A,
    "X": 0x1B,
    "Y": 0x1C,
    "Z": 0x1D,
    "!": 0x1E,
    "@": 0x1F,
    "#": 0x20,
    "$": 0x21,
    "%": 0x22,
    "^": 0x23,
    "&": 0x24,
    "*": 0x25,
    "(": 0x26,
    ")": 0x27,
    "_": 0x2D,
    "+": 0x2E,
    "{": 0x2F,
    "}": 0x30,
    "|": 0x31,
    ":": 0x33,
    '"': 0x34,
    "~": 0x35,
    "<": 0x36,
    ">": 0x37,
    "?": 0x38,
}


def get_key_info(key: str) -> KeyInfo | None:
    """
    Get keycode and shift state for a key or character.

    Args:
        key: Key name (e.g., 'enter', 'f1') or character (e.g., 'a', 'A', '!')

    Returns:
        KeyInfo with code and shift requirement, or None if not found
    """
    # Check single characters first (before lowercasing)
    if len(key) == 1:
        if key in SHIFTED_CHARS:
            return KeyInfo(SHIFTED_CHARS[key], True)
        if key in KEYCODES:
            return KeyInfo(KEYCODES[key], False)

    # Check named keys (case-insensitive)
    key_lower = key.lower()
    if key_lower in KEYCODES:
        return KeyInfo(KEYCODES[key_lower], False)

    return None


def char_to_keycode(char: str) -> tuple[int, int] | None:
    """
    Convert a character to keycode and modifier.

    Args:
        char: Single character

    Returns:
        Tuple of (keycode, modifier) or None if not mappable
    """
    if char == " ":
        return (KEYCODES["space"], 0)

    if char == "\n":
        return (KEYCODES["enter"], 0)

    if char == "\t":
        return (KEYCODES["tab"], 0)

    key_info = get_key_info(char)
    if key_info:
        modifier = KeyboardModifier.SHIFT_LEFT if key_info.shift else 0
        return (key_info.code, modifier)

    return None


# WebSocket message channels (first byte of every binary frame).
CHANNEL_HEARTBEAT = 0
CHANNEL_KEYBOARD = 1
CHANNEL_MOUSE = 2


def build_keyboard_report(modifier: int = 0, keys: list[int] | None = None) -> bytes:
    """
    Build a binary keyboard HID message for the WebSocket.

    Layout: [CHANNEL_KEYBOARD, modifier, 0x00, key1..key6] (9 bytes).
    A standard USB HID keyboard report holds up to 6 simultaneous keycodes;
    unused slots are 0. Send an all-zero report (no modifier, no keys) to
    release.

    Args:
        modifier: Modifier bitmask (KeyboardModifier flags OR'd together)
        keys: Up to 6 USB HID keycodes (extra are dropped, missing are zero)

    Returns:
        9-byte binary frame
    """
    codes = list(keys or [])[:6]
    codes += [0] * (6 - len(codes))
    return bytes([CHANNEL_KEYBOARD, modifier & 0xFF, 0x00, *[c & 0xFF for c in codes]])


def build_mouse_report(buttons: int, x: int, y: int, wheel: int = 0) -> bytes:
    """
    Build a binary absolute-mouse HID message for the WebSocket.

    Layout: [CHANNEL_MOUSE, buttons, xLow, xHigh, yLow, yHigh, wheel] (7 bytes).
    x/y are 16-bit little-endian (use scale_coordinate to produce them);
    buttons is a MouseButton bitmask; wheel is a signed byte (-127..127).

    Args:
        buttons: MouseButton bitmask (0 = no buttons held)
        x: 16-bit absolute X (1..0x8000)
        y: 16-bit absolute Y (1..0x8000)
        wheel: Scroll delta, negative = up, positive = down

    Returns:
        7-byte binary frame
    """
    return bytes(
        [
            CHANNEL_MOUSE,
            buttons & 0xFF,
            x & 0xFF,
            (x >> 8) & 0xFF,
            y & 0xFF,
            (y >> 8) & 0xFF,
            wheel & 0xFF,
        ]
    )


def build_heartbeat() -> bytes:
    """Build the single-byte heartbeat frame [CHANNEL_HEARTBEAT]."""
    return bytes([CHANNEL_HEARTBEAT])


def scale_coordinate(value: int, dimension: int) -> int:
    """
    Scale a screen pixel coordinate to the NanoKVM 16-bit absolute range.

    Matches the official firmware: floor(0x7FFF * value/dimension) + 1,
    clamped to 1..0x8000.

    Args:
        value: Pixel coordinate (0 = edge)
        dimension: Screen width or height in pixels

    Returns:
        16-bit absolute coordinate (1..0x8000)
    """
    if dimension <= 0:
        return 1
    scaled = int(0x7FFF * (max(0, value) / dimension)) + 1
    return max(1, min(0x8000, scaled))
