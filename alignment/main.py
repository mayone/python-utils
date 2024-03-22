#!/usr/bin/env python3

from alignment import align


class Colors:
    RESET = "\033[0m"
    UNDERLINE = "\033[4m"
    REVERSE = "\033[7m"
    BR_BLUE = "\033[94m"


def align_demo():
    print("Alignment demo (left align)")
    print("1. English characters (Halfwidth)")
    print("2. Chinese characters (Fullwidth)")
    print("3. Combining characters (Ambiguous)")
    print("4. Colored characters (ANSI escape code)")
    print("=" * 48)
    print("Built-in alignment method")
    print("{:<12}{:<12}{:<12}".format("I", "am", "Wayne!"))
    print("{:<12}{:<12}{:<12}".format("我", "是", "偉恩！"))
    print(
        "{0}{1}{2}".format(
            "I\u0304\u0304".ljust(12),
            "am\u0304\u0304".ljust(12),
            "W\u0304ayne\u0304!".ljust(12),
        )
    )
    print(
        "{0}{1}{2}".format(
            f"{Colors.BR_BLUE}I{Colors.RESET}".ljust(12),
            f"{Colors.UNDERLINE}am{Colors.RESET}".ljust(12),
            f"{Colors.REVERSE}Wayne{Colors.RESET}!".ljust(12),
        )
    )

    print("=" * 48)
    print("Custom alignment method")
    print("{0}{1}{2}".format(align("I"), align("am"), align("Wayne!")))

    print("{0}{1}{2}".format(align("我"), align("是"), align("偉恩！")))

    print(
        "{0}{1}{2}".format(
            align("I\u0304\u0304"), align("am\u0304\u0304"), align("W\u0304ayne\u0304!")
        )
    )

    print(
        "{0}{1}{2}".format(
            align(f"{Colors.BR_BLUE}I{Colors.RESET}"),
            align(f"{Colors.UNDERLINE}am{Colors.RESET}"),
            align(f"{Colors.REVERSE}Wayne{Colors.RESET}!"),
        )
    )


if __name__ == "__main__":
    align_demo()
