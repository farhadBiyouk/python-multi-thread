from time import sleep, perf_counter
from threading import Thread, current_thread, active_count, enumerate

start = perf_counter()


# simple code for several method in multithreading
def show(name):
    print(f'Starting {name}')
    # # print(active_count())
    # print(current_thread().ident)
    print(enumerate())
    sleep(3)
    print(f'Finishing {name}')


t1 = Thread(target=show, args=('one',), name='First')
t2 = Thread(target=show, args=('two',), name='Second')

t1.start()
t2.start()

t1.join()
t2.join()

end = perf_counter()

print(round(end - start))
