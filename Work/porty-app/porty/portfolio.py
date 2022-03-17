'''
Created on 26.02.2022

@author: ho_ksk
__updated__='2022-03-07 00:20:45'
'''

# portfolio.py


# Exercise 7:11

from porty import fileparse
from porty import stock

class Portfolio:
    
    def __init__(self):
        self._holdings = []
        
    @classmethod        
    def from_csv(cls, lines, **opts):
        self = cls()
        portfoliodict = fileparse.parse_csv(lines, 
                                            select=['name', 'shares', 'price'], 
                                            types=[str, int, float],
                                            **opts)
        for d in portfoliodict:
            self.append(stock.Stock(**d))
            
        return self

    def append(self, holding):
        self._holdings.append(holding)

        
        
    def __iter__(self):
        return self._holdings.__iter__()
    
    def __len__(self):
        return len(self._holdings)
    
    def __getitem__(self, index):
        return self._holdings[index]
    
    def  __contains__(self, name):
        return any([h.name == name for h in self._holdings])
    
        
    @property
    def total_cost(self) -> float:
        return sum([h.cost for h in self._holdings])
        
        
    def tabulate_shares(self) -> dict:
        from collections import Counter
        total_shares = Counter()
        for h in self._holdings:
            total_shares[h.name] += h.shares
        return total_shares
    
            


if __name__ == '__main__':
    with open('Data/portfolio.csv') as lines: 
        port = Portfolio.from_csv(lines)











