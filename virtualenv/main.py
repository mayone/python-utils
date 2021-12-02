# -*- coding: utf-8 -*-

try:
    import github
except Exception as e:
    print("venv test FAILED")
    exit(0)


def test():
    print("venv test SUCCESS")


if __name__ == "__main__":
    test()
