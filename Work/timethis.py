'''
Created on 06.03.2022

@author: ho_ksk
__updated__='2022-03-06 16:11:09'
'''

# timethis.py

def timethis(func):
    def wrapper(*args, **kwargs):
        import time
        t1 = time.time()
        func(*args, **kwargs)
        print(func.__name__ + 'runs' +  time.time()-t1)
        return
    return wrapper



