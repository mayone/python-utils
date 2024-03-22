# -*- coding: utf-8 -*-

from enum import IntEnum, auto


# ANSI escape code


def SGR(codes=""):
    """ANSI control sequence - Select Graphic Rendition."""
    # Escape
    # ESC = "\33"
    ESC = "\x1b"
    # CSI (Control Sequence Introducer)
    CSI = f"{ESC}["

    return f"{CSI}{codes}m"


# FG Color code


class FGC(IntEnum):
    BLACK = 30
    RED = auto()
    GREEN = auto()
    YELLOW = auto()
    BLUE = auto()
    MAGENTA = auto()
    CYAN = auto()
    WHITE = auto()
    # Bright
    GRAY = 90
    BR_RED = auto()
    BR_GREEN = auto()
    BR_YELLOW = auto()
    BR_BLUE = auto()
    BR_MAGENTA = auto()
    BR_CYAN = auto()
    BR_WHITE = auto()

    def describe(self):
        return self.name, self.value


# BG Color code


class BGC(IntEnum):
    BLACK = 40
    RED = auto()
    GREEN = auto()
    YELLOW = auto()
    BLUE = auto()
    MAGENTA = auto()
    CYAN = auto()
    WHITE = auto()
    # Bright
    GRAY = 100
    BR_RED = auto()
    BR_GREEN = auto()
    BR_YELLOW = auto()
    BR_BLUE = auto()
    BR_MAGENTA = auto()
    BR_CYAN = auto()
    BR_WHITE = auto()


# Style code


class Style(IntEnum):
    BOLD = 1
    FAINT = auto()
    ITALIC = auto()
    UNDERLINE = auto()
    BLINK = auto()
    # RAPID_BLINK = auto()  # will break xterm
    REVERSE = 7
    HIDE = auto()
    STRIKE = auto()


def colored(fmt, fg=None, bg=None, style=None):
    """Return colored text.

    Parameters
    ----------
    fmt : string
        The string to be colored.
    fg : FGC
        Foreground color.
    bg : BGC
        Background color.
    style: list
        list of styles to be applied.
    """
    # properties
    props = []
    if isinstance(style, list):
        props = [s.value for s in style if isinstance(s, Style)]
    if isinstance(fg, FGC):
        props.append(fg.value)
    if isinstance(bg, BGC):
        props.append(bg.value)

    # form string
    props = ";".join([str(x) for x in props])
    if props:
        return f"{SGR(props)}{fmt}{SGR()}"
    else:
        return fmt


def cprint(fmt, fg=None, bg=None, style=None):
    print(colored(fmt, fg, bg, style))
