"""
    Timer object
"""
from threading import Timer


def print_state():
    print('How are you?')

t = Timer(3, print_state)
t.start()
