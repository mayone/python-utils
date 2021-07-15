from alignment import align


def align_demo():
    print("Alignment demo (left align)")
    print("1. English characters (Halfwidth)")
    print("2. Chinese characters (Fullwidth)")
    print("3. Combining characters (Ambiguous)")
    print("=" * 48)
    print("Built-in alignment method")
    print("{:<12}{:<12}{:<12}".format(
        "I",
        "am",
        "Wayne!"))
    print("{:<12}{:<12}{:<12}".format(
        "我",
        "是",
        "偉恩！"))
    print("{0}{1}{2}".format(
        u"I\u0304\u0304".ljust(12),
        u"am\u0304\u0304".ljust(12),
        u"W\u0304ayne\u0304!".ljust(12)))
    print("=" * 48)
    print("Custom alignment method")
    print("{0}{1}{2}".format(
        align("I"),
        align("am"),
        align("Wayne!")))

    print("{0}{1}{2}".format(
        align("我"),
        align("是"),
        align("偉恩！")))

    print("{0}{1}{2}".format(
        align(u"I\u0304\u0304"),
        align(u"am\u0304\u0304"),
        align("W\u0304ayne\u0304!")))


if __name__ == "__main__":
    align_demo()
