from concurrent.futures import ThreadPoolExecutor
from time import sleep


# simple code for ThreadPoolExecutor multithreading
def show(name):
    print(f'Starting {name}')
    sleep(3)
    print(f'Finishing {name}')


names = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
with ThreadPoolExecutor() as executor:
    executor.map(show, names)

print('Done')
