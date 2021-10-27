# -*- coding: utf-8 -*-

from decorators import (
    timer,
    debug,
    slow_down,
)


@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)

@timer
@debug
@slow_down(rate=0.5)
def greeting(name):
    return f"Hello {name}"

if __name__ == "__main__":
    print(countdown.__name__)
    countdown(3)
    greeting("World")
    