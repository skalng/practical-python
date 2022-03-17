'''
Created on 03.03.2022

@author: ho_ksk
__updated__='2022-03-17 22:35:38'
'''
''' from http://www.dabeaz.com/coroutines/ '''
# coroutine.py  
#
# A decorator function that takes care of starting a coroutine
# automatically on call.

def coroutine(func):
    def start(*args,**kwargs):
        cr = func(*args,**kwargs)
        next(cr)
        return cr
    return start

# Example use
@coroutine
def grep(pattern):
    print ("Looking for %s" % pattern)
    while True:
        line = (yield)
        if pattern in line:
            print (line,)


if __name__ == '__main__':
    
    g = grep("python")
    # Notice how you don't need a next() call here
    g.send("Yeah, but no, but yeah, but no")
    g.send("A series of tubes")
    g.send("python generators rock!")
    
    
    
    
    