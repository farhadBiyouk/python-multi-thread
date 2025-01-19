from time import sleep, perf_counter
from threading import Thread

start = perf_counter()


# simple code for daemon in multithreading
def show(name):
    print(f'Starting {name}')
    sleep(3)
    print(f'Finishing {name}')


t1 = Thread(target=show, args=('one',), daemon=False)
t2 = Thread(target=show, args=('two',), daemon=False)

t1.start()
t2.start()

print('start waiting ....')
t1.join()
t2.join()
print('end waiting ....')
end = perf_counter()

print(round(end - start))
