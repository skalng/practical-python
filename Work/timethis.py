'''
Created on 06.03.2022

@author: ho_ksk
__updated__='2022-03-06 16:23:44'
'''

# timethis.py

# Execise 7.10

import time

def timethis(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        try:
            return func(*args, **kwargs)
        finally:
            t2 = time.time()
            print(f'{func.__module__}.{func.__name__} runs {t1-t2}')
    return wrapper


if __name__ == '__main__':
    @timethis
    def countdown(n):
        while n > 0:
            n-= 1

    countdown(1000000)

