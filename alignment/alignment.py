from __future__ import annotations

import re
import unicodedata
from sys import platform as _platform

_ANSI_ESCAPE_RE = re.compile(r"(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[ -/]*[@-~]")
_ZERO_WIDTH_RE = re.compile(r"[\u200b-\u200d\u2060\ufeff]")
_TEXT_VARIATION_SELECTOR_RE = re.compile(r"[\ufe00-\ufe0e]")  # VS1-VS15 (not VS16)
_EMOJI_MODIFIER_RE = re.compile(r"[\U0001F3FB-\U0001F3FF]")  # Fitzpatrick skin tones

_ZWJ = "\u200d"  # zero width joiner
_VS16 = "\ufe0f"  # emoji-presentation variation selector


def remove_ansi_escape(string: str) -> str:
    """Remove ANSI escape code.

    Parameters
    ----------
    string : str
        The string to be handled.

    Examples
    --------
    >>> remove_ansi_escape('\033[94mHello\033[0m')
    'Hello'

    >>> remove_ansi_escape('\033[4mHi\033[0m')
    'Hi'
    """
    return _ANSI_ESCAPE_RE.sub("", string)


def is_wide(ch: str) -> bool:
    """Check is the character wide or not.

    Parameters
    ----------
    ch : str
        The character to be checked.

    Examples
    --------
    >>> is_wide('鄭')
    True

    >>> is_wide('a')
    False
    """
    res = unicodedata.east_asian_width(ch)
    if res == "A":
        if _platform.startswith("linux"):
            return False
        elif _platform.startswith("win") or _platform.startswith("cygwin"):
            return True
        elif _platform.startswith("darwin"):
            return False
        else:
            return False
    return res in ("F", "W")


def get_width(string: str) -> int:
    """Get width of string.

    Parameters
    ----------
    string : str
        Target string.

    Examples
    --------
    >>> get_width("你好")
    4

    >>> get_width("Hello")
    5

    >>> get_width("❤️")
    2

    >>> get_width("✊")
    2

    >>> get_width("✊🏾")
    2

    >>> get_width("🏳")
    1

    >>> get_width("🌈")
    2

    >>> get_width("🏳️‍🌈")
    2

    >>> get_width("🇹🇼")
    2

    >>> get_width("👨‍👩‍👧‍👦")
    2

    >>> get_width("")
    0
    """

    if not string:
        return 0

    string = remove_ansi_escape(string)

    width = 0
    base_width = 0  # width of the most recent base char, for VS16 emoji upgrade
    join_next = False
    for ch in string:
        if join_next:
            # joined into the previous glyph by a ZWJ; occupies no extra cell
            join_next = False
            base_width = 0
            continue

        if ch == _ZWJ:
            # the next character merges into one emoji glyph; skip it
            join_next = True
            base_width = 0
            continue

        if ch == _VS16:
            # emoji-presentation selector: widen the preceding narrow base to 2 cells
            if base_width == 1:
                width += 1
            base_width = 0
            continue

        if (
            unicodedata.combining(ch)
            or _ZERO_WIDTH_RE.match(ch)
            or _TEXT_VARIATION_SELECTOR_RE.match(ch)
            or _EMOJI_MODIFIER_RE.match(ch)
        ):
            # combining marks, zero-width chars, text variation selectors,
            # and emoji skin-tone modifiers add no width
            base_width = 0
            continue

        base_width = 2 if is_wide(ch) else 1
        width += base_width

    return width


def align(string: str, direction: str = "l", length: int = 12) -> str | None:
    """Align string in given length.

    Parameters
    ----------
    string : str
        Target string.
    direction : str
        'l' means left, 'r' means right.
    length : int
        Align length.

    Examples
    >>> align("Hello", direction='r', length=8)
    '   Hello'

    >>> align("你好", direction='r', length=8)
    '    你好'
    """

    if not string:
        return ""

    diff = length - get_width(string)

    if diff < 0:
        diff = 1

    if direction == "l":
        return string + " " * diff
    elif direction == "r":
        return " " * diff + string
    return None
