"""
    Event object
"""
from threading import Thread, Event
from time import sleep


def first(f, s):
    sleep(10)
    print('First starting')
    f.set()
    s.wait()
    print('First working')


def second(f, s):
    print('Second starting')
    s.set()
    f.wait()
    print('Second working')


f = Event()
s = Event()

t1 = Thread(target=first, args=(f, s))
t2 = Thread(target=second, args=(f, s))

t1.start()
t2.start()

t1.join()
t2.join()