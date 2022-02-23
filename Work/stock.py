'''
Created on 16.02.2022

@author: ho_ksk
__updated__='2022-02-23 15:53:55'


Exercise 4.1/.2
'''
from os import name


class Stock(object):
    __slotts__ = ('name', 'shares', 'price')
    
    def __init__(self, name, shares, price):
        self.name   = name
        self.shares = shares
        self.price  = price
        
    def __repr__(self):
        return f'Stock({self.name}, {self.shares}, {self.price})'
    
    ''' --- properies --- '''
    @property
    def name(self):
        return self._name
     
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise TypeError('str expected')
    
    @property
    def shares(self):
        return self._shares
    
    @shares.setter
    def shares(self, value):
        if isinstance(value, int):
            self._shares = value
        else:
            raise TypeError('int expected')
    
 
    @property
    def price(self):
        return self._price
     
    @price.setter
    def price(self, value):
        if isinstance(value, float):
            self._price = value
        else:
            raise TypeError('float expected')
    
 
    ''' --- methods ---'''
    @property    
    def cost(self) -> float:
        return self.shares * self.price
        
        
    def sell(self, number: int) -> None:
        self.shares = self.shares - number
        
        
        
if __name__ == '__main__':
    import fileparse
    
    with open('Data/portfolio.csv') as lines:
        portdicts = fileparse.parse_csv(lines, select=['name','shares','price'], types=[str,int,float])
        
    portfolio = [Stock(d['name'], d['shares'], d['price']) for d in portdicts]
    print(sum([s.cost for s in portfolio]), 'expected is: 44671.15')
    

    
    
        