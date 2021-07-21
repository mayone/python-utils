# -*- coding: utf-8 -*-

from singleton import Singleton


class cls_testing(metaclass=Singleton):
    def __init__(self):
        self.__test_str = "Singleton test FAILED!!!"

    def set_str(self, str):
        self.__test_str = str

    def get_str(self):
        return self.__test_str


def singleton_test():
    a = cls_testing()
    b = cls_testing()
    a.set_str("Singleton test SUCCESS!!!")
    result = b.get_str()
    print(result)


if __name__ == "__main__":
    singleton_test()
