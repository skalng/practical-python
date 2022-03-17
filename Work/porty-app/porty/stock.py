'''
Created on 16.02.2022

@author: ho_ksk
__updated__='2022-03-17 17:42:52'


Exercise 4.1 / 4.2 / 5.8 / 7.9 
'''
from os import name
from .typedproperty import String, Integer, Float

class Stock(object):
    __slotts__ = ('name', 'shares', 'price')            ## restrict the set of attributes
    
    name   = String('name')
    shares = Integer('shares')
    price  = Float('price')
    
    def __init__(self, name, shares, price):
        self.name   = name
        self.shares = shares
        self.price  = price
        
    def __repr__(self):
        return f'Stock({self.name}, {self.shares}, {self.price})'
    
    
    @property    
    def cost(self) -> float:
        return self.shares * self.price
        
        
    def sell(self, number: int) -> None:
        self.shares = self.shares - number
        
        
        
if __name__ == '__main__':
    from porty import fileparse
    
    with open('../Data/portfolio.csv') as lines:
        portdicts = fileparse.parse_csv(lines, select=['name','shares','price'], types=[str,int,float])
        
    portfolio = [Stock(d['name'], d['shares'], d['price']) for d in portdicts]
    print(sum([s.cost for s in portfolio]), 'expected is: 44671.15')
    

    
    
        