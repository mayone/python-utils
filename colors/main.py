#!/usr/bin/env python3

from colors import FGC, BGC, Style, colored, cprint
from alignment import align


def showcase():
    cprint("FGC", fg=FGC.BR_RED, bg=BGC.WHITE, style=[Style.BOLD])
    output = ""
    for i, (cname, color) in enumerate([(c.name, c) for c in FGC]):
        if (i % 8 == 7):
            print(output)
            output = ""
        else:
            # output += f"{colored(cname, fg=color):>20}"
            output += f"{align(colored(cname, fg=color), dir='r', length=12)}"

    cprint("BGC", fg=FGC.WHITE, bg=BGC.RED, style=[Style.BOLD])
    output = ""
    for i, (cname, color) in enumerate([(c.name, c) for c in BGC]):
        if (i % 8 == 7):
            print(output)
            output = ""
        else:
            # output += f"{colored(cname, bg=color):>20}"
            output += f"{align(colored(cname, bg=color), dir='r', length=12)}"

    cprint("Style", bg=BGC.GRAY, style=[Style.BOLD, Style.ITALIC])
    output = ""
    for (sname, style) in [(s.name, s) for s in Style]:
        # output += f"{colored(sname, style=[style]):>20}"
        output += f"{align(colored(sname, style=[style]), dir='r', length=12)}"
    print(output)


if __name__ == "__main__":
    showcase()
