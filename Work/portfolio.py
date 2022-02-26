'''
Created on 26.02.2022

@author: ho_ksk
__updated__='2022-02-26 11:30:34'
'''

# portfolio.py

from typing import List
from stock import Stock

class Portfolio:
    
    def __init__(self, holdings: List[Stock]):
        self._hloldings = holdings
        
    def __iter__(self):
        return self._hloldings.__iter__()
        
    @property
    def total_cost(self) -> float:
        return sum([h.cost for h in self._hloldings])
        
        
    def  tabulate_shares(self) -> dict:
        from collections import Counter
        total_shares = Counter()
        for h in self._hloldings:
            total_shares[h.name] += h.shares
        return total_shares
            



if __name__ == '__main__':
    pass











